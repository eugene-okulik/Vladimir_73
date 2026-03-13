class Book:
    material = 'paper'
    has_text = True

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.reserved = False

    def __str__(self):
        info = f'Название: {self.title}, Автор: {self.author}, страниц: {
            self.pages}, материал: {self.material}'

        if self.reserved:
            info += ', зарезервирована'

        return info


#  Дочерний класс для школьных учебников
class SchoolBook(Book):  # В скобках указываем РОДИТЕЛЬСКИЙ класс
    def __init__(self, title, author, pages, subject, school_class, has_tasks):
        # Вызываем конструктор родительского класса для общих атрибутов
        super().__init__(title, author, pages)

        # Добавляем новые атрибуты
        self.subject = subject           # предмет (математика, история...)
        # класс (1, 5, 9...) — class нельзя, это зарезервированное слово!
        self.school_class = school_class
        self.has_tasks = has_tasks       # наличие заданий (bool)

    # Переопределяем __str__ для учебников
    def __str__(self):
        # Берём базовую информацию из родительского класса
        info = super().__str__()

        # Убираем слово "материал: paper" из середины и добавляем специфичную для учебников информацию
        # Но проще собрать заново, чтобы было красиво:
        info = f'Название: {self.title}, Автор: {self.author}, страниц: {
            self.pages}, предмет: {self.subject}, класс: {self.school_class}'

        if self.reserved:
            info += ', зарезервирована'

        return info


# Создаём несколько учебников
math_9 = SchoolBook("Алгебра 9 класс", "Мордкович", 320, "Математика", 9, True)
history_6 = SchoolBook("История России", "Торкунов", 240, "История", 6, True)
geography_7 = SchoolBook("География материков",
                         "Коринская", 280, "География", 7, True)
physics_8 = SchoolBook("Физика 8 класс", "Пёрышкин", 220, "Физика", 8, True)
literature_5 = SchoolBook("Литература 5 класс",
                          "Коровина", 300, "Литература", 5, True)

# Помечаем один учебник как зарезервированный
physics_8.reserved = True

# Собираем в список
school_books = [math_9, history_6, geography_7, physics_8, literature_5]

# Печатаем
for book in school_books:
    print(book)
