# Для того, что хранится под ключом ‘list’:
# добавьте в конец списка еще один элемент
# удалите второй элемент списка

my_dict = {
    'tuple': (1, 2, 3, 4, 5),
    'list': [10, 20, 30, 40, 50],
    'dict': {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5},
    'set': {1, 2, 3, 4, 5}
}

print("Создан список 'my_dict:'")

for key, value in my_dict.items():
    print(f"   {key}: {value}")

# Добавляем элемент в конец списка
my_dict['list'].append(60)

print("\nПосле добавления 60, в конец списка list:")
print(f"list:{my_dict['list']}")

# Удаляем второй элемент списка
del my_dict['list'][1]

print('\n После удаления второго элемента из списка list: ')
print(f"list:{my_dict['list']}")


# 4. Выводим весь итоговый словарь
print("\n4. Итоговый словарь my_dict:")
for key, value in my_dict.items():
    print(f"   {key}: {value}")
