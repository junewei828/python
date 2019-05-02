from selenium import webdriver

# chromedriver = '/usr/local/bin/chromedriver'
driver = webdriver.Firefox()
# driver = webdriver.Chrome()
driver.get("https://python.org")