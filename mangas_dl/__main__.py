import os
import sys, getopt
import json

from .mangas_dl_class import Mangas_dl

from .Headers.errors import ConnexionError
from .Headers.functions_formatting import str_to_chapters
from .Headers.functions_os import is_path_exists_or_creatable

__version__ = "0.4.0"

ARGS = sys.argv[1:]

sys.path.append(os.path.dirname(os.path.realpath(__file__)))

def main_one_line(argv):
    try:
        opts, args = getopt.getopt(argv, "hvl:c:p:n:", ["help", "version", "language", "chapters", "path", "list", "name"])
    except getopt.GetoptError:
        print("\nUsage:\n\tmangas-dl [options] URL")
        print("or:\n\tmangas-dl <command> [options]")
        print("\nNo such option: \"" + argv[0] + "\"")
        sys.exit(1)

    if argv[0] in ("save_path", "save_language"):
        try:
            with open('mangas_dl/settings.json', 'r+') as f:
                settings = json.load(f)
                f.seek(0)

                if argv[0] == "save_path":
                    if not is_path_exists_or_creatable(argv[1]):
                        print("The given path doesn't exist and is not creatable. Please try again.")
                        sys.exit(1)
                    settings["remembered_path"] = argv[1]
                    json.dump(settings, f)
                    print("Path \"" + argv[1] + "\" learnt")
                elif argv[0] == "save_language":
                    try:
                        with open("mangas_dl/language_codes.json") as file:
                            LANGUAGE_CODES = json.load(file)
                    except:
                        raise FileNotFoundError("The file websites_used.json has not been found. Please make sure it exists before lauching mangas-dl.")
                    if not argv[1] in LANGUAGE_CODES.keys():
                        print("The given language is not taken in charge. Please read the complete list here : https://github.com/Boubou0909/Mangas-dl/blob/main/mangas_dl/language_codes.json")
                        sys.exit(1)
                    settings["remembered_language"] = argv[1]
                    json.dump(settings, f)
                    print("Language \"" + argv[1] + "\" learnt")

                f.truncate()
                f.close()
        except IOError:
            print("ERROR : Impossible to deal the request. Please try again later.")
            sys.exit(1)
        except IndexError:
            print("ERROR : Please give the what you want to save after the command.")
            print("\nUsage:\n\tmangas_dl <command> [options]")
            sys.exit(1)
        except:
            print("ERROR : try \"pip install mangas-dl --upgrade\" to update the package")
            sys.exit(1)
        finally:
            sys.exit(0)

    try:
        with open("mangas_dl/settings.json", "r") as f:
            settings = json.load(f)
            language = settings["remembered_language"]
    except:
        language = "en"
    
    chapters_asked = ""
    listing = False
    manga_name = ""
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            f = open("mangas_dl/HELP.md", "r")
            print(f.read())
            f.close()
            sys.exit(0)
        elif opt in ("-v", "--version"):
            print("mangas-dl", __version__)
            sys.exit(0)
        elif opt in ("-l", "--language"):
            language = arg
        elif opt in ("-c", "--chapters"):
            chapters_asked = arg
        elif opt in ("-p", "--path"):
            if arg == "%":
                try:
                    f = open("mangas_dl/settings.json", "r")
                    settings = json.load(f)
                    f.close()
                    download_path = settings["remembered_path"]
                except:
                    raise OSError("There is no remebered path. Save one before using this command.")
            elif is_path_exists_or_creatable(arg):
                download_path = arg
            else:
                print("The given path does not exist and is not creatable. Please try again.")
                sys.exit(1)
        elif opt in ("--list"):
            listing = True
        elif opt in ("-n", "--name"):
            manga_name = arg
    
    if len(args) != 1:
        print("Please enter only one url at time.")
        sys.exit(1)
    elif not "download_path" in locals() and not listing:
        print("Please enter a path where scans will be saved.")
        sys.exit(1)

    url = args[0]

    mangas_dl = Mangas_dl(url)
    if not mangas_dl.test_connexion():
        raise ConnexionError(url)

    mangas_dl.pre_download(choosen_language = language)
    if len(mangas_dl.chapters) == 0:
        print("The remembered language is not available for this scan. English will be used instead.")
        mangas_dl.pre_download(choosen_language = "en")

    if listing:
        try:
            for i in range(len(mangas_dl.chapters) // 10 + 1):
                for j in range(10):
                    print(mangas_dl.chapters_name[10 * i + j], end="  ")
                print("")
        except:
            pass
        finally:
            sys.exit(0)

    if manga_name != "":
        mangas_dl.manga_name = manga_name

    mangas_dl.chapters_asked = str_to_chapters(mangas_dl.chapters, mangas_dl.chapters_name, chapters_asked)
    mangas_dl.download_path = download_path.rstrip(os.path.sep) + os.path.sep

    return mangas_dl.download_chapters()

def main_interactive(url):
    mangas_dl = Mangas_dl(url)
    if not mangas_dl.test_connexion():
        raise ConnexionError(url)

    mangas_dl.pre_download()
    mangas_dl.ask_chapters_to_download()
    mangas_dl.ask_path()

    return mangas_dl.download_chapters()

def main():
    if len(ARGS) == 0:
        print(main_interactive(input("Enter the main page of the manga you want to download : ")))
    else:
        print(main_one_line(ARGS))

if __name__ == "__main__":
    main()