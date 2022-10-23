name = input('Введите ваше имя - ')
bd = input('Введите ваш день рождения - ')
os = input('Введите вашу ОС - ')
bank = input('Введите данные вашей карточки (банковской) - ')
user_data = f'Имя - {name}\nДР - {bd}\nOS - {os}\nДанные карточки - {bank}\n----\n'
with open ('data.txt', 'a', encoding='utf-8') as f:
    f.write(user_data)


