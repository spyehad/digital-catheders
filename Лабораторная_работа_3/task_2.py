# TODO Напишите функцию find_common_participants
def find_common_participants(fst_str, snd_str, sep = ","):
    fst_set = set(fst_str.split(sep))
    snd_set = snd_str.split(sep)
    inter_set = list(fst_set.intersection(snd_set))
    inter_set.sort()
    return inter_set

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
common_participants = find_common_participants(participants_first_group, participants_second_group, "|")
print(common_participants)