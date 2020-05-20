from PySide2.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        layout = QHBoxLayout()
        self.barre = QProgressBar()
        self.slider = QSlider()
        self.setWindowTitle("IHM")
        layout.addWidget(self.barre)
        layout.addWidget(self.slider)
        self.setLayout(layout)
        self.slider.valueChanged.connect(self.Progression)

    def Progression(self):
         self.barre.setValue(self.slider.value())


if __name__ == "__main__":
    app = QApplication([])
    win = Window()
    win.show()
    app.exec_()

