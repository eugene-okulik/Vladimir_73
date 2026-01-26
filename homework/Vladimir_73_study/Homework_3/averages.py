import math

GREEN = '\033[92m'     # Зелёный
YELLOW = '\033[93m'    # Жёлтый/оранжевый
UNDERLINE = '\033[4m'   # Подчёркивание
RESET = '\033[0m'      # Сброс цвета
RED = '\033[91m'      # Красный
BLUE = '\033[94m'     # Синий
MAGENTA = '\033[95m'  # Пурпурный
CYAN = '\033[96m'     # Голубой
WHITE = '\033[97m'    # Белый
ITALIC = '\033[3m'    # Наклонный

print(f' {UNDERLINE}Найти среднее арифметическое и среднее '
      f'геометрическое из двух чисел{RESET}')
a = float(input(f' {GREEN}Введите число а={RESET}'))
b = float(input(f' {CYAN}Введите число b={RESET}'))

avg_arithmetic = (a + b) / 2
avg_geometric = math.sqrt(a * b)

print(f"Числа: {a} и {b}")
print(f'{YELLOW}Среднее арифметическое: {avg_arithmetic}{RESET}')
print(f'{MAGENTA}Среднее геометрическое: {avg_geometric:.2f}{RESET}')
