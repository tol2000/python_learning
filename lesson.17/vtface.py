import os
from pathlib import Path
import cv2
import numpy as np

FRONTAL_FACE = "haarcascade_frontalface_default.xml"
# FRONTAL_FACE = "haarcascade_profileface.xml"
faces_cascade_db = cv2.CascadeClassifier(cv2.data.haarcascades + FRONTAL_FACE)

WIN_NAME = 'image'
cv2.namedWindow(WIN_NAME, flags=cv2.WINDOW_NORMAL)
cv2.moveWindow(WIN_NAME, 1, 1)
cv2.resizeWindow(WIN_NAME, 1800, 800)

FRAMES_PERIOD = 10


def show_img(img, win_title='-', wait4key=True):
    cv2.setWindowTitle(winname=WIN_NAME, title=win_title)
    cv2.imshow(WIN_NAME, img)
    if wait4key:
        key = chr(cv2.waitKey())
    else:
        key = cv2.pollKey()
        if key >= 0:
            key = chr(key)
    return key


def find_faces(img):
    faces = faces_cascade_db.detectMultiScale(img)
    squares = []
    for i, (x, y, w, h) in enumerate(faces, start=1):
        pt1 = (x, y)
        pt2 = (x + w, y + h)
        b = (i * 10 + int(x) * i) % 255
        g = (i * 25 + int(y) * i) % 255
        color = (b, g, 255)
        thickness = 2
        squares.append((pt1, pt2, color, thickness))
    return squares


def main():
    cap = cv2.VideoCapture(0)
    try:
        key = ' '
        frames = FRAMES_PERIOD
        squares = []
        while key != 'q':
            success, img = cap.read()
            if frames < FRAMES_PERIOD:
                frames += 1
            else:
                frames = 0
                squares = find_faces(img)
            for pt1, pt2, color, thickness in squares:
                cv2.rectangle(img, pt1, pt2, color, thickness)
            key = show_img(img, wait4key=False)
    finally:
        cap.release()


if __name__ == '__main__':
    main()
    cv2.destroyAllWindows()
