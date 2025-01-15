from pprint import pprint

print('Привет! Как тебя зовут? (напиши свое имя)')
user_name = input()
print(f'{user_name}, я могу помочь тебе создать заметку')
notes = [] # список заметок
count_notes = 0 # счетчик заметок
while input('Если хочешь создать новую заметку, введи "да", если нет - просто  нажми "Enter":  ' ).lower() == 'да':
    count_notes += 1
    one_note = {'username': user_name, 'title': [input("Как назовем заметку?(введи название): ")]}
    while input('Хочешь добавить еще одно название? Тогда нажмите "пробел" и "Enter", иначе - просто "Enter"') == ' ':
        one_note['title'].append(input("Введи следующее название заметки: "))

    one_note['content'] = input("Теперь напиши само содержание: ")
    one_note['status'] = input("Какой у нее будет статус?(запланировано, в работе, выполнено, и т.п.): ")
    one_note['created_date'] = input("Введи дату создания в формате dd.mm.yyyy: ")
    one_note['modified_created_date'] = one_note['created_date'][:-5]
    one_note['issue_date'] = input("Введи дату окончания (дедлайн) в формате dd.mm.yyyy: ")
    one_note['modified_issue_date'] = one_note['issue_date'][:-5]
    notes.append(one_note)
    print('Итак, проверьте, все правильно?:')
    pprint(one_note)


print(f'СПАСИБО!  У Вас создано {count_notes} заметок! \n Закончили работу!')