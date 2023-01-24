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


# 1. Запрос на выборку сотрудников по зарплате
def salarySort():
    print('Укажите критерии поиска')
    min = input('От: ', end='\t\t')
    max = input('До: ')
    return min, max


# 2. Запрос данных по сотруднику
def requestPersonalData():
    name = input('Name: ')
    surname = input('Surname: ')
    patronymic = input('patronymic')
    position = input('Position: ')
    salary = input('Salary: ')
    return (name, surname, patronymic, position, salary)


# 3. Вывод сообщения
def info(message):
    print(message)


# 4. Вывод на экран списка сотрудников
def viewDataBase(dataBase):
    print("\n" + "=" * 50)
    print("Список сотрудников:\n")
    for i in dataBase.keys:
        print(i, end='.  ')
        for j in dataBase[i]:
            print(*j, end='  ')
    print()


# 5. Запрос ID
def enterID():
    return int(input('Укажите ID сотрудника'))


# 6. Запрос строки
def request(message):
    return input(message)





#
# # 1. Найти сотрудника
# def findPeaple():
#     return input('Введите запрос: ')
#
#
# # 2. Сделать выборку сотрудников по должности
# def positionSort():
#     return input('Введите профессию: ')
#
#
#
# # 5. Удалить сотрудника
# def delPersonal():
#     return int(input('Укажите ID сотрудника'))
#
#
# # 6. Обновить данные сотрудника
# def reloadPersonalData():
#     return int(input('Укажите ID сотрудника'))
#
#
# # 7. Экспортировать данные в формате json
# def exportJSON():
#     return 0
#
#
# # 8. Экспортировать данные в формате csv
# def exportCSV():
#     return 0
#
#
# # 9. Закончить работу
# def exitOfProgram():
#     return 0


