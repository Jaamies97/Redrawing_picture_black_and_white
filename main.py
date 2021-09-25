import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QPushButton, QBoxLayout
from PyQt5.QtCore import QDir

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(700,500)


def main():
    app = QApplication(sys.argv)
    demo = Window()
    demo.show()

    sys.exit(app.exec_())

if __import__("__main__"):
    main()
