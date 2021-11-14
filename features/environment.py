import os
from appium import webdriver


def before_scenario(context, scenario):
    desired_cap = {"deviceName": "Pixel", "platformName": "Android", "app": os.path.abspath(
        os.path.abspath
        ("D:/Загрузки/apk/white_test.apk")
    ), "appPackage": "kz.homecredit.ibank.debug", "appActivity": (
        "cz.bsc.mb.activities.prelogin.SplashScreenActivity"
    ), "newCommandTimeout": 6000}

    context.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)


def after_scenario(context, scenario):
    context.driver.quit()
