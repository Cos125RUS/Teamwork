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
    changeButton = Button(myWindow, text="Выборка", width=10, height=2, font=('Courier', 10), command=lambda :selectionView(myWindow))
    changeButton.grid(row=0, column=3)
    # кнопка удалить
    deleteButton = Button(myWindow, text="Действия", width=10, height=2, font=('Courier', 10), command=lambda :actionView(myWindow))
    deleteButton.grid(row=0, column=4)
    # кнопка экспорт
    exportButton = Button(myWindow, text="Экспорт", width=10, height=2, font=('Courier', 10), command=lambda :exportView(myWindow))
    exportButton.grid(row=0, column=5)
    # Отступ
    Label(myWindow, text='', width=10, height=2).grid(row=1, column=2)



# Высплывающии кнопки:
# Экспорт
def exportView(myWindow):
    JSONButton = Button(myWindow, text="JSON", width=10, height=2, font=('Courier', 10), command=control.exportJSON)
    JSONButton.grid(row=1, column=5)
    TXTButton = Button(myWindow, text="TXT", width=10, height=2, font=('Courier', 10), command=control.exportTXT)
    TXTButton.grid(row=2, column=5)

# Выборка
def selectionView(myWindow):
    positionButton = Button(myWindow, text="Должность", width=10, height=2, font=('Courier', 10), command=control.position)
    positionButton.grid(row=1, column=3)
    salaryButton = Button(myWindow, text="Зарплата", width=10, height=2, font=('Courier', 10), command=control.salary)
    salaryButton.grid(row=2, column=3)

# Действия
def actionView(myWindow):
    changeButton = Button(myWindow, text="Изменить", width=10, height=2, font=('Courier', 10), command=None)
    changeButton.grid(row=1, column=4)
    delButton = Button(myWindow, text="Удадить", width=10, height=2, font=('Courier', 10), command=None)
    delButton.grid(row=2, column=4)




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

# Выбор должности
def profRequest(myWindow):
    Label(myWindow, text="Должность").grid(row=4, column=1)
    request = Entry(width=10, font=('Courier', 10))
    request.grid(row=4, column=2)
    findButton = Button(myWindow, text="Найти", width=10, height=2, font=('Courier', 10),\
                       command=lambda : control.transit(2, (request.get())))
    findButton.grid(row=4, column=3)

# Выбор зарплаты
def salRequest(myWindow):
    Label(myWindow, text="От").grid(row=4, column=0)
    downLine = Entry(width=10, font=('Courier', 10))
    downLine.grid(row=4, column=1)
    Label(myWindow, text="До").grid(row=4, column=3)
    upLine = Entry(width=10, font=('Courier', 10))
    upLine.grid(row=4, column=4)
    findButton = Button(myWindow, text="Найти", width=10, height=2, font=('Courier', 10),\
                       command=lambda : control.transit(3, (downLine.get(), upLine.get())))
    findButton.grid(row=6, column=2)