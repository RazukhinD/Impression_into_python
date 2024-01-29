'''
Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
Дополните id до 10 цифр незначащими нулями.
В именах первую букву сделайте прописной.
Добавьте поле хеш на основе имени и идентификатора.
Получившиеся записи сохраните в json файл, где каждая строка csv файла представлена как отдельный json словарь.
Имя исходного и конечного файлов передавайте как аргументы функции.
'''
import csv
import json


def csv_to_json(file, res):
    # Чтение данных из CSV-файла
    data = []
    with open(file, 'r', newline='') as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            level, _id, name = row
            # Дополнение id до 10 цифр нулями
            _id = _id.zfill(10)
            # Преобразование первой буквы имени в прописную
            name = name.capitalize()
            # Вычисление хеша на основе имени и id
            hash_value = hash(f"{name}{_id}")
            data.append({
                'Level': level,
                'id': _id,
                'Name': name,
                'Hash': hash_value
            })
            # Сохранение данных в JSON-файл
            with open(res, 'w') as json_file:
                json.dump(data, json_file, indent=4)


if __name__ == '__main__':
    file = "./Seminars/Seminar8/task03/task03.csv"
    res = "./Seminars/Seminar8/task04/task04.json"
    csv_to_json(file, res)
