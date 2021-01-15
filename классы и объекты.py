# класс - это некий чертёж
class Auto:
    # метод
    def go_ahead(self):
        print('еду вперёд!!')

    def set_new_auto(self, model, year, color):
        self.m = model
        self.y = year
        self.c = color

    def get_info(self):
        print(f'''
Автомобиль: {self.m}
Год выпуска: {self.y}
Цвет: {self.c}
        ''')

nikita_car = Auto()  # объект  
nikita_car.set_new_auto("BMW", 2020, 'чёрный')
nikita_car.get_info()

father_car = Auto()
father_car.set_new_auto("Opel", 2015, 'чёрный')
father_car.get_info()
