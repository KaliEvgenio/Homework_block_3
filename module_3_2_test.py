def send_email(message,*recip_list,sender = 'university.help@gmail.com'):
#проверка правильности введенных адресов
    if len(sender.rsplit(sep='.', maxsplit=1)) > 1:
        s_right = sender.rsplit(sep='.', maxsplit=1)[1]
    else:
        s_right = ''
    if s_right == 'com' or s_right == 'ru' or s_right == 'net':
        s_right = sender.find('@') != -1
    else:
        s_right = False
    for recipient in recip_list:
        if len(recipient.rsplit(sep='.', maxsplit=1)) > 1:
            r_right = recipient.rsplit(sep='.', maxsplit=1)[1]
        else:
            r_right = ''
        if r_right == 'com' or r_right == 'ru' or r_right == 'net':
            r_right = recipient.find('@') != -1
        else:
            r_right = False
#отсечка выполнения при неправильных адресах
        if not((s_right) and (r_right)):
            print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
            continue
#осечка выполнения при совпадении адресов
        if recipient == sender:
            print('Нельзя отправить письмо самому себе!')
            continue
#ну о в конце концов!!!!
        none_stand_sender=''
        if sender != 'university.help@gmail.com':
            none_stand_sender = 'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! '
        print(f'{none_stand_sender}Письмо успешно отправлено с адреса {sender} на адрес {recipient}')


#тест

r_list=['vasyok1337@gmail.com','urban.fan@mail.ru','urban.student@mail.ru','urban.teacher@mail.ru']

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

send_email('Hi ALL !!!!','urban.fan@mail.ru','urban.student@mail.ru')
send_email('Все козлы!!!!',*r_list,sender='unknown_author@people_all.shit')