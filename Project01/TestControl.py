import workingWithData as wwd
import convertData as cd
import userView as uv

dataBase = cd.importCSV()  # Подгрузили БД
myWindow = uv.mainWindow()  # Загружаем меню
useData = dataBase # Временные данные


# Стартовое меню
def start():
    uv.upMenu(myWindow) # Верхнее меню
    myWindow.mainloop() # Мотор


# 1. Отобразить список сотрудников
def showInformation(data = dataBase):
    uv.viewList(data, myWindow)


# 2. Добавить сотрудника
def addMember():
    uv.changeField(myWindow, 0)


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


# 6. Удалить сотрудника
def delMember():
    checkList = uv.watchCheckList() # Список выбранных позиций
    keysList = wwd.createKeysList(useData, checkList) # Ключи
    for delID in keysList:
        wwd.deletionOnID(dataBase, delID)
        if useData != dataBase:
            wwd.deletionOnID(useData, delID)
    cd.exportToCSV(dataBase)
    showInformation(useData) if len(useData) else uv.clear(myWindow)
    uv.infoWindow('Удалено')


# 7. Обновить данные сотрудника
def update():
    global dataBase
    checkList = uv.watchCheckList() # Список выбранных позиций
    if not checkList:
        uv.infoWindow('Выберите сотрудника')
    elif len(checkList) > 1:
        uv.infoWindow('Выбрано несколько сотрудников')
    else:
        uv.changeField(myWindow, 4)

def saveNewMember(dataBase, personal):
    keysList = wwd.createKeysList(useData, checkList)
    dataBase = wwd.reloading(dataBase, personal, keysList[0])

    return 0


# 8. Экспортировать данные в формате json
def exportJSON():
    cd.exportToJSON(dataBase)



# 9. Экспортировать данные в формате txt
def exportTXT():
    cd.exportToTXT(dataBase) # Сохраняем БД





# Транзит данных между функциями
def transit(index, data):
    function = [wwd.newPersonal, wwd.findPersonal, wwd.sortOfPosition, wwd.sortOfSalary, saveNewMember]
    global useData
    useData = function[index](dataBase, data)
    cd.exportToCSV(dataBase)
    # uv.clear(myWindow)
    if 0 in useData.keys():
        uv.infoWindow(*useData[0])
    else:
        showInformation(useData)

