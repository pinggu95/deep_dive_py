from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_driver_path = r'C:\Users\MYNOTE\PycharmProjects\PythonProject\chromedriver-win64\chromedriver.exe'
service = Service(chrome_driver_path)
options = Options()
# options.add_argument('--headless')

driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.youtube.com/")

# 1) 검색창이 "클릭 가능(clickable)" 상태가 될 때까지 최대 10초 대기
wait = WebDriverWait(driver, 10)
search_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input#search")))

# 2) 클릭해서 포커스 맞추고
search_input.click()

# 3) 검색어 입력 + Enter
search_input.send_keys("qwer", Keys.ENTER)

# 결과 로딩 대기 후 종료
time.sleep(5)
driver.quit()
