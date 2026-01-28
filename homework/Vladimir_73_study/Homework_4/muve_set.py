my_dict = {
    'tuple': (1, 2, 3, 4, 5),
    'list': [10, 20, 30, 40, 50],
    'dict': {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5},
    'set': {1, 2, 3, 4, 5}
}

print("Создан список 'my_dict:'")

for key, value in my_dict.items():
    print(f"   {key}: {value}")

# Добавляем элемент в set
print('\nДобавляем элемент в set')
print("my_dict['set'].add(12)")
my_dict['set'].add(12)
print(f"set:{my_dict['set']}")

# Удаляем элемент из множества
print(
    "\nУдаляем элемент из множества имеющего значение 4 my_dict['set'].discard(4)")
my_dict['set'].discard(4)
print(f"set:{my_dict['set']}")

# 4. Выводим весь итоговый словарь
print("\n4. Итоговый словарь my_dict:")
for key, value in my_dict.items():
    print(f"   {key}: {value}")
