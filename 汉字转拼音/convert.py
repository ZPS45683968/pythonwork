from xpinyin import Pinyin
import csv
f1 = open('name2.csv', 'w', newline='')
writer = csv.writer(f1)
f2 = open("name.csv", "r")
reader = csv.reader(f2)

for row in reader:
    p = Pinyin()
    result = p.get_pinyin(row[0])
    name = result.replace('-', ' ')
    writer.writerow([result,name])