import os
import sys
import errno

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