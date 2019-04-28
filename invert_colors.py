import cv2
import urllib.request as urllib
import urllib.parse as urlparse
import numpy as np


def download_image(url):
    try:
        with urllib.urlopen(url) as dlFile:
            content = dlFile.read()
            filename = urlparse.urlparse(url).path.replace('/', '') + ".png"
            file = open(filename, "wb")
            file.write(content)
            file.close
        print(url + " was saved as " + filename)
        return filename
    except Exception as e:
        print(e)


def inverte(imagem, name):
    imagem = (255-imagem)
    cv2.imwrite(name, imagem)

# def inverte2(imagem, name):
#     for x in np.nditer(imagem, op_flags=['readwrite']):
#         x = abs(x - 255)
#     cv2.imwrite(name, imagem)


if __name__ == '__main__':
    img_url = "https://images.unsplash.com/photo-1556162748-a6ae062a7fa3"
    fn = download_image(img_url)
    image = cv2.imread(fn)
    #gs_imagem = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    inverte(gs_imagem, fn)
    #inverte2(gs_imagem, fn)

