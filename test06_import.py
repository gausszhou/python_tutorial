import time
import requests

print("start")
time.sleep(2)
print("finish")

r = requests.get('https://www.gausszhou.top')
print(r.content)