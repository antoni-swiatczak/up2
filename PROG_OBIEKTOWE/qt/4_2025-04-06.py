from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QFileDialog, QVBoxLayout, QWidget
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import sys

class ImageViewer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Przeglądarka obrazów")
        self.setGeometry(100, 100, 800, 600)

        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setScaledContents(False)
        self.image_label.setMinimumSize(800, 600)

        self.open_button = QPushButton("Otwórz obraz", self)
        self.open_button.clicked.connect(self.open_image)

        self.save_button = QPushButton("Zapisz jako", self)
        self.save_button.clicked.connect(self.save_image)
        self.save_button.setEnabled(False)

        layout = QVBoxLayout()
        layout.addWidget(self.open_button)
        layout.addWidget(self.image_label)
        layout.addWidget(self.save_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.current_pixmap = None

    def open_image(self):
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilters(["Obrazy (*.png *.jpg *.jpeg *.bmp *.gif)"])
        file_dialog.setViewMode(QFileDialog.Detail)
        file_dialog.setFileMode(QFileDialog.ExistingFile)

        if file_dialog.exec():
            file_path = file_dialog.selectedFiles()[0]
            self.current_pixmap = QPixmap(file_path)

            self.image_label.setPixmap(self.current_pixmap.scaled(
                self.image_label.size(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            ))

            self.save_button.setEnabled(True)

    def save_image(self):
        if self.current_pixmap:
            file_dialog = QFileDialog(self)
            file_dialog.setAcceptMode(QFileDialog.AcceptSave)
            file_dialog.setNameFilters(["Obrazy (*.png *.jpg *.jpeg *.bmp *.gif)"])

            if file_dialog.exec():
                save_path = file_dialog.selectedFiles()[0]
                self.current_pixmap.save(save_path)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageViewer()
    window.show()
    sys.exit(app.exec())
