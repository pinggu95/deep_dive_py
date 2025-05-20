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
driver.get('http://zzzscore.com/color/')
driver.implicitly_wait(10)  # 최대 10초 대기

def analysis():
    btns = driver.find_elements(By.XPATH, '//*[@id="grid"]/div')
    colors = [b.value_of_css_property('background-color') for b in btns]
    counts = Counter(colors)

    unique_color = None
    for color, cnt in counts.items():
        if cnt == 1:
            unique_color = color
            break

    if not unique_color:
        print("정답(유일한 색상)을 찾을 수 없습니다.")
        return

    # 유일한 색상 버튼 클릭
    idx = colors.index(unique_color)
    btns[idx].click()

if __name__ == "__main__":
    start = time.time()
    while time.time() - start < 60:
        analysis()
        time.sleep(0.05)

    driver.quit()
