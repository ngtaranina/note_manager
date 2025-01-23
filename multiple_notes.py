from pprint import pprint

from add_titles_loop import titles

# print('Привет! Как тебя зовут? (напиши свое имя)')
# user_name = input()
# print(f'{user_name}, я могу помочь тебе создать заметку')
# notes = [] # список заметок
# count_notes = 0 # счетчик заметок
#
# while input('Если хочешь создать новую заметку, введи "да", если нет - просто  нажми "Enter":  ' ).lower() == 'да':
#     count_notes += 1
#     one_note = {'username': user_name, 'title': [input("Как назовем заметку?(введи название): ")]}
#     while input('Хочешь добавить еще одно название? Тогда нажмите "пробел" и "Enter", иначе - просто "Enter"') == ' ':
#         one_note['title'].append(input("Введи следующее название заметки: "))
#
#     one_note['content'] = input("Теперь напиши само содержание: ")
#     one_note['status'] = input("Какой у нее будет статус?(запланировано, в работе, выполнено, и т.п.): ")
#     one_note['created_date'] = input("Введи дату создания в формате dd.mm.yyyy: ")
#     one_note['modified_created_date'] = one_note['created_date'][:-5]
#     one_note['issue_date'] = input("Введи дату окончания (дедлайн) в формате dd.mm.yyyy: ")
#     one_note['modified_issue_date'] = one_note['issue_date'][:-5]
#     notes.append(one_note)
#     print('Итак, проверьте, все правильно?:')
#     pprint(one_note)
# print(f'СПАСИБО!  У Вас создано {count_notes} заметок! \n Закончили работу!')

# Используемые переменные и др.объекты:
#   list_note = []      список созданных заметок
#   username = ''       имя пользователя
#   titles = []          список, содержащий названия заметки
#   content = ''        содержание заметки
#   status = ''         статус заметки
#   created_date = ''   дата создания заметки в формате dd.mm.yyyy
#   issue_date = ''     дата окончания в формате dd.mm.yyyy
#   number_notes = []   список для хранения номеров заметок, у которых изменяется статус


print('Привет! Как тебя зовут? (напиши свое имя)')
user_name = input()
print(f'{user_name}, я могу помочь тебе создать заметку')
list_note = [] # список созданных заметок
list_id = [] # список созданных ID
while True: # Цикл организовывает ввод нескольких заметок по желанию пользователя
    answer = input('Если хочешь создать новую заметку, введи "да" или "yes", если нет - просто  нажми "Enter":  ' ).lower()
    if answer == '':
        break
    elif answer in ["yes","да"]:
        # ВВЕДЕНИЕ ID
        print("Придумай ID для этой заметки, по которому я смогу ее потом для тебя найти (он должен быть уникальным).")
        print('у тебя уже есть следующие ID, их использовать нельзя: ')
        if len(list_id) == 0:
            print('У тебя пока нет используемых ID. Можешь вводить любое значение ')
        # распечатка используемых ID в одну строчку
        else:
            for el in list_id:
                print(el, end = ' ')
        # Проверка, что введенный ID уникальный
        check_id = True
        while check_id:
            id_note = [input('Введи новый ID:  ')]
            if check_id in list_id:
                print("Внимательней! Такой уже есть, придумай новый  ")
            else:
                check_id = False
        # ВВЕДЕНИЕ ЗАГОЛОВКОВ
        titles = [input("Введи название заметки: ")]
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
        issue_date = input("Введи дату окончания в формате dd.mm.yyyy: ")

        # Составление текущей заметки в виде словаря и добавление ее в список заметок list_note
        d = {
            'имя пользователя': user_name,
            'ID': id_note,
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
    print('Проверьте результат (даты выводятся без года):')
    for i in range(len(list_note)):
        print('__' * 40)  # разделительная строка
        print(f'Заметка номер {i + 1}')
        print(f'автор заметки: {list_note[i]['имя пользователя']}')
        print(f'ID заметки: {list_note[i]['ID']}')
        print('Заголовки заметки: ')
        k = 1  # счетчик заголовков заметки
        for one_title in list_note[i]['заголовки']:
            print(f'   {k})   {one_title}')
            k += 1
        print(f'содержание заметки: {list_note[i]['содержание']}')
        print(f'статус заметки: {list_note[i]['статус']}')
        print(f'заметка создана: {list_note[i]['дата создания'][:-5]}') # дата выводится без года
        print(f'дата окончания: {list_note[i]['дата завершения'][:-5]}')  # дата выводится без года
    print('__'*40) # разделительная строка
    print('__' * 40)  # разделительная строка

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
