# for i in range(100):
#     print(i+1)
login = ''
counter = 0
go_out = False

while login != 'admin':
    login = input('Ваш логин?\n')
    if login != 'admin':
        counter += 1 # увеличим счётчик попыток входа 
        print('неправильный логин')   
    else:
        password = input('Ваш пароль\n')
        while password != '123':
            counter += 1 # увеличим счётчик попыток входа
            print('неправильный пароль')
            if counter == 3:
                print('Вы заблокированы!')
                go_out = True
                break
            password = input('Ваш пароль\n')
            
        else:
            print('Добро пожаловать!')
            break
    # проверка количества попыток
    if counter == 3 and not go_out:
            print('Вы заблокированы!')
            break
