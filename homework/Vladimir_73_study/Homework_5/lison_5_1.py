text = "результат операции: 514"
pos = text.index(":")
right_part = text[pos+1:]
# 3. Убираем пробелы
clean = right_part.strip()
# 4. Превращаем в число
number = int(clean)
print(f"4. Число: {number}")
# 5. Прибавляем 10
result = number + 10
print(f"5. Результат: {number} + 10 = {result}")
