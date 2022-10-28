login = input('Введите новый логин - ')
pass1 = input('Введите новый пароль - ')

txt1 = input('Текст который вы хотите сохранить - ')

with open ('login.txt', 'a', encoding='utf-8') as f:
    f.write(login)
with open ('login.txt', 'r', encoding='utf-8') as f:
    log2 = input()
if login in log2:
    print('Логин существует')
    with open ('pass.txt', 'a', encoding='utf-8') as f:
        f.write(pass1)
    with open ('pass.txt', 'r', encoding='utf-8') as f:
        pass2 = input()
    if pass1 in pass2:
        print('Пароль верный')

print(txt1)


