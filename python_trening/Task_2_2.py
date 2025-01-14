def kurs(year):
    if year == 1 or year == 2 or year == 3 or year == 4:
        print('Бакалавр')
    elif year in range(5,7):
         print('Магистр')
    elif 7 <= year <=9:
         print('Аспирант')
    else:
         print('Введите коректный год обучения')

kurs(10)