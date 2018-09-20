import csv

name = "kobayashi"
path = "./blogs/" + name + "/blogs.csv"

csv_file = open(path, "r", encoding="utf_8", errors="", newline="" )

f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n",\
 quotechar='"', skipinitialspace=True)

#header =  ['date', 'title', 'blog']
header = next(f)
print(header)
for row in f:
    # 各rowは['date', 'title', 'blog']を格納したリスト
    print(row)
