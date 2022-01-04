#!/bin/sh
conda env create --file ../pytest_env.yml
DATE=$(date '+%Y-%m-%d-%H%M%S')
pytest ../scr/tests/ --html=./reports/Test_Report_"$DATE".html --junitxml=./reports/Test_Report_"$DATE".xml
conda deactivate
