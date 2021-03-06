#! /usr/bin/env python
# -*- coding: utf-8 -*-

# pip install opencv-python

import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QDialog, QFileDialog
from PySide2 import QtCore
# импортируем связанный py файл с нашим ui файлом
from desing_app import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
		# вызовем метод родительского класса
        super(MainWindow, self).__init__()

        # создадим объект
        self.ui = Ui_MainWindow()
        # инициализируем нашу форму
        self.ui.setupUi(self)

        # Соединим сигналы со слотами
        self.ui.load.clicked.connect(self.load_photo)

    # функция при нажатии на кнопку
    def load_photo(self):
        # Добавим диалоговое окно для выбора файлов
            file_names = QFileDialog.getOpenFileNames()
            self.ui.photo.setText(f'<img src="{file_names[0][0]}" width="481" />')


            # # загрузим каждый файл в соответствующую папку
            # for file_name in file_names[0]:
            #     file_name = file_name.replace('/', '\\')

            #     # проверим файл это или папка
            #     if path.isfile(file_name):
            #         where = f'{self.absolute_path}\\{directory_name}\\'
            #         # скопируем файлы в нужную директорию
            #         cmd = f'copy "{file_name}" "{where}"'
            #         system(cmd)
            #         # очистим и пересканируем список с элементами
            #         self.set_list(directory_name, clear=True)


if __name__ == "__main__":
    # Создадим Qt Application
    app = QApplication(sys.argv)
    # Создадим и покажем главное окно
    window = MainWindow()
    # Показываем окно
    window.show()
    # Запустим приложение
    sys.exit(app.exec_())

# import cv2

# # Загрузим обученные данные
# trained_face_data = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# # загрузим фото
# img = cv2.imread('images/1.jpg')

# # сделаем фото чёрно-белым
# black_and_white_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# face_coordinates = trained_face_data.detectMultiScale(black_and_white_img, minNeighbors=8)
# print(face_coordinates)

# #        0                   1
# # [[34, 18, 56, 45], [35, 77, 89, 67]]
# for face in face_coordinates:

#     x_lc, y_lc, x_rc, y_rc = face
#     # нарисуем прямоугольник
#     cv2.rectangle(img, (x_lc, y_lc), (x_lc+x_rc, y_lc+y_rc), (0, 255, 64), 3)


# cv2.imshow('Face detection', img)

# # основной цикл
# cv2.waitKey()
