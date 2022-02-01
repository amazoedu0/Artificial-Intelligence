from bs4 import BeautifulSoup
import urllib.request
from IPython.display import HTML
import re
from time import sleep
import os

# url = "https://www.rekhta.org/nazms/dastuur-diip-jis-kaa-mahallaat-hii-men-jale-habib-jalib-nazms?sort=popularity-desc&lang=ur"
url = "https://www.rekhta.org/nazms/hamesha-der-kar-detaa-huun-hamesha-der-kar-detaa-huun-main-har-kaam-karne-men-muneer-niyazi-nazms?sort=popularity-desc"


r = urllib.request.urlopen(url).read()
soup = BeautifulSoup(r,"html.parser")

file=open("nazm.doc","w",encoding="utf-8")

# UNVAAN = str(soup.find('h1').get_text())
# SHAAIR = str(soup.find('h2').get_text())
# file.write(UNVAAN+' : '+SHAAIR+'\n\n')
# 
# for text in soup.find_all('div',class_='c'):
    # for para in text:
        # word = str(para.get_text())+"\n"
        # file.write(word)
    # file.write("\n")
# file.write("\n")

for test in soup.find_all('div'):
    file.write(test.prettify())

print(test)
