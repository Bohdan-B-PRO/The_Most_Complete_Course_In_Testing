class Book:
    """
    Класс для представления книги.
    Атрибуты:
        title (str): Название книги.
        author (str): Автор книги.
        year (int): Год издания книги.
    """

    def __init__(self, title, author, year):
        """
        Конструктор класса Book
        Параметры:
            title (str): Название книги.
            author (str): Автор книги.
            year (int): Год издания книги.
        """
        self.title = title
        self.author = author
        self.year = year

    def __eq__(self, other):
        """
        Определяет равенство двух объектов Book по их атрибутам
        Параметры:
            other (Book): Другой объект Book, с которым сравнивается текущий
        Возвращает:
            bool: Результат сравнения.
        """
        return (self.title, self.author, self.year) == (other.title, other.author, other.year)

    def __hash__(self):
        """
        Возвращает хеш-значение объекта Book.
        Возвращает:
            int: Хеш-значение.
        """
        return hash((self.title, self.author, self.year))

    def __str__(self):
        """
        Возвращает строковое представление объекта Book.
        Возвращает:
            str: Строковое представление.
        """
        return f"Название книги: {self.title}\nАвтор книги: {self.author}\nГод выпуска: {self.year}"

