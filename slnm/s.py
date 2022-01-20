from tkinter.constants import BROWSE
from selenium import webdriver
import time
import random
from selenium import webdriver
from PIL import Image
from Screenshot import Screenshot_Clipping



driver = webdriver.Chrome()

for _ in range(1,10000):
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLScVWc-ObiZ8AcST7R8UU6JTQEUa1A7baY_JG9Gg1WtxuyvM4A/viewform?pli=1&pli=1")


    NC = driver.find_element_by_xpath('//*[@id="i5"]/div[3]/div')
    XC = driver.find_element_by_xpath('//*[@id="i8"]/div[3]/div')
    BUS = driver.find_element_by_xpath('//*[@id="i11"]/div[3]/div')

    Y1 = driver.find_element_by_xpath('//*[@id="i18"]/div[3]/div')
    N1 = driver.find_element_by_xpath('//*[@id="i21"]/div[3]/div')

    Y2 = driver.find_element_by_xpath('//*[@id="i28"]/div[3]/div')
    N2 = driver.find_element_by_xpath('//*[@id="i31"]/div[3]/div')

    Y3 = driver.find_element_by_xpath('//*[@id="i38"]/div[3]/div')
    N3 = driver.find_element_by_xpath('//*[@id="i41"]/div[3]/div')

    Y4 = driver.find_element_by_xpath('//*[@id="i48"]/div[3]/div')
    N4 = driver.find_element_by_xpath('//*[@id="i51"]/div[3]/div')

    # SUBMIT = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div/span/span')
    


    choice = random.randint(1,3) 
    if choice == 1:
        NC.click()
    elif choice == 2:
        XC.click()
    else:
        BUS.click()
    choice = random.randint(0,1) 
    if choice == 1:
        Y1.click()
    else:
        N1.click()
    choice = random.randint(0,1) 
    if choice == 1:
        Y2.click()
    else:
        N2.click()
    choice = random.randint(0,1) 
    if choice == 1:
        Y3.click()
    else:
        N3.click() 
    choice = random.randint(0,1) 
    if choice == 1:
        Y4.click()
    else:
        N4.click()
            
    
    # filename=f"/D:/Projects/test{_}.png"
    # shot = Screenshot_Clipping.Screenshot()
    # img_url=shot.full_Screenshot(driver, save_path='/D:/Projects/', image_name='Myimage.png')
    # print(img_url)
    
    time.sleep(5)
    SUBMIT=driver.find_element_by_xpath("//*[contains(text(), 'Submit')]")
    driver.implicitly_wait(10)
    SUBMIT.click()

driver.close()