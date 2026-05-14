#!/usr/bin/env python3
"""
Проверка домашнего задания №13
Автор: Vladimir_73
"""

import datetime
import urllib.request
import sys

def main():
    print("=" * 60)
    print("🔍 Проверка домашнего задания №13")
    print("=" * 60)
    
    # 1. Загружаем файл с GitHub
    print("\n📡 Загружаем файл data.txt с GitHub...")
    url = "https://raw.githubusercontent.com/eugene-okulik/Vladimir_73/main/homework/eugene_okulik/hw_13/data.txt"
    
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            content = response.read().decode('utf-8')
            lines = [line.strip() for line in content.split('\n') if line.strip()]
        print("✅ Файл успешно загружен\n")
    except Exception as e:
        print(f"❌ Ошибка загрузки: {e}")
        print("Проверьте подключение к интернету")
        sys.exit(1)
    
    # 2. Выводим содержимое файла
    print("=" * 60)
    print("📄 Информация в файле по заданию:")
    print("=" * 60)
    for line in lines:
        print(line)
    print("=" * 60)
    print()
    
    # 3. Обрабатываем каждую строку
    print("📊 Результаты обработки:\n")
    print("-" * 60)
    
    for line in lines:
        # Разбираем строку
        if ' - ' not in line:
            continue
            
        number_and_date, description = line.split(' - ', 1)
        
        if '. ' not in number_and_date:
            continue
            
        num_str, date_str = number_and_date.split('. ', 1)
        
        try:
            number = int(num_str)
            current_date = datetime.datetime.fromisoformat(date_str)
        except (ValueError, TypeError) as e:
            print(f"⚠️ Ошибка в строке: {line}")
            continue
        
        # Выполняем задание
        if number == 1:
            new_date = current_date + datetime.timedelta(days=7)
            print(f"📅 Задание 1:")
            print(f"   Исходная дата: {date_str}")
            print(f"   Результат: {new_date}")
            print()
            
        elif number == 2:
            weekdays = ['понедельник', 'вторник', 'среда', 'четверг',
                        'пятница', 'суббота', 'воскресенье']
            weekday_name = weekdays[current_date.weekday()]
            print(f"📆 Задание 2:")
            print(f"   Исходная дата: {date_str}")
            print(f"   Результат: {weekday_name}")
            print()
            
        elif number == 3:
            now = datetime.datetime.now()
            days_diff = (now - current_date).days
            print(f"⏰ Задание 3:")
            print(f"   Исходная дата: {date_str}")
            print(f"   Результат: {days_diff} дней назад")
            print()
    
    print("-" * 60)
    print("\n✅ Проверка завершена!")
    print("=" * 60)
    print("👤 Задание выполнял: Vladimir_73")
    print("=" * 60)

if __name__ == "__main__":
    main()
