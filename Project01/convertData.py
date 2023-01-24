# метод для экспорта БД в формат .json
def exportToJSON():
    # путь к файлам БД
    myDataBasePathCsv = 'database.csv'
    myDataBasePathJson = 'database.json'
    # словарь, в который складываются записи из БД
    myList = []
    # открываем файл CSV на чтение
    with open(myDataBasePathCsv, 'r', encoding = 'utf-8') as dataBase:
        for line in dataBase:
            # запишем в список строки, кроме первой
            if line[0] != 'i':
                myList.append(line)
    # открываем или создаем файл TXT на запись
    with open(myDataBasePathJson, 'w+', encoding = 'utf-8') as jsonFile:
        # построчно записываем в формате JSON
        jsonFile.write('[')
        # переменная для подсчета количества записей
        myCount = 0
        for item in myList:
            jsonFile.write('\n')
            jsonFile.write('    {' + '\n')
            jsonFile.write(f'        "id": {item.split(";")[0]},\n')
            jsonFile.write(f'        "name": {item.split(";")[1]},\n')
            jsonFile.write(f'        "surname": {item.split(";")[2]},\n')
            jsonFile.write(f'        "patronymic": {item.split(";")[3]},\n')
            jsonFile.write(f'        "position": {item.split(";")[4]},\n')
            jsonFile.write(f'        "salary": {item.split(";")[5]}\n')
            myCount += 1
            # определяем надо ли ставить запятую в конце
            if myCount != len(myList):
                jsonFile.write('    },')
            else:
                jsonFile.write('    }')
        jsonFile.write('\n]')
        
# метод для экспорта БД в формат .txt
def exportToTXT():
    # путь к файлам БД
    myDataBasePathCsv = 'database.csv'
    myDataBasePathTxt = 'database.txt'
    # словарь, в который складываются записи из БД
    myList = []
    # открываем файл CSV на чтение
    with open(myDataBasePathCsv, 'r', encoding = 'utf-8') as dataBase:
        for line in dataBase:
            # запишем в список строки
            myList.append(line)
    # открываем или создаем файл TXT на запись
    with open(myDataBasePathTxt, 'w+', encoding = 'utf-8') as txtFile:
        # построчно записываем список
        for item in myList:
            txtFile.write(item)

# сохранение БД
def exportToCSV(myDict):
    # путь к файлу БД
    myDataBasePath = 'database1.csv'
    # открываем файл на запись
    with open(myDataBasePath, 'w+', encoding = 'utf-8') as dataBase:
        dataBase.write(f'id;name;surname;patronymic;position;salary;\n')
        # переменная подсчета записей
        myCount = 0
        for key in myDict:
            # пропускаем первую строку
            myString = str(key) + ';'
            for item in myDict[key]:
                myString += str(item) + ';'
            myCount += 1
            if myCount != len(myDict):
                myString += '\n'
            dataBase.write(myString)

# метод для импорта БД в формат .csv. Используется для выдачи словаря, для последующей работы с ним
def importCSV():
    # путь к файлу БД
    myDataBasePath = 'database1.csv'
    # переменная подсчета записей
    myCount = 0
    # словарь, в который складываются записи из БД
    myDict = {}
    # открываем файл на чтение
    with open(myDataBasePath, 'r', encoding = 'utf-8') as dataBase:
        for line in dataBase:
            # пропускаем первую строку
            if line.strip()[0] != 'i':
                # инкрементируем счетчик
                myCount += 1
                # разбиваем строку и формируем список
                myList = line.strip().split(';')
                # удалить последний элемент ''
                myList.remove('')
                myList.pop(0)
                myDict[myCount] = myList
    # возвращаем словарь
    return myDict




'''
# ------------------------------------------------------------------------
# Проверка работы функций:

print(importCSV())

exportToTXT()

exportToJSON()

myDict = {1: ['Иван', 'Алеексеев', 'Иванович', 'электрик', '50000'], 2: ['Антон', 'Семенов', 'Петрович', 'сантехник', '51000'], 3: ['Никита', 'Иванов', 'Ильич', 'инженер', '52000']}

exportToCSV(myDict)
'''