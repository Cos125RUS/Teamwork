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
def showInformation(data = dataBase):
    global dataBase
    global myWindow
    uv.indention(myWindow, 2)
    uv.viewList(data, myWindow)


# 2. Добавить сотрудника
def addMember():
    global dataBase
    global myWindow
    uv.changeField(myWindow)




# 3. Найти сотрудника
def findMember():
    global dataBase
    global myWindow
    uv.indention(myWindow, 4)
    uv.findRequest(myWindow)





# Транзит данных между функциями
def transit(index, data):
    function = [wwd.newPersonal, wwd.findPersonal]
    res = function[index](dataBase, data)
    cd.exportToCSV(dataBase)
    showInformation(res)





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
    global dataBase
    cd.exportToJSON(dataBase)



# 8. Экспортировать данные в формате txt
def exportTXT():
    global dataBase
    cd.exportToTXT(dataBase) # Сохраняем БД






