from utils.attribute import Attribute
from utils.xpath import Xpath
from selenium.webdriver.remote.webelement import WebElement


def attribute_from_cell(cell: WebElement, xpath: Xpath):
    if xpath.attribute:
        return cell.get_attribute(xpath.attribute)
    else:
        return cell.text

def process_cells(cells, shelf_xpaths: list(Xpath)):
    cell_data = []
    for cell in cells:
        data = {}
        for xpath in shelf_xpaths:
            if xpath.name.data:
                data[xpath.name] = attribute_from_cell(cell, xpath)
        cell_data.append(data)
    return cell_data