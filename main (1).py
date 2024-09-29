from json import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from ui import Ui_MainWindow

class EditorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
    
        with open ('notes.json', 'r', encoding = 'UTF=8') as file:
            self.data = load(file)

        self.connects()

    def choose_note(self):
        pass
        
    def create_note(self):
        note_name, ok = QInputDialog.getText(
        window,
        'Створення замітки',
        'Введіть назву замітки:'
        )
        if not ok:
            return
        if note_name in self.data:
            return
        self.data[note_name] = {
        'text':'',
        'taps': []
        }
        self.ui.listWidget.addItem(note_name)
    def connects(self):
        self.ui.pushButton_3.clicked.connect(self.create_note)
        self.ui.pushButton_2.clicked.connect(self.delete_note)

    def delete_note(self):
        note_selected = self.ui.listWidget.selectedItems()
        if note_selected:
            note_name = note_selected[0].text()
            del self.data[note_name]
            self.ui.listWidget.clear()
            self.ui.listWidget.addItems(self.data)


    
    def save_note(self):
        pass
    
    def create_tag(self):
        pass
    
    def delete_tag(self):
        pass
    
    def find_by_tag(self):
        pass
        
app = QApplication([])
window = EditorWindow()

window.show()
app.exec()