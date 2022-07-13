from selenium import webdriver


PATH = "C:\\Users\\User\\Desktop\\selenium\\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("http://www.facebook.org")
gmail = driver.find_element_by_id('email').send_keys('username')
password = driver.find_element_by_id('pass').send_keys('password')

driver.find_element_by_name("login").click();