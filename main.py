import re
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
girls = ["@ani", "@authi","@sneha", "@dhiv", "@harini", "@sriva"]
boys = ["@siva", "@ct", "@dhana",  "@dins", "@gokul",  "@jas","@jel", "@karthi", "@po", "@soap","@vats","@vis"]
mass = ["@siva"]
loosu = ["@ct"] 
gays = ["@goku","@siva","@po"]
rizzler = ["@vat"]
alien = ["@dhiv"]
nigga = ["@vis"]
wolf = ["@authi"]
spirit = ["@sneha"]
blackshirt = ["@karthi"]
karadi = ["@dhana"]

flag = True
while flag:
    messages = driver.find_elements(By.XPATH, '//div[contains(@class, "message-in") or contains(@class, "message-out")]')
    last_msg = messages[-1]
    text = last_msg.text
    pattern = r"(@[a-z]+)(\((\d+)\))?"
    match = re.search(pattern, text)
    if match:
        cmd = match.group(1)
        try:
            number = int(match.group(3))
        except:
            number = 1
    else:
        number = 0

    for i in range(number):
        if cmd in ["@all"]:
            msg_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
            msg_box.click()
            for i in everyone:
                for j in i:
                    msg_box.send_keys(j)
                msg_box.send_keys(Keys.TAB)      
                msg_box.send_keys(",")
                msg_box.send_keys(" ")
            msg_box.send_keys(Keys.ENTER)      

        elif cmd in ["@boys"]:
            msg_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
            msg_box.click()
            for i in boys:
                for j in i:
                    msg_box.send_keys(j)
                msg_box.send_keys(Keys.TAB)      
                msg_box.send_keys(",")
                msg_box.send_keys(" ")
            msg_box.send_keys(Keys.ENTER)      

        elif cmd in ["@girls"]:
            msg_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
            msg_box.click()
            for i in girls:
                for j in i:
                    msg_box.send_keys(j)
                msg_box.send_keys(Keys.TAB)      
                msg_box.send_keys(",")
                msg_box.send_keys(" ")
            msg_box.send_keys(Keys.ENTER)      

        elif cmd in ["@gays"]:
            msg_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
            msg_box.click()
            for i in gays:
                for j in i:
                    msg_box.send_keys(j)
                msg_box.send_keys(Keys.TAB)      
                msg_box.send_keys(",")
                msg_box.send_keys(" ")
            msg_box.send_keys(Keys.ENTER)      

        elif cmd in ["@mass"]:
            msg_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
            msg_box.click()
            for i in mass:
                for j in i:
                    msg_box.send_keys(j)
                msg_box.send_keys(Keys.TAB)      
                msg_box.send_keys(",")
                msg_box.send_keys(" ")
            msg_box.send_keys(Keys.ENTER)      

        elif cmd in ["@loosu","@ct"]:
            msg_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
            msg_box.click()
            for i in loosu:
                for j in i:
                    msg_box.send_keys(j)
                msg_box.send_keys(Keys.TAB)      
                msg_box.send_keys(",")
                msg_box.send_keys(" ")
            msg_box.send_keys(Keys.ENTER)      
        elif cmd in ["@nigga"]:
            msg_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
            msg_box.click()
            for i in nigga:
                for j in i:
                    msg_box.send_keys(j)
                msg_box.send_keys(Keys.TAB)      
                msg_box.send_keys(",")
                msg_box.send_keys(" ")
            msg_box.send_keys(Keys.ENTER)      

        elif cmd in ["@rizzler"]:
            msg_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
            msg_box.click()
            for i in rizzler:
                for j in i:
                    msg_box.send_keys(j)
                msg_box.send_keys(Keys.TAB)      
                msg_box.send_keys(",")
                msg_box.send_keys(" ")
            msg_box.send_keys(Keys.ENTER)      

        elif cmd in ["@spirit"]:
            msg_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
            msg_box.click()
            for i in spirit:
                for j in i:
                    msg_box.send_keys(j)
                msg_box.send_keys(Keys.TAB)      
                msg_box.send_keys(",")
                msg_box.send_keys(" ")
            msg_box.send_keys(Keys.ENTER)      

        elif cmd in ["@alien"] or "@gokul" in text.lower():
            msg_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
            msg_box.click()
            for i in alien:
                for j in i:
                    msg_box.send_keys(j)
                msg_box.send_keys(Keys.TAB)      
                msg_box.send_keys(",")
                msg_box.send_keys(" ")
            msg_box.send_keys(Keys.ENTER)      

        elif cmd in ["@wolf"]:
            msg_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
            msg_box.click()
            for i in wolf:
                for j in i:
                    msg_box.send_keys(j)
                msg_box.send_keys(Keys.TAB)      
                msg_box.send_keys(",")
                msg_box.send_keys(" ")
            msg_box.send_keys(Keys.ENTER)      

        elif cmd in ["@blackshirt"]:
            msg_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
            msg_box.click()
            for i in blackshirt:
                for j in i:
                    msg_box.send_keys(j)
                msg_box.send_keys(Keys.TAB)      
                msg_box.send_keys(",")
                msg_box.send_keys(" ")
            msg_box.send_keys(Keys.ENTER)      

        elif cmd in ["@karadi"]:
            msg_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
            msg_box.click()
            for i in karadi:
                for j in i:
                    msg_box.send_keys(j)
                msg_box.send_keys(Keys.TAB)      
                msg_box.send_keys(",")
                msg_box.send_keys(" ")
            msg_box.send_keys(Keys.ENTER)      


        print(f"Command: {cmd}, Number: {number}")
    time.sleep(0.25)

