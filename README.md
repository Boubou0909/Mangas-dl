Hi there !

The goal here is to let you download your favorite mangas from scan websites, and to convert them automatically into pdf files. Thus, it's easier to read when you don't have an internet access, or if you just don't want ad.

# Installation

To run it on every platform, you can compile mangas-dl.py with a Python interpreter.
However, it's not convenient, so other ways of installation will be added later.

# Description

**mangas-dl** is a command-line program to download manga scans from multiple websites ([list of websites taken in charge]()).
It requires a [Python interpreter](https://www.python.org/), and is not platform specific.
It is released to the public domain, so you can use it, modify it, redistribute it however you want.

*If you redistribute it elsewhere, please credit this GitHub repository.*

    mangas-dl

Nowadays, only the interactive mode works, but the one-line command will be added in the future.

# Answers format

In the interactive mode, you will have to answer questions to specify what you want to download exactly. To make the program understand your answers, make sure to use those formats :

- **Manga's main page** : URL of the main page of the manga ([See this section for further informations]()).
- **Language** *optional* : Give the number correponding to the language you want to choose.
- **Chapters to download** : Give the numbers of the first and the last chapters you want to download, separated by a dash. If you want to download several intervals, separate them by a slash. To download all chapters, you can enter just '*', '-1' or leave blank.
- **Destination folder** : Give the absolute path to the folder where the scans will be located. A new folder will be created inside with the name of the manga.
- **Y/N questions** : Answer with 'Y'/'y'/1 or 'N'/'n'/0

# Examples

    mangas-dl
    Enter the main page of the manga you want to download : https://mangadex.org/title/a96676e5-8ae2-425e-b549-7f15dd34a6d8
    17 languages have been found.
    0 -> Italian
    1 -> Turkish
    2 -> Indonesian
    3 -> Russian
    4 -> Portuguese (Brasil)
    5 -> English
    6 -> tl
    7 -> fa
    8 -> nl
    9 -> mn
    10 -> Chinese
    11 -> Hungarian
    12 -> Spanish (LATAM)
    13 -> French
    15 -> Hindi
    16 -> Romanian
    Choose a language (number) : 5
    192 chapters have been found (from 1.0 to 296.0).
    Which chapter(s) would you like to download ? 1.0-7.0
    Destination folder : C:\Users\balth\Documents\Scans
    Do you want to save this path ? (Y/N) N
    Download finished successfully. Enjoy !
