from utils.attribute import Attribute

from dataclasses import dataclass


@dataclass
class Xpath:
    """Class for containing xpath properties."""
    name: Attribute
    xpath: str
    attribute: str = None