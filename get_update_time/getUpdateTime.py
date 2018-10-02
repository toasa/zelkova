import sys
sys.path.append('..')
import func
from datasets import member_const

name = sys.argv[1]
names = member_const.names

if name not in names:
    print("[USAGE]: python3 func.py NAME_OF_MEMBER")
else:
    print(func.get(name))
