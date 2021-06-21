from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time

import requests
from bs4 import BeautifulSoup
import lxml

login = ''
password = ''

driver = webdriver.Chrome('E:/project_python/selenium_rutracker/sel_rutracker/chromedriver.exe')

time.sleep(2)

driver.get('https://rutracker.org/')

driver.find_element_by_xpath('//*[@id="page_header"]/div[3]/table/tbody/tr/td/div/a[2]/b').click()

#логинимся
time.sleep(3)
driver.find_element_by_xpath('//*[@id="top-login-uname"]').send_keys(login)
time.sleep(2)
driver.find_element_by_xpath('//*[@id="top-login-pwd"]').send_keys(password)
time.sleep(1)
driver.find_element_by_xpath('//*[@id="top-login-btn"]').click()

#водим в поиск 2021
driver.find_element_by_xpath('//*[@id="search-text"]').send_keys('2021')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="search-submit"]').click()
time.sleep(2)
#кликаем на раздел Фильмы 2021
driver.find_element_by_xpath('//*[@id="fs-1950"]').click()
time.sleep(2)
#кликаем поиск
driver.find_element_by_xpath('//*[@id="tr-submit-btn"]').click()
time.sleep(2)

url = driver.current_url
response = requests.get(url)
print(response)
html = response.content
soup = BeautifulSoup(html,'html.parser') # В опции также можно указать lxml, если предварительно установить одноименный пакет
#lxml = BeautifulSoup(lxml,'lxml.parser')
print(soup)
#print(lxml)