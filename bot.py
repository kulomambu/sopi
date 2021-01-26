import time
import datetime
import pyfiglet as f
import undetected_chromedriver as UC
import pickle
import account as ac

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
from fake_useragent import UserAgent

UC.TARGET_VERSION = 87 # You can change your chrome version target

options = UC.ChromeOptions()
hl = input("Headless / Normal")
if hl == "Headless":
    options.headless = True
    options.add_argument("--headless")
else:
    options.headless = True
    options.add_argument("start-maximized")
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
options.add_argument('--disable-extensions')
# Some WEBSITE dont accept random version of user agent, make sure your choice
# Sorry for my bad english hehe
# ua = UserAgent()
# userAgent = ua.random
# print(userAgent)
# options.add_argument(f'user-agent={userAgent}')
prefs = {"profile.default_content_setting_values.notifications": 2, "credentials_enable_service": False, "profile.password_manager_enabled" : False}
options.add_experimental_option("prefs", prefs)
browser = UC.Chrome(options=options, enable_console_log=True)

def authors():
    style = f.figlet_format("RAYYYYYYYY")
    print(style)

def load_cookies():
    browser.get("https://shopee.co.id")
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        browser.add_cookie(cookie)

def tombol_beli():
    try:
        #beli = WebDriverWait(browser, 60).until(EC.element_to_be_clickable((
            #By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[5]/div/div/button[2]')))
        #browser.execute_script("arguments[0].click();", beli)
        #print("- Barang terbeli!")
        #print(datetime.datetime.now().microsecond)
        # iframe = WebDriverWait(browser, 60).until(EC.frame_to_be_available_and_switch_to_it((
        #        By.XPATH, '# //*[@id="main"]/div/div[2]/div[2]')))
        beli = WebDriverWait(browser, 60).until(EC.element_to_be_clickable((
            By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[5]/div/div/button[2]')))
        browser.execute_script("arguments[0].click();", beli)
        print("- Barang telah di masukan ke keranjang!")
        checkout = WebDriverWait(browser, 60).until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, '.shopee-button-solid')))
        browser.execute_script("arguments[0].click();", checkout)
        print("- Barang telah tercheckout!")
        Metodetransfer = WebDriverWait(browser, 60).until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, '.checkout-payment-setting__payment-methods-tab > span:nth-child(2) > button:nth-child(1)')))
        browser.execute_script("arguments[0].click();", Metodetransfer)
        print("- Metodetransfer!")
        TransferByBCA = WebDriverWait(browser, 60).until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, '#main > div > div._1Bj1VS > div.page-checkout.container > div.page-checkout__payment-order-wrapper > div.checkout-payment-method-view > div > div.checkout-payment-setting__payment-method-options > div:nth-child(1) > div.bank-transfer-category__body > div:nth-child(3) > div > div.stardust-radio-button > div')))
        browser.execute_script("arguments[0].click();", TransferByBCA)
        print("- TransferByBCA!")
        pesanan = WebDriverWait(browser, 60).until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, '.stardust-button')))
        browser.execute_script("arguments[0].click();", pesanan)
        print("- Barang terpesan, Siap di bayar !!!")
        bayar = WebDriverWait(browser, 60).until(EC.element_to_be_clickable((
            By.ID, 'pay-button'))).click()
        browser.execute_script("arguments[0].click();", bayar)
        print("- Barang terbayar!")
        pin_shopee = WebDriverWait(browser, 60).until(EC.element_to_be_clickable((
            By.XPATH, '//*[@id="pin-popup"]/div[1]/div[3]/div[1]')))
        browser.execute_script("arguments[0].click();", pin_shopee)
        pin_shopee.send_keys(ac.pin_number)
    except NoSuchElementException as e:
        print(e)


def main():
    minute = datetime.datetime.now().minute
    authors()
    time.sleep(0)
    load_cookies()
    # Input product link
    link_produk = input("Masukan link produk : ")
    browser.get(link_produk)
    # Input your flash sale minute
    menit = int(input("Masukan menit untuk memulai beli : "))

    # This is my masterpiece logic piece of shit
    # Ini countdown buat nentuin menit beli
    while minute != menit:
        minute = datetime.datetime.now().minute
    
    browser.refresh()
    tombol_beli()

if __name__ == "__main__":
    main()
