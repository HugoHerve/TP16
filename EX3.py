from PySide2.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.layout = QVBoxLayout()
        self.setWindowTitle("IHM")
        self.setFixedSize(500,300)
        self.button = QPushButton("Changer mon texte !")
        self.texte = QTextEdit("Le nombre de clics va être affiché ici")
        self.i = 1
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.texte)

        self.setLayout(self.layout)
        #self.button.clicked.connect(self.close)
        self.button.clicked.connect(self.Click)


    def Click(self):
        self.button.setText("Clic "+str(self.i))
        print("Click"+str(self.i))
        self.texte.setText("Clic"+str(self.i))
        self.i += 1

if __name__ == "__main__":
    app = QApplication([])
    win = Window()
    win.show()
    app.exec_()
