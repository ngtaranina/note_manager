from pprint import pprint
import datetime

today = datetime.datetime.now()  # сегодняшняя дата

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
def check_format_date (dat: str):
    if len(dat) > 10:
        print('что-то очень длинная дата получилась')
        return False
    if '.' in dat or '/' in dat:
        return True
    else:
        print('что-то не так в формате ввода даты')
        return False

# функция, которая будет проверять, что такая дата существует
def check_exist_date(y, m, d):
    try:
        datetime.datetime(y, m, d)
        return True
    except:
        return False

# функция проверки корректности введенной даты
def check_input_date (day):
    main_condition = True  # для организации цикла проверки правильного ввода даты
    while main_condition:
        day = input('Введи дату в формате dd.mm.yyyy или dd/mm/yyyy:  ')
        format_condition = check_format_date (day)
        if format_condition:
            # Проверка на формат выполнена, создаем объект day, как элемент datetime.datetime
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
            exist_condition = check_exist_date(us_year, us_month, us_date)  # для организации цикла проверки существования даты
            if exist_condition:
                day = datetime.datetime(us_year, us_month, us_date)
                main_condition = False
            else:
                print('Упс! Такой даты не существует!')
    return(day)

# функция вывода на экран созданных заметок
def print_all_notes(list_jf_notes):
    print('созданные тобой заметки (даты выводятся без года):')
    for i in range(len(list_jf_notes)):
        print('__' * 40)  # разделительная строка
        print(f'Заметка номер {i + 1}')
        print(f'автор заметки: {list_jf_notes[i]['имя пользователя']}')
        print(f'ID заметки: {list_jf_notes[i]['ID']}')
        print('Заголовки заметки: ')
        k = 1  # счетчик заголовков заметки
        for one_title in list_jf_notes[i]['заголовки']:
            print(f'   {k})   {one_title}')
            k += 1
        print(f'содержание заметки: {list_jf_notes[i]['содержание']}')
        print(f'статус заметки: {list_jf_notes[i]['статус']}')
        print(f'заметка создана: {list_jf_notes[i]['дата создания'][:-5]}') # дата выводится без года
        print(f'дата окончания: {list_jf_notes[i]['дата завершения'][:-5]}')  # дата выводится без года
    print('__'*40) # разделительная строка
    print('__' * 40)  # разделительная строка


print('Привет! Я - менеджер заметок! Как к тебе обращаться? (напиши свое имя)')
user_name = input()
print(f'Привет, {user_name}, я могу помочь тебе создать заметку')
list_note = [] # список созданных заметок
list_id = [] # список созданных ID
while True: # Цикл организовывает ввод нескольких заметок по желанию пользователя
    answer = input('Если хочешь создать новую заметку, введи "да" или "yes", если нет - просто  нажми "Enter":  ' ).lower()
    if answer == '':
        break
    elif answer in ["yes","да"]:

        # ВВЕДЕНИЕ ЗАГОЛОВКОВ
        titles = [input("Как назовем эту заметку?(введи название) ")]
        # Следующий цикл организовывает ввод нескольких заголовков для заметки
        while (extra_title := input('Можешь добавить еще одно название. Если нет, просто нажми "Enter"  ')) != '':
            # Следующая проверка проверяет, чтобы не было повторяющегося заголовка
             if extra_title not in titles:
                titles.append(extra_title)
             else:
                print('Такой заголовок уже есть')
        # ВВЕДЕНИЕ ОСТАЛЬНЫХ ДАННЫХ ЗАМЕТКИ
        content = input("Введи содержание заметки: ")
        status = input("Введи статус заметки (запланировано, в работе, выполнено, и т.п.): ")
        created_date = input("Введи дату создания заметки в формате dd.mm.yyyy: ")
        created_date = check_input_date(created_date)
        issue_date = input("Введи дату окончания в формате dd.mm.yyyy: ")
        issue_date = check_input_date(issue_date)

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
    else:
        print("Извини, я не понял твой ответ")

# Вывод результатов работы программы
print('__' * 40)  # разделительная строка
print('__' * 40)  # разделительная строка
print(f'СПАСИБО! было создано {len(list_note)} заметок. Закончили работу')

if len(list_note):
    print_all_notes(list_note)

    # ИЗМЕНЕНИЕ СТАТУСА ЗАМЕТКИ
    print('При желании, ты можешь изменить статус заметки.\nБудешь менять?')
    numbers_note_list = [] # список для хранения номеров заметок, у которых будет меняться статус
    while True:
        status_check = input('Если "да" введи "да" или "yes", если нет - просто  нажми "Enter":  ' ).lower()
        if status_check == '':
            print('__' * 40)  # разделительная строка
            print(f'Ок! Рад был помочь! Были изменены статусы у {len(numbers_note_list)} заметок')
            break
        elif status_check in ["yes", "да"]:
            number_note = int(input('введи номер заметки  '))
            if 0 < number_note <= len(list_note):
                numbers_note_list.append(number_note)
                print(f'сейчас статус заметки {number_note}: {list_note[number_note - 1]['статус']} ')
                list_note[number_note - 1]['статус'] = input('Введи новый статус  ')
                print("Еще какой-нибудь заметки статус меняем?")
            else:
                print(f'Упс! Что-то не так! Заметки с таким номером нет! У тебя создано {len(list_note)} заметок')
