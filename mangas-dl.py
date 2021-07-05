from mangas_dl_class import Mangas_dl

from Headers.errors import ConnexionError

def main(url):
    mangas_dl = Mangas_dl(url)
    if not mangas_dl.test_connexion():
        raise ConnexionError(url)

    mangas_dl.pre_download()
    mangas_dl.ask_chapters_to_download()
    mangas_dl.ask_path()

    return mangas_dl.download_chapters()

print(main(input("Enter the main page of the manga you want to download : ")))