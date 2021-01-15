#! /usr/bin/env python
# -*- coding: utf-8 -*-

# команда переконвертации
# pyside2-uic coder.ui > design_coder.py 

import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QDialog
from PySide2 import QtCore
# импортируем связанный py файл с нашим ui файлом
from design_coder import Ui_MainWindow


class Coder: 
    def coding(self, symbol, operation_type, indent=3):
        if operation_type == 'c':
            symbol_number = ord(symbol) + indent  # 'A' -> 65 + 3
        elif operation_type == 'e':
            symbol_number = ord(symbol) - indent  # 'D' -> 68 - 3
        new_symbol = chr(symbol_number)  # 68 -> 'D'
        return new_symbol

    def translator(self, operation, text):
        translation = ''
        for symbol in text:
            translation += self.coding(symbol, operation)
        return translation


class MainWindow(QMainWindow, Coder):
    def __init__(self):
		# вызовем метод родительского класса
        super(MainWindow, self).__init__()

        # создадим объект
        self.ui = Ui_MainWindow()
        # инициализируем нашу форму
        self.ui.setupUi(self)

        # Соединим сигналы со слотами
        self.ui.encode.clicked.connect(self.pushed_button)
        self.ui.decode.clicked.connect(self.pushed_button)

    # метод при нажатии на кнопку
    def pushed_button(self):
        button = self.sender()
        button_name = button.objectName()
        print(dir(button_name))



if __name__ == "__main__":
    # Создадим Qt Application
    app = QApplication(sys.argv)
    # Создадим и покажем главное окно
    window = MainWindow()
    # Показываем окно
    window.show()
    # Запустим приложение
    sys.exit(app.exec_())
