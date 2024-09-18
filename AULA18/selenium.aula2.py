from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import time  # Importando time para usar sleep, se necessário

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=chrome_options)

driver.get("https://www.python.org")

search = driver.find_element(By.ID, "id-search-field")
search.send_keys("Selenium")

# Clicando no botão de busca
search.submit()  # Alternativa ao find_element e click

# Esperar a página carregar (pode ser necessário)
time.sleep(2)  # Use WebDriverWait para uma abordagem mais robusta

resultado = driver.find_element(
    By.XPATH, '//*[@id="content"]/div/section/form/ul/li[1]/h3/a')

print(resultado.text)  # Imprimindo o texto do resultado

driver.quit()
