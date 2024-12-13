from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

chrome_driver = webdriver.Chrome()
chrome_driver.get("https://rahulshettyacademy.com/angularpractice/")
time.sleep(3)
chrome_driver.maximize_window()
#to print the title
print("page title:",chrome_driver.title)
#screenshot
chrome_driver.save_screenshot("pagehome1.png")
print("current page screenshot is saved")
#current url

#seleniumelement; name, classname  , id , cssSelector , xpath 
chrome_driver.find_element(By.NAME,"name").send_keys("Ashabai")
chrome_driver.find_element(By.NAME,"email").send_keys("Asha@gmail")
chrome_driver.find_element(By.ID,"exampleInputPassword1").send_keys("Asha12@")
chrome_driver.find_element(By.CLASS_NAME,"form-check-input").click()
my_select = Select(chrome_driver.find_element(By.ID,"exampleFormControlSelect1"))
my_select.select_by_index(1)
#my_select.select_by_visible_text("Female")
time.sleep(2)
chrome_driver.find_element(By.ID,"inlineRadio2").click()
chrome_driver.save_screenshot("pagehome2.png")
time.sleep(2)
print("title with current url:",chrome_driver.current_url)
#chrome_driver.find_element(By.NAME,"bday").send_keys("Asha@gmail")

chrome_driver.find_element(By.XPATH,"//input[@type='submit']").click()
message = chrome_driver.find_element(By.CLASS_NAME,"alert-success").text
time.sleep(5)
chrome_driver.quit()