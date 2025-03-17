import sys
import logging
logging.basicConfig(level=logging.INFO)

from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit
from PySide6.QtGui import QGuiApplication, QFont, QDoubleValidator
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):

    def changeBg(self):
        self.label1.setStyleSheet("color: blue; background-color: 'yellow'; padding: 8px;")

    def clearInputs(self):
        self.inputA.clear()
        self.inputB.clear()
        self.labelC.setText("WYNIK")

    def add(self):
        try:
            self.labelC.setText(f"{round(float(self.inputA.text()) + float(self.inputB.text()), 2)}")
        except ValueError:
            pass

    def subtract(self):
        try: 
            self.labelC.setText(f"{round(float(self.inputA.text()) - float(self.inputB.text()), 2)}")
        except ValueError:
            pass

    def multiply(self):
        try:
            self.labelC.setText(f"{round(float(self.inputA.text()) * float(self.inputB.text()), 2)}")
        except ValueError:
            pass

    def divide(self):
        try:
            if (float(self.inputB.text()) == 0):
                self.labelC.setText("Nie przez 0 :(")
            else:
                self.labelC.setText(f"{round(float(self.inputA.text()) / float(self.inputB.text()), 2)}")
        except ValueError:
            pass

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Fajna apka :)")

        screen_geometry = QGuiApplication.primaryScreen().geometry()
        width = (screen_geometry.width() * 0.7)
        height = (screen_geometry.height() * 0.7)
        self.setMinimumSize(width, height)

        self.label1 = QLabel("Hejka :)", self)
        self.label1.setGeometry(50, 0, 200, 100)
        self.label1.setAlignment(Qt.AlignCenter)
        self.label1.setFont(QFont("Apotos", 13, QFont.Bold))
        self.label1.setStyleSheet("color: #ddd; background-color: #222; padding: 8px;")
        
        self.button1 = QPushButton("Naciśnij :D", self)
        self.button1.setGeometry(300, 0, 200, 100)
        self.button1.setFont(QFont("Apotos", 13, QFont.Bold))
        self.button1.setStyleSheet("color: #ddd; background-color: #222; padding: 8px;")
        self.button1.clicked.connect(self.changeBg)

        self.input1 = QLineEdit(self)
        self.input1.setGeometry(550, 0, 200, 100)
        self.input1.setAlignment(Qt.AlignCenter)
        self.input1.setFont(QFont("Apotos", 13, QFont.Bold))

        self.button2 = QPushButton("Czyść :D", self)
        self.button2.setGeometry(800, 0, 200, 100)
        self.button2.setFont(QFont("Apotos", 13, QFont.Bold))
        self.button2.setStyleSheet("color: #ddd; background-color: #222; padding: 8px;")
        self.button2.clicked.connect(self.input1.clear)

        self.inputA = QLineEdit(self)
        self.inputA.setGeometry(50, 150, 200, 100)
        self.inputA.setAlignment(Qt.AlignCenter)
        self.inputA.setFont(QFont("Apotos", 13, QFont.Bold))
        self.inputA.setValidator(QDoubleValidator())
        
        self.inputB = QLineEdit(self)
        self.inputB.setGeometry(300, 150, 200, 100)
        self.inputB.setAlignment(Qt.AlignCenter)
        self.inputB.setFont(QFont("Apotos", 13, QFont.Bold))
        self.inputB.setValidator(QDoubleValidator())

        self.labelC = QLabel("WYNIK", self)
        self.labelC.setGeometry(550, 150, 200, 100)
        self.labelC.setAlignment(Qt.AlignCenter)
        self.labelC.setStyleSheet("color: #ddd; background-color: #222; padding: 8px;")
        self.labelC.setFont(QFont("Apotos", 13, QFont.Bold))

        self.button3 = QPushButton("Czyść :D", self)
        self.button3.setGeometry(800, 150, 200, 100)
        self.button3.setFont(QFont("Apotos", 13, QFont.Bold))
        self.button3.setStyleSheet("color: #ddd; background-color: #222; padding: 8px;")
        self.button3.clicked.connect(self.clearInputs)

        self.buttonA = QPushButton("+", self)
        self.buttonA.setGeometry(50, 300, 200, 100)
        self.buttonA.setFont(QFont("Apotos", 13, QFont.Bold))
        self.buttonA.setStyleSheet("color: #ddd; background-color: #222; padding: 8px;")
        self.buttonA.clicked.connect(self.add)

        self.buttonB = QPushButton("-", self)
        self.buttonB.setGeometry(300, 300, 200, 100)
        self.buttonB.setFont(QFont("Apotos", 13, QFont.Bold))
        self.buttonB.setStyleSheet("color: #ddd; background-color: #222; padding: 8px;")
        self.buttonB.clicked.connect(self.subtract)

        self.buttonC = QPushButton("x", self)
        self.buttonC.setGeometry(550, 300, 200, 100)
        self.buttonC.setFont(QFont("Apotos", 13, QFont.Bold))
        self.buttonC.setStyleSheet("color: #ddd; background-color: #222; padding: 8px;")
        self.buttonC.clicked.connect(self.multiply)

        self.buttonD = QPushButton("/", self)
        self.buttonD.setGeometry(800, 300, 200, 100)
        self.buttonD.setFont(QFont("Apotos", 13, QFont.Bold))
        self.buttonD.setStyleSheet("color: #ddd; background-color: #222; padding: 8px;")
        self.buttonD.clicked.connect(self.divide)

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