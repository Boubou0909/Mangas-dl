def ask_until_y_or_n(question):
    var = ''
    while not var in ['Y', 'y', 'N', 'n', 0, 1]: 
        var = input(question + ' (Y/N) ')
    return var in ['y', 'Y', 1]

def delete_duplicate(list):
    seen = set()
    seen_add = seen.add
    return [x for x in list if not (x in seen or seen_add(x))]

def delete_non_numeric(string):
    valid = ''
    for i in range(len(string)):
        if string[i].isnumeric() or string[i] == '.':
            valid += string[i]
    return valid

def str_at_least_n(i, n):
    nb = str(i)
    while len(nb) < n:
        nb = "0" + nb
    return nb