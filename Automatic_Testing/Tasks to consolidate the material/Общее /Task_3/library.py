from book import Book


class Library:
    """
    Класс для представления библиотеки.
    Атрибуты:
        __books (set): Множество книг в библиотеке.
    """

    def __init__(self,):
        """
        Конструктор класса Library.
        """
        self.__books = set()

    def add_book(self, title, author, year):
        """
        Добавляет книгу в библиотеку.
        Параметры:
            title (str): Название книги.
            author (str): Автор книги.
            year (int): Год издания книги.
        """
        new_book = Book(title, author, year)
        self.__books.add(new_book)

    def remove_book(self, title, author, year):
        """
        Удаляет книгу из библиотеки.
        Параметры:
            title (str): Название книги.
            author (str): Автор книги.
            year (int): Год издания книги.
        """
        delete_book = Book(title, author, year)
        self.__books.discard(delete_book)

    def find_book(self, title, author, year):
        """
        Ищет книгу в библиотеке.
        Параметры:
            title (str): Название книги.
            author (str): Автор книги.
            year (int): Год издания книги.
        Возвращает:
            Book: Найденная книга или None, если книга не найдена.
        """
        search_book = Book(title, author, year)
        for book in self.__books:
            if book == search_book:
                return book
        return None

    def list_books(self):
        """
        Выводит список всех книг в библиотеке.
        """
        for book in self.__books:
            print(book)














