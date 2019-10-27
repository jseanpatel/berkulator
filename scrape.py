from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

driver.get("https://www.berkeleytime.com/catalog")

# Then navigate to a search for each class.
classes = driver.find_elements_by_class_name("filter-selection")

# Function to write values of each input to the JSON.
def writeToJSONFile(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)

for indivClass in classes:

    data = {}

    driver.find_element_by_class_name("filter-selection").click()

    numberUnits = driver.find_element_by_class_name("filter-selection-units").text.split()[0]
    print(numberUnits)

    driver.find_element_by_xpath("//*[text()[contains(., 'See grade distributions')]]").click()
    driver.find_element_by_class_name("recharts-surface").click()

    # courseAverage = driver.find_element_by_xpath("//*[text()[contains(., 'GPA')]]").text
    data = {}
    data['class'] = ''
    break

    # writeToJSONFile('./','file-name',data)



