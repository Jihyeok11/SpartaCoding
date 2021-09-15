from bs4 import BeautifulSoup
from selenium import webdriver
import time, dload

driver = webdriver.Chrome('chromedriver')
driver.get("https://www.google.com/search?q=%EC%97%90%EC%8A%A4%ED%8C%8C+%EC%9C%88%ED%84%B0&tbm=isch&ved=2ahUKEwjJxvmX64DzAhUG8ZQKHYxjDpQQ2-cCegQIABAA&oq=%EC%97%90%EC%8A%A4%ED%8C%8C+%EC%9C%88%ED%84%B0&gs_lcp=CgNpbWcQAzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6CAgAEIAEELEDOgsIABCABBCxAxCDAVC06gRYnvQEYJX1BGgCcAB4AYABogGIAZwKkgEEMTAuM5gBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=3NNBYcnoGobi0wSMx7mgCQ&bih=762&biw=1474") # 여기에 URL을 넣어주세요
time.sleep(5)

req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')
thumbnails = soup.select("#islrg > div.islrc > div > a.wXeWr.islib.nfEiy > div.bRMDJf.islir > img")
i = 0
for thumbnail in thumbnails:
    try:
        img = thumbnail['src']
        if img[:5] == "https":
            dload.save(img, f'imgs_homework/{i}.jpg')
            i += 1
    except:
        pass

driver.quit() # 끝나면 닫아주기