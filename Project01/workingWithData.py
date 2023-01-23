

# 1. Поиск сотрудника по ключу и значению
def findPersonal(myDict, searchKey, request):
    # searchKey - выбираемый пользователем объект поиска (int)
    # request - поисковое значение, вводимое с клавиатуры (str)
    res = {}
    for i in myDict:
        if myDict[i][searchKey] == request:
            res[i] = myDict[i]
            return res # Удачный поиск
    res[0] = ['Сотрудник не найден']
    return res # Неудачный поиск



# 2. Выборка сотрудников по должности
def sortOfPosition(myDict, position):
    res = {}
    if checkValidPosition(position):
        if str(myDict.items()).count(position) > 0: # Проверка совпадений во всём словаре по запрашиваемой должности
            for i in myDict:
                if myDict[i][3] == position:
                    res[i] = myDict[i]
        else:
            res[0] = ['Нет сотрудников на данной должности']
    else:
        res[0] = ['Должность указана неверно']
    return res

# 2.1 Проверка поискового значения (профессия)
def checkValidPosition(request):
    # professions - база данных профессий в нашем учреждении по запросу из данного модуля
    # professions = def()
    professions = {1: 'электрик', 2: 'сантехник', 3: 'инженер', 4: 'директор'} # Временное решение для проверки
    return bool(list(check.count(request) for check in professions.items()).count(1))


# 3. Выборка сотрудников по зарплате
def sortOfSalary(myDict, min, max):
    res = {}
    if checkValidPosition(min, max):
        for i in myDict:
            if int(min) <= int(myDict[i][4]) <= int(max):
                res[i] = myDict[i]
        if not len(res):
            res[0] = ['Сотрудники с подходящей зарплатой не найдены']
    else:
        res[0] = ['Значение указано неверно']
    return res

# 3.1 Проверка поискового значения (зарплата)
def checkValidPosition(min, max):
    alphaCheckMin = bool((list(symbol.isalpha() for symbol in min)).count(1) == 0)
    alphaCheckMax = bool((list(symbol.isalpha() for symbol in max)).count(1) == 0)
    if alphaCheckMin and alphaCheckMax:
        min = int(min)
        max = int(max)
        if max < 0 or min < 0 or max < min:
            return False
    else:
        return False
    return True



# 4. Добавление сотрудника в словарь
def newPersonal(myDict, newMember):
    newID = len(myDict) + 1
    myDict[newID] = list(newMember)
    return myDict

# 4.1 Создание новой записи о сотруднике








# ------------------------------------------------------------------------
# Проверка работы модулей:

# 1
searchKey = 0
request = 'Иван'

myDict = {1: ['Иван', 'Алеексеев', 'Иванович', 'электрик', '50000'],\
          2: ['Антон', 'Семенов', 'Петрович', 'сантехник', '60000'],\
          3: ['Никита', 'Иванов', 'Ильич', 'инженер', '70000']}

# print(findPersonal(myDict, searchKey, request))

# 2
# position = 'электрик'
position = 'директор'
# print(sortOfPosition(myDict, position))

# 3
max = '6500'
min = '5100'

# print(sortOfSalary(myDict, min, max))



# 4

newMember = ('Марья', 'Прокофьева', 'Ивановна', 'уборщик', '35000')
newPersonal(myDict, newMember)