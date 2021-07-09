from requests_html import HTMLSession
import json

import MangaDexPy

from .Headers.functions_web import does_page_exists
from .Headers.errors import ConnexionError
from .Headers.functions import delete_non_numeric, delete_duplicate

try:
    with open("mangas_dl/language_codes.json") as file:
        LANGUAGE_CODES = json.load(file)
except:
    raise FileNotFoundError("The file websites_used.json has not been found. Please make sure it exists before lauching mangas-dl.")

def manganelo_pre_download(url, choosen_language):
    session = HTMLSession()
    r = session.get(url)
    manga_name = r.html.find('h1')[0].html[4:-5]

    url_chapter1 = url.split('/')
    url_chapter1[-2] = 'chapter'
    url_chapter1.append('chapter-')
    url_chapter1 = '/'.join(url_chapter1) + '1'
    
    if not does_page_exists(url_chapter1):
        raise ConnexionError(url_chapter1)

    r = session.get(url_chapter1)

    pre_chapters = r.html.find('.navi-change-chapter')[0].html.split(" ")

    chapters = []
    chapters_name = []
    for i in range(len(pre_chapters)-2, -1, -1):
        if 'Chapter' in pre_chapters[i]:
            test = delete_non_numeric(pre_chapters[i+1].split('\n')[0])
            if not test in ['.', '']:
                chapters.append(test)

    chapters = delete_duplicate(chapters)
    for i in range(len(chapters)):
        chapters_name.append(chapters[i])
        if ':' in chapters_name[-1]:
            chapters_name[-1] = chapters_name[-1][:-1]

        if not '.' in chapters_name[-1]:
            chapters_name[-1] += '.0'
        while len(chapters_name[-1]) < 5:
            chapters_name[-1] = '0' + chapters_name[-1]

    return chapters, chapters_name, manga_name

def mangadex_pre_download(url, choosen_language = -1):
    mangadex_client = MangaDexPy.MangaDex()
    manga = mangadex_client.get_manga(url.split('/')[-1])
    all_languages_chapters = manga.get_chapters()

    available_languages = delete_duplicate([chp.language for chp in all_languages_chapters])

    if len(available_languages) == 1:
        choosen_language = 0
    elif choosen_language == -1:
        print(len(available_languages), "languages have been found.")
        for i in range(len(available_languages)):
            try:
                print(i, "->", LANGUAGE_CODES[available_languages[i]])
            except:
                print(i, "->", available_languages[i])
        while choosen_language == -1:
            choosen_language = available_languages[int(input("Choose a language (number) : "))]

    chapters = [chp for chp in all_languages_chapters if chp.language == choosen_language]
    chapters_name = [chp.chapter for chp in chapters]

    i = 0
    while i < len(chapters_name):
        j = i + 1

        if chapters_name[i] == None:
            chapters_name.pop(i)
            chapters.pop(i)
            i -= 1
        else:
            while j < len(chapters_name):
                if chapters_name[i] == chapters_name[j]:
                    chapters_name.pop(j)
                    chapters.pop(j)
                    j -= 1
                j += 1
        i += 1

    chapters = [chp for _, chp in sorted(zip(list(map(float, chapters_name)), chapters), key=lambda pair : pair[0])]
    chapters_name = list(map(str, list(sorted(map(float, chapters_name)))))

    return chapters, chapters_name, manga.title["en"]