import urllib3
from datetime import datetime
from bs4 import BeautifulSoup
import sys
sys.path.append('..')
from datasets import member_const

# nameを指定. ex. name="kobayashi"
def get(name):
    url = "http://www.keyakizaka46.com/s/k46o/diary/member?ima=0000"

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

    # first, last
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

    return member_update_time[member_const.name_to_id[name]]
