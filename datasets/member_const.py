name_to_id = {}
id_to_name = {}

names = ["ishimori", "imaizumi", "uemura", "ozeki", "oda", "koike", \
"kobayashi", "saitou_f", "satou", "shida", "sugai", "suzumoto", "nagasawa",\
"habu", "harada_a", "harada_m", "hirate", "moriya", "yonetani", "watanabe_rik",\
"watanabe_ris", "nagahama", "iguchi", "ushio", "kakizaki", "kageyama", "katou",\
"saitou_k", "sasaki_k", "sasaki_m", "takase", "takamoto", "higashimura", \
"kanemura", "kawata", "kosaka", "tomita", "nibu", "hamagishi", "matsuda", \
"miyata", "watanabe_m"]


name_to_id = {'ishimori': 1, 'imaizumi': 2, 'uemura': 3, 'ozeki': 4, 'oda': 5, 'koike': 6, \
'kobayashi': 7, 'saitou_f': 8, 'satou': 9, 'shida': 10, 'sugai': 11, \
'suzumoto': 12, 'nagasawa': 13, 'habu': 14, 'harada_a': 15, 'harada_m': 16, \
'hirate': 17, 'moriya': 18, 'yonetani': 19, 'watanabe_rik': 20, \
'watanabe_ris': 21, 'nagahama': 22, 'iguchi': 23, 'ushio': 24, \
'kakizaki': 25, 'kageyama': 26, 'katou': 27, 'saitou_k': 28, 'sasaki_k': 29, \
'sasaki_m': 30, 'takase': 31, 'takamoto': 32, 'higashimura': 33, \
'kanemura': 34, 'kawata': 35, 'kosaka': 36, 'tomita': 37, 'nibu': 38, \
'hamagishi': 39, 'matsuda': 40, 'miyata': 41, 'watanabe_m': 42}

id_to_name = {1: 'ishimori', 2: 'imaizumi', 3: 'uemura', 4: 'ozeki', \
5: 'oda', 6: 'koike', 7: 'kobayashi', 8: 'saitou_f', 9: 'satou', \
10: 'shida', 11: 'sugai', 12: 'suzumoto', 13: 'nagasawa', 14: 'habu', \
15: 'harada_a', 16: 'harada_m', 17: 'hirate', 18: 'moriya', 19: 'yonetani', \
20: 'watanabe_rik', 21: 'watanabe_ris', 22: 'nagahama', 23: 'iguchi', \
24: 'ushio', 25: 'kakizaki', 26: 'kageyama', 27: 'katou', 28: 'saitou_k', \
29: 'sasaki_k', 30: 'sasaki_m', 31: 'takase', 32: 'takamoto', \
33: 'higashimura', 34: 'kanemura', 35: 'kawata', 36: 'kosaka', \
37: 'tomita', 38: 'nibu', 39: 'hamagishi', 40: 'matsuda', 41: 'miyata', \
42: 'watanabe_m'}



# if want update id_to_name and name_to_id, remove the below comment out
# =======================================================================
# for i in range(len(names)):
#     name_to_id[names[i]] = i+1
#
# for i in range(len(names)):
#     id_to_name[i+1] = names[i]


# ct=01 石森 虹花
# ct=02 今泉 佑唯
# ct=03 上村 莉菜
# ct=04 尾関 梨香
# ct=05 織田 奈那
# ct=06 小池 美波
# ct=07 小林 由依
# ct=08 齋藤 冬優花
# ct=09 佐藤 詩織
# ct=10 志田 愛佳
# ct=11 菅井 友香
# ct=12 鈴本 美愉
# ct=13 長沢 菜々香
# ct=14 土生 瑞穂
# ct=15 原田 葵
# # ct=16　原田 まゆ
# ct=17 平手 友梨奈
# ct=18 守屋 茜
# ct=19 米谷 奈々未
# ct=20 渡辺 梨加
# ct=21 渡邉 理佐
# ct=22 長濱 ねる
# ct=23 井口 眞緒
# ct=24 潮 紗理菜
# ct=25 柿崎 芽実
# ct=26 影山 優佳
# ct=27 加藤 史帆
# ct=28 齊藤 京子
# ct=29 佐々木 久美
# ct=30 佐々木 美玲
# ct=31 高瀬 愛奈
# ct=32 高本 彩花
# ct=33 東村 芽依
# ct=34 金村 美玖
# ct=35 河田 陽菜
# ct=36 小坂 菜緒
# ct=37 富田 鈴花
# ct=38 丹生 明里
# ct=39 濱岸 ひより
# ct=40 松田 好花
# ct=41 宮田 愛萌
# ct=42 渡邉 美穂
