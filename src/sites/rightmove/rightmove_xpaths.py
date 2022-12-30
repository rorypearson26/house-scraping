from utils.attribute import Attribute as Attr
from utils.xpath import Xpath

SHELF_XPATHS = [
    Xpath(Attr.PARENT_CELL, '//div[contains(@data-test, "propertyCard")]'),    
    Xpath(Attr.ID, '.', 'id'),
    
]

ITEM_XPATHS = [
    
]