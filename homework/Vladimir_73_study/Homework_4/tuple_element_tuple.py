# 1. Создаём словарь
my_dict = {
    'tuple': (1, 2, 3, 4, 5),
    'list': [10, 20, 30, 40, 50],
    'dict': {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5},
    'set': {1, 2, 3, 4, 5}
}

print("1. Исходный словарь создан")
for key, value in my_dict.items():
    print(f"   {key}: {value}")

print('\n2.Из списка tuple выводим последний элемент:')
print(my_dict['tuple'][-1])
