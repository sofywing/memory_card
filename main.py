from PyQt5.QtWidgets import QApplication
from random import choice, shuffle

app = QApplication([]) #створюємо дотаток

from main_window import * # імпортуємо файл з вікном
from menu_window import *

main_window.show() #показуємо вікно


class Question: #створюємо клас(обєкт) для запитань
    def __init__(self, question, answer, wrong_ans1, wrong_ans2, wrong_ans3):
        self.question = question
        self.answer = answer
        self. wrong_ans1 =  wrong_ans1
        self. wrong_ans2 = wrong_ans2
        self. wrong_ans3 =  wrong_ans3

q1 = Question('Формула теплоємності', 'Q=cmt', '', 'pinapple', 'apply') #створення запитань
q2 = Question('СОФІЯ', 'прекрасна', 'неймовірна', 'люкс', 'діамант')
q3 = Question('Срібний', 'яйце', 'добра душа', 'хто я?', 'Двааааа')
q4 = Question('Женя', 'найнайвчитель', 'лінь', 'містер гнев', 'реклама логіка')


questions = [q1, q2, q3, q4] #список з питаннями
radio_btns = [r_btn1, r_btn2, r_btn3, r_btn4] #список з кнопками

count_right = 0 #змінні для статистики
count_wrong = 0
count_all = 0

def new_question(): #додавання питання в вікно з карткою
    global cur_quest 
    cur_quest = choice(questions)#цей метод обирає рандомний елемент зі списку
    lbl_question.setText(cur_quest.question) #відображаємо питання
    lbl_right.setText(cur_quest.answer) #відображаємо правильну відповідь

    shuffle(radio_btns) #перемішує список з кнопками 
    #додаємо варіанти відповідей в кнопки
    radio_btns[0].setText(cur_quest.answer)
    radio_btns[1].setText(cur_quest.wrong_ans1)
    radio_btns[2].setText(cur_quest.wrong_ans2)
    radio_btns[3].setText(cur_quest.wrong_ans3)

new_question()#нове питання

def check_ans(): #перевірка правильності відповіді
    global count_all, count_right
    radio_buttons_group.setExclusive(False) # дозволяємо розблокування кнопки щоб стерти колір ред
    for btn in radio_btns: #перебираємо кнопки
        if btn.isChecked():#знаходимо вибрану кнопку
            if btn.text() == cur_quest.answer: #перевірка правильності відповіді
                count_right += 1
                count_all += 1
                lbl_correct.setText('Правильно') #висвічюємо надпис 
                btn.setChecked(False)# прибираємо виділення з кнопки
                break 
    else:
        lbl_correct.setText('Не правильно')
        btn.setChecked(False)
        count_all += 1
        count_all += 1
    radio_buttons_group.setExclusive(True)#блокуємо можливість зміни кнопок

def next_question():
    if btn_answer.text() == 'Відповісти':
        check_ans()
        answer_group_box.hide()
        result_group_box.show()
        btn_answer.setText('Наступне запитання')
    elif btn_answer.text() == 'Наступне запитання':
        new_question()
        result_group_box.hide()
        answer_group_box.show()
        btn_answer.setText('Відповісти')
def clear():
    question_input.clear()
    right_ans_input.clear()
    wrong_ans1_input.clear()
    wrong_ans2_input.clear()
    wrong_ans3_input.clear()

def add_question():
    question = Question(question_input.text(), right_ans_input.text(), wrong_ans1_input.text(), wrong_ans2_input.text(), wrong_ans3_input.text())
    questions.append(question)
    clear()


def to_menu(): #відкривання 2вікна       
    main_window.hide()
    menu_window.show()

def to_main(): #закривання цього вікна і повернення на 1 вікно
    menu_window.hide()
    main_window.show()
    
btn_menu.clicked.connect(to_menu) #підключання функцій до клавішей
btn_back.clicked.connect(to_main)
btn_answer.clicked.connect(next_question)
btn_add.clicked.connect(add_question)
btn_clear.clicked.connect(clear)
app.exec_() # щоб вікно не закривалось коли хотіло
