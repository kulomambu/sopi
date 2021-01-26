import pickle
import undetected_chromedriver as UC
import time
import pyfiglet as f
import account as ac

from fake_useragent import UserAgent
from selenium.webdriver.support.ui import WebDriverWait as WD
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *

UC.TARGET_VERSION = 87

options = UC.ChromeOptions()
hl = input("Headless / Normal")
if hl == "Headless":
    options.headless = True
    options.add_argument("--headless")
else:
    options.headless = True
    options.add_argument("start-maximized")
options.add_argument("disable-extensions")

# Add proxy to become more invisible
server = input("Proxy / Socks5 / None : ")
if server.lower == "proxy":
    proxy = input("Masukan proxy : ")
    options.add_argument(f'--proxy-server={proxy}')
elif server.lower == "socks5":
    socks5 = input("Masukan socks5 : ")
    options.add_argument(f'--proxy-server=socks5://{socks5}')
else:
    pass
# Delete comments below if u want to be more undetected
# Reminder : not all website can be accessed with fake useragent below, cause its randomly faking the ua. peace <3
# ua = UserAgent()
# userAgent = ua.random
# print(userAgent)
# options.add_argument(f'user-agent={userAgent}')
prefs = {"profile.default_content_setting_values.notifications": 2, "credentials_enable_service": False, "profile.password_manager_enabled" : False}
options.add_experimental_option("prefs", prefs)
browser = UC.Chrome(options=options, enable_console_log=True)
browser.get("https://shopee.co.id")

def authors():
    style = f.figlet_format("Palli V1.0")
    print(style)

def login(number, password):
    try:
        click_login = WD(browser, 60).until(EC.element_to_be_clickable((
            By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/div/div[1]/div/ul/a[2]')))
        browser.execute_script("arguments[0].click();", click_login)
    except NoSuchElementException as a:
        print(a)
    time.sleep(5)
    try:
        number_input = WD(browser, 60).until(EC.element_to_be_clickable((
            By.NAME, 'loginKey')))
        browser.execute_script("arguments[0].click();", number_input)
        number_input.clear()
        number_input.send_keys(number)
        pass_input = WD(browser, 60).until(EC.element_to_be_clickable((
            By.NAME, 'password')))
        browser.execute_script("arguments[0].click();", pass_input)
        pass_input.clear()
        pass_input.send_keys(password)
        enter = WD(browser, 60).until(EC.element_to_be_clickable((
            By.XPATH, '//*[@id="main"]/div/div[2]/div/div/form/div/div[2]/button')))
        browser.execute_script("arguments[0].click();", enter)
    except NoSuchElementException as e:
        print(e)

    time.sleep(10)

def verif():
    try:
        click_login_button = WD(browser, 60).until(EC.element_to_be_clickable((
                By.XPATH, '/html/body/div[2]/aside/div[1]/div/div[2]/button[2]')))
        browser.execute_script("arguments[0].click();", click_login_button)
        time.sleep(10)
        print("Do it manually!")
        verif_input = WD(browser,60).until(EC.element_to_be_clickable((
                By.XPATH, '/html/body/div[1]/div/div[2]/div/div/form/div/div[2]/div[3]/input[2]')))
        browser.execute_script("arguments[0].click();", verif_input)
        verif_nomor = int(input("\nMasukan kode verifikasi : "))
        time.sleep(3)
        verif_input.send_keys(verif_nomor)
        logg = WD(browser, 60).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/form/div/div[2]/button')))
        browser.execute_script("arguments[0].click();", logg)
        print("Berhasil login!")
    except NoSuchElementException as e:
        print(e)
        print("Cari sendiri y elementnya kalo pop up ini muncul hehe")
    time.sleep(20)

def main():
    authors()
    time.sleep(10)
    login(ac.email_phone_number, ac.passwd)
    verif()
    pickle.dump(browser.get_cookies(), open("cookies.pkl", "wb"))

if __name__ == "__main__":
    main()
    time.sleep(10)
    browser.quit()
