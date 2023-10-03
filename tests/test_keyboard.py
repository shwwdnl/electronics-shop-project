from src.keyboard import Keyboard
import pytest

def test_change_lang():
    """проверка раскладки клавиатуры"""

    keyboard = Keyboard('NameKeyboard', 10000, 19)
    assert str(keyboard.language) == 'EN'
    keyboard.change_lang()
    assert str(keyboard.language) == 'RU'
    keyboard.change_lang().change_lang()
    assert str(keyboard.language) == 'RU'

def test_error_setter_language():
    """тест на ошибку"""
    keyboard = Keyboard('NameKeyboard', 10000, 9)
    with pytest.raises(AttributeError):
        keyboard.language = 'CH'