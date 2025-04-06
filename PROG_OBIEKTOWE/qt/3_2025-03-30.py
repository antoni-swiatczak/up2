import sys
import logging
logging.basicConfig(level=logging.INFO)

from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setFixedSize(1280, 720)
        self.setWindowTitle("Fajna apka :)")

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.box = QWidget(self.central_widget)
        self.box.setGeometry(self.width() * 0.1, self.height() * 0.1, self.width() * 0.8, self.height() * 0.8)
        self.box.setStyleSheet("background-color: black;")
        
        self.statusBar().showMessage("Gotowy")
        self.create_horizontal_menu()
        self.create_vertical_toolbar()

    def create_horizontal_menu(self):
        red_action = QAction("Czerwony", self)
        red_action.setShortcut("Ctrl+R")
        red_action.setStatusTip("Zmień kolor boxa na czerwony")
        red_action.triggered.connect(lambda: self.change_box_color("red"))

        green_action = QAction("Zielony", self)
        green_action.setShortcut("Ctrl+G")
        green_action.setStatusTip("Zmień kolor boxa na zielony")
        green_action.triggered.connect(lambda: self.change_box_color("green"))

        blue_action = QAction("Niebieski", self)
        blue_action.setShortcut("Ctrl+B")
        blue_action.setStatusTip("Zmień kolor boxa na niebieski")
        blue_action.triggered.connect(lambda: self.change_box_color("blue"))

        yellow_action = QAction("Żółty", self)
        yellow_action.setShortcut("Ctrl+Y")
        yellow_action.setStatusTip("Zmień kolor boxa na żółty")
        yellow_action.triggered.connect(lambda: self.change_box_color("yellow"))

        menu = self.menuBar()

        colors1_menu = menu.addMenu("Kolory&1")
        colors1_menu.addAction(red_action)
        colors1_menu.addSeparator()
        colors1_menu.addAction(green_action)
        menu.addSeparator()
        colors2_menu = menu.addMenu("Kolory&2")
        colors2_menu.addAction(blue_action)
        colors2_menu.addSeparator()
        colors2_menu.addAction(yellow_action)

    def create_vertical_toolbar(self):
        red_action = QAction(QIcon("A.png"), "CZERWONY", self)
        red_action.setStatusTip("Zmień kolor boxa na czerwony")
        red_action.triggered.connect(lambda: self.change_box_color("red"))

        green_action = QAction(QIcon("B.png"), "ZIELONY", self)
        green_action.setStatusTip("Zmień kolor boxa na zielony")
        green_action.triggered.connect(lambda: self.change_box_color("green"))

        blue_action = QAction(QIcon("C.png"), "NIEBIESKI", self)
        blue_action.setStatusTip("Zmień kolor boxa na niebieski")
        blue_action.triggered.connect(lambda: self.change_box_color("blue"))

        yellow_action = QAction(QIcon("D.png"), "ŻÓŁTY", self)
        yellow_action.setStatusTip("Zmień kolor boxa na żółty")
        yellow_action.triggered.connect(lambda: self.change_box_color("yellow"))

        toolbar = QToolBar("Kolorowy Toolbar")
        toolbar.setOrientation(Qt.Vertical)
        toolbar.setIconSize(QSize(32, 32))
        self.addToolBar(Qt.LeftToolBarArea, toolbar)

        toolbar.addAction(red_action)
        toolbar.addAction(green_action)
        toolbar.addSeparator()
        toolbar.addAction(blue_action)
        toolbar.addAction(yellow_action)

    def change_box_color(self, color):
        self.box.setStyleSheet(f"background-color: {color};")

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