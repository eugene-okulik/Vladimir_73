RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
RESET = '\033[0m'


class Book:  # создаём АТРИБУТЫ класса( общие для всех книг)
    material = 'paper'  # материал - бумага
    has_text = True  # текст - присутсвует

    def __init__(self, title, author, pages, ):
        # атрибуты экземпляра(индивидуальные для кажной книги)
        self.title = title  # название
        self.author = author  # автор
        self.pages = pages  # количество страниц
        self.reserved = False  # по умолчанию не зарезервировано


# создаём 5 экземпляров книг
book1 = Book("Идиот", "Достоевский", 500)
book2 = Book("Преступление и наказание", "Достоевский", 600)
book3 = Book("Война и мир", "Толстой", 1300)
book4 = Book("Анна Каренина", "Толстой", 800)
book5 = Book("Мастер и Маргарита", "Булгаков", 400)

# помечаем одну книгу как зарезервированную
book3.reserved = True  # теперь "Война и мир" зарезервирована

# создаём список для перебора книг
books = [book1, book2, book3, book4, book5]

# распечатываем информайию о каждой книге
for book in books:
    # def __str__(self):
    # прописываем как выглядит строка с информацией о книге(типа шаблон)
    info = f'Название: {book.title}, \nАвтор: {book.author}, \nКоличество страниц: {
        book.pages}, \nМатериал: {book.material} '

# если книга зарезервирована, то добавляем пометку
    # if book.reserved:
    if book.reserved:
        info += f',{RED} зарезервирована{RESET}'
    # return info

    # for book in books:
    print(info)

    print(f"{YELLOW}={RESET}"*50)
