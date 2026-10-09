from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel)




app = QApplication([])

questions = [
    ["In what year was New York founded?",
     "1624", "1242", "1861", "1943", "1900", "1890",
     "1624"],

    ["What is the capital of France?",
     "Berlin", "Madrid", "Paris", "Rome", "London", "Tokyo",
     "Paris"],

    
]

current_question = 0



window = QWidget()
window.setWindowTitle('Memo Card')




btn_OK = QPushButton('Answer') # answer button
lb_Question = QLabel('In what year was New York founded?') # your question




RadioGroupBox = QGroupBox("Answer options") # group on the screen for radio buttons with answers
rbtn_1 = QRadioButton('1624')
rbtn_2 = QRadioButton('1242')
rbtn_3 = QRadioButton('1861')
rbtn_4 = QRadioButton('1943')   
rbtn_5 = QRadioButton('1900')
rbtn_6 = QRadioButton('1890')

from PyQt5.QtWidgets import QButtonGroup

RadioGroup = QButtonGroup()

RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
RadioGroup.addButton(rbtn_5)
RadioGroup.addButton(rbtn_6)


layout_ans1 = QHBoxLayout()  
layout_ans2 = QVBoxLayout() # the vertical ones will be inside the horizontal ones
layout_ans3 = QVBoxLayout()
layout_ans4 = QVBoxLayout()
layout_ans5 = QVBoxLayout()
layout_ans6 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) # two answers in the first column
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) # two answers in the second column
layout_ans3.addWidget(rbtn_4)
layout_ans4.addWidget(rbtn_5)
layout_ans4.addWidget(rbtn_6)


layout_ans1.addLayout(layout_ans2)




layout_ans1.addLayout(layout_ans3) # columns are in the same line

layout_ans1.addLayout(layout_ans4)



RadioGroupBox.setLayout(layout_ans1) # “panel” with answer options is ready







layout_line1 = QHBoxLayout() # question
layout_line2 = QHBoxLayout() # answer options or test results
layout_line3 = QHBoxLayout() # “Answer” button




layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)




layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) # the button should be large
layout_line3.addStretch(1)




# Now let’s put the lines we’ve created one under one another:
layout_card = QVBoxLayout()




layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # spaces between the content


def show_question():
    q = questions[current_question]

    lb_Question.setText(q[0])

    rbtn_1.setText(q[1])
    rbtn_2.setText(q[2])
    rbtn_3.setText(q[3])
    rbtn_4.setText(q[4])
    rbtn_5.setText(q[5])
    rbtn_6.setText(q[6])

    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    rbtn_5.setChecked(False)
    rbtn_6.setChecked(False)
    RadioGroup.setExclusive(True)


def check_answer():
    global current_question

    correct = questions[current_question][7]

    selected = None

    if rbtn_1.isChecked():
        selected = rbtn_1.text()
    elif rbtn_2.isChecked():
        selected = rbtn_2.text()
    elif rbtn_3.isChecked():
        selected = rbtn_3.text()
    elif rbtn_4.isChecked():
        selected = rbtn_4.text()
    elif rbtn_5.isChecked():
        selected = rbtn_5.text()
    elif rbtn_6.isChecked():
        selected = rbtn_6.text()

    current_question += 1

    if current_question < len(questions):
        show_question()
    else:
        lb_Question.setText("Quiz Finished!")
        btn_OK.setEnabled(False)
btn_OK.clicked.connect(check_answer)

window.setLayout(layout_card)

show_question()

window.show()
app.exec()


