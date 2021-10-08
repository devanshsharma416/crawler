import bs4  
import requests  
import re

  
#Creating the requests  
response = requests.get("https://www.google.com/maps/place/CorePower+Yoga/@33.5183002,-112.06563,17z/data=!4m5!3m4!1s0x0:0xa9a7ea57d481e2b0!8m2!3d33.5183002!4d-112.0634413")
response_value = response.text
pattern = "(\d{3}-\d{3}-\d{4})"
match = re.findall(pattern, response_value)
if match != []:
    print("+1", match[0])



# # match = re.findall(pattern, response_value)
# # print(match)
# import re
# with open ('new.txt',  encoding='utf8') as f:
#     for i in f.readlines():
#         new_data = i.split(',')
#         for j in new_data:
#             match = re.findall("(\d{3}-\d{3}-\d{4})", j)
#             if match != []:
#                 print(match)

# texts = "[2,\"ZZrAF8NU8Q1EQgaH3QoO-g\"],[2,2,null,[]],null,null,[[[2],[[null,null,42.072765185403675,-87.80330755664644],null,[90.48921,89.644424,0.9596588]]]],[3,null,null,[2],null,[null,null,\"launch\",[6]]]],2,null,null,null,null,null,null,[\"-8642471209781622411\",\"2890770310057047536\"],null,\"8GLOHGVBVBs\"]],null,null,null,null,null,null,0,1]]],null,null,[\"https://www.google.com/search?q\\u003dlocal+guide+program\\u0026ibp\\u003dgwp;0,26,OjAKLiIqQ29yZVBvd2VyIFlvZ2EgR2xlbnZpZXcsIElMLCBVbml0ZWQgU3RhdGVzKAI\\u0026pcl\\u003dlp\"],null,null,null,[[\"+1 847-453-9544\",[[\"(847) 453-9544\",1],[\"+1 847-453-9544\",2]],null,\"+18474539544\",null,[\"tel:+18474539544\",null,null,\"0ahUKEwiXtcbH4LjzAhUHeisKHcwbCPEQ_doBCB8oDg\"]]],null,null,[null,null,null,null,null,\"7421483639411054488\",\"105696988201694077611\"],null,[[[7,[[\"CorePower Yoga\"],[\"1819 Glenview Rd\"],[\"Glenview, IL 60025\"],[\"United States\"]]],[2,[[\"CorePower Yoga, 1819 Glenview Rd, Glenview, IL 60025, United States\"]]],[1,[[\"1819 Glenview Rd, Glenview, IL 60025, United States\"]]],[4,[[\"Glenview, IL, United States\"]]]],[null,\"1819 Glenview Rd\",\"1819 Glenview Rd\",\"Glenview\",\"60025\",\"Illinois\",\"US\"],[\"0ahUKEwiXtcbH4LjzAhUHeisKHcwbCPEQqtMBCBsoCg\",[\"86JJ35FW+2M\"],[\"35FW+2M Glenview, Illinois, USA\"],3]],"

# soup = bs4.BeautifulSoup(response.content, "html5lib")   
# phone_no = soup.find('div', {'id': 'pane'})
# # phone_no = soup.find('div',{"data-item-id": "phone:tel:+18582392619"})
# print(phone_no)
# print(phone_no)

# text = re.findall("(\d{3}-\d{3}-\d{4})", texts)[0]
# print("+1 "+text)


# # res = session.get("https://www.google.com/maps/place/CorePower+Yoga/@42.072598,-87.8054775,17z/data=!3m1!4b1!4m5!3m4!1s0x0:0x281e1447f23235f0!8m2!3d42.0726213!4d-87.8033126")  
# # print("The object type:",type(res))  

# # soup = bs4.BeautifulSoup(res.content,'html.parser')  
# # phone_no = soup.find('div', {'class': 'QSFF4-text gm2-body-2'}).text


# # ph_no=soup.find('div',class_='QSFF4-text gm2-body-2')
# # print(ph_no)




# # from selenium import webdriver
# # from selenium.webdriver.common.by import By


# # # opening the browser using driver
# # driver = webdriver.Chrome(executable_path=r"C:\Users\DEVANSH SHARMA\Desktop\chromedriver.exe")
# # driver.maximize_window()
# # driver.get("https://login.yahoo.com/")

# # # CSS_Selctor
# # # search = driver.find_element(By.CSS_SELECTOR, "#login-username")
# # # search.send_keys("Hello")


# # # # Link Text - Only used for links
# # # driver.find_element(By.LINK_TEXT, "Forgot username?").click()

# # # # PartialinkLinkText : Only for links but not recommended (For use huge link text)
# # # driver.find_element(By.PARTIAL_LINK_TEXT, "Forgot username?").click()

# # #Id and names are always unique


# # #Class name - is not unique
# # driver.find_element(By.NAME, "username").send_keys("Hello")

# from selenium import webdriver

# driver = webdriver.Chrome(executable_path=r"C:\Users\DEVANSH SHARMA\Desktop\chromedriver.exe")
# driver.maximize_window()


# url = "https://www.google.com/maps/place/Papa+John's+Pizza/@40.7936551,-74.0124687,17z/data=!3m1!4b1!4m5!3m4!1s0x89c2580eaa74451b:0x15d743e4f841e5ed!8m2!3d40.7936551!4d-74.0124687"

# driver.get(url)



# # review titles / username / Person who reviews

# review_titles = driver.find_elements_by_class_name("section-review-title")

# print([a.text for a in review_titles])

# # review text / what did they think

# review_text = driver.find_elements_by_class_name("section-review-review-content")

# print([a.text for a in review_text])