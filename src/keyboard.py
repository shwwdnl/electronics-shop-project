from src.item import Item

class MixinLang:
    __lang = "EN"

    @property
    def language(self):
        return self.__lang

    def change_lang(self):
        """изменение раскладки клавиатуры"""
        if self.__lang == "EN":
            self.__lang = "RU"
        else:
            self.__lang = "EN"

        return self



class Keyboard(MixinLang, Item):
    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__(name, price, quantity)
