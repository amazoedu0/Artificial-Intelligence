from bs4 import BeautifulSoup
import urllib.request
from IPython.display import HTML
import re
from time import sleep
import os

pages = ["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth","eleventh","twelfth","thirteenth","fourteenth","fifteenth","sixteenth","seventeenth","eighteenth","nineteenth","twentieth","twenty-first","tewnty-second","twenty-third","twenty-fourth"]

for page in pages:
    with open("new.doc","a",encoding='utf-8') as file:
        url = f"https://www.alifyar.com/ashab-e-kahaf-details-{page}-episode-abul-kalam-azad"
        r = urllib.request.urlopen(url).read()

        soup = BeautifulSoup(r,"html.parser")
        # print(soup.prettify()[:100])

        for text in soup.find_all("p",dir="RTL"):
            # print(text.get_text())
            words = str(text.get_text())+"\n"
            file.write(words)
        file.flush()
    # sleep(1000)