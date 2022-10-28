import random
id1 = random.randint(0, 100000)
passk = input('Введите ваш новый пароль - ')
name = input('Введите ваше имя - ')
bd = input('Введите ваш день рождения - ')
os = input('Введите вашу ОС - ')
bank = input('Введите данные вашей карточки (банковской) - ')
user_data = f'ID - {id1}\nИмя - {name}\nДР - {bd}\nOS - {os}\nДанные карточки - {bank}\n----\n'
with open ('data.txt', 'a', encoding='utf-8') as f:
    f.write(user_data)
passp = input('Введите ваш пароль - ')
if passp != passk:
    while True:
        print(' ')
else:
    print('ну ок')



