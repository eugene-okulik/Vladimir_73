# Вывод наименований сповторением по значениям
words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}
for name, namber in words.items():
    repeat = name * namber
    print(repeat)
