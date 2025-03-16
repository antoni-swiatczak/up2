# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QLabel
from PySide6.QtCore import Qt

app = QApplication(sys.argv)
label = QLabel("Hello World!")
label.setAlignment(Qt.AlignCenter)
label.show()
app.exec()

