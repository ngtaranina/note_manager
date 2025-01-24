import datetime

today = datetime.datetime.now() # сегодняшняя дата
main_condition = True #  для организации цикла проверки правильного ввода даты
issue_date = '' # переменная для хранения даты дедлайна

#  функция проверки правильности формата ввода даты
def check_format_data (dat: str):
    if len(dat) > 10:
        print('что-то очень длинная дата получилась')
        return False
    if '.' in dat or '/' in dat:
        return True
    else:
        print('что-то не так в формате ввода даты')
        return False

# функция, которая будет проверять, что такая дата существует
def check_exist_data(y, m, d):
    try:
        datetime.datetime(y, m, d)
        return True
    except:
        return False

# основной блок программы
while main_condition:
    issue_date = input('Введи дату в формате dd.mm.yyyy или dd/mm/yyyy:  ')
    format_condition = check_format_data (issue_date)
    if format_condition:
        # Проверка на формат выполнена, создаем объект issue_date, как элемент datetime.datetime
        # сначала выделяем значения дня, месяца и года
        if '.' in issue_date:
            issue_date = issue_date.split('.')
        elif '/' in issue_date:
            issue_date = issue_date.split('/')
        # преобразовываем их в формат целых чисел
        us_date = int(issue_date[0])
        us_month = int(issue_date[1])
        us_year = int(issue_date[2])
        # теперь используем функцию проверки, и определяем существует ли такая дата
        exist_condition = check_exist_data(us_year, us_month, us_date)  # для организации цикла проверки существования даты
        if exist_condition:
            issue_date = datetime.datetime(us_year, us_month, us_date)
            main_condition = False
        else:
            print('Упс! Такой даты не существует!')

# определяем разницу между сегодняшней датой и датой дедлайна
delta = (issue_date - today).days + 1
if delta > 0:
    print(f'до дедлайна осталось {delta} дн(я/ей)')
elif delta == 0:
    print('Дедлайн сегодня! Торопись!')
else:
    print('Хм! Сроки уже прошли. Эта дата просрочена. Нужно ввести другую!')