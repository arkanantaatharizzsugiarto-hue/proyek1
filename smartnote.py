from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel,
    QListWidget, QLineEdit, QTextEdit,
    QHBoxLayout, QVBoxLayout
)

import json

app = QApplication([])

# ---------------- Notes ---------------- #

notes = {
    "Trend": {
        "text": "This is the most known trend in 2024!",
        "tags": ["fyp", "viral"]
    },
    "Symphony": {
        "text": "I just wanna be part of your symphony!",
        "tags": ["dolphin", "symphony"]
    },
    "Dance": {
        "text": "Now tell your boyfriend I'm your new girlfriend~",
        "tags": ["song", "vibe"]
    }
}

# Save notes to JSON
with open("notes_data.json", "w", encoding="utf-8") as file:
    json.dump(notes, file, ensure_ascii=False, indent=4)

# Load notes from JSON
with open("notes_data.json", "r", encoding="utf-8") as file:
    notes = json.load(file)

# ---------------- Application Interface ---------------- #

notes_win = QWidget()
notes_win.setWindowTitle("Smart Notes")
notes_win.resize(900, 600)

# Widgets
list_notes = QListWidget()
list_notes_label = QLabel("List of notes")

button_note_create = QPushButton("Create note")
button_note_del = QPushButton("Delete note")
button_note_save = QPushButton("Save note")

field_tag = QLineEdit()
field_tag.setPlaceholderText("Enter tag...")

field_text = QTextEdit()

button_add = QPushButton("Add to note")
button_del = QPushButton("Untag from note")
button_search = QPushButton("Search notes by tag")

list_tags = QListWidget()
list_tags_label = QLabel("List of tags")

# ---------------- Layout ---------------- #

layout_notes = QHBoxLayout()

# Left column
col_1 = QVBoxLayout()
col_1.addWidget(field_text)

# Right column
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
row_3.addWidget(button_add)
row_3.addWidget(button_del)

row_4 = QHBoxLayout()
row_4.addWidget(button_search)

col_2.addLayout(row_3)
col_2.addLayout(row_4)

layout_notes.addLayout(col_1, stretch=2)
layout_notes.addLayout(col_2, stretch=1)

notes_win.setLayout(layout_notes)

# ---------------- Functions ---------------- #

def show_note():
    item = list_notes.currentItem()
    if item is None:
        return

    key = item.text()

    field_text.setText(notes[key]["text"])

    list_tags.clear()
    list_tags.addItems(notes[key]["tags"])

# ---------------- Connections ---------------- #

list_notes.addItems(notes.keys())
list_notes.itemClicked.connect(show_note)

# ---------------- Run ---------------- #

notes_win.show()
app.exec_()
