import json
import os

import pre_download_functions
import download_chapters_functions

from Headers.functions_web import does_page_exists
from Headers.errors import UnknownWebsiteError, InputError, OSError, ConnexionError
from Headers.functions import ask_until_y_or_n
from Headers.functions_os import is_path_exists_or_creatable

try:
    with open("websites_used.json") as file:
        LAUNCH_FUNCTIONS = json.load(file)
        KNOWN_WEBSITES = LAUNCH_FUNCTIONS.keys()
except:
    raise FileNotFoundError("The file websites_used.json has not been found.\nPlease make sure it exists before lauching mangas-dl.")

class Mangas_dl:
    def __init__(self, url):
        self.url = url

        pre_process = url.split('/')
        self.site_name = pre_process[2]

        self.manga_name = ""
        self.chapters = []
        self.chapters_name = []
        self.chapters_asked = []

        self.download_path = ""

    def test_connexion(self):
        return does_page_exists(self.url)

    def pre_download(self):
        if not self.site_name in KNOWN_WEBSITES:
            raise UnknownWebsiteError(self.site_name)
        
        if not does_page_exists(self.url):
            raise ConnexionError(self.url)

        self.chapters, self.chapters_name, self.manga_name = getattr(pre_download_functions, LAUNCH_FUNCTIONS[self.site_name]["pre_download"])(self.url)

    def ask_chapters_to_download(self):
        if not hasattr(self, "chapters") or not hasattr(self, "chapters_name"):
            raise Exception("No idea how you arrived here.")

        print(len(self.chapters), "chapters have been found (from " + self.chapters_name[0] + " to " + self.chapters_name[-1] + ").")
        chapters_asked = input('Which chapter(s) would you like to download ? ')

        pre_chapter_asked = []
        if chapters_asked in ['', '-1', '*']:
            pre_chapter_asked = [(self.chapters[i], self.chapters_name[i]) for i in range(len(self.chapters))]
        else:
            for list in chapters_asked.split('/'):
                try:
                    begin, end = list.split('-')
                except:
                    raise InputError()
                
                try:
                    indice_begining = self.chapters_name.index(begin)
                    indice_ending = self.chapters_name.index(end)
                except:
                    pass

                try:
                    indice_begining = self.chapters.index(begin)
                    indice_ending = self.chapters.index(end)
                except:
                    pass
                
                if not "indice_begining" in locals() or not "indice_ending" in locals():
                    raise InputError("At least one of the chapter(s) asked doesn't exist.")

                if len(str(end).split('.')) > 1:
                    k = 0.1
                    while k < 1:
                        try:
                            indice_ending = self.chapters.index(str(float(end) + round(k,1)))
                        except:
                            pass
                        
                        k += 0.1

                for i in range(indice_begining, indice_ending + 1):
                    pre_chapter_asked.append((self.chapters[i],self.chapters_name[i]))
        
        for i in range(len(pre_chapter_asked)):
            self.chapters_asked.append((pre_chapter_asked[i][0], pre_chapter_asked[i][1]))

    def ask_path(self):
        download_path = ''
        use_json = False

        is_path_valid = False

        while not is_path_valid:
            try:
                f = open('settings.json', 'r')
                settings = json.load(f)
                f.close()
                remembered_path = settings['remembered_path']
                use_remembered_path = ask_until_y_or_n('The path "' + remembered_path + '" is known. Do you want to use it ?')
                download_path = remembered_path if use_remembered_path else ''
                use_json = download_path != ''
            except:
                pass

            while download_path == '':
                download_path = input('Destination folder : ')
            
            if not is_path_exists_or_creatable(download_path):
                raise OSError("The given path doesn\'t exists and is not creatable.")

            if not os.path.exists(download_path):
                create_path = ask_until_y_or_n('The folder doesn\'t exist. Create it ?')
                if create_path:
                    os.makedirs(download_path)
                    is_path_valid = True
            else:
                is_path_valid = True
        
            if not use_json and is_path_valid:
                save_path = ask_until_y_or_n('Do you want to save this path ?')
                if save_path:
                    f = open('settings.json', 'a+')
                    saved_path = {'remembered_path' : download_path}
                    json.dump(saved_path, f)
                    f.close()

        self.download_path = download_path.rstrip(os.path.sep) + os.path.sep

    def download_chapters(self):
        if not hasattr(self, "chapters_asked") or not hasattr(self, "download_path"):
            raise Exception("No idea how you arrived here")

        getattr(download_chapters_functions, LAUNCH_FUNCTIONS[self.site_name]["download_chapters"])(self.url, self.chapters_asked, self.download_path, self.manga_name)

        return "Download finished successfully. Enjoy !"