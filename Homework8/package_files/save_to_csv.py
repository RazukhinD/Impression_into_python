'''
Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV.
'''
import csv
import json


def save_to_csv(data, filename):
    with open(filename, 'w', encoding='utf-8', newline='') as csv_file:
        fieldnames = ['Level', 'id', 'Name']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for key, value in data.items():
            level, id = key, list(value.keys())[0]
            name = value[id]
            writer.writerow({'Level': level, 'id': id, 'Name': name})


if __name__ == '__main__':
    file = "./Seminars/Seminar8/task02/task02.json"
    res = "./Seminars/Seminar8/task03/task03.csv"
    my_dict = {}

    with open(file, 'r', encoding='utf-8') as f:
        my_dict = json.load(f)

    save_to_csv(my_dict, res)
