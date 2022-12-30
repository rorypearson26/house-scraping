from sites.rightmove.rightmove_xpaths import SHELF_XPATHS, ITEM_XPATHS
from utils.attribute import Attribute as Attr
from utils.driver import Driver
from utils.util_functions import process_cells

class Rightmove:
    def __init__(self, driver: Driver, item_level: bool):
        self.driver = driver
        self.item_level = item_level
        self.start_url = 'https://www.rightmove.co.uk/property-for-sale/find.html?locationIdentifier=REGION%5E219&maxBedrooms=3&minBedrooms=1&maxPrice=300000&minPrice=140000&radius=5.0&sortType=6&propertyTypes=detached%2Csemi-detached%2Cterraced&includeSSTC=false&mustHave=&dontShow=&furnishTypes=&keywords='
        self.shelf_xpaths = SHELF_XPATHS
        self.item_xpaths = ITEM_XPATHS
        
    def main(self):
        self.driver.go_to_url(self.start_url)
        self.get_shelf_data()
        if self.item_level:
            self.get_item_data()
    
    def get_shelf_data(self):
        parent_xpath = next(x for x in SHELF_XPATHS if x.name == Attr.PARENT_CELL)
        cells = self.driver.get_elements_by_xpath(parent_xpath)
        data_dict = process_cells(cells, self.shelf_xpaths)
        print(data_dict)
    
    def get_item_data(self):
        pass