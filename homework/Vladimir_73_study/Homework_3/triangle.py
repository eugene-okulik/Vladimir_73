import math

GREEN = '\033[92m'     # Зелёный
YELLOW = '\033[93m'    # Жёлтый/оранжевый
UNDERLINE = '\033[4m' # Подчёркивание
RESET = '\033[0m'      # Сброс цвета
RED = '\033[91m'      # Красный
BLUE = '\033[94m'     # Синий
MAGENTA = '\033[95m'  # Пурпурный
CYAN = '\033[96m'     # Голубой
WHITE = '\033[97m'    # Белый
ITALIC = '\033[3m'   # Наклонный

print(f' {UNDERLINE}Найти среднее арифметическое и среднее геометрическое из двух чисел{RESET}')
katet1 = float(input(f' {GREEN}Введите katet1={RESET}'))
katet2 = float(input(f' {CYAN}Введите katet2={RESET}'))

gipotenuza = math.sqrt(katet1**2 + katet2**2)
ploshad = (katet1 * katet2) / 2

print(f"Катеты: {katet1} и {katet2}")
print(f'                 {YELLOW}Гипотенуза: {gipotenuza:.2f}{RESET}')
print(f'                 {MAGENTA}Площадь: {ploshad}{RESET}')