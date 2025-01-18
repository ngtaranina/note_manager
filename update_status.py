# В заданном списке заметок находится заметка и меняется ее статус
# Возможные статусы: запланировано, начато, в работе, отложено, заканчиваю, выполнено, отменено
# Используемые переменные и др.объекты:
#   list_note = []      список созданных заметок
#   username = ''       имя пользователя
#   titles = []         список, содержащий названия заметки
#   content = ''        содержание заметки
#   status = ''         статус заметки
#   created_date = ''   дата создания заметки в формате dd.mm.yyyy
#   issue_date = ''     дата окончания в формате dd.mm.yyyy
#   number_notes = []   список для хранения номеров заметок, у которых изменяется статус
#   choose_note_number = ''  выбранный для изменения статуса номер заметки
username = 'Наталья',
titles = ['title_1', 'title_2', 'title_3']
content ='проверка работы'
status = 'в работе'
created_date = '18.01.2025'
issue_date = '20.01.2025'


list_note = [ [username, ['title_11', 'title_12', 'title_13'], content, 'запланировано', '10.01.2025', issue_date],
              [username, ['title_21', 'title_22', 'title_23'], content, 'в работе', '12.01.2025', issue_date],
              [username, ['title_31', 'title_32', 'title_33'], content, 'отложено', '15.01.2025', issue_date]]

print(f'У тебя создано {len(list_note)}  заметок')
for i in range(len(list_note)):
    print(f'заметка {i+1} с главным названием {list_note[i][1][0]} созданная {list_note[i][4][:-5]} имеет статус {list_note[i][3]}')
print('__' * 40)  # разделительная строка
print('Хочешь поменять статус какой-либо из них?')
choose_note_number = input('Введи номер заметки, у которой нужно поменять статус или "Enter", чтобы пропустить действие:  ')
while choose_note_number != '':
    if choose_note_number.isdigit():
        if int(choose_note_number) in range(1,len(list_note)+1):
            print('__' * 40)  # разделительная строка
            print('чтобы изменить статус на "запланировано", введи цифру 1')
            print('чтобы изменить статус на "начато", введи цифру 2')
            print('чтобы изменить статус на "в работе", введи цифру 3')
            print('чтобы изменить статус на "отложено", введи цифру 4')
            print('чтобы изменить статус на "выполнено", введи цифру 5')
            print('чтобы изменить статус на "отменено", введи цифру 6')
            print('или введи свой вариант')
            print('_' * 40)
            i = input()
            match i:
                case "1":
                    list_note[int(choose_note_number) - 1][3] = "запланировано"
                case "2":
                    list_note[int(choose_note_number) - 1][3] = "начато"
                case "3":
                    list_note[int(choose_note_number) - 1][3] = "в работе"
                case "4":
                    list_note[int(choose_note_number) - 1][3] = "отложено"
                case "5":
                    list_note[int(choose_note_number) - 1][3] = "выполнено"
                case "6":
                    list_note[int(choose_note_number) - 1][3] = "отменено"
                case _:
                    list_note[int(choose_note_number) - 1][3] = i
            print(f'Статус у заметки под номером {choose_note_number} изменен.')
            print("Проверяем:")
            print(list_note[int(choose_note_number) - 1])
            choose_note_number = input('Теперь можно изменить статус другой заметки, введи номер или "Enter", чтобы закончить  ')
        else:
            print(f'Номер заметки введен неверно, у тебя создано {len(list_note)} заметки. Введи номер заметки или "Enter" ')
            choose_note_number = input()
    else:
        print('УПС!, что то не так! Попробуй еще раз!')
        print('Нужно ввести номер заметки или "Enter"')
        choose_note_number = input()
print('Закончили изменение статусов')