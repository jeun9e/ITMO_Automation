# def string_lenght(s: str = '') -> int:
#     return len(s)
# print(string_lenght())
#
# def min_list(a: list, b: list) -> int:
#     return max(len(a), len(b))
# print(min_list('один', 'тридцать'))


# def random_list(a: list, b):
#     a.append(b)
#     return a
# print(random_list([1, 2, 3], 'hi'))
#
#
# def random_list(a: list):
#     a.append('kkk')
#     return a
# print(random_list([1, 2, 3]))


def sum_list(x: list) ->int:
    a = 0
    for i in x:
        a=a+i
    return a
print(sum_list([1, 2, 3, 4, ]))
