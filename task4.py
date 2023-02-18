class Film:
    def __init__(self, name: str, dur: int):
        """
        Создание объекта класса фильм
        :param name: название фильма
        :param dur: продолжительность фильма (в минутах)
        Примеры:
        >>> test_film = Film("Jumanji", 118)  #Инициализация объекта класса
        """
        self.name = name  # Название фильма можно менять, как и его тип (не рекомендуется)
        self.duration = dur
        self._comm = None  # Комментарий к фильму, по умолчанию отсутствует, для добавления применить метод add_comm
        self._accordance = None  # Параметр соответствия фильма теме, по умолчанию отсутствует, добавляется методом


    def add_comm(self, message: str):
        """
        Метод, позволяющий оставить комментарий к фильму
        :param message:
        :return:
        Примеры:
        >>> test_film = Film("Jumanji", 118)  #Инициализация объекта класса
        >>> test_film.add_comm("Интересный фильм, с неожиданными поворотами сюжета")
        """
        self._comm = message

    def write_com(self):
        """
        Метод, позволяющий вернуть ранее оставленный комментарий к фильму
        :return: возвращает комментарий
        Примеры:
        >>> test_film = Film("Jumanji", 118)  #Инициализация объекта класса
        >>> test_film.add_comm("Интересный фильм, с неожиданными поворотами сюжета")
        >>> test_film.write_com()
        'Интересный фильм, с неожиданными поворотами сюжета'
        """
        return self._comm

    def add_accordance(self, rating: float):
        """
        Метод, позволяющий добавить степень соответствия фильму теме
        :param rating: степень соответствия фильма теме (от 0 до 10)
        Примеры:
        >>> test_film = Film("Jumanji", 118)
        >>> test_film.add_accordance(8.9)
        """

        if isinstance(rating, float):
            if 10. >= rating >= 0.:
                self._accordance = rating
            else:
                raise ValueError("accordance must be from 0 to 10")
        else:
            raise TypeError("accordance must be float")

    def check_accordance(self):
        """
        Метод, печатающий степень соответствия фильма теме. Предварительно необходимо добавить её к экземпляру класса
        Примеры:
        >>> test_film = Film("Jumanji", 118)
        >>> test_film.add_accordance(8.9)
        >>> test_film.check_accordance()
        Соответствие фильма теме: 8.9
        """
        print(f'Соответствие фильма теме:{self._accordance}')


    @property
    def duration(self):
        """
        Геттер для атрибута (длительности) фильма
        :param self:
        :return:
        """
        return self._duration

    @duration.setter  # Длительность фильма должна быть положительным целым числом, поэтому создан атрибут
    def duration(self, dur: int):
        """
        Cеттер для атрибута (длительности) фильма
        :param self:
        :param dur: длительность фильма
        :return:
        """
        if isinstance(dur, int):
            if dur > 0:
                self._duration = dur
            else:
                raise ValueError(f'duration of film must be greater than zero, while incoming {dur}')
        else:
            raise ValueError(f'film duration must be int, while incoming is {type(dur)}')

    def __str__(self):
        """
        Магический метод __str__
        :return: Возвращает название и длительность фильма
        Примеры:
        >>> test_film = Film("Jumanji", 118)
        >>> print(test_film)
        Фильм "Jumanji", длительность 118
        """
        return f'Фильм "{self.name}", длительность {self.duration}'

    def __repr__(self):
        """
        Магический метод, выдающий строку, необходимую для инициализации фильма
        :return:
        Примеры:
        >>> test_film = Film("Jumanji", 118)
        >>> repr(test_film)
        "Film(name='Jumanji', dur=118)"
        """
        return f"{self.__class__.__name__}(name={self.name!r}, dur={self.duration})"


class ComedyFilm(Film):
    def __init__(self, name: str, dur: int, year: int):
        """
        Создание объекта класса фильм жанра комедия
        :param name: название фильма
        :param dur:  длительность фильма
        :param year: год, когда создан фильм
        Примеры:
        >>> test_film = ComedyFilm("Alvin and the Chipmunks", 87, 2007) # инициализация объекта класса
        """
        super().__init__(name, dur)  # имя и длительность наследуются
        self.year = year
        self._comm = None
        self._accordance = None


    def __str__(self):  # Перегрузка необходима в связи с добавлением "жанра комедия" и параметра (год)
        """
        Магический метод __str__
        :return: Возвращает название и длительность фильма
        Примеры:
        >>> test_film = ComedyFilm("Alvin and the Chipmunks", 87, 2007)
        >>> print(test_film)
        Фильм жанра комедия "Alvin and the Chipmunks", длительность 87, 2007 год
        """
        return f'Фильм жанра комедия "{self.name}", длительность {self.duration}, {self.year} год'

    def __repr__(self):  # Перегрузка необходима ради введения в метод нового параметра (год)
        """
        Магический метод, выдающий строку, необходимую для инициализации фильма жанра комедия
        :return:
        Примеры:
        >>> test_film = ComedyFilm("Alvin and the Chipmunks", 87, 2007)
        >>> print(repr(test_film))
        ComedyFilm(name='Alvin and the Chipmunks', dur=87, year=2007)
        """
        return f"{self.__class__.__name__}(name={self.name!r}, dur={self.duration}, year = {self.year})"

    def check_accordance(self):  # методу необходима перегрузка, чтобы показывать степень соответствия жанру
        """
        Метод, печатающий степень соответствия фильма жанру комедия, ранее добавленную
        методом add_accordance
        Примеры:
        >>> test_film = ComedyFilm("Alvin and the Chipmunks", 87, 2007)
        >>> test_film.add_accordance(8.3)
        >>> test_film.check_accordance()
        Степень соответствия фильму жанру комедия:8.3
        """
        print(f'Степень соответствия жанру комедия:{self._accordance}')



if __name__ == "__main__":
    # Write your solution here
    """
    Унаследованы методы add_accordance, add_comm и write_comm. Метод check_accordance перегружен
    """
    pass
