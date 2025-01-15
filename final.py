print(('Привет! Я могу помочь создать заметку'))
list_note = []
while input('Если хочешь создать новую заметку, введи "ok", если нет - просто  нажми "Enter":  ' ).lower() == 'ok':
    username = input("Введите Ваше имя: ")

    title = [input("Введите название заметки: ")]
    while input('Хотите добавить еще одно название? Тогда нажмите "пробел" и "Enter", иначе - просто "Enter"') == ' ':
        title.append(input("Введите следующее название заметки: "))

    content = input("Введите содержание заметки: ")
    status = input("Введите статус заметки (запланировано, в работе, выполнено, и т.п.): ")
    created_date = input("Введите дату создания заметки в формате dd.mm.yyyy: ")
    issue_date = input("Введите дату окончания в формате dd.mm.yyyy: ")

    list_note.append([username, title, content, status, created_date, issue_date])

    print('Итак, проверьте, все правильно?:')
    print([username, title, content, status, created_date[:-5], issue_date[:-5]])


print('СПАСИБО! закончили работу')
