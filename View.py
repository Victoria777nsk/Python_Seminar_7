def get_value():
    value_a = int(input('value_a = '))
    value_b = int(input('value_b = '))
    return value_a, value_b


def get_mode():
    mode = input('Введите интересующую вас операцию (деление нацело или с остатком): ')
    if mode.lower() == 'нацело':
        return 1
    elif mode.lower() == 'с остатком':
        return 2
    else:
        print('Вы ввели некорректное число')
    return mode

mode = {1:'Результат деления нацело', 2:'Остаток от деления'}

def return_result(res, operation):
    return f'{mode[operation]} = {res}'
