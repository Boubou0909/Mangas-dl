import os
import sys
from requests_html import HTMLSession

from Headers.download_and_convert import download_and_convert_to_pdf

def manganelotv(url, chapters_asked, download_path, manga_name):
    if not os.path.exists(download_path + manga_name + os.path.sep):
        os.makedirs(download_path + manga_name + os.path.sep)
    download_path = download_path + manga_name + os.path.sep
    session = HTMLSession()

    url_chapter = url.split('/')
    url_chapter.append('chapter-')
    url_chapter[-3] = 'chapter'
    url_chapter = '/'.join(url_chapter)

    for chp_nb in chapters_asked:
        sys.stdout.write('\033[K')
        print('Loading chapter ', chp_nb[0], end='\r')

        if not os.path.exists(download_path + 'temp' + os.path.sep):
            os.makedirs(download_path + 'temp' + os.path.sep)
        
        r = session.get(url_chapter + chp_nb[0])
        images = r.html.find('.img-loading')
        src = [images[i].attrs['data-src'] for i in range(len(images))]

        download_and_convert_to_pdf(src, download_path, chp_nb)

def download_manganelo_com(url, chapters_asked, download_path, manga_name):
    if not os.path.exists(download_path + manga_name + os.path.sep):
        os.makedirs(download_path + manga_name + os.path.sep)
    download_path = download_path + manga_name + os.path.sep
    session = HTMLSession()

    url_chapter = url.split('/')
    url_chapter.append('chapter_')
    url_chapter[-3] = 'chapter'
    url_chapter = '/'.join(url_chapter)

    for chp_nb in chapters_asked:
        sys.stdout.write('\033[K')
        print('Loading chapter ', chp_nb[0], end='\r')

        if not os.path.exists(download_path + 'temp' + os.path.sep):
            os.makedirs(download_path + 'temp' + os.path.sep)
        
        r = session.get(url_chapter + chp_nb[0])
        div = r.html.find('.container-chapter-reader')[0].html.split("=")
        
        src = []
        for i in range(len(div)):
            if 'src' in div[i] and 'https://' in div[i+1]:
                src.append(div[i+1].split('"')[1])

        download_and_convert_to_pdf(src, download_path, chp_nb, referer=url_chapter)