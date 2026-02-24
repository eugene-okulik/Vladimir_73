def repeat_me(func):
    def wrapper(*args, **kwargs):  # Принимаем все аргументы
        count = kwargs.get(
            "count", 1
        )  # Забираем count из kwargs, если нет - по умолчанию 1
        for _ in range(count):  # Повторяем count раз
            func(*args)  # Вызываем функцию (без count, т.к. мы его забрали)

    return wrapper


@repeat_me
def example(text, count=1):  # Функция принимает count
    print(text)


example("print me", count=2)
