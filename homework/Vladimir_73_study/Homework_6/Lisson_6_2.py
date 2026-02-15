for num in range(1, 101):
    if num % 15 == 0:          # Кратно и 3 и 5 (т.е. 15)
        print("FuzzBuzz")
    elif num % 3 == 0:         # Кратно только 3
        print("Fuzz")
    elif num % 5 == 0:         # Кратно только 5
        print("Buzz")
    else:                      # Не кратно ни 3, ни 5
        print(num)
