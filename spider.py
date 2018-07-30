from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from two import *


class Action():
    def __init__(self):
        self.desired_caps = {
            "platformName": "Android",
            "deviceName": "SM_G9500",
            "appPackage": "com.luojilab.player",
            "appActivity": "com.luojilab.business.welcome.WelcomeActivity",
            "noReset": True
        }
        self.driver = webdriver.Remote(DRIVER_SERVER, self.desired_caps)
        self.wait = WebDriverWait(self.driver, TIMEOUT)

    def entry(self):
        ebook = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@resource-id="com.luojilab.player:id/classImageView"]')))
        ebook[3].click()
        while True:
            self.driver.swipe(FLICK_START_X, FLICK_START_Y+FLICK_DISTANCE, FLICK_START_X, FLICK_START_Y)
            sleep(SCROLL_SLEEP_TIME)

if __name__ == '__main__':
    action = Action()
    action.entry()





