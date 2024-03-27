from colorama import Fore, Style
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import re
import sys


def scrape_twitter_user(username):
    user_cashTag = []
    pattern = r'\$[A-Za-z]+\s*[^\$]*'
    sys.stdout.reconfigure(encoding='utf-8')
    
    # using chrome driver to simulate user browsing
    driver = './chromedriver-win64/chromedriver.exe'
    service = Service(driver)

    chrome_options = Options()
    # running chrome in the background if needed to show the chrome window just comment the two lines
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')

    driver = webdriver.Chrome(service=service, options=chrome_options)


    baseUrl = 'https://twitter.com/'
    driver.get(f'{baseUrl}{username}')
    sleep(5)
    try:
        # testing if the user is valid
        driver.find_element(By.XPATH,'//div[@data-testid="empty_state_header_text"]')
        print(Fore.RED,'Invalid user:', username)
        print(Style.RESET_ALL)
        return
    except NoSuchElementException:
        pass
    height = 0
    for _ in range(4):
        driver.execute_script(f'window.scrollTo({height}, 20000);')
        height+=20000
        sleep(3)

    # tracking the element containing the cashTag
    elements = driver.find_elements(By.XPATH,'//div[@data-testid="tweetText"]//span[@class="r-18u37iz"]//a')

    for element in elements:
        cashTag = re.findall(pattern,element.text)
        if(len(cashTag)>0):
            cashTag = cashTag[0].upper()
            print(cashTag)
        if isinstance(cashTag, str):
            user_cashTag.append(cashTag)
    return user_cashTag









# //div[@data-testid="tweetText"]



# driver.quit()



