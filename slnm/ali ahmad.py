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
ages=[]
sem=[]
subs = [
     "BSc. Architectural ","B. Architecture","B.Sc. Chemical Engineering","BSc. Civil Engineering","BSc. City and Regional Planning","BSc. Computer Science","BSc. Electrical Engineering","BSc Geological Engineering","BBA","BBIT","B.Sc Environmental Engineering","B.Sc. Industrial & Manufacturing Engineering","B.Sc. Mechanical Engineering","B.Sc Mechatronics & Control Engineering","BSc. Mining Engineering","B.Sc. Metallurgical and Materials Engineering","BSc. Petroleum & Gas Engineering","BSc. Product and Industrial Design","BSc. Polymer Engineering","B.Sc. TransportationEngineering","BSc. Chemical Engineering","BSc. Electrical Engineering","B.Sc. Chemical Technology","B.Sc. Mechanical Engineering","BSc. Computer Science","BSc. Electrical Engineering","BSc. Electrical Engineering","B.Sc. Mechanical Engineering","BSc. Computer Engineering"
]
cgpa=[]


print(csvreader)
for row in csvreader:
    name=""
    name=row[1]
    count += 1
    names.append(name)
    if count >=1000: break


for _ in range(1000):
    sem.append(str(random.randint(3,9))+"th")
    ages.append(random.randint(18,30))
    cgpa.append(round(random.uniform(2.22,4.00),2))


driver = webdriver.Chrome( options=option)



# textboxes = driver.find_elements_by_class_name("quantumWizTextinputPaperinputInput")
for _ in range(1,10000):
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdNZsZet-9BJ95tXV09N5RvepeZY2bgiyVSVEMB7OYLZeKbBQ/viewform")

    textboxes = driver.find_elements_by_class_name("quantumWizTextinputPaperinputInput")
    radiobuttons = driver.find_elements_by_class_name("appsMaterialWizToggleRadiogroupElContainer")
    textboxes[0].send_keys(random.choice(names))
    textboxes[1].send_keys(random.choice(ages))
    textboxes[2].send_keys(sem[_])
    textboxes[3].send_keys(random.choice(subs))
    textboxes[4].send_keys(cgpa[_])
    driver.implicitly_wait(1000)
    
    ch=[2,7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]
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

    for j in range(0,31):
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