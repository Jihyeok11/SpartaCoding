from wordcloud import WordCloud

text = ''
with open("카톡저장.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines[5:]:
        if '] [' in line:
            text += line.split('] ')[2].replace('사진\n', '').replace('https', '').replace('co','').replace('kr', '')
print(text)

wc = WordCloud(font_path='C:/Windows/Fonts/H2GTRM.TTF', background_color="white", width=300, height=200)
wc.generate(text)
wc.to_file("result.png")