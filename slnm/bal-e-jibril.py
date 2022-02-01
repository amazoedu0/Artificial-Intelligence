import re
from time import sleep
import os
from xml.dom.minidom import Element

from selenium import webdriver

driver = webdriver.Chrome()

file=open("bal-e-jibril.doc","w",encoding="utf-8")

url = "https://kulliyateiqbal.com/zarb-e-kaleem/%d8%ac%d8%a8-%d8%aa%da%a9-%d9%86%db%81-%d8%b2%d9%86%d8%af%da%af%db%8c-%da%a9%db%92-%d8%ad%d9%82%d8%a7%d8%a6%d9%82-%d9%be%db%81-%db%81%d9%88-%d9%86%d8%b8%d8%b1/"    

driver.get(url)

for i in range(1,500):
    
    
    UNVAAN=driver.find_element_by_class_name('entry-title')
    driver.implicitly_wait(1000)
    
    filename = UNVAAN.text+".txt"
    
    file=open(filename,"x",encoding="utf-8")
    
    file.write("\n - ["+str(i)+"] - \n"+UNVAAN.text+"\n\n")    
    driver.implicitly_wait(1000)
    # NAZM = driver.find_elements_by_class_name('')
    
    
    NAZM = driver.find_element_by_class_name('entry-content')
    driver.implicitly_wait(1000)
    
    # for band in NAZM:
    #     file.write(band.text+"\n\n")
    #     driver.implicitly_wait(1000)
    file.write(NAZM.text+"\n\n")
    
    driver.implicitly_wait(100)
    NEXT = driver.find_element_by_class_name("ast-right-arrow")
    driver.implicitly_wait(1000)
    NEXT.click()
    
    


