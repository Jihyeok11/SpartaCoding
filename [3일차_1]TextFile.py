f = open("test.txt", "w", encoding="utf-8")

for i in range(10):
    f.write(f"안녕, {i}번째 저장\n")
f.write("안녕, 스파르타!\n ")
f.close()


with open("test.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        print(line)