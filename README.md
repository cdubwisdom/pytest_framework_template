# pytest_framework_template

## A simple framework to jump start web ui testing using Selenium Webdriver and the Pytest Page Object testing framework
### Includes functions to help find and use web elements, simplifying test methods.

# Modules Breakdown
## Fixtures
### Constants is as the name applies. A place to store variables that are used throught the test suite
### Fixtures contains the functions that assist in finding and manipulating web elements

## Helpers
### Empty folder that would store classes and functions to help generate or store data

## Page Objects
### This framework uses page objects to navigate websites and simplify test writing. Currently contains an example of the Google Search Engine

## Tests
### The test to be run are stored here. Currently, contains a simple example test for searching on Google.
### The conftest.py is what initializes the driver. Is set up to check for the latest version of Chromedriver at start up

## Settings
### The settings.py is used to keep track of all variables needed for testing such as directory and urls.

## Environment Setup
### The pytest_env.yml can be used to create a conda python environment that will run the suite

## Build
###Build script to run test suite from a command line and generate reports
###Requires Andaconda or Miniconda to be installed and added to the PATH_VARIABLES 