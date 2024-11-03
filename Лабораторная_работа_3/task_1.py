# TODO Напишите функцию для поиска индекса товара

# Своя функция
def get_ind(item_list, item):
    item_index = None
    for ind, i in enumerate(item_list):
        if i == item:
            item_index = ind
            break
    return item_index

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = get_ind(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")

