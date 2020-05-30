import sys
from PyQt5 import QtWidgets


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        # creating EmailBlast widget and setting it as central
        self.email_blast_widget = EmailBlast(parent=self)
        self.setCentralWidget(self.email_blast_widget)
        # filling up a menu bar
        bar = self.menuBar()
        # File menu
        file_menu = bar.addMenu('File')
        # adding actions to file menu
        open_action = QtWidgets.QAction('Open', self)
        close_action = QtWidgets.QAction('Close', self)
        file_menu.addAction(open_action)
        file_menu.addAction(close_action)
        # Edit menu
        edit_menu = bar.addMenu('Edit')
        # adding actions to edit menu
        undo_action = QtWidgets.QAction('Undo', self)
        redo_action = QtWidgets.QAction('Redo', self)
        edit_menu.addAction(undo_action)
        edit_menu.addAction(redo_action)

        # use `connect` method to bind signals to desired behavior
        close_action.triggered.connect(self.close)


class EmailBlast(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # create and set layout to place widgets
        grid_layout = QtWidgets.QGridLayout(self)

        self.text_box = QtWidgets.QTextEdit(self)
        self.save_button = QtWidgets.QPushButton('Save')
        self.clear_button = QtWidgets.QPushButton('Clear')
        self.open_button = QtWidgets.QPushButton('Open')
        # add widgets to layout. Params are:
        # (widget, fromRow, fromColumn, rowSpan=1, columnSpan=1)
        grid_layout.addWidget(self.text_box, 0, 0, 1, 3)
        grid_layout.addWidget(self.save_button, 1, 0)
        grid_layout.addWidget(self.clear_button, 1, 1)
        grid_layout.addWidget(self.open_button, 1, 2)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # creating main window
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())