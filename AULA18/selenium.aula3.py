from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import time  # Para dar tempo à página carregar

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=chrome_options)
driver.get("https://www.python.org")


time.sleep(2)


botoes = driver.find_elements(
    By.CLASS_NAME, "flex-control-nav flex-control-paging")

elementos = driver.find_elements(By.CLASS_NAME, "slide-code")


for elemento in elementos:
    print(elemento.text)
driver.quit()
