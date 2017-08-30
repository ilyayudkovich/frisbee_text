from selenium import webdriver

def main():
    browser = webdriver.Firefox()
    browser.get('http://seleniumhq.org')

main()
