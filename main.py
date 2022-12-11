import doctest


class WashingMachine:
    def __init__(self, max_load: float, current_load: float, washing_mode: int):
        """
                Создание и подготовка к работе объекта "Стиральная машина"
                :param max_load: Максимально допустимая загрузка машины
                :param current_load: Загрузка машины
                :param washing_mode: Номер режима стирки
                Примеры:
                >>> wash = WashingMachine(4.5, 3, 2)  # инициализация экземпляра класса
                """

        if not isinstance(max_load, (int, float)):
            raise TypeError("Максимальная загрузка должна быть типа int или float")
        if max_load <= 0:
            raise ValueError("Максимальная загрузка должна быть положительным числом")
        self.max_load = max_load

        if not isinstance(current_load, (int, float)):
            raise TypeError("Загрузка машины должна быть типа int или float")
        if current_load <= 0:
            raise ValueError("Загрузка машины должна быть положительным числом")
        self.current_load = current_load

        if not isinstance(washing_mode, (int)):
            raise TypeError("Номер режима стирки должен быть типа int")
        if washing_mode < 0:
            raise ValueError("Номер режима стирки должен не может быть отрицательным числом")
        self.washing_mode = washing_mode

    def can_it_be_washed(self) -> bool:
        """
        Функция, которая проверяет, возможна ли стирка
        :return: Возможна ли стирка
        Примеры:
        >>> wash = WashingMachine(4.5, 3.2, 2)
        >>> wash.can_it_be_washed()
        """
        ...

    def washing_time(self) -> float:
        """
        Функция для расчета времени стирки
        :return: Время стирки
        Примеры:
        >>> wash = WashingMachine(4.5, 3.2, 2)
        >>> wash.washing_time()
        """
        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()  # тестирование примеров, которые находятся в документации


class СashMachine:
    def __init__(self, product_name: str, amount_of_product: int):
        """
                Создание и подготовка к работе объекта "Касса"
                :param product_name: Наименование товара
                :param amount_of_product: Количество товара одного типа
                Примеры:
                >>> apple = СashMachine('Яблоко', 3)  # инициализация экземпляра класса
                """

        if not isinstance(product_name, (str)):
            raise TypeError("Наименование товара должно быть типа string")
        self.product_name = product_name

        if not isinstance(amount_of_product, (int)):
            raise TypeError("Количество товара одного типа должно быть типа int")
        if amount_of_product <= 0:
            raise ValueError("Количество товара одного типа должно быть положительным числом")
        self.amount_of_product = amount_of_product

    def can_it_be_sale(self) -> bool:
        """
        Функция, которая проверяет, есть ли такой товар в базе магазина
        :return: Возможна ли продажа
        Примеры:
        >>> apple = СashMachine('Яблоко', 3)
        >>> apple.can_it_be_sale()
        """
        ...

    def cost(self, product_price: float) -> float:
        """
        Функция для расчета общей стоимости товаров одного типа
        :param product_price: стоимость одной единицы товара
        :rise TypeError: Cтоимоcть должна быть типа float или int
        :rise ValueError: Стоимость не может быть меньше 0,01
        :return: Общая стоимость товаров одного типа
        Примеры:
        >>> apple = СashMachine('Яблоко', 3)
        >>> apple.cost(20.3)
        """
        if not isinstance(product_price, (int, float)):
            raise TypeError("Стоимость товара одного типа должна быть типа float или int")
        if product_price <= 0.01:
            raise ValueError("Стоимость товара одного типа должна быть больше 0,01")
        ...

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()  # тестирование примеров, которые находятся в документации


class Heater:
    def __init__(self, water_volume: float, temperature: float):
        """
                Создание и подготовка к работе объекта "Нагреватель"
                :param water_volume: Объём нагреваемой воды
                :param temperature: Необходимая температура воды
                Примеры:
                >>> water_heat = Heater(10, 65)  # инициализация экземпляра класса
                """

        if not isinstance(water_volume, (float, int)):
            raise TypeError("Объём нагреваемой воды должен быть типа float или int")
        if water_volume < 1:
            raise ValueError("Объем воды должен быть не менее 1 литра")
        self.water_volume = water_volume

        if not isinstance(temperature, (float, int)):
            raise TypeError("Желаемая температура воды должна быть типа float или int")
        if temperature < 35:
            raise ValueError("Желаемая температура воды должна быть не менее 35 градусов")
        self.temperature = temperature

    def constant(self) -> None:
        """
        Поддержание температуры воды
        Примеры:
        >>> water_heat = Heater(10, 65)
        >>> water_heat.constant()
        """
        ...

    def time(self, power_level: int) -> float:
        """
        Функция для расчета необходимого времени для нагрева
        :param power_level: уровень мощности нагрева
        :rise TypeError: уровень мощности нагрева должен быть типа int
        :rise ValueError: уровень мощности нагрева должен быть от 1 до 5
        :return: время, необходимое для нагрева объема воды
        Примеры:
        >>> water_heat = Heater(10, 65)
        >>> water_heat.time(5)
        """
        if not isinstance(power_level, int):
            raise TypeError("уровень мощности нагрева должен быть типа int")
        if 5 < power_level < 1:
            raise ValueError("уровень мощности нагрева должен быть от 1 до 5")
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
    