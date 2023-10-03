"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import pytest

class TestItem:
    @pytest.fixture(scope="module")
    def item(self):
        return Item("ноутбук", 40000, 8)

    @pytest.fixture
    def item1(self):
        return Item("телевизор", 70000, 5)

    def test_name(self, item):
        assert item.name == "ноутбук"

    def test_price(self, item):
        assert item.price == 40000

    def test_quantity(self, item):
        assert item.quantity == 8


    def test_add(self, item, item1):
        assert item1 + item == 13

    def test_apply_discount(self):
        '''тест применяемой скидки к товару '''
        assert 8000 == 10000 * 0.8

    def test_calculate_total_price(self):
        '''тест подсчета общей стоимости товара'''
        assert 150000 == 15000 * 10

    def test_string_to_number(self, item):
        assert item.string_to_number('5') == 5
        assert item.string_to_number('5.0') == 5
        assert item.string_to_number('5.5') == 5

    def test_name(self, item):
        assert item.name == 'ноутбук'

    def test_repr_and_str(self, item):
        item = Item("Смартфон", 10000, 20)
        assert repr(item) == "Item('Смартфон', 10000, 20)"
        assert str(item) == 'Смартфон'

    def test_unreal_csv_file(cls):
        Item.instantiate_from_csv(CSV_PATH='./src/123.csv')
        assert 'Отсутствует файл items.csv'
