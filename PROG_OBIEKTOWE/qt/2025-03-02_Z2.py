import sys
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QHBoxLayout, QWidget
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

app = QApplication(sys.argv)

# Main widget
main_widget = QWidget()

# Create the layout
layout = QVBoxLayout()

# Add the top label
top_label = QLabel("Top Label")
top_label.setAlignment(Qt.AlignLeft)
layout.addWidget(top_label)

# Add the image
image_label = QLabel()
pixmap = QPixmap("Z2.jpg")
image_label.setPixmap(pixmap)
image_label.setAlignment(Qt.AlignCenter)
layout.addWidget(image_label)

# Add the bottom label
bottom_label = QLabel("Bottom Label")
bottom_label.setAlignment(Qt.AlignRight)
layout.addWidget(bottom_label)

# Set layout to the main widget
main_widget.setLayout(layout)

# Show the main widget
main_widget.show()

app.exec()