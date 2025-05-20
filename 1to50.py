from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from collections import Counter
import time


chrome_driver_path = r'C:\Users\MYNOTE\PycharmProjects\PythonProject\chromedriver-win64\chromedriver.exe'  # 실제 chromedriver.exe 경로로 수정
chrome_options = Options()
# chrome_options.add_argument('--headless')
service = Service(executable_path=chrome_driver_path)

driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get('http://zzzscore.com/1to50')
driver.implicitly_wait(300)

num = 1

def clickBtn():
    global num
    btns = driver.find_elements(By.XPATH,'//*[@id="grid"]/div[*]')

    for btn in btns:
        print(btn.text, end='\t')
        if btn.text == str(num):
            btn.click()
            print(True)
            num += 1
            return

while num<=50:
    clickBtn()
