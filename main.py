from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = Options()
options.add_argument("--headless")
options.add_argument("-profile")
options.add_argument("/home/akash/.mozilla/firefox/qymcnn0s.default")  # replace this

driver = webdriver.Firefox(service=Service(), options=options)
driver.get("https://web.whatsapp.com")

time.sleep(5)

group_name = "A120 4 lyf ❤️"  # replace this with actual group name
search = driver.find_element(By.XPATH, '//div[@contenteditable="true"]')
search.click()
for i in group_name:
    search.send_keys(i)
time.sleep(2)

group = driver.find_element(By.XPATH, f'//span[@title="{group_name}"]')
group.click()

everyone = ["@ani","@siva", "@ct", "@authi","@sneha","@dhana", "@dhiv", "@dins", "@gokul", "@harini", "@jas","@jel", "@karthi", "@po", "@soap","@vats","@vis", "@sriva"]
girls = ["@ani", "@authi","@sneha", "@dhiv", "@harini" "@sriva"]
boys = ["@siva", "@ct", "@dhana",  "@dins", "@gokul",  "@jas","@jel", "@karthi", "@po", "@soap","@vats","@vis"]
flag = True
while flag:
    messages = driver.find_elements(By.XPATH, '//div[contains(@class, "message-in") or contains(@class, "message-out")]')
    last_msg = messages[-1]
    text = last_msg.text
    if "@all" in text.lower():
        msg_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
        msg_box.click()
        for i in everyone:
            for j in i:
                msg_box.send_keys(j)
            msg_box.send_keys(Keys.TAB)      
            msg_box.send_keys(",")

        msg_box.send_keys(Keys.ENTER)      

    if "@boys" in text.lower():
        msg_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
        msg_box.click()
        for i in boys:
            for j in i:
                msg_box.send_keys(j)
            msg_box.send_keys(Keys.TAB)      
            msg_box.send_keys(",")
        msg_box.send_keys(Keys.ENTER)      

    if "@girls" in text.lower():
        msg_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
        msg_box.click()
        for i in girls:
            for j in i:
                msg_box.send_keys(j)
            msg_box.send_keys(Keys.TAB)      
            msg_box.send_keys(",")
        msg_box.send_keys(Keys.ENTER)      

    print("Command:",text)
    time.sleep(0.25)

