from PyQt5.QtWidgets import QWidget
import cv2
import numpy


class sketchwindow(QWidget):
    def __init__(self, filename):
        super(sketchwindow, self).__init__()
        img = cv2.imread(filename)
        filenameasstr = str(filename)
        cv2.namedWindow(filenameasstr, cv2.WINDOW_AUTOSIZE)

        dimension = (int(img.shape[1]), int(img.shape[0]))

        if int(img.shape[1]) >= 1920:
            while (int(img.shape[1]) >= 1920) or (int(img.shape[0]) >= 1080 * 0.6):
                width = int(img.shape[1] * 0.9)
                height = int(img.shape[0] * 0.9)
                dimension = (width, height)
                img = cv2.resize(img, dimension)

        img = cv2.resize(img, dimension)
        grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        grey_invert = cv2.bitwise_not(grey)
        blurred_img = cv2.GaussianBlur(grey_invert, (111, 111), 0)

        grey_invert_blur = cv2.bitwise_not(blurred_img)
        sketched_img = cv2.divide(grey, grey_invert_blur, scale=256.0)

        cv2.imshow(filenameasstr, sketched_img)
        cv2.waitKey(0)
