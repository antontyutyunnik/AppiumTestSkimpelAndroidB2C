import time
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import Page


class LoginPage(Page):
    WIDGET_TEXTVIEW = (By.CLASS_NAME, 'android.widget.TextView')
    WIDGET_EDITTEXT = (By.CLASS_NAME, 'android.widget.EditText')