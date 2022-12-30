from pathlib import Path
from sites.rightmove.rightmove import Rightmove

from utils.driver import Driver

ROUTE_DIR = Path(__file__).parents[0]

driver = Driver()
rm = Rightmove(driver, False)

