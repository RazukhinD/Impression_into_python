'''
Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл.
Для тестированию возьмите pickle версию файла из задачи 4 этого семинара.
Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.
'''
import pickle
import csv
import os


def pickle_to_csv(pickle_file_path, csv_file_dir):
    # Проверяем, существует ли указанный pickle файл
    if not os.path.isfile(pickle_file_path):
        print("Указанный файл не существует.")
        return
    # Извлекаем имя файла без расширения
    file_name_without_extension = os.path.splitext(os.path.basename(pickle_file_path))[0]
    # Формируем имя CSV файла на основе имени исходного файла и заданной директории
    csv_file_path = os.path.join(csv_file_dir, f"{file_name_without_extension}.csv")
    # Создаем директорию, если она не существует
    os.makedirs(csv_file_dir, exist_ok=True)
    # Открываем pickle файл для чтения
    with open(pickle_file_path, 'rb') as pickle_file:
        data = pickle.load(pickle_file)
    if not data:
        print("Pickle файл пуст.")
        return
    # Определяем заголовки столбцов на основе ключей первого словаря
    column_headers = data[0].keys()
    # Открываем CSV файл для записи
    with open(csv_file_path, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=column_headers)
        # Записываем заголовки
        writer.writeheader()
        # Записываем данные из списка словарей в CSV файл
        for row in data:
            writer.writerow(row)

    print(f"Преобразование завершено. CSV файл сохранен по пути: {csv_file_path}")


if __name__ == '__main__':
    csv_file_dir = "./Seminars/Seminar8/task6"
    pickle_file_path = "./Seminars/Seminar8/task5/task04.pickle"
    pickle_to_csv(pickle_file_path, csv_file_dir)
