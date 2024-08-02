from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

# define url
url = "http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html"

# instantiate webdriver and open a chrome browser
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# maximize browser window
driver.maximize_window()

# load the webpage
driver.get(url)

# find the source
source = driver.find_element(By.XPATH,'//*[@id="box3"]')

# find the destination
destination = driver.find_element(By.XPATH,'//*[@id="box103"]')

# instantiate ActionChains
actions = ActionChains(driver)

# perform the drag and drop
actions.drag_and_drop(source, destination).perform()

# pause the program for 5 seconds to view the results
sleep(5)

# close the driver
driver.quit()