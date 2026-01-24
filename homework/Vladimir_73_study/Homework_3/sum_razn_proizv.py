CYAN = '\033[96m'     # Голубой
GREEN = '\033[92m'     # Зелёный
YELLOW = '\033[93m'    # Жёлтый/оранжевый
UNDERLINE = '\033[4m'  # Подчёркивание
RESET = '\033[0m'

print(f'                {UNDERLINE}Вывод  СУММЫ, РАЗНОСТИ И ПРОИЗВЕДЕНИЯ{RESET}')

a=6
b=2
print(f' {GREEN}                       Сумма: {a+b}{RESET}')
print(f' {YELLOW}                       РАЗНОСТЬ: {a-b}{RESET}')
print(f'  {CYAN}                      ПРОИЗВЕДЕНИЕ: {a*b}{RESET}')