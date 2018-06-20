from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui
from threading import Timer
import time
UN = "9894055756"
PWD = "Psss@123"

browser = webdriver.Firefox()
browser.get('https://www.flipkart.com/')
browser.maximize_window()
username_x = "/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input"
password_x = '/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/input'
login_x = '/html/body/div[2]/div/div/div/div/div[2]/div/form/div[3]/button'
def login():
    def invalid_un():
        username = browser.find_element_by_xpath(username_x).send_keys("8754232355")
        time.sleep(3)
        validpassword = browser.find_element_by_xpath(password_x).send_keys(PWD)
        login_into = browser.find_element_by_xpath(login_x).click()
        Timer(5.0,valid_un_pwd).start()
        # except:
        #     print("pass")

    def valid_un_pwd():
        validusername = browser.find_element_by_xpath(username_x).send_keys(UN)
        time.sleep(3)
        validpassword = browser.find_element_by_xpath(password_x).send_keys(PWD)
        login_into = browser.find_element_by_xpath(login_x).click()
        print ("login successful")
        time.sleep(3)  
    
    invalid_un()

login()

