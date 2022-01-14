from pathlib import Path
from os import path

#paths for testing
URL = 'https://www.google.com/'
TEST_PATH = Path(__file__).parent
PROJ_PATH = Path(__file__).parent.parent
REPORT_PATH = path.join(PROJ_PATH, r"build\reports")
