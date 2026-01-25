GREEN = '\033[92m'     # Зелёный
YELLOW = '\033[93m'    # Жёлтый/оранжевый
UNDERLINE = '\033[4m' # Подчёркивание
RESET = '\033[0m'      # Сброс цвета
RED = '\033[91m'      # Красный
BLUE = '\033[94m'     # Синий
MAGENTA = '\033[95m'  # Пурпурный
CYAN = '\033[96m'     # Голубой
WHITE = '\033[97m'    # Белый
ITALIC = '\033[3m'

print(f'                   {MAGENTA}{UNDERLINE} Выводим результат выражения x-y/5+xy{RESET}')

x=int(input(f'\n                           {GREEN}ВВЕДИТЕ целое число x={RESET}'))
y=int(input(f'                           {CYAN}ВВЕДИТЕ целое число y={RESET}'))

print(f'\n  {YELLOW}{ITALIC}ВЫРАЖЕНИЕ x-y/5+xy ={ x-y/5+x*y}{RESET}')