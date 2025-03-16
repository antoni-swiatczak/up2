import sys
import logging
logging.basicConfig(level=logging.INFO)

from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtGui import QGuiApplication
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Fajna apka :)")

        screen_geometry = QGuiApplication.primaryScreen().geometry()
        width = (screen_geometry.width() * 0.7)
        height = (screen_geometry.height() * 0.7)
        self.setMinimumSize(width, height)


def main():
    try:
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        logging.info("Status: OK")
        sys.exit(app.exec())
    except Exception as e:
        logging.error(f"An error occurred: {e}")


if __name__ == "__main__":
    main()