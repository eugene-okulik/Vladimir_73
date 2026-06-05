import datetime
from pathlib import Path

# Путь к файлу data.txt (относительно корня репозитория)
data_file = Path('homework/eugene_okulik/hw_13/data.txt')

# Проверяем, существует ли файл
if not data_file.exists():
    print(f"Файл не найден: {data_file}")
    exit(1)

# Читаем файл
with open(data_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Обрабатываем каждую строку
for line in lines:
    line = line.strip()
    if not line:
        continue
    
    # Разделяем на номер с датой и описание
    parts = line.split(' - ')
    if len(parts) != 2:
        continue
    
    number_and_date = parts[0]
    description = parts[1]
    
    # Разделяем номер и дату
    num_str, date_str = number_and_date.split('. ')
    number = int(num_str)
    
    # Преобразуем строку в datetime
    current_date = datetime.datetime.fromisoformat(date_str)
    
    # Выполняем действие в зависимости от номера
    if number == 1:
        new_date = current_date + datetime.timedelta(days=7)
        print(f"1. {date_str} - {description}")
        print(f"   Результат: {new_date}\n")
        
    elif number == 2:
        weekdays = ['понедельник', 'вторник', 'среда', 'четверг', 
                    'пятница', 'суббота', 'воскресенье']
        weekday_name = weekdays[current_date.weekday()]
        print(f"2. {date_str} - {description}")
        print(f"   Результат: {weekday_name}\n")
        
    elif number == 3:
        now = datetime.datetime.now()
        days_diff = (now - current_date).days
        print(f"3. {date_str} - {description}")
        print(f"   Результат: {days_diff} дней назад\n")
