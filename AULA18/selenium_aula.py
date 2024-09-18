from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=chrome_options)

driver.get("https://www.python.org")

elements = driver.find_elements(By.CSS_SELECTOR, "shrubbery")

for element in elements:
    element_date = element.find_element(By.TAG_NAME, 'time').text
    element_name = element.find_element(By.TAG_NAME, 'a').text
    element_link = element.find_element(By.TAG_NAME, 'a').get_attribute('href')
    print(f"{element_date}, {element_name}, {element_link} ")

driver.quit()
