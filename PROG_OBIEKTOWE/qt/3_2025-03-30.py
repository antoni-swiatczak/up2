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

        self.create_modal_button()
        self.create_alert_button()

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

    def create_modal_button(self):
        modal_button = QPushButton("Otwórz Modal", self)
        modal_button.setGeometry(50, 50, 150, 50)
        modal_button.clicked.connect(self.open_modal)

    def create_alert_button(self):
        alert_button = QPushButton("Otwórz Alert", self)
        alert_button.setGeometry(50, 120, 150, 50)
        alert_button.clicked.connect(self.show_alert)

    def open_modal(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Modal Dialog")
        dialog.setGeometry(200, 200, 300, 200)

        layout = QVBoxLayout()

        question_label = QLabel("Czy chcesz zmienić kolor?")
        layout.addWidget(question_label)

        radiobutton_red = QRadioButton("Czerwony")
        radiobutton_green = QRadioButton("Zielony")
        layout.addWidget(radiobutton_red)
        layout.addWidget(radiobutton_green)

        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        layout.addWidget(button_box)

        button_box.accepted.connect(lambda: self.handle_modal_accept(radiobutton_red.isChecked(), radiobutton_green.isChecked()))
        button_box.rejected.connect(dialog.reject)

        dialog.setLayout(layout)
        dialog.exec()

    def handle_modal_accept(self, is_red_selected, is_green_selected):
        if is_red_selected:
            self.change_box_color("red")
        elif is_green_selected:
            self.change_box_color("green")

    def show_alert(self):
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Alert")
        msg.setText("Czy na pewno chcesz kontynuować?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        result = msg.exec()

        if result == QMessageBox.Yes:
            self.statusBar().showMessage("OK")
        else:
            self.statusBar().showMessage("ANULOWANO")
            self.change_box_color("black")

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