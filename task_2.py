import json
import csv# TODO импортировать необходимые молули


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"
indent = 4

def task() -> None:
    with open(INPUT_FILENAME, "r") as file:  # TODO считать содержимое csv файла
        reader = csv.DictReader(file)
        data = []
        for row in reader:
            data.append(row)

    with open(OUTPUT_FILENAME, "w") as out_f:  # TODO Сериализовать в файл с отступами равными 4
        json.dump(data, out_f, indent=indent)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
