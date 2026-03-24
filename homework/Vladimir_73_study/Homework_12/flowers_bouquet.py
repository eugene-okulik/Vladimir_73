class Flower:
    """Базовый класс для всех цветов"""

    def __init__(self, name, price, freshness, stem_length, color, lifetime):
        self.name = name  # Название (например, "Роза")
        self.price = price  # Цена за штуку
        self.freshness = freshness  # Свежесть в процентах (0-100)
        self.stem_length = stem_length  # Длина стебля в см
        self.color = color  # Цвет
        self.lifetime = lifetime  # Время жизни в днях

    def __repr__(self):
        """Метод для красивого вывода информации о цветке в консоль"""
        return f"{self.name} ({self.color}): {self.price}$, свежесть {self.freshness}%, жизнь {self.lifetime} дн."


# Классы конкретных цветов наследуются от Flower
class Rose(Flower):
    def __init__(self, price, freshness, stem_length, color, lifetime):
        # Вызываем конструктор родительского класса, передавая имя "Роза"
        super().__init__("Роза", price, freshness, stem_length, color, lifetime)


class Tulip(Flower):
    def __init__(self, price, freshness, stem_length, color, lifetime):
        super().__init__("Тюльпан", price, freshness, stem_length, color, lifetime)


class Chamomile(Flower):
    def __init__(self, price, freshness, stem_length, color, lifetime):
        super().__init__("Ромашка", price, freshness, stem_length, color, lifetime)


class Bouquet:
    """Класс Букет, который хранит список объектов цветов"""

    def __init__(self):
        self.flowers = []  # Список для хранения объектов цветов

    def add_flower(self, flower):
        """Добавляет цветок в букет"""
        if isinstance(flower, Flower):
            self.flowers.append(flower)
        else:
            print("Ошибка: Можно добавить только объект класса Flower!")

    def get_total_cost(self):
        """Вычисляет общую стоимость букета"""
        total = 0
        for flower in self.flowers:
            total += flower.price
        return total

    def get_average_lifetime(self):
        """Определяет время увядания букета (среднее время жизни цветов)"""
        if not self.flowers:
            return 0

        total_lifetime = 0
        for flower in self.flowers:
            total_lifetime += flower.lifetime

        return total_lifetime / len(self.flowers)

    def sort_flowers(self, by="price"):
        """
        Сортирует цветы в букете.
        Параметр 'by' определяет критерий: 'price', 'freshness', 'stem_length', 'color'.
        """
        # Словарь сопоставляет строку-параметр с реальным атрибутом объекта
        key_map = {
            "price": lambda f: f.price,
            "freshness": lambda f: f.freshness,
            "stem_length": lambda f: f.stem_length,
            "color": lambda f: f.color,
        }

        if by in key_map:
            # sorted возвращает новый отсортированный список
            self.flowers = sorted(self.flowers, key=key_map[by])
            print(f"Букет отсортирован по: {by}")
        else:
            print(f"Неизвестный параметр для сортировки: {by}")

    def find_flowers(self, param, value):
        """
        Ищет цветы в букете по параметру и значению.
        Возвращает список найденных цветов.
        """
        found = []
        for flower in self.flowers:
            # getattr позволяет получить значение атрибута по его имени в виде строки
            if getattr(flower, param, None) == value:
                found.append(flower)
        return found

    def __repr__(self):
        """Вывод информации о всем букете"""
        result = f"Букет (цветов: {len(self.flowers)}, стоимость: {self.get_total_cost()}$)\n"
        for flower in self.flowers:
            result += f" - {flower}\n"
        return result


# --- ДЕМОНСТРАЦИЯ РАБОТЫ ---

if __name__ == "__main__":
    # 1. Создаем экземпляры цветов разных видов
    r1 = Rose(price=10, freshness=90, stem_length=50, color="red", lifetime=5)
    r2 = Rose(price=15, freshness=80, stem_length=60, color="white", lifetime=7)
    t1 = Tulip(price=5, freshness=95, stem_length=30, color="yellow", lifetime=4)
    c1 = Chamomile(price=3, freshness=100, stem_length=20, color="white", lifetime=3)

    # 2. Создаем букет и добавляем туда цветы
    my_bouquet = Bouquet()
    my_bouquet.add_flower(r1)
    my_bouquet.add_flower(r2)
    my_bouquet.add_flower(t1)
    my_bouquet.add_flower(c1)

    # 3. Выводим информацию о букете
    print("--- Изначальный букет ---")
    print(my_bouquet)

    # 4. Смотрим среднее время увядания
    avg_life = my_bouquet.get_average_lifetime()
    print(f"Среднее время жизни букета: {avg_life:.2f} дней\n")

    # 5. Сортируем цветы (например, по цене)
    print("--- Сортировка по цене ---")
    my_bouquet.sort_flowers(by="price")
    print(my_bouquet)

    # 6. Ищем цветы (например, белого цвета)
    print("--- Поиск белых цветов ---")
    white_flowers = my_bouquet.find_flowers(param="color", value="white")
    if white_flowers:
        for f in white_flowers:
            print(f"Найден: {f}")
    else:
        print("Белых цветов не найдено.")
