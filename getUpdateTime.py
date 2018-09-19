import urllib3
import time
from datetime import datetime
from bs4 import BeautifulSoup

# start = time.time()

url = "http://www.keyakizaka46.com/s/k46o/diary/detail/17235?ima=0000&cd=member"

# for urllib3
http = urllib3.PoolManager()
r = http.request('GET', url)

soup = BeautifulSoup(r.data, "html.parser")

script = soup.find_all("script")


for tag in script:
    try:
        if "blogUpdate" in tag.string:
            blogUpdate = tag.string
            break

    except:
        pass

# elapsed_time = time.time() - start

indexF = blogUpdate.find('[')
indexL = blogUpdate.find(']')

blogUpdate = blogUpdate[indexF+3:indexL-4]
blogUpdate = blogUpdate.replace('\n','')
updates = blogUpdate.split('},{')


member_update_time = {}
for update in updates:
    update_time = update[22: 32] + " " + update[33:38]
    d = datetime.strptime(update_time, "%Y-%m-%d %H:%M")
    member_update_time[int(update[9:11])] = d


#kobayashi
print(member_update_time[7])
#hirate
print(member_update_time[17])
