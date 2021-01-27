from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
import time
import random
import urllib.request
from PIL import Image

def convertImage(jpgfile,width=256,height=256):
	img = Image.open(jpgfile)
	if img.mode != 'RGB':
		img = img.convert('RGB')
	try:
		new_img = img.resize((width,height),Image.BILINEAR)  
		new_img.save("/Desktop/Images/"+jpgfile)
	except Exception as e:
		print(e)

PATH = "/Downloads/chromedriver"
driver = webdriver.Chrome(PATH)
driver.implicitly_wait(200)
excel_file = "/Desktop/CompanyNames.xlsx"
file = pd.read_excel(excel_file, engine='openpyxl')
companies = file["Company"]
companies = companies[1:] 
try:
	for company in companies:
		try:
			driver.get("https://www.google.com/search?q="+company+"+logo")
		except:
			print(company)
			continue;
		time.sleep(random.randint(1,3))
		try:
			images = driver.find_element_by_link_text("Images")
		except:
			print(company)
			continue;
		images.click()
		time.sleep(random.randint(1,3))
		try:
			image = driver.find_element_by_xpath('//img[@class="rg_i Q4LuWd"]')
		except:
			print(company)
			continue;
		try:
			urllib.request.urlretrieve(image.get_attribute('src'), company+".jpg")
		except:
			print(company)
			continue;
		convertImage(company+".jpg")
finally:
	driver.quit()

