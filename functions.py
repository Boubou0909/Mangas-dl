def ask_until_y_or_n(question):
    var = ''
    while not var in ['Y', 'y', 'N', 'n']: 
        var = input(question + ' (Y/N) ')
    return var in ['y', 'Y']