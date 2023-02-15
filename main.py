from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
import time

INSTAGRAM_EMAIL = "pythoncoderoom@gmail.com"
INSTAGRAM_PASSWORD = "lsr211425"
INSTAGRAM_USERNAME = "pythoncoderoom"
SIMILAR_ACCOUNT = "python.hub"


class InstaFollower:

    def __init__(self):
        self.chrome_driver = Service("/Applications/chromedriver")
        self.driver = webdriver.Chrome(service=self.chrome_driver)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")

        time.sleep(3)
        username = self.driver.find_element(By.NAME, "username")
        username.send_keys(INSTAGRAM_EMAIL)
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(INSTAGRAM_PASSWORD)
        login = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        login.click()

        time.sleep(3)
        dismiss_save = self.driver.find_element(By.CSS_SELECTOR, ".cmbtv button")
        dismiss_save.click()

        time.sleep(3)
        dismiss_notification = self.driver.find_element(By.CSS_SELECTOR, "._a9--._a9_1")
        dismiss_notification.click()

    def find_followers(self):
        time.sleep(3)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/")

        time.sleep(3)
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "followers").click()

        time.sleep(3)
        modal = self.driver.find_element(By.CLASS_NAME, "_aano")

        for x in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(3)

    def follow(self):
        follow_button = self.driver.find_elements(By.CLASS_NAME, "_acan._acap._acas")
        for x in follow_button:
            time.sleep(3)

            try:
                x.click()

            except ElementClickInterceptedException:
                time.sleep(3)
                dismiss_unfollow = self.driver.find_element(By.CLASS_NAME, "_a9--._a9_1")
                dismiss_unfollow.click()


bot = InstaFollower()

bot.login()
bot.find_followers()
bot.follow()

time.sleep(10)
bot.driver.quit()
