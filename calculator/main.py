from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QLineEdit

app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("Calculator")
main_window.resize(350, 420)

text_box = QLineEdit()
grid_layout = QGridLayout()

buttons = [
    "7", "8", "9", "/", 
    "4", "5", "6", "*", 
    "1", "2", "3", "-", 
    "0", ".", "=", "+"
    ]

clear = QPushButton("Clear")
delete = QPushButton("Delete")


row = 0
cols = 0

for text in buttons:
    button = QPushButton(text)
    # button.clicked.connect(None)
    grid_layout.addWidget(button, row, cols)
    cols += 1

    if cols > 3:
        cols = 0
        row += 1


# Design
master_layout = QVBoxLayout()
master_layout.addWidget(text_box)
master_layout.addLayout(grid_layout)

button_row = QHBoxLayout()
button_row.addWidget(clear)
button_row.addWidget(delete)

master_layout.addLayout(button_row)

main_window.setLayout(master_layout)



main_window.show()
app.exec_()