from bs4 import BeautifulSoup
from selenium import webdriver
from openpyxl import Workbook

wb = Workbook()
ws1 = wb.active
ws1.title = "articles"
ws1.append(["제목", "링크", "신문사"])

driver = webdriver.Chrome('chromedriver')

url = "https://search.naver.com/search.naver?where=nexearch&sm=top_sug.pre&fbm=0&acr=4&acq=%EC%B6%94%EC%84%9D&qdt=0&ie=utf8&query=%EC%B6%94%EC%84%9D"

driver.get(url)
req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')
# main_pack > section.sc_new.sp_nnews._prs_nws_all > div > div.group_news > ul
# articles = soup.select('#sp_nws_all1 > div.news_wrap.api_ani_send > div')
articles = soup.select('#main_pack > section.sc_new.sp_nnews._prs_nws_all > div > div.group_news > ul > li')
for article in articles:
    title = article.select_one('div.news_area > a').text
    url = article.select_one('div.news_area > a')['href']
    # 언론사 확인하면(copy seletor)
    # sp_nws_all1 > div.news_cluster > ul > li > span > span > a
    comp = article.select_one('span > span > a').text
    ws1.append([title, url, comp])
    print(title, url, comp)
wb.save(filename="articles.xlsx")
driver.quit() 