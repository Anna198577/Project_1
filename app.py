import sys
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *
from Components.windows import MainWindow

if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex=MainWindow("Aplikacja Restauracja")
    sys.exit(app.exec_())