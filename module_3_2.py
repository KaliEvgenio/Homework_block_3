def send_email(message,recipient,sender = 'university.help@gmail.com'):
#проверка правильности введенных адресов
    s_right = sender.rsplit(sep='.', maxsplit=1)[1]
    r_right = recipient.rsplit(sep='.', maxsplit=1)[1]
    if s_right == 'com' or s_right == 'ru' or s_right == 'net':
        s_right = sender.find('@') != -1
    else:
        s_right = False
    if r_right == 'com' or r_right == 'ru' or r_right == 'net':
        r_right = recipient.find('@') != -1
    else:
        r_right = False
#отсечка выполнения при неправильных адресах
    if not((s_right) and (r_right)):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return None #все нижлежащее выполнится если не выполнится это
#осечка выполнения при совпадении адресов
    if recipient == sender:
        print('Нельзя отправить письмо самому себе!')
        return None
#ну о в конце концов!!!!
    none_stand_sender=''
    if sender != 'university.help@gmail.com':
        none_stand_sender = 'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! '
    print(f'{none_stand_sender}Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    return None #вернуть хоть что нибудь в любом случае

#тест

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')