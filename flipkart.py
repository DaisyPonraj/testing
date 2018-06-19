from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui
from threading import Timer
import time

# KHJKJH

item1 = input('Enter item to search : ')
brand1 = input('please enter your brand : ')
item2 = "saree"
browser = webdriver.Firefox()
browser.get('https://www.flipkart.com/')
browser.maximize_window()

def closeMethod():
    closeButton = browser.find_element_by_xpath('/html/body/div[2]/div/div/button')
    closeButton.click()
    Timer(5.0,searchBar).start()

def searchBar():
    searchField = browser.find_element_by_xpath('/html/body/div[1]/div/header/div[1]/div/div/div/div[1]/form/div/div[1]/div/input').send_keys(item1)
    seachButton = browser.find_element_by_xpath('/html/body/div[1]/div/header/div[1]/div/div/div/div[1]/form/div/div[2]/button').click()
    Timer(5.0,brandFunc).start()

def brandFunc():
    brandSearch = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div[1]/div[1]/div/div/div/section[4]/div[2]/div[1]/div[1]/input')
    brandSearch.send_keys(brand1)  
    AvailBrand = browser.find_element_by_css_selector("div[title='"+brand1+"']").click()
    Timer(5.0,sortingFunc).start()

def sortingFunc():
    sortingPop = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div[2]/div[2]').click()
    Timer(5.0,selectProduct).start()

def selectProduct():
    ProductSelect = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]').click()
    time.sleep(3)
    browser.switch_to_window(browser.window_handles[1])
    Timer(5.0,AddTocartFunc).start()
def AddTocartFunc():
    # pincodeCheck = browser.find_element_by_id('pincodeInputId').send_keys(pincode)
    AddtoCart = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div/div/div[1]/div/div[1]/div[2]/ul/li[1]').click()
    time.sleep(3)
    browser.close()
    time.sleep(3)
    browser.switch_to_window(browser.window_handles[0])
    Timer(5.0,nextItemFunc).start()
def nextItemFunc():
    nextItem = browser.find_element_by_xpath('/html/body/div[1]/div/header/div[1]/div/div/div/div[1]/form/div/div[1]/div/input').clear()
    time.sleep(3)
    searchField = browser.find_element_by_xpath('/html/body/div[1]/div/header/div[1]/div/div/div/div[1]/form/div/div[1]/div/input').send_keys(item2)
    seachButton = browser.find_element_by_xpath('/html/body/div[1]/div/header/div[1]/div/div/div/div[1]/form/div/div[2]/button').click()
closeMethod()


