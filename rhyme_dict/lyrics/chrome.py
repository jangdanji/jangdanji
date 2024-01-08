from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
import subprocess
import shutil
import time

def startchrome():

    try:
        time.sleep(3)
        shutil.rmtree(r"c:\\chrometemp")  #쿠키 / 캐쉬파일 삭제
    except FileNotFoundError:
        pass
    except:
        print('permission error')
        print('permission error')
        print('permission error')

    subprocess.Popen(r'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\\chrometemp"') # 디버거 크롬 구동

    option = Options()
    option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    option.add_argument("--blink-setting=imagesEnable=false")
    
    # # 사용자 크롬 (subprocess 지우고)
    # option.add_argument('--profile-directory=Profile 1')
    # option.add_argument("user-data-dir=C:\\Users\\NADANN\\AppData\\Local\\Google\\Chrome\\User Data\\") #Path to your chrome profile

    chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
    try:
        dv = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
    except:
        chromedriver_autoinstaller.install(True)
        dv = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)

    dv.implicitly_wait(10)

    return dv


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


# wait = WebDriverWait(dv, 10)
# element = wait.until(EC.element_to_be_clickable((By.ID, 'someid')))