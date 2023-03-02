import requests
from base64 import b64encode
from hashlib import md5
import time
from random import randint

phone = "邮箱或手机号"
password = "密码"
step = randint(10000, 20000) # 步数范围
time = int(time.time())
key = md5(b64encode(f"{phone}1{password}2{step}xjdsb{time}".encode('utf-8'))).hexdigest()



url = "https://api.shuabu.net/apix/xm.php"

headers = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "origin": "https://shuabu.net",
        "referer": "https://shuabu.net/",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

data = {
    "time": time,
    "phone": phone,
    "password": password,
    "step": step,
    "key": key,
}

print("data:", data)
res = requests.post(url=url, headers=headers, data=data)

if res.json()["code"] == 200: 
    print(res.json()["msg"])
    # {"code":200,"msg":"同步成功"}
else:
    print(res.text)