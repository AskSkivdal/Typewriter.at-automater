from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

url = "https://at4.typewriter.at"

# Login details
username = ""
password = ""

# Config options
waitTimeBetweenLetters = 0.03
loadWait = 5

# Open website
driver = webdriver.Chrome("chromedriver.exe")
driver.get(url)
sleep(loadWait)

# Do login
driver.find_element_by_id("LoginForm_username").send_keys(username)
driver.find_element_by_id("LoginForm_pw").send_keys(password)
driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/form/div[3]/input").click()
sleep(loadWait)
driver.find_element_by_xpath("/html/body/div[3]/div[3]/div[1]/div[1]/a").click()
sleep(loadWait)
driver.find_element_by_xpath("/html/body/div[6]/div[3]/div/button").click()

# Do letter loop
while True:
    # Find the current letter
    currentLetter = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[4]/div[2]/div[2]/span[1]").get_attribute('innerHTML')
    currentLetter = str(currentLetter)

    # If is nobreakspace set space
    if currentLetter == "&nbsp;":
        currentLetter = " "

    if not currentLetter.lower() in ["ö","ä","ü"]:
        print(currentLetter)
        driver.find_element_by_xpath("/html/body").send_keys(currentLetter)
    else:
        print("Manual input required!!!")
