from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
import random
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time

PATH = "/Downloads/chromedriver"
driver = webdriver.Chrome(PATH)
driver.implicitly_wait(15)
excel_file = "/Desktop/CompanyNames.xlsx"
file = pd.read_excel(excel_file, engine='openpyxl')
companies = file["Company"] #use name of column which contains all the company names
companies = companies[1:] #change according to the excel file
all_links = []
try:
	for company in companies:
		driver.get("https://www.youtube.com/results?search_query="+company)
		time.sleep(random.randint(3,15))
		user_data = driver.find_elements_by_xpath('//*[@id="video-title"]')
		links = []
		if (len(user_data) >= 3):
			for i in range(3):
			    links.append(user_data[i].get_attribute('href'))
		all_links.append(links)
finally:
	df = pd.DataFrame({'Company' : companies[:len(all_links)],'Links' : all_links})
	df.to_excel("/Desktop/links.xlsx") #creates a new excel file with the company names and their top 3 links
	driver.quit()