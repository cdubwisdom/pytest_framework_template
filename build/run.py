import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-dt", "--Datetime", help="Datetime stamp")
today = parser.parse_args()


if __name__ == "__main__":
    os.system(
        "pytest --no-header -v ../scr/tests/ "
        f"--html=./reports/Test_Report_{today.Datetime}.html "
        f"--junitxml=./reports/Test_Report_{today.Datetime}.xml "
        "--self-contained-html "
        f"--Datetime {today.Datetime}"
    )
