import os
import time

import chromedriver_autoinstaller
from selenium import webdriver


def get_bb_slot(url):
    chromedriver_autoinstaller.install()

    driver = webdriver.Chrome()
    driver.get(url)
    print("Please login using OTP and then wait for a while.")
    time.sleep(60)

    while 1:
        driver.get(url)
        time.sleep(2)
        print("Trying to find a slot!")
        try:
            driver.find_element_by_xpath("//button[@id = 'checkout']").click()

            time.sleep(5)
            src = driver.page_source
            if "checkout" in driver.current_url and not "Unfortunately, we do not have" in src:
                print("Found the slots!")
                for i in range(60):
                    notify("Slots Available!", "Please go and choose the slots!")
                    time.sleep(20)
        except Exception  as e:
            print("If this message pops up multiple times, please find the error and create a PR!")
            print(e)
            pass
        print("No Slots found. Will retry again.")
        time.sleep(50)


def notify(title, text):
    if os.name == 'posix':
        os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))
        os.system('say "Slots for delivery available!"')
    elif os.name == 'Linux':
        os.system('spd-say "Slots for delivery available!"')


def main():
    get_bb_slot('https://www.bigbasket.com/basket/?ver=1')


if __name__ == '__main__':
    main()
