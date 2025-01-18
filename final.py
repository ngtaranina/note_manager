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
while input('Если хочешь создать новую заметку, введи "да", если нет - просто  нажми "Enter":  ' ).lower() == 'да':
    username = input("Введите Ваше имя: ")

    title = [input("Введите название заметки: ")]
    while (extra_title := input('Можете добавить еще одно название. Если не хотите, просто нажмите "Enter"  ')) != '':
        title.append(extra_title)

    content = input("Введите содержание заметки: ")
    status = input("Введите статус заметки (запланировано, в работе, выполнено, и т.п.): ")
    created_date = input("Введите дату создания заметки в формате dd.mm.yyyy: ")
    issue_date = input("Введите дату окончания в формате dd.mm.yyyy: ")

    list_note.append([username, title, content, status, created_date, issue_date])

# Вывод результатов работы программы
print('*'*40) # разделительная строка
print(f'СПАСИБО! было создано {len(list_note)} заметок. Закончили работу')

if len(list_note):
    print('Проверьте результат (даты выводятся без года):')
    for i in range(len(list_note)):
        print('*'*40) # разделительная строка
        print(f'Заметка номер {i + 1}')
        print(f'автор заметки  - username: {list_note[i][0]}')
        print('Заголовки заметки (title): ')
        k = 1  # счетчик заголовков заметки
        for one_title in list_note[i][1]:
            print(f'    название №{k}: {one_title}')
            k += 1
        print(f'содержание заметки: {list_note[i][2]}')
        print(f'статус заметки: {list_note[i][3]}')
        print(f'заметка создана: {list_note[i][4][:-5]}') # дата выводится без года
        print(f'дата окончания: {list_note[i][5][:-5]}')  # дата выводится без года
