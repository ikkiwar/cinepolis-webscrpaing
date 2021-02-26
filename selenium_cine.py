from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import TimeoutException
import time
import pandas as pd

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'C:\\Users\\degon\\Desktop\\chromedriver.exe'
driver = webdriver.Chrome(driver_path, chrome_options = options)

driver.get('https://www.cinepolis.com.sv/')


WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'input.btn.btnEnviar.btnVerCartelera'))).click()

lista = driver.find_elements_by_class_name('btn.btnhorario.ng-scope')

for href in lista:
    link = href.find_element_by_tag_name('a').get_attribute('href')
    hora = href.find_element_by_tag_name('a').text
    print(link)
    print(hora)
