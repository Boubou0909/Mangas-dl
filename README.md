Hi there !

The goal here is to let you download your favorite mangas from scan websites, and to convert them automatically into pdf files. Thus, it's easier to read when you don't have an internet access, or if you just don't want ad.

# Installation

To install it, you must have a [Python interpreter](https://www.python.org/) installed, with a working pip.
Then, you can use the pip command :

    pip install mangas-dl

This command will update mangas-dl if you already have it. See the [PyPI page](https://pypi.org/project/mangas-dl/).

Other ways of download are going to be added.

# Description

**mangas-dl** is a command-line program to download manga scans from multiple websites ([list of websites taken in charge](https://github.com/Boubou0909/Mangas-dl#list-of-websites-staken-in-charge)).
It requires a [Python interpreter](https://www.python.org/), and is not platform specific.
It is released to the public domain, so you can use it, modify it, redistribute it however you want.

    mangas-dl

# One-line mode

To launch the one-line mode, you have to run the command :
    mangas-dl [OPTIONS] URL

The only option to be filled in is the path where you want the scans to be saved.
By default, all the chapters are downloaded and the default language is english.

## Options
    -h, --help                          Print help text and exit

    --version                           Print the current version and exit
    
    -p, --path                          Path to the folder where the scans will be downloaded

    -l, --language                      Choose the language with the language code (see language_codes.json)
    
    -c, --chapters                      Choose which chapters will be downloaded (see the format in
                                        the interactive mode description)

# Interactive mode

To launch the interactive mode, you have to run the .exe file with the command :
    mangas-dl

## Answers format

In the interactive mode, you will have to answer questions to specify what you want to download exactly. To make the program understand your answers, make sure to use those formats :

- **Manga's main page** : URL of the main page of the manga ([See this section for further informations](https://github.com/Boubou0909/Mangas-dl#example-of-mangas-main-page)).
- **Language** *optional* : Give the number correponding to the language you want to choose.
- **Chapters to download** : Give the numbers of the first and the last chapters you want to download, separated by a dash. If you want to download several intervals, separate them by a slash. To download all chapters, you can enter just '*', '-1' or leave blank.
- **Destination folder** : Give the absolute path to the folder where the scans will be located. A new folder will be created inside with the name of the manga.
- **Y/N questions** : Answer with 'Y'/'y'/1 or 'N'/'n'/0

# Commands

To launch a command, the general usage is :
    mangas-dl <command> [OPTIONS]

## Remember preferences 
    save_path PATH                      Remember PATH to be the default folder where the scans 
                                        will be downloaded

    save_language LANGUAGE_CODE         Remember LANGUAGE_CODE to be the default language if a choice
                                        is possible

## Use remembered informations

You can reuse remembered informations in one-line mode : instead of a path, you can write "%" if a path is remembered, and you can leave language blank if a choice is possible (english will be taken if the language is not available). 

# List of websites taken in charge

- [https://mangadex.org/](https://mangadex.org/)
- [https://manganelo.tv/](https://manganelo.tv/)

# Examples

## Example of mangas' main page

- mangadex.org : [https://mangadex.org/title/32d76d19-8a05-4db0-9fc2-e0b0648fe9d0](https://mangadex.org/title/32d76d19-8a05-4db0-9fc2-e0b0648fe9d0)
- manganelo.tv : [https://manganelo.tv/manga/manga-dr980474](https://manganelo.tv/manga/manga-dr980474)

## Example of one-line mode command

    mangas-dl -p C:\This\is\a\path -c 1-7 https://mangadex.org/title/a96676e5-8ae2-425e-b549-7f15dd34a6d8
    
## Example of interactive mode command

    > mangas-dl
    Enter the main page of the manga you want to download : https://mangadex.org/title/a96676e5-8ae2-425e-b549-7f15dd34a6d8
    17 languages have been found.
    0 -> Italian
    1 -> Turkish
    2 -> Indonesian
    3 -> Russian
    4 -> Portuguese (Brasil)
    5 -> English
    6 -> Filipino
    7 -> Persian
    8 -> Dutch
    9 -> Mongolian
    10 -> Czech
    11 -> Hungarian
    12 -> Spanish (LATAM)
    13 -> French
    15 -> Hindi
    16 -> Romanian
    Choose a language (number) : 5
    192 chapters have been found (from 1.0 to 296.0).
    Which chapter(s) would you like to download ? 1-7
    Destination folder : C:\Users\balth\Documents\Scans
    Do you want to save this path ? (Y/N) N
    Download finished successfully. Enjoy !

## Example of save functions

    > mangas-dl save_path C:/This/is/a/path
    Path "C:/users/balth/Documents/Scans" learnt
    
    > mangas-dl -p % -c 1-2 https://mangadex.org/title/a96676e5-8ae2-425e-b549-7f15dd34a6d8
    Download finished successfully. Enjoy !

# FAQ

## Why is mangadex taking so much time compared to manganelo ?

The implementation of [https://mangadex.org/](https://mangadex.org/) is made with [mangadex's API](https://api.mangadex.org/docs.html) with the [python package MangaDex.py](https://github.com/Proxymiity/MangaDex.py). This is necessary because of the anti-DDOS system. Thus, web-scraping is impossible because it is too fast for the website (it will understand that you're using a bot). However, manganelo.tv : [https://manganelo.tv/manga/manga-dr980474](https://manganelo.tv/manga/manga-dr980474) doesn't have such system, so web scraping is possible, and is much faster.

## Will other websites be implemented in the future ?

Of course : the final goal is that everyone can download their mangas wherever they want, so if you have a website you would like to be added to this project (and if it's enough important to be really useful to other people), I will try to add it to this project.