from tkinter import *
import TestControl as control


def mainWindow():
    # инициализация окна
    myWindow = Tk()
    myWindow.title('ДЗ-8')
    myWindow.geometry('540x600')
    myWindow.resizable(width=False, height=False)
    return myWindow



# Верхнее меню
def upMenu(myWindow):

    # кнопка справка
    menuButton = Button(myWindow, text="Сотрудники", width=10, height=2, font=('Courier', 10), command=control.showInformation)
    menuButton.grid(row=0, column=0)

    # кнопка добавить
    addButton = Button(myWindow, text="Добавить", width=10, height=2, font=('Courier', 10), command=control.addMember)
    addButton.grid(row=0, column=1)

    # кнопка найти
    findButton = Button(myWindow, text="Найти", width=10, height=2, font=('Courier', 10), command=control.findMember)
    findButton.grid(row=0, column=2)

    # кнопка изменить
    changeButton = Button(myWindow, text="Изменить", width=10, height=2, font=('Courier', 10), command=control.update)
    changeButton.grid(row=0, column=3)

    # кнопка удалить
    deleteButton = Button(myWindow, text="Удалить", width=10, height=2, font=('Courier', 10), command=control.delMember)
    deleteButton.grid(row=0, column=4)

    # кнопка экспорт
    exportButton = Button(myWindow, text="Экспорт", width=10, height=2, font=('Courier', 10), command=lambda :exportView(myWindow))
    exportButton.grid(row=0, column=5)

    # Отступ
    indention = Label(myWindow, text='', width=10, height=2)
    indention.grid(row=1, column=1)



# Кнопки экспорта
def exportView(myWindow):
    JSONButton = Button(myWindow, text="JSON", width=10, height=2, font=('Courier', 10), command=control.exportJSON)
    JSONButton.grid(row=1, column=5)
    TXTButton = Button(myWindow, text="TXT", width=10, height=2, font=('Courier', 10), command=control.exportTXT)
    TXTButton.grid(row=2, column=5)

# Отступ
def indention(myWindow, rows):
    labelList = []
    indentionRows = rows
    for i in range(indentionRows):
        indention = Label(myWindow, text='')
        indention.grid(row=i + 1, column=1)
        labelList.append([indention])


# Список на экране
def viewList(myDict, myWindow):
    varList = []
    checkbuttonList = []
    labelList = []
    lines = len(myDict.keys())
    myCount = lines

    # цикл вывода Checkbutton и строчек БД
    for key in myDict:
        varList.append(IntVar())
        myCheckbutton = Checkbutton(text=key, variable=varList[myCount - lines])
        myCheckbutton.grid(row=myCount, column=0)
        checkbuttonList.append(myCheckbutton)
        surname = Label(myWindow, text=myDict[key][1])
        surname.grid(row=myCount, column=1)
        name = Label(myWindow, text=myDict[key][0])
        name.grid(row=myCount, column=2)
        patronomic = Label(myWindow, text=myDict[key][2])
        patronomic.grid(row=myCount, column=3)
        position = Label(myWindow, text=myDict[key][3])
        position.grid(row=myCount, column=4)
        salary = Label(myWindow, text=myDict[key][4])
        salary.grid(row=myCount, column=5)
        labelList.append([surname, name, patronomic, position, salary])
        myCount += 1



# Добавление сотрудника
def changeField(myWindow):
    # вывести строку наименования таблицы БД
    Label(myWindow, text="Фамилия").grid(row=5, column=0)
    Label(myWindow, text="Имя").grid(row=5, column=1)
    Label(myWindow, text="Отчество").grid(row=5, column=2)
    Label(myWindow, text="Должность").grid(row=5, column=3)
    Label(myWindow, text="З/П").grid(row=5, column=4)
    #
    enSurname = Entry(width=10, font=('Courier', 10))
    enSurname.grid(row=6, column=0)
    enName = Entry(width=10, font=('Courier', 10))
    enName.grid(row=6, column=1)
    enPatronomic = Entry(width=10, font=('Courier', 10))
    enPatronomic.grid(row=6, column=2)
    enPosition = Entry(width=10, font=('Courier', 10))
    enPosition.grid(row=6, column=3)
    enSalary = Entry(width=10, font=('Courier', 10))
    enSalary.grid(row=6, column=4)
    # кнопка добавить
    addButton = Button(myWindow, text="Добавить", width=10, height=2, font=('Courier', 10),\
                       command=lambda : control.transit(0, (enName.get(), enSurname.get(), enPatronomic.get(), enPosition.get(), enSalary.get())))
    addButton.grid(row=6, column=5)


# Окно запросов
def findRequest(myWindow):
    Label(myWindow, text="Запрос").grid(row=4, column=1)
    request = Entry(width=10, font=('Courier', 10))
    request.grid(row=4, column=2)
    findButton = Button(myWindow, text="Найти", width=10, height=2, font=('Courier', 10),\
                       command=lambda : control.transit(1, (request.get())))
    findButton.grid(row=4, column=3)