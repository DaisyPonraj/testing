from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from threading import Timer
import time

browser = webdriver.Firefox()
browser.get('https://www.flipkart.com/')
browser.maximize_window()


