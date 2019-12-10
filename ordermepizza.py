#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driverpath = r'C:\Users\Student\Downloads\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driverpath)
driver.get("https://dominos.com/en/")
time.sleep(15)
# order carryout
click_delivery = driver.find_element_by_xpath('//*[@id="homeWrapper"]/main/section[1]/div/div[2]/a[2]')
click_delivery.click()
time.sleep(5)
#postal code
driver.find_element_by_xpath('//*[@id="Postal_Code_Sep"]').send_keys('98498' + Keys.RETURN)
time.sleep(3)
#pick the store
driver.find_element_by_xpath('//*[@id="locationsResultsPage"]/div/div[2]/div[2]/div[2]/div/div[2]/div').click()
time.sleep(5)
# pick your order (speciality pizza in this case)
driver.find_element_by_xpath('//*[@id="entree-Pizza"]/a/div[2]/h2').click()
time.sleep(3)
# pick what kind of speciality pizza
driver.find_element_by_xpath('//*[@id="categoryPage2"]/section/div/div[7]/div/div/a/img').click()
time.sleep(3)
# size
driver.find_element_by_xpath('//*[@id="SizeCrustWrapper"]/div[3]').click()

# large
driver.find_element_by_xpath('/html/body/div[27]/section/div/div[3]/div[3]/div[5]/div[3]/div/div/div[4]/div/div[3]/label/span[2]').clcik()
time.sleep(3)
# what style
driver.find_element_by_xpath('//*[@id="SizeCrustWrapper"]/div[5]/div[7]/div/label/span[2]').click()
time.sleep(3)
# qty
#driver.find_element_by_xpath('//*[@id="pizzaSummaryInColumn"]/div[1]/div[2]/p/select').send_keys('2').click()
time.sleep(3)
# pick cheese and sauce
driver.find_element_by_xpath('//*[@id="pizzaBuilderPage"]/div[3]/div[8]/div[2]/button').click()
time.sleep(3)
# cheese amount
driver.find_element_by_xpath('//*[@id="cheeseSauceWrapper"]/div[2]/div/div/div[1]/div[2]').click()
time.sleep(3)
# pick sauce
driver.find_element_by_xpath('//*[@id="cheeseSauceWrapper"]/div[3]/div[1]/label').clcik()
time.sleep(3)
#select garlic parm
driver.find_element_by_xpath('//*[@id="cheeseSauceWrapper"]/div[3]/div[2]/div[4]/label/span').click()
time.sleep(3)
#add to order (chicken )
driver.find_element_by_xpath('//*[@id="pizzaSummaryInColumn"]/div[1]/div[2]/div[2]/button').click()
time.sleep(3)
#save order
driver.find_element_by_xpath('//*[@id="pizzaSummaryInColumn"]/div[1]/div[2]/div[2]/button').click()
time.sleep(3)
# slect no xtra cheese
driver.find_element_by_xpath('//*[@id="stepUpsell"]/div/button[1]/span').click()
time.sleep(3)
# select time
driver.find_element_by_xpath('//*[@id="orderDetailsInColumn"]/ul/li[4]/h3').click()
time.sleep(3)
# pick later time
driver.find_element_by_xpath('//*[@id="orderDetailsInColumn"]/ul/li[4]/form/ul/li[2]/label').click()
time.sleep(3)
#date



#select another pizza
#driver.find_element_by_xpath('//*[@id="categoryPage2"]/section/div/div[6]/div/div/a/img').click()
#time.sleep(3)
# cutomize the pizza
#driver.find_element_by_xpath('//*[@id="categoryPage2"]/section/div/div[6]/div/a[2]').click()
#time.sleep(3)
#driver.find_element_by_xpath('//*[@id="SizeCrustWrapper"]/div[4]/div/div[3]/label').click()
# hand tossed
#time.sleep(3)
#driver.find_element_by_xpath('//*[@id="SizeCrustWrapper"]/div[5]/div[7]/div/label/span[1]').click()
# pick cheese and sauce
#time.sleep(3)
#driver.find_element_by_xpath('//*[@id="pizzaBuilderPage"]/div[3]/div[5]/div[1]/div[2]/button').click()

