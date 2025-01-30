from pprint import pprint
from datetime import date

today = date.today()  # сегодняшняя дата


# Используемые переменные и др.объекты:
#   list_note = []      список созданных заметок
#   username = ''       имя пользователя
#   titles = []          список, содержащий названия заметки
#   list_id = []        список, содержащий ID заметок
#   content = ''        содержание заметки
#   status = ''         статус заметки
#   created_date = ''   дата создания заметки в формате dd.mm.yyyy
#   issue_date = ''     дата окончания в формате dd.mm.yyyy
#   number_notes = []   список для хранения номеров заметок, у которых изменяется статус

#  функция проверки правильности формата ввода даты
def check_format_date(dat: str):
    if len(dat) != 10:
        return False
    if dat.count('.') == 2 or dat.count('/') == 2:
        return True
    else:
        return False


# функция, которая будет проверять, что такая дата существует
def check_exist_date(y, m, d):
    try:
        date(y, m, d)
        return True
    except:
        return False


# определяем что введенная дата не просрочена
def check_date_to_today(dat):
    delta = (dat - today).days
    if delta < 0:
        return False
    else:
        return True


# определяем разницу между сегодняшней датой и датой дедлайна, если срок прошел, вернет 1
def time_to_deadline(d1, d2):
    delta = (d1 - d2).days
    if delta < 0:
        print(f'дата окончания не может быть раньше даты начала!')
        return 1
    delta = (d1 - today).days
    if delta > 0:
        print(f'до дедлайна осталось {delta} дн(я/ей)')
        return 0
    elif delta == 0:
        print('Дедлайн сегодня! Торопись!')
        return 0
    else:
        print('Хм! Сроки уже прошли. Эта дата просрочена. Нужно ввести другую!')
        return 1


# функция проверки корректности введенной даты
def check_input_date(day):
    main_condition = True  # для организации цикла проверки правильного ввода даты
    while main_condition:
        format_condition = check_format_date(day)
        if format_condition:
            # Проверка на формат выполнена, создаем объект day, как элемент date from datetime
            # сначала выделяем значения дня, месяца и года
            if '.' in day:
                day = day.split('.')
            elif '/' in day:
                day = day.split('/')
            # преобразовываем их в формат целых чисел
            us_date = int(day[0])
            us_month = int(day[1])
            us_year = int(day[2])
            # теперь используем функцию проверки, и определяем существует ли такая дата
            exist_condition = check_exist_date(us_year, us_month,
                                               us_date)  # для организации цикла проверки существования даты
            if exist_condition:
                day = date(us_year, us_month, us_date)
                # проверяем, что дата не просрочена
                if not check_date_to_today(day):
                    print(f'Введенная дата уже прошла,сегодня {date.today()}')
                    print('Уверен, что ввел правильную дату?')
                    marker = input('Если все правильно, введи любой символ, если нет - просто  нажми "Enter":  ')
                    if marker == '':
                        continue
                main_condition = False
            else:
                print('Упс! Такой даты не существует!')
                day = input('Введи правильную дату в формате dd.mm.yyyy или dd/mm/yyyy:  ')
        else:
            print('Что то не так с форматом ввода!')
            day = input('Введи дату в формате dd.mm.yyyy или dd/mm/yyyy:  ')
    return day


# функция вывода на экран созданных заметок
def print_all_notes(list_jf_notes):
    print('созданные тобой заметки (даты выводятся без года):')
    for i in range(len(list_jf_notes)):
        print('__' * 40)  # разделительная строка
        print(f'Заметка номер {i + 1}')
        print(f'автор заметки: {list_jf_notes[i]['имя пользователя']}')
        print('Заголовки заметки: ')
        k = 1  # счетчик заголовков заметки
        for one_title in list_jf_notes[i]['заголовки']:
            print(f'   {k})   {one_title}')
            k += 1
        print(f'содержание заметки: {list_jf_notes[i]['содержание']}')
        print(f'статус заметки: {list_jf_notes[i]['статус']}')
        print(f'заметка создана: {list_jf_notes[i]['дата создания'].strftime('%d.%m')}')  # дата выводится без года
        print(f'дата окончания: {list_jf_notes[i]['дата завершения'].strftime('%d.%m')}')  # дата выводится без года
    print('__' * 40)  # разделительная строка
    print('__' * 40)  # разделительная строка


# функция выбора статуса для заметки под номером number_note
def input_status():
    print(' чтобы задать статус "запланировано", введи цифру 1')
    print(' чтобы задать статус "начато", введи цифру 2')
    print(' чтобы задать статус "в работе", введи цифру 3')
    print(' чтобы задать статус "отложено", введи цифру 4')
    print(' чтобы задать статус "выполнено", введи цифру 5')
    print(' чтобы задать статус "отменено", введи цифру 6')
    print(' или введи свой вариант')
    i = input()
    match i:
        case "1":
            return "запланировано"
        case "2":
            return "начато"
        case "3":
            return "в работе"
        case "4":
            return "отложено"
        case "5":
            return "выполнено"
        case "6":
            return "отменено"
        case _:
            return i


# MAIN BLOCK of PROGRAM
print('Привет! Я - менеджер заметок! Как к тебе обращаться? (напиши свое имя)')
user_name = input()
print(f'Привет, {user_name}, я могу помочь тебе создать заметку')
list_note = []  # список созданных заметок
list_id = []  # список созданных ID
while True:  # Цикл организовывает ввод нескольких заметок по желанию пользователя
    answer = input('Если хочешь создать новую заметку, введи любой символ, если нет - просто  нажми "Enter":  ').lower()
    if answer == '':
        break
    else:

        # ВВЕДЕНИЕ ЗАГОЛОВКОВ
        titles = [input("Как назовем эту заметку?(введи название) ")]
        # Следующий цикл организовывает ввод нескольких заголовков для заметки
        while (extra_title := input('Можешь добавить еще одно название. Если нет, просто нажми "Enter"  ')) != '':
            # Следующая проверка проверяет, чтобы не было повторяющегося заголовка
            if extra_title not in titles:
                titles.append(extra_title)
            else:
                print('Такой заголовок у этой заметки уже есть')
        # ВВЕДЕНИЕ ОСТАЛЬНЫХ ДАННЫХ ЗАМЕТКИ
        content = input("Введи содержание заметки: ")
        status = input_status()
        created_date = input("Введи дату начала заметки в формате dd.mm.yyyy: ")
        created_date = check_input_date(created_date)  # проверка, что дата введена корректно
        # создаем и проверяем дату дедлайна
        check_date = True
        while check_date:
            issue_date = input("Введи дату окончания в формате dd.mm.yyyy: ")
            issue_date = check_input_date(issue_date)  # проверка, что дата введена корректно
            check_date = time_to_deadline(issue_date, created_date)  # проверка сроков дедлайна

        # Составление текущей заметки в виде словаря и добавление ее в список заметок list_note
        d = {
            'имя пользователя': user_name,
            'заголовки': titles,
            'содержание': content,
            'статус': status,
            'дата создания': created_date,
            'дата завершения': issue_date
        }
        list_note.append(d)

# Вывод результатов работы программы
print('__' * 40)  # разделительная строка
print(f'СПАСИБО! было создано {len(list_note)} заметок. Закончили работу')

if len(list_note):
    print_all_notes(list_note)

    # ИЗМЕНЕНИЕ СТАТУСА ЗАМЕТКИ
    print('При желании, ты можешь изменить статус заметки.\nБудешь менять?')
    numbers_note_list = []  # список для хранения номеров заметок, у которых будет меняться статус
    while True:
        status_check = input('Если "да" введи любой символ, если нет - просто  нажми "Enter":  ').lower()
        if status_check == '':
            print(f'Ок! Рад был помочь! Были изменены статусы у {len(numbers_note_list)} заметок')
            print_all_notes(list_note)
            break
        else:
            number_note = int(input('введи номер заметки  '))
            if number_note in range(1, len(list_note) + 1):
                numbers_note_list.append(number_note)
                print(f'сейчас статус заметки {number_note}: {list_note[number_note - 1]['статус']} ')
                list_note[number_note - 1]['статус'] = input_status()
                print("Еще какой-нибудь заметки статус меняем?")
            else:
                print(f'Упс! Что-то не так! Заметки с таким номером нет! У тебя создано {len(list_note)} заметок')

    # УДАЛЕНИЕ ЗАМЕТКИ
    print('Я могу удалить заметку, если хочешь.\nУдалить?')
    marker_1 = 1
    while marker_1:
        marker_1 = 0 if input('Если удаляем, введи любой символ, если "нет", то просто "Enter"') == '' else 1
        if marker_1:
            print('Помнишь какие заметки у тебя есть?')
            marker_2 = 0 if input('Если нужно напомнить введи любой символ, если "нет", то просто "Enter"') == '' else 1
            if marker_2:
                print_all_notes(list_note)
            number = int(input("Введи номер заметки для удаления  "))
            if number in range(1, len(list_note) + 1):
                list_note.pop(number - 1)
                print(f'Заметка удалена. У тебя осталось {len(list_note)} заметок')
                print_all_notes(list_note)
            else:
                print(f'такой заметки нет, у тебя всего {len(list_note)} заметок')
            print('Будешь еще что-нибудь удалять?')
        else:
            marker_1 = 0

    print(f'Работу закончили! Хорошего дня, {user_name}!')
