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


from pyvirtualdisplay import Display
from selenium import webdriver

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
    """
    Open and closes the end link tabs, while retrieving it's url
    """
    window_handles: list[str] = driver.window_handles

    assert len(window_handles) == 1
    driver.execute_script(f'''window.open("{url}","_blank");''')
    driver.switch_to.window(driver.window_handles[1])

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

    driver.close()
    driver.switch_to.window(driver.window_handles[0])

    return end_link


if __name__ == '__main__':
    ser = Service("./chromedriver.exe")
    op = webdriver.ChromeOptions()

    op.add_experimental_option(
        "excludeSwitches", ["enable-logging", "enable-automation"])
    op.add_experimental_option('useAutomationExtension', False)
    op.add_argument("--disable-blink-features=AutomationControlled")
    op.add_argument("--disable-blink-features")
    # op.add_argument("--headless")
    op.add_argument("--disable-dev-shm-usage")
    op.add_argument("--no-sandbox")

    op.add_argument("--log-level=3")

    driver = webdriver.Chrome(service=ser, options=op)
    # driver.set_window_position(-10000, 0)

    driver.get(
        'https://www.zone-telechargement.cam/animes/64804-boku-no-hero-academia-4.html')

    page_links = get_links(driver)
    print('\n\n\n\nLiens:')
    for l in page_links:
        end_link = get_end_link(driver, l)
        print(end_link)

    time.sleep(2)

    # links = get_links(driver)
