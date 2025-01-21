import datetime

today = datetime.datetime.now() # сегодняшняя дата
flag = True #  для организации цикла проверки правильного ввода даты
issue_date = '' # переменная для хранения даты дедлайна

# функция, которая будет проверять, что такая дата существует
def checkdata(y, m, d):
    try:
        datetime.datetime(y, m, d)
        return True
    except:
        return False

# проверка правильности формата
while flag:
    issue_date = input('Введи дату дедлайна в формате dd.mm.yyyy или dd/mm/yyyy:  ')
    if len(issue_date) > 10:
        print('ошибка в формате ввода даты')
        continue
    if '.' in issue_date:
        issue_date = issue_date.split('.')
        flag = False
    elif '/' in issue_date:
        issue_date = issue_date.split('/')
        flag = False
    else:
        print('ошибка в формате ввода даты')
        continue
print("Молодец, формат даты правильный!")

# Проверка на формат выполнена, создаем объект issue_date, как элемент datetime.datetime

# сначала выделяем значения дня, месяца и года
us_date = int(issue_date[0])
us_month = int(issue_date[1])
us_year = int(issue_date[2])

# теперь используем функцию проверки, и определяем существует ли такая дата
flag = True  # для организации цикла проверки существования даты
while flag:
    if checkdata(us_year, us_month, us_date):
        issue_date = datetime.datetime(us_year, us_month, us_date)
        flag = False
    else:
        print('Ошибка в дате. Такой даты не существует')


# определяем разницу между сегодняшней датой и датой дедлайна
delta = (issue_date - today).days
print(delta)

if delta > 0:
    print(f'до дедлайна осталось {delta}')
    flag = False
elif delta == 0:
    print('Дедлайн сегодня! Торопись!')
    flag = False
else:
    print('Хм! Сроки уже прошли. Эта дата просрочена. Нужно ввести другую!')