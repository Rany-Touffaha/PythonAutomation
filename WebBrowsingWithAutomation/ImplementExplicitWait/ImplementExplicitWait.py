from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# define url
url = "http://the-internet.herokuapp.com/dynamic_controls"

# instantiate webdriver and open a chrome browser
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# maximize browser window
driver.maximize_window()

# load the webpage
driver.get(url)

# define a wait
wait = WebDriverWait(driver, 10)

# find the Enable button
enable_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/form[2]/button')
# click the Enable button
enable_button.click()
sleep(3)

# find the disable button
disable_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div[1]/form[2]/button')))
# click the Disable button
disable_button.click()
# pause the program execution for 3 seconds to view the result
sleep(3)

# find the Remove button
remove_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/form[1]/button')
# click the Remove button
remove_button.click()
# pause the program execution for 3 seconds to view the result
sleep(3)

# find the Add button
add_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div[1]/form[1]/button')))
# click the Add button
add_button.click()
# pause the program execution for 3 seconds to view the result
sleep(3)

# find the checkbox
checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="checkbox"]')))
# click the checkbox
checkbox.click()
# pause the program execution for 3 seconds to view the result
sleep(3)

# close the browser and quit the webdriver
driver.quit()
