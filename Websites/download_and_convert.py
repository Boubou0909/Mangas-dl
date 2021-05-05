import os
from shutil import rmtree
from PIL import Image

from .functions_web import download_image

def download_and_convert(srcs, download_path, chp_nb, referer=''):
    
    img_list = []
    for j in range(len(srcs)):
        ext = srcs[j].split('.')[-1]

        download_image(srcs[j], download_path + 'temp' + os.path.sep, 'chp_' + chp_nb[1] + '_' + str(j) + '.' + ext, referer=referer + chp_nb[0])
        img_list.append(Image.open(download_path + 'temp' + os.path.sep + 'chp_' + chp_nb[1] + '_' + str(j) + '.' + ext).convert('RGB'))

    if len(img_list) > 0:
        image = img_list.pop(0)
        image.save(download_path + 'chp_' + chp_nb[1] + '.pdf', save_all=True, append_images=img_list)

    rmtree(download_path + 'temp' + os.path.sep)