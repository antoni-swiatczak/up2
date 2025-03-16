import sys
import logging
logging.basicConfig(level=logging.INFO)

from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QMessageBox
from PySide6.QtGui import QGuiApplication, QFont, QPixmap
from PySide6.QtCore import Qt

class ClickLink(QLabel):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
    
    def mousePressEvent(self, event):
        self.setText("Ładny kwiatek? ->")

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Fajna apka :)")

        screen_geometry = QGuiApplication.primaryScreen().geometry()
        width = (screen_geometry.width() * 0.7)
        height = (screen_geometry.height() * 0.7)
        self.setMinimumSize(width, height)

        self.label1 = ClickLink("Klinkij ;)", self)
        self.label2 = QLabel("<a href=\"https://github.com/antoni-swiatczak/up2/blob/main/PROG_OBIEKTOWE/qt/img/1_Z2.jpg\">Hejka ze środka :)</a>", self)
        self.label3 = QLabel("Hejka z prawej :)", self)

        self.label1.setGeometry(50, 0, 200, 100)
        self.label2.setGeometry(350, 0, 200, 100)
        self.label3.setGeometry(650, 0, 200, 100)

        self.label1.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.label2.setAlignment(Qt.AlignCenter)
        self.label3.setAlignment(Qt.AlignVCenter | Qt.AlignRight)

        self.label1.setTextFormat(Qt.RichText)
        self.label2.setTextFormat(Qt.RichText)
        self.label3.setTextFormat(Qt.RichText)

        self.label1.setFont(QFont("Apotos", 13, QFont.Bold))
        self.label2.setFont(QFont("Apotos", 13, QFont.Bold))
        self.label3.setFont(QFont("Apotos", 13, QFont.Bold))

        self.label1.setStyleSheet("color: #ddd; background-color: #222; padding: 8px;")
        self.label2.setStyleSheet("color: #ddd; background-color: #222; padding: 8px;")
        self.label3.setStyleSheet("color: #ddd; background-color: #222; padding: 8px;")

        self.label2.setOpenExternalLinks(True)
        self.label2.setOpenExternalLinks(True)

        self.pixmap1 = QPixmap("./img/1_Z2.jpg")
        self.pixmap2 = QPixmap("./img/1_Z2.jpg")
        self.pixmap3 = QPixmap("./img/1_Z2.jpg")

        self.img1 = QLabel(self)
        self.img2 = QLabel(self)
        self.img3 = QLabel(self)

        self.img1.setPixmap(self.pixmap1)
        self.img2.setPixmap(self.pixmap2)
        self.img3.setPixmap(self.pixmap3)

        self.img1.setGeometry(0, 250, 300, 300)
        self.img2.setGeometry(350, 250, 400, 400)
        self.img3.setGeometry(800, 250, 500, 500)

        self.img1.setScaledContents(True)
        self.img2.setScaledContents(True)
        self.img3.setScaledContents(True)


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