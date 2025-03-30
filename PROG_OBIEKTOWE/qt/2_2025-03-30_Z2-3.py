import sys
import logging
logging.basicConfig(level=logging.INFO)

from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QGridLayout")
        self.sequence = ['C', 'B', 'D', 'A']
        self.current_index = 0

        widget = QWidget()
        layout = QGridLayout()

        self.buttons = {}
        positions = [(0, 0), (0, 1), (1, 0), (1, 1)]
        for i, letter in enumerate(['A', 'B', 'C', 'D']):
            button = QPushButton(letter)
            button.clicked.connect(self.check_sequence)
            layout.addWidget(button, *positions[i])
            self.buttons[letter] = button

        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def check_sequence(self):
        sender = self.sender()
        if sender.text() == self.sequence[self.current_index]:
            sender.setStyleSheet("background-color: green")
            self.current_index += 1
            if self.current_index == len(self.sequence):
                for btn in self.buttons.values():
                    btn.setStyleSheet("background-color: gold")
                self.current_index = 0
        else:
            for btn in self.buttons.values():
                btn.setStyleSheet("")
            self.current_index = 0



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