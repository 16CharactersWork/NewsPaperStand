from concurrent.futures.process import _sendback_result
from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
import re
import pickle


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
pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))
cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)
#Waits webpage to load
driver.implicitly_wait(2)
newslink = "Financial Times USA – August 10, 2022"
#Prints recent avalable selections
newspsearch = urlifyundo(newspsearch)
list_links=driver.find_elements(By.XPATH, "//a[contains(text(),'" + newspsearch + "')]")
for i in list_links:
    print (i.get_attribute('title'))
    #Ask user for webpage
driver.find_element(By.XPATH, "//button[@aria-label='Close this dialog']").send_keys(Keys.ENTER)

driver.find_element(By.CSS_SELECTOR, "h2[class='entry-title'] a[title='" + newslink + "']").send_keys(Keys.ENTER)
driver.refresh
driver.implicitly_wait(4)
driver.find_element(By.CSS_SELECTOR, "h2[class='entry-title'] a[title='" + newslink + "']").send_keys(Keys.ENTER)
driver.refresh
driver.implicitly_wait(3)
james = driver.find_element(By.XPATH, "//a[@class='btn btn-dark']")
james2 = james.find_element(By.CSS_SELECTOR, "a")
for e in james2:
    print(e.text)
#driver.switch_to.new_window('tab')
#driver.get(john)



driver.implicitly_wait(2)
driver.implicitly_wait(10)

#driver.find_element(By.XPATH, "//a[@class='btn btn-dark']").send_keys(Keys.ENTER)



driver.find_element(By.XPATH, "//a[@class='hz-icon hz-icn-down down-pdf']").send_keys(Keys.ENTER)
#driver.implicitly_wait(30)
#driver.quit()

#driver.find_element(By.CSS_SELECTOR, "#dismiss-button").send_keys(Keys.ENTER)
#userselection.send_keys(Keys.ENTER)
#linkfound1 = userselections.get_attribute('href')
#driver.navigate.to(linkfound1)

#driver.find_element(By.XPATH, "//a[@class='btn btn-dark']").send_keys(Keys.ENTER)

#dateselected =  urlify(input("Which selection would you like to make?: "))
# #printnewspsearch = driver.g
#driver.quit()
