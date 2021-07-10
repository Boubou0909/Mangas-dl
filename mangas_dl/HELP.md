Usage : 
    mangas-dl [OPTIONS] URL

or :
    mangas-dl <command> [OPTIONS]

Complete help here : https://github.com/Boubou0909/Mangas-dl

Options :
    -h, --help                      Print this help text and exit
    -v, --version                   Print program version and exit

    -p, --path                      Path to the folder where the scans will be downloaded (needed)
    -l, --language                  Choose the language with the language code (see 
                                    https://github.com/Boubou0909/Mangas-dl/blob/main/mangas_dl/language_codes.json)
    -c, --chapters                  Choose which chapters will be downloaded (see the format in
                                    the interactive mode description)

    -n, --name                      Change the name of the final folder (where the chapter(s) 
                                    will be downloaded). If not specified, an automatic one will
                                    be used (the one available on the main page given). Put the name in 
                                    quotes if it has more than one word.

    --list                          Print the complete list of available chapters with the settings
                                    (path not necessary) without download them. Relaunch another 
                                    command to download choosen ones.

Commands :
    save_path                       Remember PATH to be the default folder where the scans 
                                    will be downloaded (use % instead of the path)

    save_language                   Remember LANGUAGE_CODE to be the default language if a choice
                                    is possible (english if the language is not available)