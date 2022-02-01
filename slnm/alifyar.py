from selenium import webdriver
from time import sleep

pages = ["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth","eleventh","twelfth","thirteenth","fourteenth","fifteenth","sixteenth","seventeenth","eighteenth","nineteenth","twentieth","twenty-first","tewnty-second","twenty-third","twenty-fourth"]

driver = webdriver.Chrome()


for page in pages:
    link = f"https://www.alifyar.com/ashab-e-kahaf-details-{page}-episode-abul-kalam-azad"
    driver.get(link)
    
    article = driver.find_element_by_class_name("article-detail")
    article.screenshot_as_png();
    
    sleep(1000)
    
    