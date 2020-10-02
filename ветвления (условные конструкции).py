login = 'ask'
password = '12345'

l = input('Введите логин\n')


if l == login:
    print("ok, правильно!")
    p = input('Введите пароль\n')
    if p == password:
        print('Добро пожаловать!')
    else:
        print('Ты не угадал!')
else:
    print('Нет такого')

