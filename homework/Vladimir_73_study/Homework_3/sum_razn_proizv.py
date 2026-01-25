GREEN = '\033[92m'     # Зелёный
YELLOW = '\033[93m'    # Жёлтый/оранжевый
UNDERLINE = '\033[4m'  # Подчёркивание
RESET = '\033[0m'      # Сброс цвета
RED = '\033[91m'      # Красный
BLUE = '\033[94m'     # Синий
MAGENTA = '\033[95m'  # Пурпурный
CYAN = '\033[96m'     # Голубой
WHITE = '\033[97m'    # Белый
ITALIC = '\033[3m'

print(f'                {UNDERLINE}Вывод  СУММЫ, РАЗНОСТИ И ПРОИЗВЕДЕНИЯ{RESET}')

a = float(input(f'    {MAGENTA}Введите число a:{RESET}'))
b = float(input(f'    {MAGENTA}Введите число b:{RESET}'))
print(f' {GREEN}                       Сумма: {a+b}{RESET}')
print(f' {YELLOW}                       РАЗНОСТЬ: {a-b}{RESET}')
print(f'  {CYAN}                      ПРОИЗВЕДЕНИЕ: {a*b}{RESET}')
