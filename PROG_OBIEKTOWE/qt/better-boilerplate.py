import sys
import logging
logging.basicConfig(level=logging.INFO)

from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # start


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