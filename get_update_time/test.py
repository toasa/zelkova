import sys
sys.path.append('..')
import getUpdateTime
from datasets import member_const

name = sys.argv[1]
names = member_const.names

if name not in names:
    print("input correct members name")
else:
    print(getUpdateTime.get(name))
