import os
import requests
from requests_html import HTMLSession

def page_exists(url):
    session = HTMLSession()
    
    try:
        r = session.get(url)
        return r.status_code == 200
    except:
        return False

def download_image(url, download_path, name):
    image = requests.get(url, stream=True).content

    f = open(download_path.rstrip(os.path.sep) + os.path.sep + name, 'wb')
    f.write(image)
    f.close()