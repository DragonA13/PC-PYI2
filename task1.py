class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        if isinstance(pages, int):
            if pages > 0:
                self.pages = pages
            else:
                raise ValueError(f"Неверный номер страницы: {pages!r}")
        else:
            raise ValueError("Номер страницы должен быть в виде числа")

    def __str__(self):
        super_str = super().__str__()
        return f"{super_str}. Кoличество страниц {self.pages}"

    def __repr__(self):
        super_repr = super().__repr__()
        return f'{super_repr}. Количество страниц {self.pages}'


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        if isinstance(duration, float):
            if duration > 0:
                self.duration = duration
            else:
                raise ValueError(f'Неверная длительность аудио книги: {duration!r}')
        else:
            raise ValueError('Нет длительности')

    def __str__(self):
        ret_str = super().__str__()
        return f"{ret_str}. Длительность {self.duration}"

    def __repr__(self):
        ret_rep = super().__repr__()
        return f'{ret_rep}. Длительность {self.duration}'



if __name__ == "__main__":
    book = PaperBook("Сила Воли", "Келли Макгонигал", 304)
    print(book)
    book_1 = AudioBook("Маленькие женщины", "Луиза Мэй Олкотт", 3.47)
    print(book_1)
