username = input("Введите Ваше имя: ")

title1 = input("Введите 1-е название заметки: ")
title2 = input("Введите 2-е название заметки: ")
title3 = input("Введите 3-е название заметки: ")
title = [title1, title2, title3]

content = input("Введите содержание заметки: ")
status = input("Введите статус заметки (запланировано, в работе, выполнено): ")
created_date = input("Введите дату создания заметки в формате dd.mm.yyyy: ")
issue_date = input("Введите дату дедлайна в формате dd.mm.yyyy: ")

print('*'*30) # Разделительная строка
print(f'имя пользователя: {username}')
print(f'названия заметки: {title}')
print(f'содержание заметки: {content}')
print(f'статус заметки: {status}')
print(f'дата создания заметки: {created_date}')
print(f'дата дедлайна: {issue_date}')

print('*'*30) # Разделительная строка
print('Измененные даты:')
print(issue_date[:-5])
print(created_date[:-5])