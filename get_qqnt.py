from requests import get
from sys import argv
from json import loads

# get plat
name = argv[1]
plat = argv[2]
args= argv[3:]
print(f"plat:{plat}")

# get link
r=get(f"https://cdn-go.cn/qq-web/im.qq.com_new/latest/rainbow/{plat}Config.js").text
r=r[r.find("params"):]
r=loads(r[r.find("{"):r.find("};")+1])
for arg in args:
    r=r[arg]
print(f"url:{r}")

with open(name, "wb") as QQ:
    for chunk in get(r, stream=True).iter_content(chunk_size=4096):
        QQ.write(chunk)
