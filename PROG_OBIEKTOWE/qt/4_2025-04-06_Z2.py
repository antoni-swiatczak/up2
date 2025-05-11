import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QFileDialog, QVBoxLayout, QWidget, QSlider, QCheckBox, QSpinBox
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import Qt

class PersistentWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Persistent Window")
        self.setGeometry(600, 200, 500, 400)
        self.setMinimumSize(300, 200)
        self.setMaximumSize(800, 600)

        self.layout = QVBoxLayout()
        self.image_label = QLabel("Załaduj obrazek")
        self.image_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.image_label)
        self.setLayout(self.layout)

        self.pixmap = None

    def load_image(self, path):
        self.pixmap = QPixmap(path)
        self.update_image_size()

    def resizeEvent(self, event):
        if self.pixmap:
            self.update_image_size()
        super().resizeEvent(event)

    def update_image_size(self):
        if self.pixmap:
            scaled_pixmap = self.pixmap.scaled(self.size(), Qt.KeepAspectRatio)
            self.image_label.setPixmap(scaled_pixmap)

    def apply_edits(self, grayscale, mirror, scale, crop_size):
        if not self.pixmap:
            return

        image = self.pixmap.toImage()

        if grayscale:
            image = image.convertToFormat(QImage.Format_Grayscale8)

        if mirror:
            image = image.mirrored(True, False)

        if crop_size > 50:
            width = min(image.width(), crop_size)
            height = min(image.height(), crop_size)
            image = image.copy(0, 0, width, height)

        scaled_pixmap = QPixmap.fromImage(image).scaled(self.size() * scale / 100, Qt.KeepAspectRatio)
        self.image_label.setPixmap(scaled_pixmap)

class OnDemandWindow(QWidget):
    def __init__(self, persistent_window):
        super().__init__()
        self.setWindowTitle("On Demand Window")
        self.setGeometry(650, 250, 350, 350)
        self.persistent_window = persistent_window

        self.layout = QVBoxLayout()
        self.label = QLabel("Opcje edycji obrazu")
        self.layout.addWidget(self.label)

        self.grayscale_checkbox = QCheckBox("Skala szarości")
        self.layout.addWidget(self.grayscale_checkbox)

        self.mirror_checkbox = QCheckBox("Odbicie lustrzane")
        self.layout.addWidget(self.mirror_checkbox)

        self.scale_slider = QSlider(Qt.Horizontal)
        self.scale_slider.setMinimum(10)
        self.scale_slider.setMaximum(200)
        self.scale_slider.setValue(100)
        self.layout.addWidget(QLabel("Przeskalowanie"))
        self.layout.addWidget(self.scale_slider)

        self.crop_spinbox = QSpinBox()
        self.crop_spinbox.setMinimum(50)
        self.crop_spinbox.setMaximum(300)
        self.layout.addWidget(QLabel("Kadrowanie"))
        self.layout.addWidget(self.crop_spinbox)

        self.apply_button = QPushButton("Zastosuj")
        self.apply_button.clicked.connect(self.apply_changes)
        self.layout.addWidget(self.apply_button)

        self.setLayout(self.layout)

    def apply_changes(self):
        grayscale = self.grayscale_checkbox.isChecked()
        mirror = self.mirror_checkbox.isChecked()
        scale = self.scale_slider.value()
        crop_size = self.crop_spinbox.value()
        self.persistent_window.apply_edits(grayscale, mirror, scale, crop_size)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")
        self.setGeometry(100, 100, 500, 400)

        self.persistent_window = PersistentWindow()
        self.on_demand_window = OnDemandWindow(self.persistent_window)

        self.button_open_persistent = QPushButton("Otwórz Persistent Window")
        self.button_open_persistent.clicked.connect(self.open_persistent)

        self.button_open_on_demand = QPushButton("Otwórz On Demand Window")
        self.button_open_on_demand.clicked.connect(self.on_demand_window.show)

        self.button_load_image = QPushButton("Załaduj obrazek")
        self.button_load_image.clicked.connect(self.load_image)

        layout = QVBoxLayout()
        layout.addWidget(self.button_open_persistent)
        layout.addWidget(self.button_open_on_demand)
        layout.addWidget(self.button_load_image)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def open_persistent(self):
        self.persistent_window.show()

    def load_image(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Wybierz obraz", "", "Obrazy (*.png *.jpg *.bmp)")
        if file_path:
            self.persistent_window.load_image(file_path)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
