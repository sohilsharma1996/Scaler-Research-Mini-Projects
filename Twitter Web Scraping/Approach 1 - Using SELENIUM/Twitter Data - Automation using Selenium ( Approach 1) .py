# IMPORT DEPENDENCIES

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

PATH = "C:/Users/ehhosas/.wdm/drivers/chromedriver/win32/106.0.5249.61/chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://twitter.com/Login")

subject = "Elon Musk"

# SETUP THE LOGIN

sleep(5)
username = driver.find_element(By.XPATH,"//input[@name='text']")
username.send_keys("SOHILSH73354720")
next_button = driver.find_element(By.XPATH,"//span[contains(text(),'Next')]")
next_button.click()

sleep(5)
password = driver.find_element(By.XPATH,"//input[@name='password']")
password.send_keys("Lock@123")
log_in = driver.find_element(By.XPATH,"//span[contains(text(),'Log in')]")
log_in.click()

# SEARCH ITEMS AND FETCH IT

sleep(5)
search_box = driver.find_element(By.XPATH,"//input[@data-testid='SearchBox_Search_Input']")
search_box.send_keys(subject)
search_box.send_keys(Keys.ENTER)

sleep(5)
people = driver.find_element(By.XPATH,"//span[contains(text(),'People')]")
people.click()

sleep(5)
profile = driver.find_element(By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[3]/div/section/div/div/div[1]/div/div/div/div/div[2]/div[1]/div[1]/div/div[1]/a/div/div[1]/span/span")
profile.click()

# UserTag = driver.find_element(By.XPATH,"//div[@data-testid = 'User-Names']").text
# TimeStamp = driver.find_element(By.XPATH,"//time").get_attribute('datetime')
# Tweet = driver.find_element(By.XPATH,"//div[@data-testid='tweetText']").text
# Reply = driver.find_element(By.XPATH,"//div[@data-testid='reply']").text
# reTweet = driver.find_element(By.XPATH,"//div[@data-testid='retweet']").text
# Like = driver.find_element(By.XPATH,"//div[@data-testid='like']").text

UserTags = []
TimeStamps = []
Tweets = []
Replies = []
reTweets = []
Likes = []

# articles = driver.find_elements(By.XPATH,"//article[@data-testid = 'tweet']")

while True :
    articles = driver.find_elements(By.XPATH,"//article[@data-testid = 'tweet']")
    for article in articles:
        UserTag = driver.find_element(By.XPATH,".//div[@data-testid = 'User-Names']").text
        UserTags.append(UserTag)

        TimeStamp = driver.find_element(By.XPATH,".//time").get_attribute('datetime')
        TimeStamps.append(TimeStamp)

        Tweet = driver.find_element(By.XPATH,".//div[@data-testid='tweetText']").text
        Tweets.append(Tweet)

        Reply = driver.find_element(By.XPATH,".//div[@data-testid='reply']").text
        Replies.append(Reply)

        reTweet = driver.find_element(By.XPATH,".//div[@data-testid='retweet']").text
        reTweets.append(reTweet)

        Like = driver.find_element(By.XPATH,".//div[@data-testid='like']").text
        Likes.append(Like)

    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    sleep(1)
    # articles = driver.find_elements(By.XPATH,"//article[@data-testid = 'tweet']")
    Tweets2 = list(set(Tweets))

    print(Tweets2)
    print(len(Tweets2))

    if len(Tweets2) > 5000:
        break

import pandas as pd

df = pd.DataFrame(zip(UserTags , TimeStamps , Tweets , Replies , reTweets , Likes),
columns = ['UserTags' , 'TimeStamps' , 'Tweets' , 'Replies' , 'reTweets' , 'Likes'])

# df = df.remove_duplicates()

df.to_excel('Elon_Musk_5000_Tweets.xlsx',index = False)

# import os
# os.system('start' "excel" "Elon Musk 5000 Tweets.xlsx")
# Increase count to 5k
# Remove Duplicates

