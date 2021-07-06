# pyinstaller --onefile run.py --copy-metadata pyppeteer
import sys, getopt
import json

from mangas_dl_class import Mangas_dl

from Headers.errors import ConnexionError
from Headers.functions_formatting import str_to_chapters
from Headers.functions_os import is_path_exists_or_creatable

ARGS = sys.argv[1:]

def main_one_line(argv):
    try:
        opts, args = getopt.getopt(argv, "hl:c:o:", ["help", "language", "chapters", "output"])
    except getopt.GetoptError:
        print("#TODO")
        sys.exit(1)

    language = "en"
    chapters_asked = ""
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print("#TODO")
            sys.exit(0)
        elif opt in ("-l", "--language"):
            language = arg
        elif opt in ("-c", "--chapters"):
            chapters_asked = arg
        elif opt in ("-o", "--output"):
            if arg == "%":
                try:
                    f = open("settings.json", "r")
                    settings = json.load(f)
                    f.close()
                    download_path = settings["remembered_path"]
                except:
                    raise OSError("There is no remebered path. Save one before using this command.")
            elif is_path_exists_or_creatable(arg):
                download_path = arg
            else:
                print("The given path does not exist and is not creatable. Please try again.")
                sys.exit(2)
    
    if len(args) != 1:
        print("Please enter only one url at time.")
        sys.exit(3)
    elif not "download_path" in locals():
        print("Please enter a path where scans will be saved.")
        sys.exit(2)

    url = args[0]

    mangas_dl = Mangas_dl(url)
    if not mangas_dl.test_connexion():
        raise ConnexionError(url)

    mangas_dl.pre_download(choosen_language = language)
    mangas_dl.chapters_asked = str_to_chapters(mangas_dl.chapters, mangas_dl.chapters_name, chapters_asked)
    mangas_dl.download_path = download_path

    return mangas_dl.download_chapters()

def main_interactive(url):
    mangas_dl = Mangas_dl(url)
    if not mangas_dl.test_connexion():
        raise ConnexionError(url)

    mangas_dl.pre_download()
    mangas_dl.ask_chapters_to_download()
    mangas_dl.ask_path()

    return mangas_dl.download_chapters()

if len(ARGS) == 0:
    print(main_interactive(input("Enter the main page of the manga you want to download : ")))
else:
    print(main_one_line(ARGS))