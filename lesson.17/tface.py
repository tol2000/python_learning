import os
# from pathlib import Path
import cv2
import numpy as np

FRONTAL_FACE = "haarcascade_frontalface_default.xml"
# PROFILE_FACE = "haarcascade_profileface_default.xml"
PATH = '/media/sf_VBOX_PUBLIC/temp/Photos/'

faces_cascade_db = cv2.CascadeClassifier(cv2.data.haarcascades + FRONTAL_FACE)


def show_img(img):
    win_name = 'Image'
    cv2.namedWindow(win_name, flags=cv2.WINDOW_NORMAL)
    cv2.moveWindow(win_name, 1, 1)
    cv2.resizeWindow(win_name, 1800, 800)
    cv2.imshow(win_name, img)
    cv2.waitKey()


def main2():

    # profile
    # p = '/media/sf_VBOX_PUBLIC/temp/Photos/DSLR/Репортаж/События/ДР_Одессы_2008/2008-09-03_01-10__DSC0042.jpg'

    # frontal
    # p = '/media/sf_VBOX_PUBLIC/temp/Photos/DSLR/Репортаж/На_работе/НГ_2006//D01_9139.jpg'
    p = '/media/sf_VBOX_PUBLIC/temp/Photos/DSLR/Репортаж/На_работе/НГ_2007_2008/D200805_3250_002.jpg'

    img = cv2.imread(p)
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
    show_img(img)


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
