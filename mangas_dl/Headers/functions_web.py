import requests
from requests_html import HTML, HTMLSession

def does_page_exists(url):
    session = HTMLSession()

    try:
        r = session.get(url)
        return r.status_code == 200
    except:
        return False

def download_image(url, download_path, name, referer = ""):
    headers = {
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 OPR/73.0.3856.434",
        "referer" : referer
        }

    image = requests.get(url, stream=True, headers=headers).content
    f = open(download_path + name, 'wb+')
    f.write(image)
    f.close()