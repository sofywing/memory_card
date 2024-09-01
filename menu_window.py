from PyQt5.Qt import Qt #підкючаємо біблфотеку і підводемо віджети які будемо використовувати
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QLineEdit

menu_window = QWidget() #створення, вікна, розмірів, заголовку та розміщення
menu_window.resize(400, 300)
menu_window.setWindowTitle("Memory card")
menu_window.move(700, 300) #КООРДИНАТИ

question_lbl = QLabel("Введіть запитання:") #створення текстових питань
right_ans_lbl = QLabel("Введіть правильну відповідь:")
wrong_ans1_lbl = QLabel("Введіть неправильну відповідь:")
wrong_ans2_lbl = QLabel("Введіть неправильну відповідь:")
wrong_ans3_lbl = QLabel("Введіть неправильну відповідь:")

question_input = QLineEdit() #поля для вводу відповідей
right_ans_input = QLineEdit()
wrong_ans1_input = QLineEdit()
wrong_ans2_input = QLineEdit()
wrong_ans3_input = QLineEdit()

btn_add = QPushButton("Додати запитання") #створення клавіші з назвою +
btn_clear = QPushButton("Очистити") #створення клавіші з назвою -

lbl_stat = QLabel("СТАТИСТИКА") # створення тексту з шрифтом і розміром
lbl_stat.setStyleSheet("font-size: 25px; font-weight: bold;")

statistics = QLabel()

btn_back = QPushButton("Назад") #створення кнопки назад

col1 = QVBoxLayout() #створення вертикальних ліній і упорядкування на них віджетів
col2 = QVBoxLayout()

col1.addWidget(question_lbl)
col1.addWidget(right_ans_lbl)
col1.addWidget(wrong_ans1_lbl)
col1.addWidget(wrong_ans2_lbl)
col1.addWidget(wrong_ans3_lbl)

col2.addWidget(question_input)
col2.addWidget(right_ans_input)
col2.addWidget(wrong_ans1_input)
col2.addWidget(wrong_ans2_input)
col2.addWidget(wrong_ans3_input)

line2 = QHBoxLayout() #створення горизонтальньої лінії і упорядкування на неї віджетів
line2.addWidget(btn_add)
line2.addWidget(btn_clear)

line1 = QHBoxLayout() #створення горизонтальньої лінії і упорядкуванння на неї ліній 
line1.addLayout(col1)
line1.addLayout(col2)

main_line =QVBoxLayout() #створення вертикальної лінії і упорядковання на неї всього
main_line.addLayout(line1)
main_line.addLayout(line2)
main_line.addWidget(lbl_stat)
main_line.addWidget(statistics)
main_line.addWidget(btn_back)

menu_window.setLayout(main_line) #весь візуал відображуємо у вікні
