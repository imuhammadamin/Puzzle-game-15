import sys, random, threading, time
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QVBoxLayout, QMessageBox, QLabel
from PyQt5.QtGui import QFont
from MyBtn15 import MyButton

class MainWindow(QWidget):
    nametxt = " Пятнашки Пятнашки Пятнашки "
    numbers = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    winner = numbers[1:] + numbers[:1]
    attempts = 0
    def __init__(self):
        random.shuffle(self.numbers)
        super().__init__()
        self.grid = QGridLayout()
        self.layout = QVBoxLayout()
        self.name = QLabel(self.nametxt)
        self.name.setFont(QFont('Arial', 18))
        self.btnRestart = QPushButton("RESTART")

        self.buttons = [MyButton(i) for i in self.numbers]
        self.positions = [(i, j) for i in range(4) for j in range(4)]

        for btn, pos in zip(self.buttons, self.positions):
            btn.position = list(pos)
            self.grid.addWidget(btn, *pos)
            btn.clicked.connect(self.btn_clicked)
        
        self.btnRestart.clicked.connect(self.restart)
        threading.Thread(target=self.runner_title).start()

        self.layout.addWidget(self.btnRestart)
        self.layout.addWidget(self.name)
        self.layout.addLayout(self.grid)

        self.setLayout(self.layout)
        self.show()

    def btn_clicked(self):
        self.attempts += 1
        # self.tabriklation()
        btn = self.sender()
        for i in self.buttons:
            if i.value == 0 and (i.position[0] == btn.position[0] + 1 or i.position[0] == btn.position[0] - 1) and i.position[1] == btn.position[1]:
                btn.value, i.value = i.value, btn.value
                btn.setText(btn.value == 0)
                i.setText(i.value == 0)
            elif i.value == 0 and (i.position[1] == btn.position[1] + 1 or i.position[1] == btn.position[1] - 1) and i.position[0] == btn.position[0]:
                btn.value, i.value = i.value, btn.value
                btn.setText(btn.value == 0)
                i.setText(i.value == 0)
        
        self.checker()

    
    def restart(self):
        self.attempts = 0
        self.buttons.clear()
        random.shuffle(self.numbers)
        self.buttons = [MyButton(i) for i in self.numbers]
        for btn, pos in zip(self.buttons, self.positions):
            btn.position = list(pos)
            self.grid.addWidget(btn, *pos)
            btn.clicked.connect(self.btn_clicked)
    

    def checker(self):
        count = 0
        if self.buttons[15].value == 0:
            for i in range(16):
                if self.buttons[i].value == self.winner[i]:
                    count += 1
        if count >= 15:
            self.tabriklation()

    
    def tabriklation(self):
        dlg = QMessageBox()
        
        dlg.setWindowTitle("TABRIKLATION!")
        text = f"\nSiz {self.attempts} ta urinishda g'alabaga erishdingiz!\n"
        dlg.setText(text)
        dlg.setFont(QFont('Arial', 15))
        
        dlg.setStandardButtons(QMessageBox.Ok)
        dlg.exec_()


    def runner_title(self):
        txt = self.nametxt
        ln = len(txt)
        while True:
            txt = txt[1:] + txt[:1]
            self.name.setText(txt)
            time.sleep(0.15)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainw = MainWindow()
    sys.exit(app.exec_())