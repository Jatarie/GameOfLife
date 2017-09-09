from PyQt5 import QtWidgets
import sys

def window():
    app = QtWidgets.QApplication(sys.argv)

    w = QtWidgets.QWidget()
    w.setWindowTitle("GameOfLife")
    w.setGeometry(100, 100, 300, 300)

    l1 = QtWidgets.QLabel(w)
    l1.setText("nothing")
    l1.move(125, 20)
    w.show()
    sys.exit(app.exec())

window()
