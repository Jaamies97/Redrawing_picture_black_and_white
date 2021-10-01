import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QPushButton, QGroupBox, QGridLayout

from showpicture import picturewindow


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.buttonLayout = QGroupBox("Push button to select a file")
        self.resize(500, 100)
        self.downloadButton()
        self.setWindowTitle("Redrawing the picture")
        layout = QGridLayout()
        layout.addWidget(self.buttonLayout)
        self.setLayout(layout)

    def downloadButton(self):
        settingdownloadb = QPushButton('Open a file', self)
        settingdownloadb.clicked.connect(self.openselection)
        layout = QGridLayout()
        layout.addWidget(settingdownloadb)
        self.buttonLayout.setLayout(layout)

    def openselection(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Select a file", "D:/",
                                                  "Accepted files (*.jpg *.png)", options=options)

        self.picture_window = picturewindow(fileName)


def main():
    app = QApplication(sys.argv)
    demo = Window()
    demo.show()

    sys.exit(app.exec_())


if __import__("__main__"):
    main()
