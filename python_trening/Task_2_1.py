# str_2 содержит в себе str_1?


str_1 = 'test'
str_2 = 'test1'

if str_1 in str_2:
    print('ДА')
else:
    print('НЕТ')


def task_yes_no(str_1, str_2):
    if str_1 in str_2:
        print('ДА')
    else:
        print('НЕТ')
task_yes_no(str_1='test', str_2='test1')
