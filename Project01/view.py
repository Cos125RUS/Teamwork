def showMenu() -> int:
    print("\n" + "=" * 50)
    print("Выберите необходимое действие")
    print("1. Найти сотрудника")
    print("2. Сделать выборку сотрудников по должности")
    print("3. Сделать выборку сотрудников по зарплате")
    print("4. Добавить сотрудника")
    print("5. Удалить сотрудника")
    print("6. Обновить данные сотрудника")
    print("7. Экспортировать данные в формате json")
    print("8. Экспортировать данные в формате csv")
    print("0. Закончить работу")
    return int(input("Введите номер необходимого действия: "))

# 1. Найти сотрудника
def findPeaple():
    input('Wat`s find? ')
    return 0


# 2. Сделать выборку сотрудников по должности
def positionSort():

    return 0


# 3. Сделать выборку сотрудников по зарплате
def salarySort():

    return 0


# 4. Добавить сотрудника
def addNewPersonal():
    name = input('Name: ')
    surname = input('Surname: ')
    position = input('Position: ')
    salary = input('Salary: ')
    return name, surname, position, salary


# 5. Удалить сотрудника
def delPersonal():

    return 0


# 6. Обновить данные сотрудника
def reloadPersonalData():

    return 0


# 7. Экспортировать данные в формате json
def exportJSON():

    return 0


# 8. Экспортировать данные в формате csv
def exportCSV():

    return 0


# 9. Закончить работу
def exitOfProgram():

     return 0



# Вывод результата
def info(message):
    print(message)