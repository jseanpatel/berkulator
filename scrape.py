from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json

driver = webdriver.Firefox()

driver.maximize_window()

# Then navigate to a search for each class.
classes = driver.find_elements_by_class_name("filter-selection-content")

print(len(classes))


def writeToJSONFile(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)


data = {}
data['key'] = 'value'

# writeToJSONFile('./','file-name',data)
