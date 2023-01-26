import workingWithData as wwd
import convertData as cd
import userView as uv

dataBase = cd.importCSV()  # Подгрузили БД
myWindow = uv.mainWindow()  # Загружаем меню


# Стартовое меню
def start():
    uv.upMenu(myWindow) # Верхнее меню
    myWindow.mainloop() # Мотор


# 1. Отобразить список сотрудников
def showInformation(data = dataBase):
    uv.viewList(data, myWindow)


# 2. Добавить сотрудника
def addMember():
    uv.changeField(myWindow)




# 3. Найти сотрудника
def findMember():
    uv.findRequest(myWindow)

# 4. Сделать выборку сотрудников по должности
def position():
    uv.profRequest(myWindow)
def checkPosition(position):
    professionsList = cd.importProf()
    return wwd.checkValidPosition(professionsList, position)
def newPos(pos):
    cd.exportProf(pos)

# 5. Сделать выборку сотрудников по зарплате
def salary():
    uv.salRequest(myWindow)


# Транзит данных между функциями
def transit(index, data):
    function = [wwd.newPersonal, wwd.findPersonal, wwd.sortOfPosition, wwd.sortOfSalary]
    res = function[index](dataBase, data)
    cd.exportToCSV(dataBase)
    showInformation(res)
















# 5. Удалить сотрудника
def delMember():

    return 0


# 6. Обновить данные сотрудника
def update():

    return 0


# 7. Экспортировать данные в формате json
def exportJSON():
    cd.exportToJSON(dataBase)



# 8. Экспортировать данные в формате txt
def exportTXT():
    cd.exportToTXT(dataBase) # Сохраняем БД






