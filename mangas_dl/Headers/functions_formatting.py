from .errors import InputError

def str_to_chapters(chapters, chapters_name, chapters_asked):
    
    pre_chapter_asked = []
    chapters_to_download = []
    if chapters_asked in ['', '-1', '*']:
        pre_chapter_asked = [(chapters[i], chapters_name[i]) for i in range(len(chapters))]
    else:
        try:
            chapters_asked = str(float(chapters_asked))
            i = chapters_name.index(chapters_asked)
            pre_chapter_asked = [(chapters[i], chapters_name[i])]
        except:
            for list in chapters_asked.split('/'):
                try:
                    begin, end = list.split('-')
                except:
                    raise InputError("The given format of chapters to download is not correct. Please check https://github.com/Boubou0909/Mangas-dl#answers-format.")
                
                try:
                    indice_begining = chapters_name.index(str(float(begin)))
                    indice_ending = chapters_name.index(str(float(end)))
                except:
                    pass

                try:
                    indice_begining = chapters.index(begin)
                    indice_ending = chapters.index(end)
                except:
                    pass
                
                if not "indice_begining" in locals() or not "indice_ending" in locals():
                    raise InputError("At least one of the chapter(s) asked doesn't exist.")

                if len(str(end).split('.')) > 1:
                    k = 0.1
                    while k < 1:
                        try:
                            indice_ending = chapters.index(str(float(end) + round(k,1)))
                        except:
                            pass
                        
                        k += 0.1

                for i in range(indice_begining, indice_ending + 1):
                    pre_chapter_asked.append((chapters[i], chapters_name[i]))
        
    for i in range(len(pre_chapter_asked)):
        chapters_to_download.append((pre_chapter_asked[i][0], pre_chapter_asked[i][1]))

    return chapters_to_download