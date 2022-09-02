from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from time import sleep

driver = webdriver.Chrome("/home/arsemenov/Документы/susel/r1/first-repo/chromedriver")
driver.get("https://google.com")
driver.find_element(By.XPATH, "//input[@title=\"Поиск\"]").send_keys ('Skillfactory' + Keys.RETURN)
sleep (2)
driver.save_screenshot('sf.png')
driver.quit()

