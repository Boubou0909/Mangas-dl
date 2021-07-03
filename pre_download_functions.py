import os
from requests_html import HTMLSession

from Headers.functions_web import does_page_exists
from Headers.errors import ConnexionError
from Headers.functions import delete_non_numeric, delete_duplicate

def manganelo_pre_download(url):
    if not does_page_exists(url):
        raise ConnexionError(url)

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