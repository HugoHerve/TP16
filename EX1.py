from PySide2.QtWidgets import *
import random

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        layout = QVBoxLayout()
        self.setWindowTitle("Cycles de l'ISEN Yncrea Ouest")
        button = QPushButton("Changer le cycle")
        self.label = QLabel("CSI")
        layout.addWidget(self.label)
        layout.addWidget(button)
        self.setLayout(layout)
        self.setFixedSize(500,300)
        button.clicked.connect(self.buttonclicked)

    def buttonclicked(self, ):
        liste = ["CSI","CIR","BIOST","CENT","BIAST","EST"]
        mot = random.choice(liste)
        self.label.setText(mot)





if __name__ == "__main__":
    app = QApplication([])
    win = Window()
    win.show()
    app.exec_()



