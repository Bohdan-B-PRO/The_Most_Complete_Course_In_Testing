from library import Library

# Создание объекта библиотеки
library = Library()


def main():
    """
    Основная функция для взаимодействия пользователя с программой управления библиотекой.
    """
    while True:
        try:
            # Взаимодействие с пользователем для выбора действия
            user_actions = input("Введите ваше действия например:\nДобавить книгу\nУдалить книгу\nНайти книгу\n"
                                 "Показать все книги\nВыйти из программы")
            if user_actions == "Добавить книгу":
                # Логика добавления книги
                while True:
                    print("Пожалуйста введите название книги, автора и год выпуска через запятую:")
                    addition_book = input().split(",")
                    if len(addition_book) >= 3:
                        title, author, year = addition_book[:3]
                        try:
                            year = int(year)
                            library.add_book(title.strip(), author.strip(), year)
                            break
                        except ValueError:
                            print("Год должен быть числом.")
                    else:
                        print("Некорректный ввод. Введите данные в формате 'Название, Автор, Год'.")

            elif user_actions == "Удалить книгу":
                # Логика удаления книги
                while True:
                    print("Пожалуйста введите название книги, автора и год выпуска через запятую:")
                    addition_book = input().split(",")
                    if len(addition_book) >= 3:
                        title, author, year = addition_book[:3]
                        try:
                            year = int(year)
                            library.remove_book(title.strip(), author.strip(), year)
                            break
                        except ValueError:
                            print("Год должен быть числом.")

            elif user_actions == "Найти книгу":
                # Логика поиска книги
                while True:
                    print("Пожалуйста введите название книги, автора и год выпуска через запятую:")
                    addition_book = input().split(",")
                    if len(addition_book) >= 3:
                        title, author, year = addition_book[:3]
                        try:
                            year = int(year)
                            library.find_book(title.strip(), author.strip(), year)
                            break
                        except ValueError:
                            print("Год должен быть числом.")
                    else:
                        print("Некорректный ввод. Введите данные в формате 'Название, Автор, Год'.")

            elif user_actions == "Показать все книги":
                # Вывод списка всех книг
                library.list_books()

            elif user_actions == "Выйти из программы":
                # Выход из программы
                break

        except ValueError as e:
            print(f"Команда {e} не существует!")
            print("Попробуйте ещё раз")
            continue


# Проверка на запуск как главного скрипта и вызов функции main
if __name__ == "__main__":
    main()











