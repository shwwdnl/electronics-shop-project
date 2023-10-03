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

    @staticmethod
    def string_to_number(string):
        number = float(string)
        number = math.floor(number)

        return number


    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity

    @classmethod
    def instantiate_from_csv(cls, CSV_PATH='./src/items.csv'):
        """
        Класс-метод для инициализации экземпляров класса Item данными из файла src/items.csv.
        """
        try:
            with open(CSV_PATH, "r", encoding='windows-1251') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if list(row.keys()) == ["name", "price", "quantity"]:
                        cls(row['name'], float(row['price']), int(row['quantity']))

                    else:
                        raise InstantiateCSVError

        except FileNotFoundError:
            print("Отсутствует файл items.csv")
            return "Отсутствует файл items.csv"

class InstantiateCSVError(Exception):
    """Создан класс для исключений"""
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else "Файл item.csv поврежден"

    def __str__(self):
        return self.message
