from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.action_chains import ActionChains
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
        time.sleep(3)
        try:
            error_mess = browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/span[3]/span')
            print('invalid username - valid pass word scenario pass')
        except:
            print('invalid username - valid pass word scenario fail')
        username = browser.find_element_by_xpath(username_x).clear()
        validpassword = browser.find_element_by_xpath(password_x).clear()
        Timer(5.0,invalid_pwd).start()

    def invalid_pwd():
        validusername = browser.find_element_by_xpath(username_x).send_keys(UN)
        time.sleep(3)
        password = browser.find_element_by_xpath(password_x).send_keys("psss@456")
        login_into = browser.find_element_by_xpath(login_x).click()
        time.sleep(3)
        try:
            error_mess = browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/span[3]/span')
            print('valid username - invalid pass word scenario pass')
        except:
            print('valid username - invalid pass word scenario fail')
        username = browser.find_element_by_xpath(username_x).clear()
        validpassword = browser.find_element_by_xpath(password_x).clear()
        Timer(5.0,emptyfields).start()  

    def emptyfields():
        login_into = browser.find_element_by_xpath(login_x).click()
        time.sleep(3)
        try:
            error_mess = browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/span[2]/span')
            print('empty username and password scenario pass')
        except:
            print('empty username and password scenario fail')
        Timer(5.0,valid_un_pwd).start()

    def valid_un_pwd():
        validusername = browser.find_element_by_xpath(username_x).send_keys(UN)
        time.sleep(3)
        validpassword = browser.find_element_by_xpath(password_x).send_keys(PWD)
        login_into = browser.find_element_by_xpath(login_x).click()
        print ("login successful")
        time.sleep(3)
        Timer(5.0,logout).start()  

    def logout():
        element_to_hover_over = browser.find_element_by_xpath('/html/body/div/div/header/div[1]/div/div/div/div[2]/div[1]/div/div/div')
        hover = ActionChains(browser).move_to_element(element_to_hover_over)
        hover.perform()
        logoutbutton = browser.find_element_by_xpath('/html/body/div/div/header/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/ul/li[7]').click()
        time.sleep(2)
        print('logout successfull')
    invalid_un()

login()

