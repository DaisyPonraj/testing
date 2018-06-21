from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from threading import Timer
import time

UN = "9894055756"
PWD = "Psss@123"
count = 1 
browser = webdriver.Firefox()
browser.get('https://www.flipkart.com/')
browser.maximize_window()

username_x = "/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input"
password_x = '/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/input'
login_x = '/html/body/div[2]/div/div/div/div/div[2]/div/form/div[3]/button'

def valid_un_pwd():
        validusername = browser.find_element_by_xpath(username_x).send_keys(UN)
        time.sleep(3)
        validpassword = browser.find_element_by_xpath(password_x).send_keys(PWD)
        login_into = browser.find_element_by_xpath(login_x).click()
        print ("login successful")
        time.sleep(3)
        Timer(5.0,searchBar).start()

def searchBar():
    searchField = browser.find_element_by_xpath('/html/body/div[1]/div/header/div[1]/div/div/div/div[1]/form/div/div[1]/div/input').send_keys("sofa")
    seachButton = browser.find_element_by_xpath('/html/body/div[1]/div/header/div[1]/div/div/div/div[1]/form/div/div[2]/button').click()
    print ("search method successfull")
    Timer(5.0,selectProduct).start()

def selectProduct():
    ProductSelect = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]').click()
    time.sleep(3)
    browser.switch_to_window(browser.window_handles[1])
    print ("product select successful")
    Timer(5.0,AddTocartFunc).start()

def AddTocartFunc():
    # pincodeCheck = browser.find_element_by_id('pincodeInputId').send_keys(pincode)
    AddtoCart = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div/div/div[1]/div/div[1]/div[2]/ul/li[1]').click()
    time.sleep(3)
    browser.close()
    time.sleep(3)
    browser.switch_to_window(browser.window_handles[0])
    print ("add to cart successful")
    Timer(5.0,nextItemFunc).start()

def logout():
        element_to_hover_over = browser.find_element_by_xpath('/html/body/div/div/header/div[1]/div/div/div/div[2]/div[1]/div/div/div')
        hover = ActionChains(browser).move_to_element(element_to_hover_over)
        hover.perform()
        logoutbutton = browser.find_element_by_xpath('/html/body/div/div/header/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/ul/li[7]').click()
        time.sleep(2)
        print('logout successfull')  

def nextItemFunc():
    nextItem = browser.find_element_by_xpath('/html/body/div[1]/div/header/div[1]/div/div/div/div[1]/form/div/div[1]/div/input').clear()
    time.sleep(3)
    searchField = browser.find_element_by_xpath('/html/body/div[1]/div/header/div[1]/div/div/div/div[1]/form/div/div[1]/div/input').send_keys("shelf")
    seachButton = browser.find_element_by_xpath('/html/body/div[1]/div/header/div[1]/div/div/div/div[1]/form/div/div[2]/button').click()
    print ('next product ')
    Timer(5.0,selectProduct1).start()

def selectProduct1():
    ProductSelect = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]').click()
    time.sleep(3)
    browser.switch_to_window(browser.window_handles[1])
    print ("product select successful")
    Timer(5.0,AddTocartFunc1).start()

def AddTocartFunc1():
    # pincodeCheck = browser.find_element_by_id('pincodeInputId').send_keys(pincode)
    AddtoCart = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div/div/div[1]/div/div[1]/div[2]/ul/li[1]').click()
    time.sleep(3)
    browser.close()
    time.sleep(3)
    browser.switch_to_window(browser.window_handles[0])
    print ("add to cart successful")
    Timer(5.0,checkcart).start()
def checkcart():
        cart = browser.find_element_by_xpath('/html/body/div[1]/div/header/div[1]/div/div/div/div[2]/a').click()
        time.sleep(3)
valid_un_pwd()