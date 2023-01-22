import view as v
import modul as m



# Стартовое меню
def start():
    options = [find_member,position,salary,add_member,del_member,update,export_json,export_csv,exit_of_program]
    return options[v.show_menu() - 1]()


# 1. Найти сотрудника

def find_member():
    return v.info(m.find_personal(v.find_peaple()))


# 2. Сделать выборку сотрудников по должности
def position():

    return 0


# 3. Сделать выборку сотрудников по зарплате
def salary():

    return 0


# 4. Добавить сотрудника
def add_member():
    res = m.new_personal(v.add_new_personal())
    return v.info(res)


# 5. Удалить сотрудника
def del_member():

    return 0


# 6. Обновить данные сотрудника
def update():

    return 0


# 7. Экспортировать данные в формате json
def export_json():
    # передавать словарь
    return 0


# 8. Экспортировать данные в формате csv
def export_csv():

    return 0


# 9. Закончить работу
def exit_of_program():

    return 0