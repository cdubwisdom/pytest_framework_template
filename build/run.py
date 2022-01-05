import os
import datetime

today = datetime.datetime.today().strftime("%d-%m-%y-%H%M")


if __name__ == "__main__":
    os.system(f"pytest --no-header -v ../scr/tests/ --html=./reports/Test_Report_{today}.html --junitxml=./reports/Test_Report_{today}.xml")
