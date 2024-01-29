'''
Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
Распечатайте его как pickle строку
'''
import csv
import pickle


def read_csv_to_pickle(csv_file_path):
    try:
        # Читаем CSV файл и сохраняем строки в список
        with open(csv_file_path, 'r', newline='', encoding='utf-8') as f:
            csv_reader = csv.reader(f)
            data = list(csv_reader)
        # Преобразуем список строк в строку Pickle
        return pickle.dumps(data, protocol=4)
    except Exception as e:
        print(f"Ошибка при чтении CSV файла: {e}")
        return None


if __name__ == '__main__':
    csv_file_path = "./Seminars/Seminar8/task6/task04.csv"
    pickle_data = read_csv_to_pickle(csv_file_path)
    if pickle_data:
        print(pickle_data)
