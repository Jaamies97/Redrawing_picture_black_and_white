from PyQt5.QtWidgets import QWidget
import cv2
import numpy


class picturewindow(QWidget):
    def __init__(self, filename):
        super(picturewindow, self).__init__()
        img = cv2.imread(filename)
        filenameasstr = str(filename)
        cv2.namedWindow(filenameasstr, cv2.WINDOW_AUTOSIZE)

        dimension = (int(img.shape[1]), int(img.shape[0]))

        if int(img.shape[1]) >= 1920:
            while (int(img.shape[1]) >= 1920) or  (int(img.shape[0]) >= 1080 * 0.6):
                width = int(img.shape[1] * 0.9)
                height = int(img.shape[0] * 0.9)
                dimension = (width, height)
                img = cv2.resize(img, dimension)

        img = cv2.resize(img, dimension)
        grey = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        grey_invert = cv2.cvtColor(grey, cv2.COLOR_GRAY2BGR)

        numpy_vertical = numpy.vstack((img, grey_invert))
        numpy_horizontal = numpy.hstack((img, grey_invert))

        numpy_vertical_concat = numpy.concatenate((img, grey_invert), axis=0)
        numpy_horizontal_concat = numpy.concatenate((img, grey_invert), axis=1)
        if (dimension[0]) > (dimension[1]*2):
            cv2.imshow(filenameasstr, numpy_vertical)
            cv2.imshow(filenameasstr, numpy_vertical_concat)
        else:
            cv2.imshow(filenameasstr, numpy_horizontal)
            cv2.imshow(filenameasstr, numpy_horizontal_concat)

        cv2.waitKey(0)
