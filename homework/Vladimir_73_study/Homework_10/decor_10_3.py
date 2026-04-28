# Задание на декораторы 3
# Напишите программу:
# Есть функция которая делает одну из арифметических операций с переданными ей числами
# (числа и операция передаются в аргументы функции).
# Функция выглядит примерно так:

# def calc(first, second, operation):
# if operation == '+':
# return first + second
# elif .....
# Программа спрашивает у пользователя 2 числа (вне функции)

# Создайте декоратор, который декорирует функцию calc и управляет тем какая операция будет произведена:

# если числа равны, то функция calc вызывается с операцией сложения этих чисел
# если первое больше второго, то происходит вычитание второго из певрого
# если второе больше первого - деление первого на второе
# сли одно из чисел отрицательное - умножение


def operation_manager(func):
    """
    Декоратор, который управляет выбором операции
    """

    def wrapper(first, second, operation):  # <--- ОСТАВЛЯЕМ operation!
        # Анализируем числа и ВЫБИРАЕМ СВОЮ операцию (игнорируем переданную)
        print(f"\nАнализируем числа: {first} и {second}")
        print(f"Переданная операция '{operation}' будет проигнорирована")

        if first < 0 or second < 0:
            print("Выбираем УМНОЖЕНИЕ")
            return func(first, second, "*")  # Подставляем *
        elif first == second:
            print("Выбираем СЛОЖЕНИЕ")
            return func(first, second, "+")  # Подставляем +
        elif first > second:
            print("Выбираем ВЫЧИТАНИЕ")
            return func(first, second, "-")  # Подставляем -
        elif second > first:
            print("Выбираем ДЕЛЕНИЕ")
            return func(first, second, "/")  # Подставляем /

    return wrapper


def calc(first, second, operation):
    """Функция выполняет арифметическую операцию"""
    if operation == "+":
        result = first + second
        print(f"  {first} + {second} = {result}")
        return result
    elif operation == "-":
        result = first - second
        print(f"  {first} - {second} = {result}")
        return result
    elif operation == "*":
        result = first * second
        print(f"  {first} * {second} = {result}")
        return result
    elif operation == "/":
        if second == 0:
            print("  Ошибка: деление на ноль!")
            return None
        result = first / second
        print(f"  {first} / {second} = {result}")
        return result


# Применяем декоратор
calc = operation_manager(calc)

# Основная программа
print("Программа для вычислений с умным выбором операции")
print("-" * 50)

num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

# Передаем какую-то операцию (она будет проигнорирована декоратором)
result = calc(num1, num2, "+")  # Можно любую операцию передать

print("=" * 50)
if result is not None:
    print(f"РЕЗУЛЬТАТ: {result}")
