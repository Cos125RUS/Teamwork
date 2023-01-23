

# 1. Поиск сотрудника по ключу и значению
def findPersonal(myDict, searchKey, request):
    # searchKey - выбираемый пользователем объект поиска (int)
    # request - поисковое значение, вводимое с клавиатуры (str)
    res = {}
    for i in myDict: # Проход по словарю
        if myDict[i][searchKey].lower() == request.lower(): # Ищем совпадения по объекту поиска
            res[i] = myDict[i]
            return res # Удачный поиск
    res[0] = ['Сотрудник не найден']
    return res # Неудачный поиск



# 2. Выборка сотрудников по должности
def sortOfPosition(myDict, position):
    res = {}
    if checkValidPosition(position): # Проверка на правильный ввод (если реализуем выбор профессии из списка вместо ввода, проверка не нужна)
        if str(myDict.items()).count(position) > 0: # Проверка совпадений во всём словаре по запрашиваемой должности
            for i in myDict:
                if myDict[i][3] == position:
                    res[i] = myDict[i] # Формируем новый словарь из подходящих сотрудников
        else:
            res[0] = ['Нет сотрудников на данной должности']
    else:
        res[0] = ['Должность указана неверно']
    return res

# 2.1 Проверка поискового значения (профессия)
def checkValidPosition(request):
    # professions - база данных профессий в нашем учреждении по запросу из данного модуля
    # professions = def()
    professions = {1: 'электрик', 2: 'сантехник', 3: 'инженер', 4: 'директор', 5: 'уборщик'} # Временное решение для проверки
    return bool(list(check.count(request) for check in professions.items()).count(1))


# 3. Выборка сотрудников по зарплате
def sortOfSalary(myDict, min, max):
    res = {}
    if checkValue(min, max): # Проверка введённых значений
        for i in myDict:
            if int(min) <= int(myDict[i][4]) <= int(max): # Проверка критериев по каждому сотруднику
                res[i] = myDict[i] # Подходящих сотрудников добавляем в новый словарь
        if not len(res): # Проверка пустого списка результатов
            res[0] = ['Сотрудники с подходящей зарплатой не найдены']
    else:
        res[0] = ['Значение указано неверно']
    return res

# 3.1 Проверка поискового значения (зарплата)
def checkValue(min, max):
    if alphaCheck(min) and alphaCheck(max): # Проверка на символьный ввод
        # Преобразуем строку в число при удачной проверки
        min = int(min)
        max = int(max)
        # Проверка на отрицательные значения и min > max
        if max < 0 or min < 0 or max < min:
            return False
    else:
        return False
    return True


# Проверка на символьный ввод
def alphaCheck(value):
    return bool((list(symbol.isalpha() for symbol in value)).count(1) == 0)



# 4. Добавление сотрудника в словарь
def newPersonal(myDict, newMember):
    lastKeys = int(list(myDict.keys())[-1]) # Смотрим id последней записи
    # Проверяем, равен ли последний id общему количеству записей
    if lastKeys == len(myDict):
        newID = len(myDict) + 1
        myDict[newID] = list(newMember)
    else:
        # Поиск пустых строк (при удалении пользователя id не меняется)
        for i, key in enumerate(myDict, 1):
            if int(key) != i:
                # Если находим пустую строку, вписываем туда нового пользователя
                myDict[i] = list(newMember)
                myDict = dict(sorted(myDict.items()))
                break # Прерываем поиск после первой найденной пустой строки
    return myDict


# 4.1 Проверка введённых данных о сотруднике (вызывается из Контроллера после полученных от пользователя значений)
def checkCorrectInput(myDict, newMember):
    # Если реализуем пошаговый ввод данных, тогда общую проверку заменим на поочерёдный вызов из Контроллера
    name, surname, patronymic, position, salary = newMember # Разнуменуем входящие данные
    # Проверка зп на символьные и отрицательные значения
    if not (alphaCheck(salary) and int(salary) > 0):
        return False
    if not checkValidPosition(position): # Проверяем, не отсутствует ли профессия в нашем списке профессий
        # Создать запрос на добавление новой профессии в список вместо прерывания
        print('Новая профессия')
    # Проверка на повторный ввод сотрудника (поиск аналогичной записи в БД)
    find = findPersonal(myDict, 1, surname)
    if not (0 in find.keys()): # Проверяем фамилии на совпадения
        find = findPersonal(find, 0, name)
        if not (0 in find.keys()):# Проверяем имена на совпадения
            find = findPersonal(find, 2, patronymic)
            if not (0 in find.keys()): # Проверяем отчество на совпадения
                print('Человек с таким ФИО уже записан') # Запрос пользователю на продолжение ввода
                find = findPersonal(find, 3, position)
                if not (0 in find.keys()): # Проверяем должность на совпадения
                    print('Полное совпадение с ранее записанным сотрудником') # Запрос пользователю на продолжение ввода
    return True



# 5.1 Удаление сотрудника по записи
def deletionOnPerson(myDict, delMember):
    for delID in delMember.keys(): # Извлекаем id пользователя
        del myDict[delID] # Удаляем пользователя по id
    return myDict

# 5.2 Удаление сотрудника по ID
def deletionOnID(myDict, delID):
    del myDict[delID]
    return myDict




# 6. Обновление данных сотрудника
def reloading(myDict, changedPersonal, PersID):
    deletionOnID(myDict, PersID) # Удаляем запись сотрудника
    checkCorrectInput(myDict, changedPersonal) # Проверка на повторения
    myDict[PersID] = list(changedPersonal) # Создаём новую запись под тем же id
    myDict = dict(sorted(myDict.items())) # Сортируем словарь
    return myDict


# Извлечение записи из БД
def takeProfile(myDict, id):
    return {id: myDict[id]}







# ------------------------------------------------------------------------
# Проверка работы функций:

# 1
searchKey = 0
request = 'ивАн'

myDict = {1: ['Иван', 'Алеексеев', 'Иванович', 'электрик', '50000'],\
          4: ['Антон', 'Семенов', 'Петрович', 'сантехник', '60000'],\
          5: ['Никита', 'Иванов', 'Ильич', 'инженер', '70000']}

print(findPersonal(myDict, searchKey, request))

# 2
position = 'электрик'
# position = 'директор'
print(sortOfPosition(myDict, position))

# 3
max = '65000'
min = '5100'

print(sortOfSalary(myDict, min, max))



# 4

newMember = ('Марья', 'Прокофьева', 'Ивановна', 'уборщик', '35000')
myDict = newPersonal(myDict, newMember)
print(myDict)

# 4.1
checkCorrectInput(myDict, ('Петр', 'Прохоров', 'Петрович', 'менеджер', '100000'))
checkCorrectInput(myDict, ('Иван', 'Алеексеев', 'Иванович', 'электрик', '50000'))


# 5

myDict = deletionOnPerson(myDict, {1: ['Иван', 'Алеексеев', 'Иванович', 'электрик', '50000']})
print(myDict)


# Извлечение записи из БД
takeID = 4
takeMan = takeProfile(myDict, takeID)
print(takeMan)

myDict = deletionOnID(myDict, 5)
print(myDict)

# 6
myDict = reloading(myDict, ('Марья', 'Прокофьева', 'Ивановна', 'уборщик', '40000'), 2)
print(myDict)
