import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait


from selenium import webdriver
import requests
import re

import os

# display = Display(visible=0, size=(800, 600))
# display.start()


def get_links(driver: WebDriver) -> list[str]:
    sub_nodes: list[WebElement] = driver.find_elements(
        by=By.CSS_SELECTOR, value='.postinfo > b')

    possible_downloads_elements: list[WebElement] = driver.find_elements(
        by=By.CSS_SELECTOR, value='.postinfo > b > div')
    possible_downloads: list[str] = list(
        map(lambda x: x.text, possible_downloads_elements))

    idx = list(map(lambda x: x.text, sub_nodes)).index('1fichier')

    links: list[str] = []
    for link_name in sub_nodes[idx+1:]:
        if link_name.text in possible_downloads:
            break
        link_url: WebElement = link_name.find_element(
            by=By.CLASS_NAME, value='btnToLink')
        links.append(link_url.get_attribute('href'))

    return links


def get_end_link(driver: WebDriver, url: str) -> str:
    driver.get(url)

    # Checks for the button to be present
    wait = WebDriverWait(driver, 60, poll_frequency=2,
                         ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
    button = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "form > center > button.btn.btn-primary")))
    button.click()

    # Checks for the link to be present
    end_link_element = wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "a > p.showURL")))
    end_link: str = end_link_element.text

    return end_link


urlRegex = re.compile(
    r"<p\s*class=\"showURL\"\s*>\s*(.*)\s*</p>")


def get_end_link2(url: str) -> str:
    left, right = url.split('?link=')

    headers = {
        'authority': 'zt-protect.cam',
        'content-length': '0',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'upgrade-insecure-requests': '1',
        'origin': 'https://zt-protect.cam',
        'content-type': 'application/x-www-form-urlencoded',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': url,
        'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7,es;q=0.6,zh-CN;q=0.5,zh;q=0.4',
        'cookie': os.getenv('COOKIE'),
    }

    params = (
        ('link', right),
    )

    response = requests.post(left,
                             headers=headers, params=params)
    if response.status_code != 200:
        print("Bad cookie probably")
        exit(-1)

    whole_page = response.text
    return urlRegex.findall(whole_page)[-1]


if __name__ == '__main__':
    if not os.getenv('COOKIE'):
        print("Env needs COOKIE=")
        exit(1)

    ser = Service("./chromedriver.exe")
    op = webdriver.ChromeOptions()

    op.add_experimental_option(
        "excludeSwitches", ["enable-logging", "enable-automation"])
    op.add_experimental_option('useAutomationExtension', False)
    op.add_argument("--disable-blink-features=AutomationControlled")
    op.add_argument("--disable-blink-features")
    # op.add_argument("--headless")
    op.add_argument("--disable-dev-shm-usage")
    op.add_argument('--ignore-certificate-errors')
    op.add_argument("--incognito")
    op.add_argument("--no-sandbox")

    op.add_argument("--log-level=3")

    driver = webdriver.Chrome(service=ser, options=op)
    driver.get(
        'https://www.zone-telechargement.cam/telecharger-serie/25512-my-hero-academia-saison-02-vostfr-hd-1080p.html')

    page_links = get_links(driver)
    print('\n\n\n\nLiens:')
    for l in page_links:
        end_link = get_end_link2(l)
        print(end_link)

    time.sleep(2)

    # links = get_links(driver)
