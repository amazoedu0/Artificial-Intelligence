from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('https://10minutesemail.net/')

recovery_key = 'MQKAETC4209121' 

recovery = driver.find_element_by_xpath('//*[@id="sectionsNav"]/div/div[2]/ul/li[2]/a')

recovery.click()


recovery_box = driver.find_element_by_xpath('//*[@id="recoverForm"]/div[1]/div/input')

recovery_box.send_keys(recovery_key)

sub = driver.find_element_by_xpath('//*[@id="recoverForm"]/div[2]/button')

sub.click()

time.sleep(10)



while True:
    get_again = driver.find_element_by_xpath('//*[@id="moreMinutes"]/div/div[2]/i')
    get_again.click()
    time.sleep(500)
