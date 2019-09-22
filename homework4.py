from pprint import pprint


def name_by_number(d):
    """ функция которая по номеру документа определяет има и выводит его на экран"""
    num = input('номер')
    for numbre in d:
        name = 0
        if numbre['number'] == num:
            name = numbre['name']

            return name


def lists(di):
    """ функция которая выводит на экран весь словарь
    """

    for i in di:
        for k, v in i.items():
            pprint(v)


def shalfs(s):
    """ функция котрая по номеру документа называет полку на которой он лежит
  #   """
    num = input('введите номер документа')
    for k, numbre in s.items():
        if num in numbre:
            print('номер полки', k)


def add_document(dicts, lists):
    """функция которая позволяет добавит документ и поместить его на полку
    """
    types = input('введите тип документа ')
    numbers = input('введите номер документа ')
    owner = input('введите владельца ')
    num_of_shalf = (input('введите номер полки '))
    dic = {}
    dic["type"] = types
    dic["number"] = numbers
    dic["name"] = owner
    lists.append(dic)
    dicts.setdefault(num_of_shalf, [])

    dicts[num_of_shalf].append(numbers)

    return (dicts, lists)


def delit_sobre(lists, dicts):
    """ функция удаляющая по номеру мсю информацию из документов и уберает его с полки
    """
    num = input('введите номер')
    for number in lists:
        if number['number'] == num:
            lists.remove(number)
    if number['number'] != num:
        print('нет таких, не удалить то чего нет')
    for k, number in directories.items():
        if num in number:
            number.remove(num)
    print(lists, dicts)


def add_new_shalf(dicts):
    """функция добовляющая новую полку
    """
    number_of_shalf = input('введите номер новой полки')
    if number_of_shalf in dicts.keys():
        print('такая полка есть')
    else:
        dicts[number_of_shalf] = []
        print(dicts)


def move_doc(dicts):
    """функция перемещающая документ на выбранную полку
    """
    num = input('введите номер документа')
    num_of_shalf = input('введите номер полки на которую надо переместить')
    for k, number in dicts.items():
        if num in number:
            number.remove(num)

            dicts.setdefault(num_of_shalf, [])
            dicts[num_of_shalf].append(num)

            return (dicts)


def giv_name(do):
    """ функция которая будет выдовать список всех владельцев документов
    """
    try:
        names_of = []
        for name in do:
            names_of.append(name['name'])
        return (names_of)
    except KeyError:
        print('у этих документов нет владельца')


def user(a):
    """функция обрабатывающая пользывательский выводит
    """

    a = comand

    if a == 'p':
        p = name_by_number(documents)
        print(p)
    elif a == 'l':
        l = lists(documents)
        print(l)

    elif a == 's':
        s = shalfs(directories)
        print(s)
    elif a == 'a':
        a = add_document(directories, documents)
        print(a)
    elif a == 'd':
        d = delit_sobre(documents, directories)
        print(d)
    elif a == 'a_s':
        a_s = add_new_shalf(directories)
    elif a == 'm':
        m = move_doc(directories)
        print(m)
    elif a == 'n':
        n = giv_name(documents)
        print(n)


documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

begin = input('для начала работы нажмите enter')

while True:

    comand = input('выбирите функцию: p,l,s,a,a_s,d,m   _')
    if comand == '0':
        break
    else:
        start = user(begin)
        print('продолжим')