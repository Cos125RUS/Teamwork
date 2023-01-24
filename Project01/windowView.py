from tkinter import *
from tkinter import ttk

import convertData as cd

# инициализация окна
myWindow = Tk()
myWindow.title('ДЗ-8')
myWindow.geometry('540x600')
myWindow.resizable(width=False, height=False)

# кнопка добавить
addButton = Button(myWindow, text = "Добавить", width = 10, height = 2, font=('Courier', 10,), command = None)
addButton.grid(row = 0, column = 0)

# кнопка найти
findButton = Button(myWindow, text = "Найти", width = 10, height = 2, font=('Courier', 10,), command = None)
findButton.grid(row = 0, column = 1)

# кнопка экспорт
exportButton = Button(myWindow, text = "Экспорт", width = 10, height = 2, font=('Courier', 10,), command = None)
exportButton.grid(row = 0, column = 2)

# кнопка изменить
changeButton = Button(myWindow, text = "Изменить", width = 10, height = 2, font=('Courier', 10,), command = None)
changeButton.grid(row = 0, column = 3)

# кнопка удалить
deleteButton = Button(myWindow, text = "Удалить", width = 10, height = 2, font=('Courier', 10,), command = None)
deleteButton.grid(row = 0, column = 4)

# кнопка удалить
deleteButton = Button(myWindow, text = "Справка", width = 10, height = 2, font=('Courier', 10,), command = None)
deleteButton.grid(row = 0, column = 5)

# считать БД в словарь
myDict = cd.importCSV()

CBVariableList = []

CBList = []

for key, value in myDict.items():
    CBVariableList.append(BooleanVar())
    myCheckbutton = Checkbutton(text = str(key), variable = CBVariableList[key - 1], onvalue=1, offvalue=0)
    myCheckbutton.grid(row = key, column = 0)
    CBList.append(myCheckbutton)
    myLabel = Label(text = value)
    myLabel.grid(row = key, column = 1, columnspan = 5)

# открыть окно
myWindow.mainloop()

