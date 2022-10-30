# Login details
username = ""
password = ""

# Config options
waitTimeBetweenLetters = 0.001
do_random_shit = True
min_random_add_wait = 0.05
max_random_add_wait = 0.15
loadWait = 5
mistake_percentage = 0.005



from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from random import randrange, random
from time import sleep

url = "https://at4.typewriter.at"


def get_random_pause():
    if do_random_shit:
        return randrange(int(min_random_add_wait*1000), int(max_random_add_wait*1000))/1000
    return 0

def is_mistake():
    return random() < mistake_percentage

# Open website
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get(url)
sleep(loadWait)

# Do login
driver.find_element(By.ID, "LoginForm_username").send_keys(username)
driver.find_element(By.ID, "LoginForm_pw").send_keys(password)
driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[1]/form/div[3]/input").click()
sleep(loadWait)
# Start thing
driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[1]/div[1]/a").click()
sleep(loadWait)
driver.find_element(By.XPATH, "/html/body/div[6]/div[3]/div/button").click()
sleep(0.25)
# Do letter loop
while True:
    try:
        # Find the current letter
        currentLetter = driver.find_element(By.ID, "actualLetter").get_attribute('innerHTML')
        try:
            remainingText = driver.find_element(By.ID, "remainingText").get_attribute('innerHTML')
        except:
            remainingText = ""
        
    except:
        print("No more text found")
        break
    if remainingText == "":
        break
    to_type = currentLetter+remainingText
    to_type = to_type.replace("&nbsp;", " ")
    to_type = to_type.replace(" ", Keys.SPACE)
    
    actions = ActionChains(driver)
    for i in range(len(to_type)):
        if is_mistake():
            if i == 0 or len(to_type) < 2: idx = 1 
            else: idx = 0
            actions.send_keys(to_type[0])\
                .pause(waitTimeBetweenLetters+get_random_pause())
        
        actions.send_keys(to_type[i])\
            .pause(waitTimeBetweenLetters+get_random_pause())
    
    actions.perform()
