# АБСОЛЮТНЫЙ МИНИМУМ для начала
text = "число: 7"
print(f'Записано:{text}')

# 1. Найти двоеточие
pos = text.index(":")
print(pos)
# 2. Взять правую часть (после двоеточия)
right_part = text[pos + 1:]
print(right_part)

# 3. Убрать пробелы
clean = right_part.strip()

# 4. Напечатать что получилось
print(f"Правая часть: '{clean}'")
