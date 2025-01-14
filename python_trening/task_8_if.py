# Программа проверяет является число положительным или отрицательным и выводит соответствующее сообщение

num = 0

if num >=0:
    print('Число больше либо ровно 0')
else:
    print('Число отрицательно')

num_float = 0

if num_float >0:
    print('Положительное число')
elif num_float == 0:
    print('Ноль')
else:
    print('Отрицательное число')

permit_print = True

if num > 0 and permit_print:
    print('num - положительное число')
elif not permit_print:
    print('Печать запрещена')
