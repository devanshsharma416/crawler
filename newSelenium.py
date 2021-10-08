from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(executable_path=r"C:\Users\DEVANSH SHARMA\Desktop\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.corepoweryoga.com/")

def studios():
    driver.find_element(By.XPATH, "//a[contains(text(), 'Studios')]").click()
    driver.find_element(By.XPATH, "//a[contains(text(), 'Chandler')]").click()
    driver.find_element(By.CLASS_NAME, "btn-outline-black btn-lg cursor-pointer px-3 direction-button").click()

studios()

def phone_number():
    phone_num = driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[7]/div[5]/button/div[1]/div[2]/div[1]")
    print(phone_num.text)

phone_number()

driver.close()