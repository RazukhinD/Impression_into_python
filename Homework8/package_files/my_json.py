'''
Напишите функцию, которая в бесконечном цикле запрашивает имя,
личный идентификатор и уровень доступа (от 1 до 7).
После каждого ввода добавляйте новую информацию в JSON файл.
Пользователи группируются по уровню доступа.
Идентификатор пользователя выступает ключём для имени.
Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
При перезапуске функции уже записанные в файл данные должны сохраняться.
'''


import json

my_dict = {}


def my_json(res):

    with open(res, 'r', encoding='utf-8') as f:
        my_dict = json.load(f)

    _id = 4
    while True:
        _id += 1
        name = input('Введите имя ')
        if name == 'exit':
            break
        level = input('Введите уровень ')
        if int(level) < 0 or int(level) > 7:
            print('Error')
            continue
        if level not in my_dict.keys():
            my_dict[level] = {}
        my_dict[level][_id] = name
        print(my_dict)

    with open(res, 'w', encoding='utf-8') as f:
        json.dump(my_dict, f)


if __name__ == "__main__":
    res = "./Seminars/Seminar8/task02/task02.json"
    my_json(res)
