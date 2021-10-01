import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QPushButton, QGroupBox, QGridLayout

from showpicture import picturewindow
from showsketch import sketchwindow


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(500, 100)
        self.downloadButton()
        self.downloadButtonSketch()
        self.setWindowTitle("Redrawing the picture")
        layout = QGridLayout()
        layout.addWidget(self.buttonLayout, 0, 0)
        layout.addWidget(self.buttonSketchLayout, 1, 0)
        self.setLayout(layout)

    def downloadButton(self):
        self.buttonLayout = QGroupBox("Push button to select a file")
        settingdownloadb = QPushButton('Open a file to redo in black and white', self)
        settingdownloadb.clicked.connect(lambda: self.openselection(0))
        layout = QGridLayout()
        layout.addWidget(settingdownloadb)
        self.buttonLayout.setLayout(layout)

    def downloadButtonSketch(self):
        self.buttonSketchLayout = QGroupBox("Push button to select a file")
        settingdownloadSketch = QPushButton('Open a file remake it in sketch', self)
        settingdownloadSketch.clicked.connect(lambda: self.openselection(1))
        layout = QGridLayout()
        layout.addWidget(settingdownloadSketch)
        self.buttonSketchLayout.setLayout(layout)
    def openselection(self, type):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Select a file", "D:/",
                                                  "Accepted files (*.jpg *.png)", options=options)

        if type == 0:
            self.picture_window = picturewindow(fileName)
        else:
            self.picture_window = sketchwindow(fileName)


def main():
    app = QApplication(sys.argv)
    demo = Window()
    demo.show()

    sys.exit(app.exec_())


if __import__("__main__"):
    main()
