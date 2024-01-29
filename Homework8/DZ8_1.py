'''
Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
Результаты обхода сохраните в файлы json, csv и pickle.
    Для дочерних объектов указывайте родительскую директорию.
    Для каждого объекта укажите файл это или директория.
    Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов
    и директорий.
'''
import os
import json
import csv
import pickle


def directory_info(directory):
    results = []

    def calc_dir_size(path):
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                total_size += os.path.getsize(file_path)
        return total_size

    for dirpath, dirnames, filenames in os.walk(directory):
        for dirname in dirnames:
            dir_info = {
                'path': os.path.join(dirpath, dirname),
                'type': 'directory',
                'size': calc_dir_size(os.path.join(dirpath, dirname))
            }
            results.append(dir_info)

        for filename in filenames:
            file_info = {
                'path': os.path.join(dirpath, filename),
                'type': 'file',
                'size': os.path.getsize(os.path.join(dirpath, filename))
            }
            results.append(file_info)

    return results


def save_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)


def save_to_csv(data, filename):
    with open(filename, 'w', encoding='utf-8', newline='') as csv_file:
        fieldnames = ['path', 'type', 'size']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for item in data:
            writer.writerow(item)


def save_to_pickle(data, filename):
    with open(filename, 'wb') as pickle_file:
        pickle.dump(data, pickle_file)


if __name__ == '__main__':
    directory = './Homework/'
    data = directory_info(directory)

    json_filename = './Homework/DZ8/DZ8_1/directory_info.json'
    csv_filename = './Homework/DZ8/DZ8_1/directory_info.csv'
    pickle_filename = './Homework/DZ8/DZ8_1/directory_info.pkl'

    save_to_json(data, json_filename)
    save_to_csv(data, csv_filename)
    save_to_pickle(data, pickle_filename)
