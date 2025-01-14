class Button:
    type str = 'Кнопка'

    def __init__(self, text, link):
        self.text = text
        self.link = link

# Создаем экзэмпляр класса
home = Button ('Домой', '/home')
catalog_msk = Button ('Каталог','/msk/catalog')

# Получаем доступ к атрибутам
print(home.text)
print('Кнопка' + home.text + 'имеет ссылку' + home.link)

print('/n')

print(catalog_msk.text)
print('Кнопка' + catalog_msk.text + 'имеет ссылку' + catalog_msk.link)


class ButtonTwo:
    def __init__(self, text, link, loc):
        self.text = text
        self.link = link
        self.loc = loc

    def click(self):
        return "Клик по локатору - {}".format(self.loc)
# Создаем экзэмпляры класса
home_two = ButtonTwo('Домой', '/home', 'button#home')

# Вызываем метод

print(home_two.click())

class Input:
    def __init__(self, text, loc):
        self.text = text
        self.loc = loc
search = Input('Кнопка инпут','#home')


class Button:
    def __init__(self, text, loc):
        self.text = text
        self.loc = loc
click = Button('Кнопка клик', 'click#click')


class Title:
    def __init__(self, text, loc):
        self.text = text
        self.loc = loc
Title_list = Title('Кнопка титульный', '#title list')


class Link:
    def __init__(self, text, loc):
        self.text = text
        self.loc = loc
URL = Link('Кнопка ссылки', 'click#link')


print(search.text, search.loc, click.text, click.loc, Title_list.text, Title_list.loc, URL.text, URL.loc)
