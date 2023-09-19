"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import pytest

class TestItem:
    @pytest.fixture(scope="module")
    def item(self):
        return Item("ноутбук", 40000, 8)

    def test_name(self, item):
        assert item.name == "ноутбук"

    def test_price(self, item):
        assert item.price == 40000

    def test_quantity(self, item):
        assert item.quantity == 8

def test_apply_discount():
    '''тест применяемой скидки к товару '''
    assert 8000 == 10000 * 0.8

def test_calculate_total_price():
    '''тест подсчета общей стоимости товара'''
    assert 150000 == 15000 * 10

def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5

def test_name():
    Item.name = 'Смартфон'
    assert Item.name == 'Смартфон'

def test_repr_and_str():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert str(item1) == 'Смартфон'