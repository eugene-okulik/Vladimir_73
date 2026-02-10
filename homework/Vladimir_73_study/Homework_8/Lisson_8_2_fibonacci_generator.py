def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Как делали для миллионного числа в progression
count = 0
for number in fibonacci_generator():
    if count == 5:
        print(f"5-е число Фибоначчи: {number}")
    elif count == 200:
        print(f"200-е число Фибоначчи: {number}")
    elif count == 1000:
        print(f"1000-е число Фибоначчи: {number}")
        break  # Нашли все - выходим
    
    count += 1
    