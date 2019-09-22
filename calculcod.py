s = []
num = input('введите операцию а затем числа')
s = num.split(' ')
# try:
#assert s[0] in ['+', '-', '*', '/'], 'Ñ‚Ð°ÐºÐ¾Ð¹ Ð¾Ð¿ÐµÑ€Ð°Ñ†Ð¸Ð¸ Ð½ÐµÑ‚'
try:
    assert s[0] in ['+', '-', '*', '/'], 'Ñ‚Ð°ÐºÐ¾Ð¹ Ð¾Ð¿ÐµÑ€Ð°Ñ†Ð¸Ð¸ Ð½ÐµÑ‚'
    a = int(s[1])
    b = int(s[2])
    if s[0] == '+':
        suma = a + b
    elif s[0] == '-':
        suma = a - b
    elif s[0] == '*':
        suma = a * b
    if s[0] == '/':
        suma = a / b
except ZeroDivisionError:
    print('делить на ноль нельзя')
    suma = 0
except ValueError:
    print('ввели начение не int')
    suma = 0
except IndexError:
    print('введены не все аргументы')
    suma = 0
except AssertionError:
    suma = 0
    print('такой операции нет')
print(suma)
