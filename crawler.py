import argparse
import os
import random
import time

import pyautogui
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from constance import DOWNLOAD_PATH, MODE


class Browser:

    def __init__(self, download_path, mode='url'):
        chrome_options = Options()
        cwd = os.getcwd()

        prefs = {'download.default_directory': download_path}
        chrome_options.add_experimental_option('prefs', prefs)
        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])

        self.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='{}/chromedriver'.format(cwd))
        self.driver.get('https://www.remove.bg/upload')
        time.sleep(random.randint(1, 3))

        if mode == 'url':
            self.action = self.action_url
        else:
            self.action = self.action_path

    def close(self):
        self.driver.quit()
        exit()

    def action_path(self, href):
        # Click in the upload button
        self.driver.find_element_by_css_selector('.btn.btn-primary.btn-lg').click()
        # Switch to select file button
        self.driver.switch_to.active_element
        time.sleep(2)
        # Focus on the select file window
        pyautogui.write(href)
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(2)

    def action_url(self, href):
        # Click in the URL upload
        self.driver.find_element_by_css_selector('.text-muted.select-photo-url-btn').click()
        # Switch to alert url
        alert = self.driver.switch_to.alert
        time.sleep(2)
        # Focus on the select file window
        alert.send_keys(href)
        time.sleep(1)
        alert.accept()
        time.sleep(2)

    def remove_background(self, href):
        wait = WebDriverWait(self.driver, 30)
        time.sleep(1)
        self.action(href)
        try:
            # Wait for result
            wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'img[class*="transparency-grid"]')))
            time.sleep(2)
            self.driver.find_element_by_css_selector('a[href*="o.remove.bg/downloads"]').click()
            time.sleep(2)
            self.close()
        except TimeoutException:
            time.sleep(2)
            print('Time out')
            self.close()
            return


def query(href):
    print('Execute: ', href)
    try:
        browser = Browser(DOWNLOAD_PATH, mode=MODE)
        browser.remove_background(href)
    except Exception:
        print('Have error when crawler with image ', href)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Crawler remove background images')
    parser.add_argument('--href', default='')
    args = vars(parser.parse_args())
    query(args['href'])
