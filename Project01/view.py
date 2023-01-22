def show_menu() -> int:
    print("\n" + "=" * 20)
    print("Выберите необходимое действие")
    print("1. Найти сотрудника")
    print("2. Сделать выборку сотрудников по должности")
    print("3. Сделать выборку сотрудников по зарплате")
    print("4. Добавить сотрудника")
    print("5. Удалить сотрудника")
    print("6. Обновить данные сотрудника")
    print("7. Экспортировать данные в формате json")
    print("8. Экспортировать данные в формате csv")
    print("9. Закончить работу")
    return int(input("Введите номер необходимого действия: "))


# 1. Найти сотрудника
def find_peaple():
    return input('Wat`s find? ')


# 2. Сделать выборку сотрудников по должности
def position_sort():

    return 0


# 3. Сделать выборку сотрудников по зарплате
def salary_sort():

    return 0


# 4. Добавить сотрудника
def add_new_personal():
    name = input('Name: ')
    surname = input('Surname: ')
    position = input('Position: ')
    salary = input('Salary: ')
    return name, surname, position, salary


# 5. Удалить сотрудника
def del_personal():

    return 0


# 6. Обновить данные сотрудника
def reload_personal_data():

    return 0


# 7. Экспортировать данные в формате json
def export_json():

    return 0


# 8. Экспортировать данные в формате csv
def export_csv():

    return 0


# 9. Закончить работу
def exit_of_program():

     return 0



# Вывод результата
def info(message):
    print(message)