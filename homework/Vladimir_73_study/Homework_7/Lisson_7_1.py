# Определяем все эффекты
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BG_BLUE = '\033[104m'
BG_RED = '\033[101m'
BG_GREEN = '\033[102m'
BG_YELLOW = '\033[103m'
BLINK = '\033[5m'
BOLD = '\033[1m'
coral = '#FF7F50'
burlywood = '#DEB887'
azure = '#F0FFFF'
aquamarine = '#7FFFD4'
purpur = '#C40EE8'
blanchedalmond = '#FFEBCD'
crimson = '#DC143C'
antiquewhite = '#FAEBD7'
MAGENTA = '\033[95m'
ELLOW_FONE = '\033[103m'  # ЗАДНИЙ ФОН
BLINK = '\033[5m'  # МИГАНИЕ
UNDERLINE = '\033[4m'  # ПОДЧЁРКИВАНИЕ
RESET = '\033[0m'


print(f'{MAGENTA}{UNDERLINE} ИГРА - угадай СЕКРЕТНОЕ число.{RESET}\n')
sekret_number = 6
while True:
    user_input = input(f'{BG_BLUE}Веедите целое число:{RESET}\n')
    if not user_input.isdigit():
        print(f'{BLINK}{BG_RED}Вы ввели не целое число, попробуйте ещё.{RESET}\n')
        continue
    number = int(user_input)
    if number == sekret_number:
        print(f'{GREEN}УРА-А-А!!! Вы угадали номер!!{RESET}\n')
        break
    elif number > sekret_number:
        print(f'{YELLOW}Введите меньше:{RESET}\n')
    else:

        print(f'{YELLOW}Попробуйте большее:{RESET}\n')
