from enum import Enum


class Attribute(Enum):
    ID = ('id', True)
    URL = ('url', True)
    ADDRESS = ('address', True)
    TYPE = ('property type', True)
    PRICE = ('price', True)
    BEDROOMS = ('bedrooms', True)
    BATHROOMS = ('bathrooms', True)
    DESCRIPTION = ('description', True)
    KEY_FEATURES = ('key features', True)
    NEXT_BTN = ('next button', False)
    EXPAND_BTN = ('expand button', False)
    PARENT_CELL = ('parent cell', False)
    def __init__(self, name: str, data: bool):
        self.name = name
        self.data = data