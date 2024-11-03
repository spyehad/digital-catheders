# TODO  Напишите функцию count_letters
def count_letters(text):
    letters_dict = {}
    for letter in text:
        if not letter.isalpha(): continue
        let = letter.lower()
        if letters_dict.get(let) is None:
            letters_dict[let] = 1
        else:
            letters_dict[let] += 1
    return letters_dict


# TODO Напишите функцию calculate_frequency
def calculate_frequency(letters_dict):
    frequency_dict = {}
    letters_total = sum(letters_dict.values())
    for item in letters_dict.items():
        name = item[0]
        value = item[1]
        frequency_dict[name] = float(value/letters_total)
    return frequency_dict

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
let_dict = count_letters(main_str)
freq_dict = calculate_frequency(let_dict)

for pair in freq_dict.items():
    item_name = pair[0]
    item_value = pair[1]
    print(f"{item_name}: {item_value:.2f}")