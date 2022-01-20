import time
import random
from selenium import webdriver
import csv

option = webdriver.ChromeOptions()
option.add_argument("-incognito")

file = open('D:/STUDY/1-AI/AI LAB/Code/Lab Codes/muslim-names-crawler-master/muslim-names-crawler-master/output.csv')
csvreader = csv.reader(file)
csvreader


count=0
names=[]
emails=[]

print(csvreader)
for row in csvreader:
    name=""
    name=row[1]
    count += 1
    names.append(name)
    if count >=1000: break


for name in names:
    email=""
    email=name.replace(" ","")+"@gmail.com"
    emails.append(email.lower())



driver = webdriver.Chrome( options=option)


# textboxes = driver.find_elements_by_class_name("quantumWizTextinputPaperinputInput")
for _ in range(1,10000):
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdvum4KwsQuQIW9T-rpYnanZIUbsM62Sm2rltcnDJJovhCwZw/viewform")

    textboxes = driver.find_elements_by_class_name("quantumWizTextinputPaperinputInput")
    radiobuttons = driver.find_elements_by_class_name("appsMaterialWizToggleRadiogroupElContainer")
    textboxes[0].send_keys(names[_])
    textboxes[1].send_keys(emails[_])
    
    ch=[2,4,4,5,2,4,4,2,4,3,4]
    high=[]
    for i in range(1,len(ch)+1  ):
        sum=0
        for j in range(0,i):
            sum+=ch[j]
        high.append(sum)
    lower=[]
    lens=len(ch)
    for i in range(0,len(ch)):
        sum=0
        for j in range(0,i):
            sum+=ch[j]
        lower.append(sum)

    for j in range(0,11):
        test=lower[j]
        highs=high[j]
        print(f"{test},{highs}")
        choice = random.randint(test,highs-1)
        choice = random.randint(test,highs-1)
        radiobuttons[choice].click()
        


    SUBMIT=driver.find_element_by_xpath("//*[contains(text(), 'Submit')]")
    driver.implicitly_wait(3)
    SUBMIT.click()

driver.close()