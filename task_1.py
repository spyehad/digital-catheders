import json
INPUT_FILE = "input.json"

# TODO решите задачу
def task() -> float:
    with open(INPUT_FILE, "r") as file:
        data = json.load(file)
        total = 0
        for item in data:
            total += item["score"] * item["weight"]
    return round(total, 3)


print(task())
