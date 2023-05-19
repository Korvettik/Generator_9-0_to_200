# Напишите, пожалуйста, программу на любом языке программирования,
# которая поместит + (2+3), - (3-2), или ничего ( ) в промежутках
# между цифрами от 9 до 0 (в таком порядке) так, чтобы в результате
# получилось 200. Например: 98+76-5+43-2-10=200.

# Программа должна вставить плюс, минус или ничего в промежуток между
# цифрами 9876543210, чтобы итоговое выражение было равно 200. Программа
# должна выдать несколько вариантов.

from random import choice
result_list = []
line = '876543210'


def choosing(digit, res_str, res_sum):
    todo_from = ['+', '-', '']
    todo = choice(todo_from)
    if todo == '+':
        r_str = res_str + todo + digit
        r_sum = res_sum + int(digit)
    elif todo == '-':
        r_str = res_str + todo + digit
        r_sum = res_sum - int(digit)
    elif todo == '':
        r_str = res_str + todo + digit
        r_sum = res_sum * 10 + int(digit)

    return r_sum, r_str

count = int(input('Введите количество нужных комбинаций (число): ')) # сколько нужно вариантов
while len(set(result_list)) != count:

    res_sum = 9
    res_str = '9'
    while res_sum != 200:
        res_sum = 9
        res_str = '9'
        for digit in line:
            flag = True
            while flag:
                t_res_sum, t_res_str = choosing(digit, res_str, res_sum)
                if 0 < t_res_sum <= 200:
                    res_sum, res_str = t_res_sum, t_res_str
                    flag = False
    # print(f'{res_str} = {res_sum}')
    res = f'{res_str} = {res_sum}'
    result_list.append(res)

result_list = list(set(result_list))
print(*result_list, sep='\n')
