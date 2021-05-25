from showImageDimensions import dim
import cv2
import time
from fps import showfps

def human_detector(img):
    detection = cv2.CascadeClassifier('haarcascade_fullbody.xml')
    human = detection.detectMultiScale(img, 1.9, 1)
    for x, y, b, h in human:
        cv2.rectangle(img, (x, y), (x+b, y+h), (0, 255, 0), 2)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(img, 'Human', (x + 6, y - 6), font, 0.5, (0, 255, 0), 1)
    return img
def image():
    img = cv2.imread('image.jpg')
    human_detector(img)  
    x, y = dim(img)  
    res = cv2.resize(img, (x-120, y-120))
    cv2.imshow('Frame', res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def video():
    cap = cv2.VideoCapture('people.mp4')
    prev = time.time()
    fps = 0.0
    while cap.isOpened():
        _, frame = cap.read()
        prev, fps = showfps(frame, prev, fps)
        blur = cv2.GaussianBlur(frame, (5,5), 0)
        op = human_detector(blur)
        res = cv2.resize(op, (720, 480))
        cv2.imshow('Human Detection', res)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows() 
def main():
    # image()
    video()
if __name__ == '__main__':
    main()