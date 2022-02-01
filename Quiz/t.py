# import random
# ages=[]

# buttons = []
# sem = []

# cgpa=[]

# for i in range(10):
#     ages.append(random.randint(22,33))
#     sem.append(str(random.randint(3,9))+"th")
#     buttons.append(7)
#     cgpa.append(round(random.uniform(2.22,4.00),2))

# print(ages)
# print(sem)
# print(cgpa)
# print(buttons)


# from re import sub
# from selenium import webdriver

# driver = webdriver.Chrome()


# element = 'tr:nth-child(2)'


# url = "https://www.uet.edu.pk/faculties/facultiesinfo/index.html?RID=undergraduate_academic_programs"
# driver.get(url)
subs = [
     "BSc. Architectural ","B. Architecture","B.Sc. Chemical Engineering","BSc. Civil Engineering","BSc. City and Regional Planning","BSc. Computer Science","BSc. Electrical Engineering","BSc Geological Engineering","BBA","BBIT","B.Sc Environmental Engineering","B.Sc. Industrial & Manufacturing Engineering","B.Sc. Mechanical Engineering","B.Sc Mechatronics & Control Engineering","BSc. Mining Engineering","B.Sc. Metallurgical and Materials Engineering","BSc. Petroleum & Gas Engineering","BSc. Product and Industrial Design","BSc. Polymer Engineering","B.Sc. TransportationEngineering","BSc. Chemical Engineering","BSc. Electrical Engineering","B.Sc. Chemical Technology","B.Sc. Mechanical Engineering","BSc. Computer Science","BSc. Electrical Engineering","BSc. Electrical Engineering","B.Sc. Mechanical Engineering","BSc. Computer Engineering"
]

# subj= driver.find_elements_by_css_selector(element)
# for subs in subj:
#     print(subs.text)
import random
print(random.choice(subs))