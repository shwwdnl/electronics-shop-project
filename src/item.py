import math
import csv
class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.__name}"


    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * Item.pay_rate
        return self.price

    @property
    def name(self) -> str:
        """
        Геттер для приватного атрибута name..
        """
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        if len(value) > 10:
            value = value[:10]
        self.__name = value

    @classmethod
    def instantiate_from_csv(cls, data) -> None:
        """
        Класс-метод для инициализации экземпляров класса Item данными из файла src/items.csv.
        """
        with open(data, "r", encoding='windows-1251') as file:
            reader = csv.DictReader(file)
            for row in reader:
                item = cls(
                    name=row["name"],
                    price=float(row["price"]),
                    quantity=int(row["quantity"])
                )
                cls.all.append(item)

    @staticmethod
    def string_to_number(string):


        number = float(string)
        number = math.floor(number)

        return number
