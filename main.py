import json
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow

class Widget(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.read_notes()
        self.ui.vikno_zamit.addItems(self.notes)
        self.ui.vikno_zamit.itemClicked.connect(self.show_note)
        self.ui.save_btn.clicked.connect(self.save_note)
        self.ui.vikno_zamit.clicked.connect(self.save_note)
        self.ui.delete_btn.clicked.connect(self.delete_note)
        self.ui.add_teg.clicked.connect(self.add_tag_new)
        self.ui.delete_teg.clicked.connect(self.del_teg)





    def show_note(self):
        self.name = self.ui.vikno_zamit.selectedItems()[0].text()
        self.ui.title_edit.setText(self.name)
        self.ui.text_edit.setText(self.notes[self.name]["текст"])
        self.ui.listWidget_2.clear()
        self.ui.listWidget_2.addItems(self.notes[self.name]["теги"])

    def save_note(self):
        tags = []
        for i in range(self.ui.listWidget_2.count()):
            tags.append(self.ui.listWidget_2.item(i).text())

        self.notes[self.ui.title_edit.text()] = {
                "текст": self.ui.text_edit.toPlainText(),
                "теги": tags

            }
        with open("notes.json", "w", encoding="utf-8") as file:
            json.dump(self.notes, file)
        self.ui.vikno_zamit.clear()
        self.ui.vikno_zamit.addItems(self.notes)
        

    def clear(self):
        self.ui.title_edit.clear()
        self.ui.text_edit.clear()   
    def create_note(self):
        self.clear()
    

    def read_notes(self):
        try:
            with open("notes.json", "r", encoding="utf-8") as file:
                self.notes = json.load(file)
        except:
            self.notes = {
                "Перша замітка":{
                    "текст": "Це текст першої замітки",
                    "теги": []
                }
            }

    def delete_note(self):
        try:
            del self.notes[self.name]
            self.clear()
            self.ui.vikno_zamit.clear()
            self.ui.vikno_zamit.addItems(self.notes)
            self.save_note()
        except:
            print("помилка видалення")

    def add_tag_new(self):
        tag_name = self.ui.tag_edit.text()
        if tag_name!="":
            if tag_name not in self.notes[self.name]["теги"]:
                self.notes[self.name]["теги"].append(tag_name)
                self.ui.listWidget_2.clear()
                self.ui.listWidget_2.addItems(self.notes[self.name]["теги"])

    def del_teg(self):
        if self.ui.listWidget_2.selectedItems()[0]:
            tag_name = self.ui.listWidget_2.selectedItems()[0].text()
            if tag_name in self.notes[self.name]["теги"]:
                self.notes[self.name]["теги"].remove(tag_name)
                self.ui.listWidget_2.clear()
                self.ui.listWidget_2.addItems(self.notes[self.name]["теги"])

app = QApplication([])
ex = Widget()
ex.show()
app.exec_()
