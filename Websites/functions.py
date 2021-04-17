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