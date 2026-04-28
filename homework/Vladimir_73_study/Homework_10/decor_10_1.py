def finish_me(func):  # 1. Создаем декоратор
    def wrapper(*args):  # Добавляем *args, чтобы принимать аргументы
        func(*args)  # Передаем аргументы в исходную функцию и выполняем
        print("finished")  # Добавляем наше "украшение"

    return wrapper  # Возвращаем новую функцию


@finish_me  # Вместо example = finish_me(example)
def example(text):
    print(text)


example("print me")
