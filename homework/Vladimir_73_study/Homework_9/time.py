import datetime

# Исходная дата
my_time = "Jan 15, 2023 - 12:05:33"

# 1. Преобразуем строку в datetime-объект
# %b - сокращённое название месяца (Jan, Feb...)
# %d - день (15)
# %Y - год (2023)
# %H - часы (12)
# %M - минуты (05)
# %S - секунды (33)
python_date = datetime.datetime.strptime(my_time, "%b %d, %Y - %H:%M:%S")

# 2. Распечатайте полное название месяца
print(f"Полное название месяца: {python_date.strftime('%B')}")

# 3. Распечатайте дату в формате "15.01.2023, 12:05"
human_date = python_date.strftime("%d.%m.%Y, %H:%M")
print(f"Дата в нужном формате: {human_date}")
