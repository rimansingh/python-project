from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QLineEdit
from PyQt5.QtGui import QFont

class CalcApp(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")
        self.resize(350, 420)

        self.text_box = QLineEdit()
        self.text_box.setFont(QFont("Helvetica", 32))

        self.grid_layout = QGridLayout()

        self.buttons = [
            "7", "8", "9", "/", 
            "4", "5", "6", "*", 
            "1", "2", "3", "-", 
            "0", ".", "=", "+"
            ]
        row = 0
        cols = 0
        for text in self.buttons:
            button = QPushButton(text)
            button.clicked.connect(self.button_clicked)
            button.setStyleSheet("QPushButton { font: 25pt Comic Sans MS; padding: 10px; }")
            self.grid_layout.addWidget(button, row, cols)
            cols += 1

            if cols > 3:
                cols = 0
                row += 1

        self.clear = QPushButton("Clear")
        self.delete = QPushButton("Delete")
        self.clear.setStyleSheet("QPushButton { font: 25pt Comic Sans MS; padding: 10px; }")
        self.delete.setStyleSheet("QPushButton { font: 25pt Comic Sans MS; padding: 10px; }")


        master_layout = QVBoxLayout()
        master_layout.addWidget(self.text_box)
        master_layout.addLayout(self.grid_layout)

        button_row = QHBoxLayout()
        button_row.addWidget(self.clear)
        button_row.addWidget(self.delete)

        master_layout.addLayout(button_row)
        master_layout.setContentsMargins(25,25,25,25)

        self.setLayout(master_layout)

        self.clear.clicked.connect(self.button_clicked)
        self.delete.clicked.connect(self.button_clicked)

    def button_clicked(self):
        button = app.sender()
        text = button.text()

        if text == "=":
            symbol = self.text_box.text()
            try:
                res = eval(symbol)
                self.text_box.setText(str(res))
            except Exception as e:
                print("Error: ", e)
        
        elif text == "Clear":
            self.text_box.clear()

        elif text == "Delete":
            current_text = self.text_box.text()
            self.text_box.setText(current_text[:-1])

        else:
            current_text = self.text_box.text()
            self.text_box.setText(current_text + text) 

if __name__ == "__main__":
    app = QApplication([])
    main_window = CalcApp()
    main_window.setStyleSheet("QWidget { background-color: #f0f0 }")
    main_window.show()
    app.exec_()