import os
from shutil import rmtree
from requests_html import HTML, HTMLSession
from PIL import Image

from .functions_web import page_exists, download_image
from .functions import delete_duplicate, delete_non_numeric

def nb_chp_manganelo(url):
    if not page_exists(url):
        return 'This page doesn\'t exist : try another one.'

    session = HTMLSession()
    r = session.get(url)
    manga_name = r.html.find('h1')[0].html

    url_chapter1 = url.split('/')
    url_chapter1[-2] = 'chapter'
    url_chapter1.append('chapter_')
    url_chapter1 = '/'.join(url_chapter1) + '1'
    
    if not page_exists(url_chapter1):
        return 'This manga has no chapter, or the issue is unknown.'

    r = session.get(url_chapter1)

    pre_chapters = r.html.find('.navi-change-chapter')[0].html.split(" ")

    chapters = []
    chapters_to_save = []
    for i in range(len(pre_chapters)-2, -1, -1):
        if 'Chapter' in pre_chapters[i]:
            chapters.append(delete_non_numeric(pre_chapters[i+1].split('\n')[0]))
            
    chapters = delete_duplicate(chapters)
    for i in range(len(chapters)):
        chapters_to_save.append(chapters[i])
        if ':' in chapters_to_save[-1][-1]:
            chapters_to_save[-1] = chapters_to_save[-1][:-1]

        if not '.' in chapters_to_save[-1]:
            chapters_to_save[-1] += '.0'
        while len(chapters_to_save[-1]) < 5:
            chapters_to_save[-1] = '0' + chapters_to_save[-1]

    return chapters, chapters_to_save, manga_name

def download_manganelo_tv(url, to_save, download_path, manga_name):
    download_path = download_path.rstrip(os.path.sep) + os.path.sep
    if not os.path.exists(download_path + manga_name + os.path.sep):
        os.makedirs(download_path + manga_name + os.path.sep)
    download_path = download_path + manga_name + os.path.sep
    session = HTMLSession()

    url_chapter = url.split('/')
    url_chapter.append('chapter_')
    url_chapter[-3] = 'chapter'
    url_chapter = '/'.join(url_chapter)

    for chp_nb in to_save:
        print('Loading chapter ', chp_nb[0])

        if not os.path.exists(download_path + 'temp' + os.path.sep):
            os.makedirs(download_path + 'temp' + os.path.sep)
        
        r = session.get(url_chapter + chp_nb[0])
        images = r.html.find('.img-loading')

        img_list = []
        for j in range(len(images)):
            src = images[j].attrs['data-src']
            ext = src.split('.')[-1]

            download_image(src, download_path + 'temp' + os.path.sep, 'chp_' + chp_nb[1] + '_' + str(j) + '.' + ext)
            img_list.append(Image.open(download_path + 'temp' + os.path.sep + 'chp_' + chp_nb[1] + '_' + str(j) + '.' + ext).convert('RGB'))

        if len(img_list) > 0:
            image = img_list.pop(0)
            image.save(download_path + 'chp_' + chp_nb[1] + '.pdf', save_all=True, append_images=img_list)

        rmtree(download_path + 'temp' + os.path.sep)