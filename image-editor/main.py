import sys
from PyQt5.QtWidgets import (
    QApplication,
    QFileDialog,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QListWidget,
    QComboBox,
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from editor import Editor  # Import Editor class from editor.py

# App settings
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("Photo Editor")
main_window.resize(1000, 850)

# App widgets
btn_folder = QPushButton("Select Folder")
file_list = QListWidget()

btn_left = QPushButton("Left")
btn_right = QPushButton("Right")
mirror = QPushButton("Mirror")
sharpness = QPushButton("Sharpness")
gray = QPushButton("Gray")
saturation = QPushButton("Saturation")
contrast = QPushButton("Contrast")
blur = QPushButton("Blur")

# Dropdown box
filter_box = QComboBox()
filter_box.addItem("Original")
filter_box.addItem("Left")
filter_box.addItem("Right")
filter_box.addItem("Mirror")
filter_box.addItem("Sharpness")
filter_box.addItem("Gray")
filter_box.addItem("Saturation")
filter_box.addItem("Contrast")
filter_box.addItem("Blur")

picture_box = QLabel("Image will appear here!")

# App layout
master_layout = QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()

col1.addWidget(btn_folder)
col1.addWidget(file_list)
col1.addWidget(filter_box)
col1.addWidget(btn_left)
col1.addWidget(btn_right)
col1.addWidget(mirror)
col1.addWidget(sharpness)
col1.addWidget(gray)
col1.addWidget(saturation)
col1.addWidget(contrast)
col1.addWidget(blur)

col2.addWidget(picture_box)

master_layout.addLayout(col1, 20)
master_layout.addLayout(col2, 80)

main_window.setLayout(master_layout)

# Initialize Editor instance
main = Editor(picture_box, file_list)


# File operations
def get_working_directory():
    directory = QFileDialog.getExistingDirectory()
    if directory:
        main.set_working_directory(directory)
        main.load_file_list()


# Handle filter changes
def handle_filter():
    if file_list.currentRow() >= 0:
        selected_filter = filter_box.currentText()
        main.apply_filter(selected_filter)


# Display image in QLabel
def display_image():
    if file_list.currentRow() >= 0:
        filename = file_list.currentItem().text()
        main.load_image(filename)
        main.show_image()


# Event handlers
btn_folder.clicked.connect(get_working_directory)
file_list.currentRowChanged.connect(display_image)
filter_box.currentTextChanged.connect(handle_filter)

gray.clicked.connect(main.gray)
btn_left.clicked.connect(main.left)
btn_right.clicked.connect(main.right)
sharpness.clicked.connect(main.sharpen)
saturation.clicked.connect(main.saturation)
contrast.clicked.connect(main.contrast)
blur.clicked.connect(main.blur)
mirror.clicked.connect(main.mirror)

# Run app
main_window.show()
sys.exit(app.exec_())
