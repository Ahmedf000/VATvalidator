from PyQt5.QtWidgets import QApplication
import sys
from gui.gui import MainWindow
from PyQt5.QtCore import Qt


def main():
    QApplication.setAttribute(Qt.AA_UseSoftwareOpenGL)

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
