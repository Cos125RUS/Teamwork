import view as v
import workingWithData as wwd
import convertData as cd


# Стартовое меню
def start():
    programRun = True
    options = [exitOfProgram, findMember, position, salary, addMember, delMember, update, exportJSON, exportCSV]
    while programRun:
        userIn = v.showMenu()
        if userIn == 0:
            programRun = False
        options[userIn]
    return 0


# 1. Найти сотрудника
def findMember():
    return 0


# 2. Сделать выборку сотрудников по должности
def position():
    return 0


# 3. Сделать выборку сотрудников по зарплате
def salary():
    return 0


# 4. Добавить сотрудника
def addMember():
    return 0


# 5. Удалить сотрудника
def delMember():
    return 0


# 6. Обновить данные сотрудника
def update():
    return 0


# 7. Экспортировать данные в формате json
def exportJSON():
    # передавать словарь
    return 0


# 8. Экспортировать данные в формате csv
def exportCSV():
    return 0


# 9. Закончить работу
def exitOfProgram():
    return 0
