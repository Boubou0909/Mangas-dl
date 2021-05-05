def asked_chapters(chapters, chapters_to_save, ask_to_save):
    to_save = []
    
    if ask_to_save in ['', '-1', '*']:
        to_save = [(chapters[i], chapters_to_save[i]) for i in range(len(chapters))]
    else:
        for list in ask_to_save.split('/'):
            try:
                begin, end = list.split('-')
            except:
                return 'The format given to choose the chpaters is not correct. Example of correct format : 2-5/9.5-17'
            
            try:
                indice_begining = chapters.index(begin)
                indice_ending = chapters.index(end)
            except:
                return 'One of the asked chapters doesn\'t exist.'

            if float(end) == int(end):
                k = 0.1
                while k < 1:
                    try:
                        indice_ending = chapters.index(str(float(end) + round(k,1)))
                    except:
                        pass
                    
                    k += 0.1

            for i in range(indice_begining, indice_ending + 1):
                to_save.append((chapters[i],chapters_to_save[i]))

    return to_save

def couples_of_chapters(to_save):
    chapters_to_save = []
    for i in range(len(to_save)):
        chapters_to_save.append((to_save[i][0], to_save[i][1]))
    return chapters_to_save