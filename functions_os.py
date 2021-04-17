import os
import sys
import errno
import json

import functions

def is_pathname_valid(path):
    try:
        if not isinstance(path, str) or not path:
            return False
        
        _, path = os.path.splitdrive(path)

        root_dirname  = os.environ.get('HOMEDRIVE', 'C:') if sys.platform == 'win32' else os.path.sep

        if not os.path.isdir(root_dirname):
            raise ValueError('No idea of what happened.')
        
        root_dirname = root_dirname.rstrip(os.path.sep) + os.path.sep

        for path_part in path.split(os.path.sep):
            try:
                os.lstat(root_dirname + path_part)
            except OSError as exc:
                if hasattr(exc, 'winerror'):
                    if exc.winerror == 123:
                        return False
                elif exc.errno in {errno.ENAMETOOLONG, errno.ERANGE}:
                    return False
    except TypeError as exc:
        return False
    
    else:
        return True

def is_path_creatable(path):
    dirname = os.path.dirname(path) or os.getcwd()
    return os.access(dirname, os.W_OK)

def is_path_exists_or_creatable(path):
    try:
        return is_pathname_valid(path) and (os.path.exists(path) or is_path_creatable(path))
    except OSError:
        return False

def asked_path():
    download_path = ''
    use_json = False

    is_path_valid = False

    while not is_path_valid:
        try:
            f = open('settings.json', 'r')
            settings = json.load(f)
            f.close()
            remembered_path = settings['remembered_path']
            use_remembered_path = functions.ask_until_y_or_n('The path "' + remembered_path + '" is known. Do you want to use it ?')
            download_path = remembered_path if use_remembered_path else ''
            use_json = download_path != ''
        except:
            pass

        while download_path == '':
            download_path = input('Destination folder : ')
        
        if not is_path_exists_or_creatable(download_path):
            return ['The given path doesn\'t exists and is not creatable.']

        if not os.path.exists(download_path):
            create_path = functions.ask_until_y_or_n('The folder doesn\'t exist. Create it ?')
            if create_path:
                os.makedirs(download_path)
                is_path_valid = True
        else:
            is_path_valid = True
    
        if not use_json:
            save_path = functions.ask_until_y_or_n('Do you want to save this path ?')
            if save_path:
                f = open('settings.json', 'a+')
                saved_path = {'remembered_path' : download_path}
                json.dump(saved_path, f)
                f.close()

    return download_path