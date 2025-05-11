import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QFileDialog, QVBoxLayout, QWidget, QCheckBox, QButtonGroup, QSpinBox
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

        self.original_pixmap = None
        self.modified_pixmap = None
        self.scale_factor = 1.0

    def load_image(self, path):
        self.original_pixmap = QPixmap(path)
        self.modified_pixmap = self.original_pixmap
        self.update_image()

    def resizeEvent(self, event):
        self.update_image()
        super().resizeEvent(event)

    def update_image(self):
        if self.modified_pixmap:
            scaled_pixmap = self.modified_pixmap.scaled(self.size() * self.scale_factor, Qt.KeepAspectRatio)
            self.image_label.setPixmap(scaled_pixmap)

    def apply_edits(self, grayscale, mirror, crop_percent, scale_factor):
        if not self.original_pixmap:
            return

        image = self.original_pixmap.toImage()

        if grayscale:
            image = image.convertToFormat(QImage.Format_Grayscale8)

        if mirror:
            image = image.mirrored(True, False)

        if 1 <= crop_percent <= 999:
            crop_width = int(image.width() * (crop_percent / 100))
            crop_height = int(image.height() * (crop_percent / 100))
            image = image.copy(0, 0, crop_width, crop_height)

        self.scale_factor = scale_factor
        self.modified_pixmap = QPixmap.fromImage(image)
        self.update_image()

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

        self.crop_spinbox = QSpinBox()
        self.crop_spinbox.setMinimum(1)
        self.crop_spinbox.setMaximum(999)
        self.crop_spinbox.setValue(100)
        self.layout.addWidget(QLabel("Kadrowanie (%)"))
        self.layout.addWidget(self.crop_spinbox)

        # Grupa checkboxów dla skalowania
        self.scale_group = QButtonGroup()
        self.scale_options = {
            0.25: QCheckBox("x0.25"),
            0.5: QCheckBox("x0.5"),
            1.0: QCheckBox("x1.0"),
            1.5: QCheckBox("x1.5"),
            2.0: QCheckBox("x2.0")
        }

        for factor, checkbox in self.scale_options.items():
            self.scale_group.addButton(checkbox)
            self.layout.addWidget(checkbox)

        self.scale_options[1.0].setChecked(True)

        self.apply_button = QPushButton("Zastosuj")
        self.apply_button.clicked.connect(self.apply_changes)
        self.layout.addWidget(self.apply_button)

        self.setLayout(self.layout)

    def apply_changes(self):
        grayscale = self.grayscale_checkbox.isChecked()
        mirror = self.mirror_checkbox.isChecked()
        crop_percent = self.crop_spinbox.value()
        selected_scale = next((factor for factor, checkbox in self.scale_options.items() if checkbox.isChecked()), 1.0)
        self.persistent_window.apply_edits(grayscale, mirror, crop_percent, selected_scale)

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
