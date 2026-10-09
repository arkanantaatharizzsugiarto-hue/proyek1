import json
import os
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QLabel,
    QListWidget,
    QLineEdit,
    QTextEdit,
    QInputDialog,
    QHBoxLayout,
    QVBoxLayout,
    QFormLayout,
)


app = QApplication([])


# App interface
# app window parameters
notes_win = QWidget()
notes_win.setWindowTitle("Smart Notes")
notes_win.resize(900, 600)


# app window widgets
list_notes = QListWidget()
list_notes_label = QLabel("List of notes")


button_note_create = QPushButton("Create note")  # a window with field "Enter note name" appears
button_note_del = QPushButton("Delete note")
button_note_save = QPushButton("Save note")


field_tag = QLineEdit("")
field_tag.setPlaceholderText("Enter tag...")
field_text = QTextEdit()
button_tag_add = QPushButton("Add to note")
button_tag_del = QPushButton("Unpin from note")
button_tag_search = QPushButton("Search notes by tag")
list_tags = QListWidget()
list_tags_label = QLabel("List of tags")


# arrangement of widgets by layouts
layout_notes = QHBoxLayout()
col_1 = QVBoxLayout()
col_1.addWidget(field_text)


col_2 = QVBoxLayout()
col_2.addWidget(list_notes_label)
col_2.addWidget(list_notes)
row_1 = QHBoxLayout()
row_1.addWidget(button_note_create)
row_1.addWidget(button_note_del)
row_2 = QHBoxLayout()
row_2.addWidget(button_note_save)
col_2.addLayout(row_1)
col_2.addLayout(row_2)


col_2.addWidget(list_tags_label)
col_2.addWidget(list_tags)
col_2.addWidget(field_tag)
row_3 = QHBoxLayout()
row_3.addWidget(button_tag_add)
row_3.addWidget(button_tag_del)
row_4 = QHBoxLayout()
row_4.addWidget(button_tag_search)


col_2.addLayout(row_3)
col_2.addLayout(row_4)


layout_notes.addLayout(col_1, stretch=2)
layout_notes.addLayout(col_2, stretch=1)
notes_win.setLayout(layout_notes)




# Fungsi untuk membuat laporan dalam format TXT yang ramah pembaca
def generate_txt_report():
    try:
        with open("notes_report.txt", "w", encoding="utf-8") as file:
            file.write("=" * 50 + "\n")
            file.write("           LAPORAN SMART NOTES SUMMARY           \n")
            file.write("=" * 50 + "\n\n")
           
            if not notes:
                file.write("Belum ada catatan yang tersimpan.\n")
            else:
                for idx, (title, content) in enumerate(notes.items(), 1):
                    file.write(f"{idx}. JUDUL CATATAN: {title}\n")
                    file.write(f"   Tags : {', '.join(content['tags']) if content['tags'] else '-'}\n")
                    file.write("   Isi Catatan :\n")
                    # Memberikan indentasi pada isi catatan agar rapi
                    lines = content['text'].split('\n')
                    for line in lines:
                        file.write(f"     {line}\n")
                    file.write("-" * 50 + "\n")
        print("Laporan TXT berhasil diperbarui (notes_report.txt)")
    except Exception as e:
        print(f"Gagal membuat laporan TXT: {e}")




# App functionality


# Working with note text
def add_note():
    note_name, ok = QInputDialog.getText(notes_win, "Add note", "Note name: ")
    if ok and note_name != "":
        notes[note_name] = {"text": "", "tags": []}
        list_notes.addItem(note_name)
        list_tags.addItems(notes[note_name]["tags"])
        generate_txt_report()  # Perbarui laporan TXT
        print(notes)




def show_note():
    # receiving text from the note with highlighted title and displaying it in the edit field
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        print(key)
        field_text.setText(notes[key]["text"])
        list_tags.clear()
        list_tags.addItems(notes[key]["tags"])




def save_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        notes[key]["text"] = field_text.toPlainText()
       
        # Simpan ke JSON
        with open("notes_data.json", "w", encoding="utf-8") as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
       
        # Simpan ke TXT (Laporan)
        generate_txt_report()
        print(notes)
    else:
        print("Note to save is not selected!")




def del_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        del notes[key]
        list_notes.clear()
        list_tags.clear()
        field_text.clear()
        list_notes.addItems(notes)
       
        # Simpan ke JSON
        with open("notes_data.json", "w", encoding="utf-8") as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
       
        # Simpan ke TXT (Laporan)
        generate_txt_report()
        print(notes)
    else:
        print("Note to delete is not selected!")




# Working with note tags
def add_tag():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = field_tag.text()
        if not tag in notes[key]["tags"]:
            notes[key]["tags"].append(tag)
            list_tags.addItem(tag)
            field_tag.clear()
           
        with open("notes_data.json", "w", encoding="utf-8") as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
       
        # Simpan ke TXT (Laporan)
        generate_txt_report()
        print(notes)
    else:
        print("Note to add a tag is not selected!")




def del_tag():
    if list_tags.selectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = list_tags.selectedItems()[0].text()
        notes[key]["tags"].remove(tag)
        list_tags.clear()
        list_tags.addItems(notes[key]["tags"])
       
        with open("notes_data.json", "w", encoding="utf-8") as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
           
        # Simpan ke TXT (Laporan)
        generate_txt_report()
    else:
        print("Tag to delete is not selected!")




def search_tag():
    print(button_tag_search.text())
    tag = field_tag.text()
    if button_tag_search.text() == "Search notes by tag" and tag:
        print(tag)
        notes_filtered = {}  # notes with the highlighted tag will be here
        for note in notes:
            if tag in notes[note]["tags"]:
                notes_filtered[note] = notes[note]
        button_tag_search.setText("Reset search")
        list_notes.clear()
        list_tags.clear()
        list_notes.addItems(notes_filtered)
        print(button_tag_search.text())
    elif button_tag_search.text() == "Reset search":
        field_tag.clear()
        list_notes.clear()
        list_tags.clear()
        list_notes.addItems(notes)
        button_tag_search.setText("Search notes by tag")
        print(button_tag_search.text())
    else:
        pass




# App startup
# attaching event handling
button_note_create.clicked.connect(add_note)
list_notes.itemClicked.connect(show_note)
button_note_save.clicked.connect(save_note)
button_note_del.clicked.connect(del_note)
button_tag_add.clicked.connect(add_tag)
button_tag_del.clicked.connect(del_tag)
button_tag_search.clicked.connect(search_tag)


# app startup
notes_win.show()


# --- BAGIAN AUTO-GENERATE JSON JIKA BELUM ADA ---
try:
    with open("notes_data.json", "r", encoding="utf-8") as file:
        notes = json.load(file)
except FileNotFoundError:
    notes = {}
    with open("notes_data.json", "w", encoding="utf-8") as file:
        json.dump(notes, file)


list_notes.addItems(notes)


# Jalankan pembuatan laporan pertama kali saat aplikasi dibuka
generate_txt_report()
# -----------------------------------------------


app.exec_()




