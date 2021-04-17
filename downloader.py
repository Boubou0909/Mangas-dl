#!/usr/bin/python

import website_function

launch_functions = {
    'manganelo.tv' : website_function.manganelo_tv,
    'manganelo.com' : website_function.manganelo_com
}
known_sites = launch_functions.keys()

url = input("Main page of the manga : ")

pre_process = url.split('/')

def main():
    try:
        site_name = pre_process[2]
    except:
        return 'Incorrect input : try using one of those websites : ' + ", ".join(known_sites)

    if not site_name in known_sites:
        return 'Unknow website : ' + site_name + '\nTry using one of those : ' + ", ".join(known_sites)

    return launch_functions[site_name](url)

print(main())