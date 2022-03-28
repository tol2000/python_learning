import cv2

FRONTAL_FACE = "haarcascade_frontalface_default.xml"
# FRONTAL_FACE = "haarcascade_profileface.xml"
faces_cascade_db = cv2.CascadeClassifier(cv2.data.haarcascades + FRONTAL_FACE)

WIN_NAME = 'image'
cv2.namedWindow(WIN_NAME, flags=cv2.WINDOW_NORMAL)
cv2.moveWindow(WIN_NAME, 1, 1)
cv2.resizeWindow(WIN_NAME, 1800, 800)

FRAMES_UPDATE_HISTORY_PERIOD = 1
FRAMES_HISTORY_MAX_SIZE = 50

history = []
frames_count = FRAMES_UPDATE_HISTORY_PERIOD


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


def select_tracked(cap):
    global history
    history = []
    # clear the image first
    success, img = cap.read()
    show_img(
        img, win_title='Select a ROI and then press SPACE or ENTER button (c - cancel)', wait4key=False
    )
    t_square = cv2.selectROI(WIN_NAME, img)
    tracker = cv2.TrackerKCF_create()
    tracker.init(img, t_square)
    return tracker


def update_tracker(img, tracker):
    global frames_count
    global history
    pt1, pt2, color, thickness = None, None, None, None
    ok, (x, y, w, h) = tracker.update(img)

    if ok:
        if frames_count < FRAMES_UPDATE_HISTORY_PERIOD:
            frames_count += 1
        else:
            frames_count = 0
            if len(history) > FRAMES_HISTORY_MAX_SIZE:
                history = []
            history.append((int(x), int(y), int(w), int(h)))
            pt1 = (int(x), int(y))
            pt2 = (int(x + w), int(y + h))
            b = int(x * w) % 255
            g = int(y * h) % 255
            color = (b, g, 255)
            thickness = 2
        if pt1 and pt2 and color and thickness:
            cv2.rectangle(img, pt1, pt2, color, thickness)

        for (x, y, w, h) in history:
            w_center = w // 2
            h_center = h // 2
            pt1 = (x + w_center, y + h_center)
            pt2 = (x + w_center + 1, y + h_center + 1)
            b = int(x * w) % 255
            g = int(y * h) % 255
            color = (b, g, 255)
            thickness = 2
            cv2.rectangle(img, pt1, pt2, color, thickness)


def main():
    cap = cv2.VideoCapture(0)
    try:
        tracker = None
        key = ' '

        while key != 'q':
            success, img = cap.read()
            if tracker:
                update_tracker(img, tracker)

            if key == 't':
                tracker = select_tracked(cap)

            key = show_img(img, win_title='Cam (q - exit, t - track object)', wait4key=False)
    finally:
        cap.release()


if __name__ == '__main__':
    main()
    cv2.destroyAllWindows()
