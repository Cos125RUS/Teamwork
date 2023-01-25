import view as v
import workingWithData as wwd
import convertData as cd
import userView as uv

dataBase = cd.importCSV()  # Подгрузили БД
myWindow = uv.mainWindow()  # Загружаем меню


# Стартовое меню
def start():
    global myWindow
    uv.upMenu(myWindow) # Верхнее меню
    myWindow.mainloop() # Мотор


# 1. Отобразить список сотрудников
def showAllPersonal():
    global dataBase
    global myWindow
    uv.indention(myWindow, 2)
    uv.viewList(dataBase, myWindow)


# 2. Добавить сотрудника
def addMember():
    global dataBase
    global myWindow
    uv.indention(myWindow, 4)
    uv.changeField(myWindow)

def transit(data):
    wwd.newPersonal(dataBase, data)





# 1. Найти сотрудника
def findMember():
    global dataBase
    global myWindow

    return 0



# 2. Сделать выборку сотрудников по должности
def position():
    global dataBase
    global myWindow

    return 0



# 3. Сделать выборку сотрудников по зарплате
def salary():
    global dataBase
    global myWindow

    return 0






# 5. Удалить сотрудника
def delMember():
    global dataBase
    global myWindow

    return 0


# 6. Обновить данные сотрудника
def update():
    global dataBase
    global myWindow

    return 0


# 7. Экспортировать данные в формате json
def exportJSON():
    cd.exportToJSON()



# 8. Экспортировать данные в формате txt
def exportCSV():
    cd.exportToTXT() # Сохраняем БД






