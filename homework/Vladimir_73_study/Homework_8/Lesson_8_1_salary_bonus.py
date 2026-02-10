'''import random

# Запрашиваем зарплату
salary_input = input("Введите вашу зарплату (число): ")
salary = int(salary_input)

# Случайно определяем, будет ли бонус
bonus = random.choice([True, False])

# Обрабатываем бонус
if bonus:
    bonus_amount = random.randint(100, 5000)
    total_salary = salary + bonus_amount
else:
    total_salary = salary

# Выводим результат
print(f"${total_salary}")

# Для наглядности можно добавить информацию о бонусе
print(f"Бонус: {'Да' if bonus else 'Нет'}")
if bonus:
    print(f"Размер бонуса: ${bonus_amount}")
'''

import random

# Бесконечный цикл для нескольких расчетов
while True:
    # Запрашиваем зарплату
    salary_input = input(
        "\nВведите вашу зарплату (число) или 'выход' для завершения: ")

    # Проверяем, хочет ли пользователь выйти
    if salary_input.lower() == 'выход':
        print("Программа завершена!")
        break  # Выходим из цикла

    # Преобразуем в число
    salary = int(salary_input)

    # Случайно определяем, будет ли бонус
    bonus = random.choice([True, False])

    # Обрабатываем бонус
    if bonus:
        bonus_amount = random.randint(100, 5000)
        total_salary = salary + bonus_amount
    else:
        total_salary = salary
        bonus_amount = 0

    # Выводим результат
    print(f"Результат: ${total_salary}")
    print(f"Бонус: {'Да' if bonus else 'Нет'}")
    if bonus:
        print(f"Размер бонуса: ${bonus_amount}")
