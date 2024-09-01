from PyQt5.Qt import Qt #підкючаємо біблфотеку і підводемо віджети які будемо використовувати
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QRadioButton, QSpinBox, QHBoxLayout, QVBoxLayout, QGroupBox, QButtonGroup 


main_window = QWidget() #створюємо вікно з певними розмірами
main_window.resize(600, 500)
main_window.setWindowTitle("Memory card") #заголовок вікна
main_window.move(300, 300) #відкоригування розташування

btn_menu = QPushButton("Меню") #створюємо кнопки
btn_sleep = QPushButton("Відпочити")

box_minuts = QSpinBox() #створення лічільника хв
box_minuts.setValue(30) #задаєм 30хв
box_minuts_lbl = QLabel("хвилин")

lbl_question = QLabel('Question') # питання

answer_group_box = QGroupBox("Варіанти відповідей")#створення групи віджетів

radio_buttons_group = QButtonGroup() #створення групи для кнопок відповідей
r_btn1 = QRadioButton('1') #створюємо круглі кнопки
r_btn2 = QRadioButton('2')
r_btn3 = QRadioButton('3')
r_btn4 = QRadioButton('4')

radio_buttons_group.addButton(r_btn1) #додаємо кнопки в группу
radio_buttons_group.addButton(r_btn2)
radio_buttons_group.addButton(r_btn3)
radio_buttons_group.addButton(r_btn4)

v_line1 = QVBoxLayout() #створення горизонтальних і вертикальних ліній
v_line2 = QVBoxLayout()
h_line = QHBoxLayout()

v_line1.addWidget(r_btn1)#кладем кнопки на лінії
v_line1.addWidget(r_btn2)

v_line2.addWidget(r_btn3)
v_line2.addWidget(r_btn4)

h_line.addLayout(v_line1)
h_line.addLayout(v_line2)
answer_group_box.setLayout(h_line)

result_group_box = QGroupBox("Результат теста") #створення группи віджетів
lbl_correct = QLabel('правильно')
lbl_right = QLabel('правильна відповідь')

result_line = QVBoxLayout() #створення лінії
result_line.addWidget(lbl_correct, alignment=(Qt.AlignLeft|Qt.AlignTop))  #вирівнювання відповіді в левий угол
result_line.addWidget(lbl_right, alignment=Qt.AlignCenter, stretch=3)
result_group_box.setLayout(result_line) #групуємо в груп бокс
result_group_box.hide()  #ховаємо поки цей груп бокс

btn_answer = QPushButton("Відповісти")

line1 = QHBoxLayout()
line1.addWidget(btn_menu)
line1.addStretch(2)
line1.addWidget(btn_sleep)
line1.addWidget(box_minuts)
line1.addWidget(box_minuts_lbl)

main_line = QVBoxLayout()
main_line.addLayout(line1)
main_line.addWidget(lbl_question, alignment=(Qt.AlignCenter|Qt.AlignCenter))

line2 = QHBoxLayout()
line2.addWidget(answer_group_box)
line2.addWidget(result_group_box)

main_line.addLayout(line2, stretch=4)
main_line.addWidget(btn_answer)
main_line.addStretch(1)

main_window.setLayout(main_line)

