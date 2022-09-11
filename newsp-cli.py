from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
import re

def urlify(s):

    # Remove all non-word characters (everything except numbers and letters)
    s = re.sub(r"[^\w\s]", '', s)

    # Replace all runs of whitespace with +
    s = re.sub(r"\s+", '+', s)

    return s

def urlifyundo(p):

    #Returns spaces
    p = re.sub(r"[+]", ' ', p)
    
    return p


options = Options()
options.headless = False
driver = webdriver.Firefox(options=options, executable_path=GeckoDriverManager().install())

url = "https://mgreader.com/?cat=231&s="
#newspsearch = urlify(input("What newspaper are you looking for: "))
newspsearch = urlify("Financial Times") 

#Pulls website from the users input
driver.get(url + newspsearch)

#Waits webpage to load
driver.implicitly_wait(2)

#Prints recent avalable selections
newspsearch = urlifyundo(newspsearch)
list_links=driver.find_elements(By.XPATH, "//a[contains(text(),'" + newspsearch + "')]")
for i in list_links:
    print (i.get_attribute('title'))
    #Ask user for webpage
userselection = input("What title would you like to read:")
userselections = driver.find_element(By.CSS_SELECTOR, "h2[class='entry-title'] a[title='" + userselection + "']")
linkfound1 = userselections.get_attribute('href')
driver.get(linkfound1)
driver.implicitly_wait(2)
linkfound2 = driver.find_element(By.CSS_SELECTOR, ".btn.btn-dark")
linkfound2.click
#dateselected =  urlify(input("Which selection would you like to make?: "))
# #printnewspsearch = driver.g
#driver.quit()
