import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import variaveis


# Work thread
class WorkThread(QThread):
    def run(self):
        ss = 0
        while variaveis.cb_intervalo:
            # Sleep for 1 second
            self.sleep(1)
            ss += 1
            print(ss)



class Counter(QWidget):
    def __init__(self):
        super(Counter, self).__init__()

        self.setWindowTitle("Contar")
        self.resize(300, 200)

        layout = QVBoxLayout()

        button = QPushButton("Iniciar")
        layout.addWidget(button)

        button1 = QPushButton("Terminar")
        layout.addWidget(button1)

        self.workThread = WorkThread()
        button.clicked.connect(self.iniciar)
        button1.clicked.connect(self.parar)
        self.setLayout(layout)

    def parar(self):
        variaveis.cb_intervalo = False

    def iniciar(self):
        self.workThread.start()
        variaveis.cb_intervalo = True

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Counter()
    main.show()
    sys.exit(app.exec_())
