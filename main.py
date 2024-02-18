import json
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow

class Widget(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.notes = {
            "Перша замітка":{
                "текст": "Це текст першої замітки",
                "теги": []

            }
        }
        self.ui.vikno_zamit.addItems(self.notes)
        self.ui.vikno_zamit.itemClicked.connect(self.show_note)
        self.ui.save_btn.clicked.connect(self.save_note)

    def show_note(self):
        name = self.ui.vikno_zamit.selectedItems()[0].text()
        self.ui.title_edit.setText(name)
        self.ui.text_edit.setText(self.notes[name]["текст"])

    def save_note(self):
        self.notes[self.ui.title_edit.text()] = self.ui.text_edit.toPlainText()
        with open("notes.json", "w", encoding="utf-8") as file:
            json.dump(self.notes, file)

app = QApplication([])
ex = Widget()
ex.show()
app.exec_()
