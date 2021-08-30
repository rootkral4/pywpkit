import time
import pywpkit


def main() -> None:
    """
    Example of seleniummethod function
    """
    kit = pywpkit.wpkit(chromedriverpath=r"C\\chromedriver.exe")

    kit.seleniummethod(
        "90537xxxxxxx",
        "Selenium",
        sendnow=False
        ) # a browser window will popup and ask for qr code scan

    time.sleep(60) # wait for 1 min before sending
    kit.selenium_lock = False # send message now
