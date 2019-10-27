from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import os, sys

cwd = os.getcwd()

driver = webdriver.Firefox()

driver.get("https://www.berkeleytime.com/catalog")


# Function to write values of each input to the JSON.
def writeToJSONFile(path, file_name, data):
    with open('classData.json', 'w') as fp:
        json.dump(data, fp)

data = {}

courses = ["COMPSCI 61A", "COMPSCI 70", "Math 54", "History 7B", "French 139"]
for course in courses:

    # MARK BERKELEYTIME
    inputElement = driver.find_element_by_id("classSearch")
    inputElement.send_keys(course)

    # First navigate to Berkeleytime and look at each class.
    driver.find_element_by_class_name("filter-selection-description").click()

    driver.find_element_by_class_name("app-container").click()

    # Get the amount of units.
    number_units = driver.find_element_by_class_name("filter-selection-units").text.split()[0]

    # Now navigate to grade distributions.
    driver.find_element_by_xpath("//*[text()[contains(., 'See grade distributions')]]").click()
   # classAverage = driver.find_element_by_class_name("class-avg-stats").click()

    # courseAverage = driver.find_element_by_xpath("//*[text()[contains(., 'GPA')]]").text

    data['number_units'] = number_units


    # Go back and clear search box for next query.
    driver.back()
    driver.refresh()
    driver.find_element_by_id('classSearch').clear()

    # MARK RATEMYPROFESSOR


