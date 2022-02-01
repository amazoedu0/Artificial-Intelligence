from bs4 import BeautifulSoup
import urllib.request
from IPython.display import HTML
import re
from time import sleep
import os

from selenium import webdriver

driver = webdriver.Chrome()


file=open("manto ke afsaany.doc","a",encoding="utf-8")

login = "https://world.rekhta.org/"
driver.get(login)

email = "amazokabali@moakt.cc"
password = "U@ganda1234"

mail = driver.find_element_by_id("Email")
mail.send_keys(email)

psd = driver.find_element_by_id("Password")
psd.send_keys(password)

login_click = driver.find_element_by_id("BtnWrldLogin")
login_click.click()
sleep(30)

url = "https://www.rekhta.org/stories/thanda-gosht-saadat-hasan-manto-stories?lang=ur"    
driver.get(url)

for i in range(1,500):
    UNVAAN=driver.find_element_by_xpath('//*[@id="content"]/div/div/div[1]/h1')
    SHAAIR=driver.find_element_by_xpath('//*[@id="content"]/div/div/div[1]/div[1]/h2')
    
    
    file.write("\n - ["+str(i)+"] - \n"+UNVAAN.text+" : "+SHAAIR.text+"\n\n")    
    
    NAZM = driver.find_elements_by_class_name('c')
    for band in NAZM:
        file.write(band.text+"\n\n")
    driver.implicitly_wait(100)
    NEXT = driver.find_element_by_class_name("nextPoem")
    NEXT.click()
    
    


