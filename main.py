# coding:utf-8
import os
import sys
from PIL import Image, ImageStat


def dirFilesWithCallBack(dir: str):
    for root, dirs, files in os.walk(dir):
        for name in files:
            path = os.path.join(root, name)
            yield path


def isPngNoAlpha(path: str):
    img = Image.open(path, 'r')
    img = img.convert("RGBA")
    stat = ImageStat.Stat(img)
    return (stat.extrema[3] == (255, 255))


def callBack(path: str):
    ext = os.path.splitext(path)[-1]
    if (ext == '.png' and not ".9" in path):
        if (isPngNoAlpha(path)):
            print(path)
            return os.path.getsize(path) / 1024
    return 0


if __name__ == '__main__':
    all_size = 0
    respngs = dirFilesWithCallBack('res')
    for x in respngs:
        all_size += callBack(x)
    assetspngs = dirFilesWithCallBack('assets')
    for x in assetspngs:
        all_size += callBack(x)

    print("%s Kb" % int(all_size))
