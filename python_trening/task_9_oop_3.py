class Soda:
    def __init__(self, text=None):
        self.text = text
    def show_my_drink(self):
        if self.text:
            print('Газировка' + self.text)
        else:
            print('Обычная газировка')

drink1 = Soda()
drink2 = Soda('Malina')

drink1.show_my_drink()
drink2.show_my_drink()