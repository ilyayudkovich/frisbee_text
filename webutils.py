from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from utilities import getLogin
import time

def main():
    login()
    createLabel()

def quit():
    driver.quit()

def login():
    driver = webdriver.Firefox()
    driver.get('http://gmail.com')
    sib = driver.find_element_by_id('identifierId')
    user, pw = getLogin()
    sib.send_keys(user)
    time.sleep(2)
    sib = driver.find_element_by_name('password')
    sib.send_keys(pw)

def login(email, pw):
    driver = webdriver.Firefox()
    driver.get('http://gmail.com')
    sib = driver.find_element_by_id('identifierId')
    user, pw = getLogin()
    sib.send_keys(email)
    time.sleep(2)
    sib = driver.find_element_by_name('password')
    sib.send_keys(pw)

def carrierHomePage():
    driver = webdriver.Firefox()
    driver.get('http://freecarrierlookup.com/')
    return driver

def getSMSNumber(driver, number):
    pib = driver.find_element_by_name('phonenum')
    pib.send_keys(number)
    time.sleep(2)
    driver.find_element_by_xpath('html/body/div[2]/div[3]/div/div/div[1]/form/table/tbody/tr[3]/td/input[2]').click()
    time.sleep(2)
    smsNumber = driver.find_element_by_xpath('html/body/div[2]/div[3]/div/div/div[1]/div[3]/div/table/tbody/tr[4]/td[2]').text
    time.sleep(1)
    driver.get('http://freecarrierlookup.com/')
    return smsNumber


def getAllNumbers(driver, numbers):
    lon = []
    for n in numbers:
        lon.append(getSMSNumber(driver, n))
    driver.quit()
    return lon

# This will create a 'Failed' label in the inbox
def createLabel():
    pass

# This will create a Filter to send all failed emails
# to the 'Failed' label folder
def createFilter():
    pass


