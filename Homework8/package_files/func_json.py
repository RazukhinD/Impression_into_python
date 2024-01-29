'''
Вспоминаем задачу 3 из прошлого семинара.
Мы сформировали текстовый файл с псевдо именами и произведением чисел.
Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
Имена пишите с большой буквы.
Каждую пару сохраняйте с новой строки.
'''
import json


def func_json(file1, res):
    with (
        open(file1, "r", encoding="utf-8") as f,
        open(res, "w", encoding="utf-8") as f2,
    ):
        new_json = {}
        for line in f:
            my_dict = line.replace('\n', '').split('=')
            new_json[my_dict[0]] = my_dict[1]
        my_dict = json.dump(new_json, f2, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    file1 = "./Seminars/Seminar8/task01/task03.txt"
    res = "./Seminars/Seminar8/task01/task01.json"
    func_json(file1, res)
