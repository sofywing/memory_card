from PyQt5.QtWidgets import QApplication

app = QApplication([]) #створюємо дотаток

from main_window import * # імпортуємо файл з вікном
from menu_window import *

main_window.show() #показуємо вікно

def to_menu():
    main_window.hide()
    menu_window.show()

def to_main():
    menu_window.hide()
    main_window.show()
    
btn_menu.clicked.connect(to_menu)
btn_back.clicked.connect(to_main)
app.exec_() # щоб вікно не закривалось коли хотіло
