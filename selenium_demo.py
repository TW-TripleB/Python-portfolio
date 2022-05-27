from selenium import webdriver
import time


url = "https://www.newegg.com/"
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path=r"C:\Users\bl0k\Desktop\practice\chromedriver.exe",options=options)
driver.get(url)
driver.implicitly_wait(3)
#to sign in page
loginPage = driver.find_element_by_xpath('//*[@id="app"]/header/div[1]/div[1]/div[2]/div[4]/a')
loginPage.click()
#input email
email = driver.find_element_by_name("signEmail")
email.send_keys("bryce.k.lin@newegg.com")
time.sleep(0.5)
#sign in 
signIn = driver.find_element_by_name("signIn")
signIn.click()
time.sleep(0.5)
#password
psw = driver.find_element_by_xpath('//*[@id="labeled-input-password"]')
psw.send_keys("1qaz@WSX3edc")
signIn = driver.find_element_by_name("signIn")
signIn.click()
time.sleep(10)

driver.quit()

