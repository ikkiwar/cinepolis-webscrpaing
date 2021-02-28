from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import TimeoutException
import time
import pandas as pd
import numpy as np

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'C:\\Users\\degon\\Desktop\\trabajo_final\chromedriver.exe'
driver = webdriver.Chrome(driver_path, chrome_options = options)

driver.get('https://www.cinepolis.com.sv/')


WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'input.btn.btnEnviar.btnVerCartelera'))).click()

link = []
hora = []

lista_ss = driver.find_elements_by_class_name('btn.btnhorario.ng-scope') 

for href in lista_ss:
    link_ss = href.find_element_by_tag_name('a').get_attribute('href')
    hora_ss = href.find_element_by_tag_name('a').text
    link.append(link_ss)
    hora.append(hora_ss)
   

WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'option:nth-child(3)'))).click()
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'input.btn.btnEnviar.btnVerCartelera'))).click()


lista_sa = driver.find_elements_by_class_name('btn.btnhorario.ng-scope')

for href in lista_sa:
    link_sa = href.find_element_by_tag_name('a').get_attribute('href')
    hora_sa = href.find_element_by_tag_name('a').text
    link.append(link_sa)
    hora.append(hora_sa)
    
df = pd.DataFrame(list(zip(link,hora)), columns = ['Link','Hora'])
df.to_excel(r'C:\Users\degon\Desktop\trabajo_final\link.xlsx', index = False, header=True) 
df.to_csv(r'C:\Users\degon\Desktop\trabajo_final\link.csv', index=False)

driver.quit(
