from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *

class CustomListItem(QWidget):
    edit_button_clicked = pyqtSignal()
    remove_button_clicked = pyqtSignal()

    def __init__(self, name, price, parent=None):
        super(CustomListItem, self).__init__(parent)

        self.row = QHBoxLayout()

        # Labels
        self.name_label = QLabel(name)
        self.price_label = QLabel(str(price))
        # Buttons
        self.edit_button = QPushButton("Edit")
        self.edit_button.clicked.connect(self.on_edit_clicked)
        self.remove_button = QPushButton("-")
        self.remove_button.clicked.connect(self.on_remove_clicked)

        # Adding all the widgets to the row layout
        self.row.addWidget(self.name_label)
        self.row.addWidget(self.price_label)
        self.row.addWidget(self.edit_button)
        self.row.addWidget(self.remove_button)

        self.setLayout(self.row)

    def on_edit_clicked(self):
        self.edit_button_clicked.emit()

    def on_remove_clicked(self):
        self.remove_button_clicked.emit()