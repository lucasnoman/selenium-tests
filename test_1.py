# pylint: disable=invalid-name
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Edge()
browser.get('https://techstepacademy.com/trial-of-the-stones')

# get the first input XPATH and send 'rock' to it
input_stone = '//input[@name="r1Input"]'
input1 = browser.find_element(By.XPATH, input_stone)
input1.send_keys('rock')

# get the button of the 'rock' input and clicks
btn_stone = 'button#r1Btn'
btn1 = browser.find_element(By.CSS_SELECTOR, btn_stone)
btn1.send_keys(Keys.RETURN)


# get the answer
secret_div = '//div[@id="passwordBanner"]/h4'
secret_div_value = browser.find_element(By.XPATH, secret_div).text

# find the input for the secret and type the answer on it
input_secrets = '//input[@name="r2Input"]'
input2 = browser.find_element(By.XPATH, input_secrets)
input2.send_keys(secret_div_value)

# get the button of the secret and clicks
btn_secrets = '//button[@id="r2Butn"]'
btn2 = browser.find_element(By.XPATH, btn_secrets)
btn2.send_keys(Keys.RETURN)


# get the welthier person name
wealthier_person = '//p[contains(text(), "3000")]/../span/b'
person = browser.find_element(By.XPATH, wealthier_person).text

# get the input for the wealthier person and prints the name on it
input_person = '//input[@name="r3Input"]'
input3 = browser.find_element(By.XPATH, input_person)
input3.send_keys(person)

# get the button for the person and clicks
btn_person = '//button[@id="r3Butn"]'
btn3 = browser.find_element(By.XPATH, btn_person)
btn3.send_keys(Keys.RETURN)


# end the trial by clicking on 'Check Answers'
btn_check = 'button[name="checkButn"]'
click_check = browser.find_element(By.CSS_SELECTOR, btn_check)
click_check.send_keys(Keys.RETURN)
