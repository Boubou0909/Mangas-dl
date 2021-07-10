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

    -n, --name                          Change the name of the final folder (where the chapter(s) 
                                        will be downloaded). If not specified, an automatic one will
                                        be used (the one available on the main page given). Put the name in 
                                        quotes if it has more than one word.

    --list                              Print the complete list of available chapters with the settings
                                        (path not necessary) without download them. Relaunch another 
                                        command to download choosen ones.

# Interactive mode

To launch the interactive mode, you have to run the .exe file with the command :
    mangas-dl

## Answers format

In the interactive mode, you will have to answer questions to specify what you want to download exactly. To make the program understand your answers, make sure to use those formats :

- **Manga's main page** : URL of the main page of the manga ([See this section for further informations](https://github.com/Boubou0909/Mangas-dl#example-of-mangas-main-page)).
- **Language** *optional* : Give the number correponding to the language you want to choose.
- **Chapters to download** : Give the numbers of the first and the last chapters you want to download, separated by a dash. If you want to download several intervals, separate them by a slash. If the number of the first and the last chapters are integers, you can write them normally. If not, you have to specify with float numbers. To download all chapters, you can enter just '*', '-1' or leave blank. Moreover, you can tap "list" to have the complete list of the chapters that have been found, then the program will reask you the same question ("list" option won't be available the second time).
- **Name of the final folder** : Name of new folder where the chapter(s) will be downloaded. To make it automatic, you can leave this field blank.
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
- [https://cubari.moe/](https://cubari.moe/)

# Examples

## Example of mangas' main page

- mangadex.org : [https://mangadex.org/title/32d76d19-8a05-4db0-9fc2-e0b0648fe9d0](https://mangadex.org/title/32d76d19-8a05-4db0-9fc2-e0b0648fe9d0)
- manganelo.tv : [https://manganelo.tv/manga/manga-dr980474](https://manganelo.tv/manga/manga-dr980474)
- cubari.moe (several chapters): [https://cubari.moe/read/gist/JO7JN/](https://cubari.moe/read/gist/JO7JN/)
- cubari.moe (one chapter) : [https://cubari.moe/read/imgur/Xo1KODZ/](https://cubari.moe/read/imgur/Xo1KODZ/)

## Examples of one-line mode command

    > mangas-dl -p C:\This\is\a\path -c 1-7 https://mangadex.org/title/a96676e5-8ae2-425e-b549-7f15dd34a6d8
    
    > mangas-dl -n "Kumo desu ga !" -p % -l nl https://mangadex.org/title/eb2d1a45-d4e7-4e32-a171-b5b029c5b0cb

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

## Example of a command in interactive mode using listing of all chpaters

    > mangas-dl
    Enter the main page of the manga you want to download : https://manganelo.tv/manga/manga-dr980474
    162 chapters have been found (from 000.0 to 157.0).
    Which chapter(s) would you like to download ? list       
    000.0  001.0  002.0  003.0  004.0  005.0  006.0  007.0  008.0  009.0  
    010.0  011.0  012.0  013.0  014.0  015.0  016.0  017.0  018.0  019.0
    020.0  021.0  022.0  023.0  024.0  025.0  026.0  027.0  028.0  029.0
    030.0  031.0  032.0  033.0  034.0  035.0  036.0  037.0  038.0  039.0
    040.0  041.0  042.0  043.0  044.0  045.0  046.0  047.0  048.0  049.0
    050.0  051.0  052.0  053.0  054.0  055.0  056.0  057.0  058.0  059.0
    060.0  061.0  062.0  063.0  064.0  065.0  066.0  067.0  068.0  069.0
    070.0  071.0  072.0  073.0  074.0  075.0  076.0  077.0  078.0  079.0
    080.0  081.0  082.0  083.0  084.0  085.0  086.0  087.0  088.0  089.0  
    090.0  090.1  090.2  091.0  092.0  093.0  094.0  095.0  096.0  097.0
    098.0  099.0  100.0  101.0  102.0  103.0  104.0  105.0  106.0  107.0
    108.0  109.0  110.0  110.5  111.0  112.0  113.0  114.0  115.0  116.0
    117.0  118.0  119.0  120.0  121.0  122.0  123.0  124.0  125.0  126.0
    127.0  128.0  129.0  129.1  130.0  131.0  132.0  133.0  134.0  135.0
    136.0  137.0  138.0  139.0  140.0  141.0  142.0  143.0  144.0  145.0
    146.0  147.0  148.0  149.0  150.0  151.0  152.0  153.0  154.0  155.0
    156.0  157.0  156.0  157.0
    Which chapter(s) would you like to download ? 0-5                                      
    The path "C:/users/balth/Documents/Scans" is known. Do you want to use it ? (Y/N) Y
    Name of the final folder : Leveling alone
    Download finished successfully. Enjoy !

## Example of a one-line listing command

    > mangas-dl -l fr --list https://mangadex.org/title/a96676e5-8ae2-425e-b549-7f15dd34a6d8
    1.0  2.0  3.0  4.0  5.0  6.0  7.0  8.0  9.0  10.0  
    11.0  12.0  13.0  13.5  14.0  15.0  16.0  17.0  18.0  19.0
    19.5  20.0  21.0  22.0  23.0  24.0  25.0  26.0  27.0  28.0
    29.0  30.0  31.0  32.0  33.0  34.0  34.5  35.0  36.0  37.0
    38.0  39.0  40.0  41.0  42.0  43.0  44.0  45.0  46.0  47.0
    47.5  48.0  49.0  50.0  51.0  52.0  53.0  54.0  55.0  56.0
    57.0  57.5  58.0  59.0  60.0  61.0  62.0  63.0  64.0  65.0
    66.0  67.0  68.0  69.0  70.0  71.0  72.0  72.5  73.0  74.0  
    75.0  76.0  77.0  78.0  79.0  80.0  81.0  82.0  83.0  84.0
    85.0  85.5  86.0  87.0  88.0  89.0

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