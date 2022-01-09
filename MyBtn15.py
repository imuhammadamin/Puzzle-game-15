from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFont

class MyButton(QPushButton):
    def __init__(self, value, position = None):
        super().__init__()

        self.setFixedSize(QSize(80,80))
        self.setFont(QFont('Arial', 20))
        self.value = value
        self.position = position
        self.setText(False)
    
    def setText(self, click: bool):
        if self.value == 0:
            super().setText(f"")
        else:
            super().setText(f"{self.value}")