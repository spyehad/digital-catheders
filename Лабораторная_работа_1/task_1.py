
numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
numbers_no_none = numbers[:4] + numbers[5:]
mean = sum(numbers_no_none) / len(numbers)
numbers_fixed = numbers[:4] + [mean] + numbers[5:]
print("Измененный список:", numbers_fixed)
