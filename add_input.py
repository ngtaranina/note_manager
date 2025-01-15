username = input("Введите Ваше имя: ")
title = input("Введите название заметки: ")
content = input("Введите содержание заметки: ")
status = input("Введите статус заметки (запланировано, в работе, выполнено): ")
created_date = input("Введите дату создания заметки в формате dd.mm.yyyy: ")
issue_date = input("Введите дату окончания в формате dd.mm.yyyy: ")

print('*'*30) # разделительная строка
print(f'имя пользователя: {username}')
print(f'название заметки: {title}')
print(f'содержание заметки: {content}')
print(f'статус заметки: {status}')
print(f'дата создания заметки: {created_date}')
print(f'дата окончания: {issue_date}')

print('*'*30) # разделительная строка
print('Измененные даты:')
print(issue_date[:-5])
print(created_date[:-5])