import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QPushButton, QBoxLayout, QGroupBox, QGridLayout
from PyQt5.QtCore import QDir


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 100)
        self.downloadButton()
        self.setWindowTitle("Redrawing the picture")
        layout = QGridLayout()
        layout.addWidget(self.buttonLayout)
        self.setLayout(layout)


    def downloadButton(self):
        self.buttonLayout = QGroupBox("Push button to select a file")
        settingDownloadB = QPushButton('Open a file',self)
        settingDownloadB.clicked.connect(self.openSelection)
        layout = QGridLayout()
        layout.addWidget(settingDownloadB)
        self.buttonLayout.setLayout(layout)
        settingDownloadB
    def openSelection(self):
        pass


def main():
    app = QApplication(sys.argv)
    demo = Window()
    demo.show()

    sys.exit(app.exec_())


if __import__("__main__"):
    main()
