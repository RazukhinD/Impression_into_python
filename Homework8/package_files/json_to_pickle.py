'''
Напишите функцию, которая ищет json файлы в указанной
директории и сохраняет их содержимое в виде
одноимённых pickle файлов
'''
import os
import json
import pickle


def convert_json_to_pickle(directory_path, output_directory):
    # Проверяем, существует ли указанная директория
    if not os.path.exists(directory_path):
        print(f"Директория '{directory_path}' не существует.")
        return

    # Создаем выходную директорию, если она не существует
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for root, _, files in os.walk(directory_path):
        for filename in files:
            if filename.endswith(".json"):
                json_file_path = os.path.join(root, filename)
                pickle_filename = f"{os.path.splitext(filename)[0]}.pickle"
                pickle_file_path = os.path.join(output_directory, pickle_filename)

                try:
                    with open(json_file_path, "r") as json_file:
                        # Загружаем JSON данные
                        data = json.load(json_file)

                        # Сохраняем данные в pickle файл
                        with open(pickle_file_path, "wb") as pickle_file:
                            pickle.dump(data, pickle_file)
                            print(f"Файл '{json_file_path}' был успешно конвертирован в '{pickle_file_path}'")

                except Exception as e:
                    print(f"Произошла ошибка при обработке файла '{json_file_path}': {str(e)}")


if __name__ == '__main__':
    directory_path = "./Seminars/Seminar8/"
    output_directory = "./Seminars/Seminar8/task5/"
    convert_json_to_pickle(directory_path, output_directory)
