BLUE = '\033[34m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
RED = '\033[31m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
RESET = '\033[0m'

temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]

# 1. Получаем отсортированный список
sorted_temps = sorted(temperatures)
print(f'{GREEN} Отсортированный список всех температур:{RESET}')
print(f'{GREEN}{sorted_temps}{RESET}')
print()

# 2. Создаём список с жаркими днями (выше 28)
hot_days = list(filter(lambda x: x > 28, sorted_temps))
print(f'{YELLOW}Жаркие дни (из отсортированного списка):{RESET}')
print(f'{YELLOW}{hot_days}{RESET}')
print()

# 3. Самая низкая температура среди жарких дней
min_hot = min(hot_days)  # или hot_days[0] так как список отсортирован
print(f'{BLUE}Самая низкая температура среди жарких дней: {min_hot}{RESET}')

# 4. Самая высокая температура среди жарких дней
max_hot = max(hot_days)  # или hot_days[-1] так как список отсортирован
print(f'{RED} Самая высокая температура среди жарких дней: {max_hot}')

# 5. Средняя температура среди жарких дней
avg_hot = sum(hot_days) / len(hot_days)
print(f'{MAGENTA} Средняя температура среди жарких дней: {avg_hot:.1f}{RESET}')