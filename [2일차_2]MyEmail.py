import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders


# 보내는 사람 정보
me = "sorrybut75@gmail.com"
my_password = "Ajw9137648!@"

# 로그인하기
s = smtplib.SMTP_SSL('smtp.gmail.com')
s.login(me, my_password)

# 받는 사람 정보 
you = "dksud67@naver.com"

# 여러 받는 사람
emails = ['dksud67@naver.com','dksud67@naver.com']

for you in emails:
      
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