print(('Привет! Я могу помочь создать заметку'))
list_note = []
while input('Если хочешь создать заметку, введи "ok", если нет просто "Enter":  ' ).lower() == 'ok':
    username = input("Введите Ваше имя: ")

    # title1 = input("Введите 1-е название заметки: ")
    # title2 = input("Введите 2-е название заметки: ")
    # title3 = input("Введите 3-е название заметки: ")
    # title = [title1, title2, title3]

    # Организация ввода дополнительного названия по желанию
    title = [input("Введите название заметки: ")]
    while input('Хотите добавить еще одно название? Тогда нажмите "пробел" и "Enter", иначе - просто "Enter"') == ' ':
        title.append(input("Введите следующее название заметки: "))

    content = input("Введите содержание заметки: ")
    status = input("Введите статус заметки (запланировано, в работе, выполнено, и т.п.): ")
    created_date = input("Введите дату создания заметки в формате dd.mm.yyyy: ")
    issue_date = input("Введите дату окончания в формате dd.mm.yyyy: ")

    list_note.append([username, title, content, status, created_date, issue_date])

    print([username, title, content, status, created_date[:-5], issue_date[:-5]])


print('СПАСИБО! закончили работу')