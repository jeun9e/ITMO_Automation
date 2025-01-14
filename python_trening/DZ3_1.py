class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def start(self):
        print('Автомобиль заведен')

    def stop(self):
        print('Автомобиль заглушен')

    # def year(self, year):
    #     self.year = year
    #
    # def type(self, type):
    #     self.type = type
    #
    # def color(self, color):
    #     self.color = color

    def display(self):
        # print(f"Марка:{self.color}, Model: {self.type}, Year: {self.year}")
        print('Цвет:' + self.color, 'Модель:' + self.type, 'Год выпуска:' + self.year)
a = Car ('Blue', 'BMW', '2022')
a.display()
