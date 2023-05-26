from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

desired_caps = {
    "deviceName": "Galaxy S23",
    "platformName": "Android",
    "platformVersion": "13",
    "app": "lt://APP10160591891685028695220393",  # Enter app_url here
    "isRealMobile": True,
    "build": "Python Vanilla Android",
    "name": "Sample Test - Python",
    "network": False,
    "visual": True,
    "video": True
}


def startingTest():
    if os.environ.get("LT_USERNAME") is None:
        # Enter LT username here if environment variables have not been added
        username = "sandhyas"
    else:
        username = os.environ.get("LT_USERNAME")
    if os.environ.get("LT_ACCESS_KEY") is None:
        # Enter LT accesskey here if environment variables have not been added
        accesskey = "6honM8azteHGSod0hN9273gFT36Tl5dKJfVdxzySqDhUNkRrcs"
    else:
        accesskey = os.environ.get("LT_ACCESS_KEY")

    try:
        driver = webdriver.Remote(desired_capabilities=desired_caps, command_executor="https://" +
                                  username+":"+accesskey+"@mobile-hub.lambdatest.com/wd/hub")
        clkElement = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (MobileBy.ID, "com.handycloset.android.jpegpng:id/loadButton")))
        clkElement.click()

        perElement = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.drawerlayout.widget.DrawerLayout/android.widget.ScrollView/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView")))
        perElement.click()

        clkElement = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (MobileBy.ID, "com.handycloset.android.jpegpng:id/loadButton")))
        clkElement.click()

        clkElement = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (MobileBy.ID, "com.handycloset.android.jpegpng:id/loadButton")))
        clkElement.click()
        time.sleep(5)

        
         # Push a file
        dest_path = 'C://Users//sandhyas//Pictures//Screenshots//pierre.png'
        driver.push_file(dest_path, 'Hello World'.encode("utf-8"))
    
        # Pull a file
        file_base64 = driver.pull_file(dest_path)
        driver.back()
        driver.quit()
    except:
        driver.quit()


startingTest()