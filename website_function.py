import functions_os
import functions_chapters

import Websites.manganelo

def manganelo_tv(url):
    pre_chapters = Websites.manganelo.nb_chp_manganelo(url)
    if isinstance(pre_chapters, str):
        return pre_chapters
    chapters, chapters_to_save, manga_name = pre_chapters
    manga_name = functions_os.delete_non_creatable_symbols('_'.join(manga_name[4:-5].split(' ')))

    print('Total : ' + str(len(chapters)) + ' chapter(s) found (' + str(chapters[0]) + ' to ' + str(chapters[-1]) + ')')
    ask_to_save = input('Chapters to save : ')

    pre_to_save = functions_chapters.asked_chapters(chapters, chapters_to_save, ask_to_save)
    if isinstance(pre_to_save, str):
        return pre_to_save

    to_save = functions_chapters.couples_of_chapters(pre_to_save)

    download_path = functions_os.asked_path()
    if isinstance(download_path, list):
        return download_path[0]

    Websites.manganelo.download_manganelo_tv(url, to_save, download_path, manga_name)

    return "Download finished. Enjoy !"

def manganelo_com(url):
    pre_chapters = Websites.manganelo.nb_chp_manganelo(url)
    chapters, chapters_to_save, manga_name = pre_chapters
    manga_name = functions_os.delete_non_creatable_symbols('_'.join(manga_name[4:-5].split(' ')))

    print('Total : ' + str(len(chapters)) + ' chapter(s) found (' + str(chapters[0]) + ' to ' + str(chapters[-1]) + ')')
    ask_to_save = input('Chapters to save : ')

    pre_to_save = functions_chapters.asked_chapters(chapters, chapters_to_save, ask_to_save)
    if isinstance(pre_to_save, str):
        return pre_to_save

    to_save = functions_chapters.couples_of_chapters(pre_to_save)

    download_path = functions_os.asked_path()
    if isinstance(download_path, list):
        return download_path[0]

    Websites.manganelo.download_manganelo_com(url, to_save, download_path, manga_name)

    return "Download finished. Enjoy !"