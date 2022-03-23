# profile
# p = '/media/sf_VBOX_PUBLIC/temp/Photos/DSLR/Репортаж/События/ДР_Одессы_2008/2008-09-03_01-10__DSC0042.jpg'

# frontal
# p = '/media/sf_VBOX_PUBLIC/temp/Photos/DSLR/Репортаж/На_работе/НГ_2006//D01_9139.jpg'
IMAGE_NAME = '/media/sf_VBOX_PUBLIC/temp/Photos/DSLR/Репортаж/На_работе/НГ_2007_2008/D200805_3250_002.jpg'
PATH = '/media/sf_VBOX_PUBLIC/temp/Photos/'

import os
from pathlib import Path
import cv2
import numpy as np

WIN_NAME = 'image'

cv2.namedWindow(WIN_NAME, flags=cv2.WINDOW_NORMAL)
cv2.moveWindow(WIN_NAME, 1, 1)
cv2.resizeWindow(WIN_NAME, 1800, 800)


def show_img(img, win_title='-'):
    cv2.setWindowTitle(winname=WIN_NAME, title=win_title)
    cv2.imshow(WIN_NAME, img)
    key = chr(cv2.waitKey())
    return key


def find_faces(img, xml_full_name):
    faces_cascade_db = cv2.CascadeClassifier(xml_full_name)
    # img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faces_cascade_db.detectMultiScale(img)
    for i, (x, y, w, h) in enumerate(faces):
        pt1 = (x, y)
        pt2 = (x + w, y + h)
        b = (i * 10 + int(x) * i) % 255
        g = (i * 25 + int(y) * i) % 255
        color = (b, g, 255)
        thickness = 2
        cv2.rectangle(img, pt1, pt2, color, thickness)


def main2():
    xml_list = []
    for root, dirs, files in os.walk(cv2.data.haarcascades):
        for c_file in files:
            if c_file.lower().endswith('.xml') and c_file.__contains__('eye'):
                xml_list.append(str(Path(root) / Path(c_file)))

    i = 0
    loop = True
    while loop:
        img = cv2.imread(IMAGE_NAME)
        find_faces(img, xml_list[i])
        key = show_img(img, f'[{i} of {len(xml_list)-1}] {xml_list[i]} (q - exit)')
        i = i+1 if i < len(xml_list)-1 else 0
        if key.lower() == 'q':
            loop = False


def main1():
    shape = (480, 640, 3)
    img = np.zeros(shape, np.uint8)
    img[...] = [170, 255, 255]
    show_img(img)


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
    main2()
    cv2.destroyAllWindows()
