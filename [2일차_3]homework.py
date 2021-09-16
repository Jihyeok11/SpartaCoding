import smtplib
from bs4 import BeautifulSoup
from selenium import webdriver
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

driver = webdriver.Chrome('chromedriver')

from openpyxl import Workbook

wb = Workbook()
ws1 = wb.active
ws1.title = "articles"
ws1.append(["제목", "링크", "신문사", "썸네일"])

url = "https://search.naver.com/search.naver?&where=news&query=추석"

driver.get(url)
req = driver.page_source

soup = BeautifulSoup(req, 'html.parser')

# 1. 기사 크롤링해서 저장하기
articles = soup.select('#main_pack > section.sc_new.sp_nnews._prs_nws > div > div.group_news > ul > li')
for article in articles:
    title = article.select_one('div.news_area > a').text
    link = article.select_one('div.news_area > a')['href']
    comp = article.select_one('div.info_group > a').text
    thumbnail = article.select_one('div.news_wrap > a > img')['src']
    ws1.append([title, link, comp, thumbnail])

wb.save(filename='articles.xlsx')
driver.quit()

# 2. 기사를 이메일로 보내기

# 보내는 사람 정보
me = "보내는 사람 이메일"
my_password = "계정 비밀번호"

# 로그인하기
s = smtplib.SMTP_SSL('smtp.gmail.com')
s.login(me, my_password)

# 받는 사람 정보 (나한테 보내는 중 )
you = "받는사람 이메일"
    
# 메일 기본 정보 설정
msg = MIMEMultipart('alternative')
msg['Subject'] = "이메일 보내기 test"
msg['From'] = me
msg['To'] = you

# 메일 내용 쓰기
content = "이것은 폭탄입니다?"
part2 = MIMEText(content, 'plain')
msg.attach(part2)

# 파일 첨부하기
part = MIMEBase('application', "octet-stream")
# 전시간에 만든 articles.xlsx를 보내보자
with open("articles.xlsx", 'rb') as file:
    part.set_payload(file.read())
encoders.encode_base64(part)
# 추석기사.xlsx를 첨부한다는 뜻
part.add_header('Content-Disposition', "attachment", filename="추석기사.xlsx")
msg.attach(part)

# 메일 보내고 서버 끄기
s.sendmail(me, you, msg.as_string())
s.quit()