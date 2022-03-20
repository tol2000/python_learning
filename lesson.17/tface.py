import os
# from pathlib import Path
import cv2

FRONTAL_FACE = "haarcascade_frontalface_default.xml"
PATH = '/media/sf_VBOX_PUBLIC/temp/Photos/'


def main1():
    p = '/media/sf_VBOX_PUBLIC/temp/Photos/DSLR/Репортаж/События/Бодибилдинг_Одесса_апрель_2007/D200708_3917.jpg'
    img = cv2.imread(p)
    cv2.imshow('Image', img)
    cv2.waitKey()


def main():
    count = 0
    for path, dirs, files in os.walk(PATH):
        for file in files:
            if file.lower().endswith('.jpg'):
                fname = path + os.sep + file
                img = cv2.imread(fname)
                print(count, img.shape, fname)
                count += 1
    print('Files qnty:', count)


if __name__ == '__main__':
    main1()
