# Используемые переменные и др.объекты:
#   list_note = []      список созданных заметок
#   username = ''       имя пользователя
#   title = []          список, содержащий названия заметки
#   content = ''        содержание заметки
#   status = ''         статус заметки
#   created_date = ''   дата создания заметки в формате dd.mm.yyyy
#   issue_date = ''     дата окончания в формате dd.mm.yyyy

print('Привет! Я могу помочь создать заметку')
list_note = [] # список созданных заметок
while True: # Цикл организовывает ввод нескольких заметок по желанию пользователя
    answer = input('Если хочешь создать новую заметку, введи "да" или "yes", если нет - просто  нажми "Enter":  ' ).lower()
    if answer == '':
        break
    elif answer in ["yes","да"]:
        username = input("Введи свое имя: ")
        title = [input("Введи название заметки: ")]

        # Следующий цикл организовывает ввод нескольких заголовков для заметки
        while (extra_title := input('Можешь добавить еще одно название. Если нет, просто нажми "Enter"  ')) != '':
            # Следующая проверка проверяет, чтобы не было повторяющегося заголовка
            if extra_title not in title:
                title.append(extra_title)
            else:
                print('Такой заголовок уже есть')

        content = input("Введи содержание заметки: ")
        status = input("Введи статус заметки (запланировано, в работе, выполнено, и т.п.): ")
        created_date = input("Введи дату создания заметки в формате dd.mm.yyyy: ")
        issue_date = input("Введи дату окончания в формате dd.mm.yyyy: ")

        # Составление текущей заметки в виде списка и добавление ее в список заметок list_note
        list_note.append([username, title, content, status, created_date, issue_date])

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
        print(f'автор заметки: {list_note[i][0]}')
        print('Заголовки заметки: ')
        k = 1  # счетчик заголовков заметки
        for one_title in list_note[i][1]:
            print(f'   {k})   {one_title}')
            k += 1
        print(f'содержание заметки: {list_note[i][2]}')
        print(f'статус заметки: {list_note[i][3]}')
        print(f'заметка создана: {list_note[i][4][:-5]}') # дата выводится без года
        print(f'дата окончания: {list_note[i][5][:-5]}')  # дата выводится без года
    print('__'*40) # разделительная строка
    print('__' * 40)  # разделительная строка
    print('При желании, ты можешь изменить статус заметки.\nБудешь менять?')
    number_notes = [] # список для хранения номеров заметок, у которых будет меняться статус
    while True:
        status_check = input('Если "да" введи "да" или "yes", если нет - просто  нажми "Enter":  ' ).lower()
        if status_check == '':
            print('__' * 40)  # разделительная строка
            print(f'Ок! Рад был помочь! Были изменены статусы у {len(number_notes)} заметок')
            break
        elif status_check in ["yes", "да"]:
            number_note = int(input('введи номер заметки  '))
            if 0 < number_note <= len(list_note):
                number_notes.append(number_note)
                print(f'сейчас статус заметки {number_note}: {list_note[number_note - 1][3]} ')
                list_note[number_note - 1][3] = input('Введи новый статус  ')
                print("Еще какой-нибудь статус меняем?")
            else:
                print(f'Упс! Что-то не так! Заметки с таким номером нет! У тебя создано {len(list_note)} заметок')

