from PIL import Image
import os
import sys

path = 'anger/'
new_path = 'dataset2/'

dirs = os.listdir(path)


def resize():
    for item in dirs:
        if os.path.isfile(path + item):
            im = Image.open(path + item)
            f, e = os.path.splitext(new_path + item)
            imResize = im.resize((1024, 1024), Image.ANTIALIAS)
            imResize.save(f + '.png', 'PNG', quality=95)


resize()
