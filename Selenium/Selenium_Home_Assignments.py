from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#Assingment 1.
# options = Options()
# options.add_argument("start-maximized")
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# driver.get("http://www.walla.co.il")

# options = Options()
# options.add_argument("start-maximized")
# driver = webdriver.Firefox()
# driver.get("http://www.ynet.co.il")

#Assignment 2.
# w_title = driver.title
# driver.refresh()
# if w_title == driver.title:
#     print("Titles are the same")

#Assignment 3.
#The elements are the same. Browser doesn't make a difference.


#Assignment 4.
# options = Options()
# options.add_argument("start-maximized")
# driver = webdriver.Firefox()
# driver.get("https://translate.google.com/")
# driver.find_element(By.ID, "source").send_keys("ברכות")
# driver.find_element(By.ID, "gt-submit").click()


#Assignment 5.
# options = Options()
# options.add_argument("start-maximized")
# driver = webdriver.Firefox()
# driver.get("https://www.youtube.com/")
# WebDriverWait(driver, 10000).until(EC.visibility_of_element_located((By.TAG_NAME, 'body')))
# driver.find_element(By.ID, "search").send_keys("Child in time")
# #driver.find_element(By.ID, "search")
# driver.find_element(By.ID, "search-icon-legacy").click()

#Assigment 6.

#1. driver.find_element(By.ID, "source")
#2. driver.find_element(By.CLASS_NAME, "jfk-button")
#3. driver.find_element(By.XPATH, "//input[@type='submit']")

#Assignment 7.

# options = Options()
# options.add_argument("start-maximized")
# driver = webdriver.Firefox()
# driver.get("https://www.facebook.com//")
# WebDriverWait(driver, 10000).until(EC.visibility_of_element_located((By.TAG_NAME, 'body')))
# driver.find_element(By.ID, "email").send_keys("facebook_login_email")
# driver.find_element(By.ID, "pass").send_keys("super_secret_passwd")





