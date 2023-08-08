# 姓名：郭宏亮
# 时间：2023/8/8 21:50
import requests

url = "http://127.0.0.1:5000/"
url_token = "http://127.0.0.1:8866/api/login"
url_get_user_info = "http://127.0.0.1:8866/api/getUserInfo"
data = {
    "username": "zz",
    "password": "123456"
}


def test_post():
    response = requests.post(url=url, json=data)
    print(response.text)


def test_get():
    response = requests.get(url=url, params=data)
    print(response.text)


def test_login():
    response = requests.post(url=url_token, json=data)
    print(response.json())
    print(type(response.json()))


def test_get_user_info():
    login = requests.post(url=url_token, json=data)
    token = login.json().get("token")
    print("token", token)
    response = requests.get(url=url_get_user_info, headers={"token": token})
    print(response.json())
    print(type(response.json()))
