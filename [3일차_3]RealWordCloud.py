import numpy as np
from PIL import Image
from wordcloud import WordCloud

# cloud 사진 저장
# import dload
# dload.save("https://s3.ap-northeast-2.amazonaws.com/materials.spartacodingclub.kr/free/cloud.png", 'cloud.jpg')

text = ''
with open("카톡저장.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines[5:]:
        if '] [' in line:
            text += line.split('] ')[2].replace('사진\n', '').replace('https', '').replace('co','').replace('kr', '')

mask = np.array(Image.open('cloud.jpg'))
wc = WordCloud(font_path='C:\Windows\Fonts\H2GTRM.TTF', background_color="white", mask=mask)
wc.generate(text)
wc.to_file("result_masked.png")