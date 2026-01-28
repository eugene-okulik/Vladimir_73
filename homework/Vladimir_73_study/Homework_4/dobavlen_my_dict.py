RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
BOLD = '\033[1m'
NDERLINE = '\033[4m'
RESET = '\033[0m'

my_dict = {
    'tuple': (1, 2, 3, 4, 5),
    'list': [10, 20, 30, 40, 50],
    'dict': {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5},
    'set': {1, 2, 3, 4, 5}
}
my_dict['dict']['i am a tuple',] = 'new element'
print(my_dict)
print(f"Вы добавили в словарь dict, элемент:{my_dict['dict']}")
