# Создать калькулятор, который считает деление нацело или остаток от деления – операцию определяет пользователь. 
# Организовать систему логирования.

from Calculation import init, devision, ostatok
from Logger import general
from View import get_mode, get_value, return_result

def launch_rocket():
    num1, num2 = get_value()
    action = get_mode()
    init(num1, num2)
    if action == 1:
        result = devision()
    else:
        result = ostatok()
    print(return_result(result, action))
    general(num1, num2, action, result)
