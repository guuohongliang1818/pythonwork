# 姓名：郭宏亮
# 时间：2023/8/8 21:31
import requests

url = "http://127.0.0.1:5000/zz"

# 通过get方法访问对象

response = requests.get(url=url)
print(response)
print(response.text)

# 通过post访问方法

response1 = requests.post(url=url)
print(response1)
print(response1.text)
