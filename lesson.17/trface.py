import cv2

FRONTAL_FACE = "haarcascade_frontalface_default.xml"
# FRONTAL_FACE = "haarcascade_profileface.xml"
faces_cascade_db = cv2.CascadeClassifier(cv2.data.haarcascades + FRONTAL_FACE)

WIN_NAME = 'image'
cv2.namedWindow(WIN_NAME, flags=cv2.WINDOW_NORMAL)
cv2.moveWindow(WIN_NAME, 1, 1)
cv2.resizeWindow(WIN_NAME, 1800, 800)

FRAMES_UPDATE_HISTORY_PERIOD = 0
FRAMES_HISTORY_MAX_SIZE = 1000

tracking_history = []
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
    global tracking_history
    tracking_history = []
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
    global tracking_history
    pt1, pt2 = None, None
    ok, (x, y, w, h) = tracker.update(img)

    if ok:
        if frames_count < FRAMES_UPDATE_HISTORY_PERIOD:
            frames_count += 1
        else:
            # Calculating current tracking rectangle and tracking line history
            frames_count = 0
            if len(tracking_history) > FRAMES_HISTORY_MAX_SIZE:
                tracking_history = []
            pt1 = (int(x), int(y))
            pt2 = (int(x + w), int(y + h))
            tracking_history.append((int(x + w // 2), int(y + h // 2)))

        if pt1 and pt2:
            # drawing current tracking rectangle
            cv2.rectangle(img, pt1, pt2, color=(0, 0, 255), thickness=1)

        # drawing tracking line history
        for i, point in enumerate(tracking_history):
            pt2 = point
            pt1 = tracking_history[i - 1] if i > 0 else pt2
            cv2.line(img, pt1, pt2, color=(0, 255, 0), thickness=1)


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
