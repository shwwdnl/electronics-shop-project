from src import phone
import pytest

@pytest.fixture()
def test_phone():
    return phone.Phone("iPhone 14", 120000, 5, 2)

@pytest.fixture()
def test_phone1():
    return phone.Phone("iPhone 11", 47000, 2, 1)


def test_init_phone(test_phone):

    assert test_phone.name == 'iPhone 14'
    assert test_phone.price == 120000
    assert test_phone.quantity == 5
    assert test_phone.number_of_sim == 2


def test_number_of_sim_setter(test_phone):

    test_phone.number_of_sim = 3
    assert test_phone.number_of_sim == 3
    try:
        test_phone.number_of_sim = 0
    except ValueError:
        pass
