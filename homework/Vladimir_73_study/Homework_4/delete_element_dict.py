# 1. Создаём словарь
my_dict = {
    'tuple': (1, 2, 3, 4, 5),
    'list': [10, 20, 30, 40, 50],
    'dict': {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5},
    'set': {1, 2, 3, 4, 5}
}

print("1. Исходный словарь создан")
print(f"   my_dict['dict'] = {my_dict['dict']}")

# 2. Добавляем элемент с ключом-кортежем
my_dict['dict'][('i am a tuple',)] = 'new element'
print("\n2. Добавили элемент с ключом-кортежем")
print(f"   my_dict['dict'] = {my_dict['dict']}")

# 3. Удаляем какой-нибудь элемент
del my_dict['dict']['c']
print("\n3. Удалили элемент с ключом 'c'")
print(f"   my_dict['dict'] = {my_dict['dict']}")

# 4. Выводим весь итоговый словарь
print("\n4. Итоговый словарь my_dict:")
for key, value in my_dict.items():
    print(f"   {key}: {value}")
