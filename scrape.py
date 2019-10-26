from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

# Navigate to berkeleytime.
driver.get("https://berkeleytime.com/catalog")

# Then navigate to a search for each class.
classes = driver.find_elements_by_class_name("filter-selection-content")

print(classes[0])
