class Book:
    def __init__(self, name: str, author: str):
        """Создание и подготовка к работе объекта "Book(Книга)"
        :param name: Название
        :param author: Автор
        """
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self) -> str:
        return f"Книга: {self.name}. Автор: {self.author}."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}: (name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        """Создание и подготовка к работе объекта "PaperBook(Бумажная книга)"
        :param name: Название
        :param author: Автор
        :param pages: Количество страниц
        """
        super().__init__(name, author)
        self._pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, new_pages: int) -> None:
        """Устанавливает количество страниц в книге"""
        if not isinstance(new_pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if new_pages <= 0:
            raise ValueError("Количество страниц не может иметь отрицательное значение")
        self._pages = new_pages

    def __str__(self) -> str:
        return f"Книга: {self.name}. Автор: {self.author}. Количество страниц: {self.pages}."


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        """Создание и подготовка к работе объекта "AudioBook(Аудиокнига)"
        :param name: Название
        :param author: Автор
        :param duration: Продолжительность аудиозаписи
        """
        super().__init__(name, author)
        self._duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, new_duration: float) -> None:
        """Устанавливает продолжительность аудиозаписи"""
        if not isinstance(new_duration, float):
            raise TypeError("Продолжительность должна быть типа float")
        if new_duration <= 0:
            raise ValueError("Продолжительность не может иметь отрицательное значение")
        self._duration = new_duration

    def __str__(self) -> str:
        return f"Книга: {self.name}. Автор: {self.author}. Продолжительность: {self.duration}."


print(PaperBook("Сила Воли", "Келли Макгонигал", 304))
print(AudioBook("Маленькие женщины", "Луиза Мэй Олкотт", 3.47))