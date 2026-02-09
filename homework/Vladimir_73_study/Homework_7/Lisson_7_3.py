
BLUE = '\033[34m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
RED = '\033[31m'
RESET = '\033[0m'

colors = [BLUE, GREEN, YELLOW, RED]

data = [
    "результат операции: 42",
    "результат операции: 54",
    "результат работы программы: 209",
    "результат: 2"
]


def print_colored(line, color_code):
    name, value = line.split(':')
    new_value = int(value) + 10
    # Печатаем строку в цвете и сбрасываем его в конце
    print(f"{color_code}{name}: {new_value}{RESET}")


# Используем zip, чтобы объединить строку с её цветом
for row, color in zip(data, colors):
    print_colored(row, color)
