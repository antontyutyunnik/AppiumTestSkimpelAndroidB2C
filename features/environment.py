import time
from appium import webdriver
from app.application import Application


def before_scenario(context, scenario):
    desired_capabilities = {
        "platformName": "Android",
        "platformVersion": "10",
        "deviceName": "Xiaomi M2006C3MNG",
        # "app": "/Users/anton/Downloads/app-release7.apk",
        "app": "/Users/anton/Build/app-release7.apk",
        "appPackage": "com.skimpel.business",
        "appActivity": "com.skimpel.business.MainActivity"
    }

    context.driver = webdriver.Remote('http://127.0.0.1:8200/wd/hub', desired_capabilities=desired_capabilities)
    context.driver.implicitly_wait(5)
    context.app = Application(context.driver)


def after_scenario(context, scenario):
    time.sleep(3)
    context.driver.quit()