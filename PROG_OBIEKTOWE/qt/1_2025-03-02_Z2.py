import sys
import logging
logging.basicConfig(level=logging.INFO)

from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtGui import QGuiApplication, QFont
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Fajna apka :)")

        screen_geometry = QGuiApplication.primaryScreen().geometry()
        width = (screen_geometry.width() * 0.7)
        height = (screen_geometry.height() * 0.7)
        self.setMinimumSize(width, height)

        self.label1 = QLabel("Hejka z lewej :)", self)
        self.label2 = QLabel("Hejka ze środka :)", self)
        self.label3 = QLabel("Hejka z prawej :)", self)

        self.label1.setGeometry(50, 0, 200, 100)
        self.label2.setGeometry(350, 0, 200, 100)
        self.label3.setGeometry(650, 0, 200, 100)

        self.label1.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.label2.setAlignment(Qt.AlignCenter)
        self.label3.setAlignment(Qt.AlignVCenter | Qt.AlignRight)

        font = QFont("Apotos", 13, QFont.Bold)
        self.label1.setFont(font)
        self.label2.setFont(font)
        self.label3.setFont(font)

        self.label1.setStyleSheet("background-color: #222; color: #ddd; padding: 8px;")
        self.label2.setStyleSheet("background-color: #222; color: #ddd; padding: 8px;")
        self.label3.setStyleSheet("background-color: #222; color: #ddd; padding: 8px;")


def main():
    try:
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        logging.info("Application started successfully.")
        sys.exit(app.exec())
    except Exception as e:
        logging.error(f"An error occurred: {e}")


if __name__ == "__main__":
    main()