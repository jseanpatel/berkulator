from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

driver.get("https://www.berkeleytime.com/catalog")

# Then navigate to a search for each class.
classes = driver.find_elements_by_class_name("filter-selection")

def writeToJSONFile(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)

for indivClass in classes:
    click1 = driver.find_element_by_class_name("filter-selection").click()
    click2 = driver.find_element_by_xpath("//*[text()[contains(., 'See grade distributions')]]")
    data = {}
    data['class'] = ''
    pass

    # writeToJSONFile('./','file-name',data)



