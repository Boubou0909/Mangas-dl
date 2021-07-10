import os
from shutil import rmtree
import sys
import configparser
from requests_html import HTMLSession
from PIL import Image

from MangaDexPy import downloader
from imgurpython import ImgurClient

from .Headers.download_and_convert import convert_to_pdf, download_and_convert_to_pdf
from .Headers.functions import str_at_least_n
from .Headers.functions_os import enable_print, disable_print

def download_manganelo_tv(url, chapters_asked, download_path, manga_name):
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

    for chp_src, chp_nb in chapters_asked:
        sys.stdout.write('\033[K')
        print('Loading chapter ', chp_src, end='\r')

        if not os.path.exists(download_path + 'temp' + os.path.sep):
            os.makedirs(download_path + 'temp' + os.path.sep)
        
        r = session.get(url_chapter + chp_src)
        div = r.html.find('.container-chapter-reader')[0].html.split("=")
        
        src = []
        for i in range(len(div)):
            if 'src' in div[i] and 'https://' in div[i+1]:
                src.append(div[i+1].split('"')[1])

        download_and_convert_to_pdf(src, download_path, chp_nb, referer=url_chapter)

def download_mangadex_org(url, chapters_asked, download_path, manga_name):
    if not os.path.exists(download_path + manga_name + os.path.sep):
        os.makedirs(download_path + manga_name + os.path.sep)
    download_path = download_path + manga_name + os.path.sep

    for chp_src, chp_nb in chapters_asked:
        sys.stdout.write('\033[K')
        print('Loading chapter ', chp_nb, end='\r')

        if not os.path.exists(download_path + 'temp' + os.path.sep):
            os.makedirs(download_path + 'temp' + os.path.sep)

        disable_print()
        downloader.dl_chapter(chp_src, download_path + 'temp' + os.path.sep)
        enable_print()

        extensions = [code.split('.')[-1] for code in chp_src.pages]

        img_list = []
        for i in range(len(chp_src.pages)):
            img_list.append(Image.open(download_path + 'temp' + os.path.sep + str_at_least_n(i + 1, len(str(len(chp_src.pages)))) + '.' + extensions[i]).convert('RGB'))

        convert_to_pdf(img_list, download_path + 'chp_' + chp_nb + '.pdf')

        rmtree(download_path + 'temp' + os.path.sep)

def download_cubari_moe(url, chapters_asked, download_path, manga_name):
    if not os.path.exists(download_path + manga_name + os.path.sep):
        os.makedirs(download_path + manga_name + os.path.sep)
    download_path = download_path + manga_name + os.path.sep

    config = configparser.ConfigParser()
    config.read("mangas_dl/conf.ini")    

    client = ImgurClient(config["IMGUR"]["ClientID"], config["IMGUR"]["ClientSecret"])

    for chp_src, chp_nb in chapters_asked:
        sys.stdout.write('\033[K')
        print('Loading chapter ', chp_nb, end='\r')
        
        if not os.path.exists(download_path + 'temp' + os.path.sep):
            os.makedirs(download_path + 'temp' + os.path.sep)

        album = client.get_album(chp_src)
        srcs = [img["link"] for img in album.images]

        download_and_convert_to_pdf(srcs, download_path, chp_nb)