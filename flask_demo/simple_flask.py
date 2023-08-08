# 姓名：郭宏亮
# 时间：2023/8/8 20:38
from flask import Flask, request, jsonify

# 创建一个flask实例

app = Flask(__name__)

app.config["JSON_AS_ASCII"] = False


# 路由系统生成
@app.route("/zz", methods=["get", "post"])
def first_flask():
    return "hello flask"


@app.route("/", methods=["GET", "POST"])
def request_flask():
    # 注意，接下来用到的方法是flask特有的
    # post 请求参数
    # 写法1.获取未经过处理的原始数据，如果数据格式是json的，则取得的是json字符串，排序和请求参数一直
    print(request.method)
    if request.method == "POST":
        c = request.get_data()
        print(c)
        print("request.data", request.data)
        print(type(c))

        # 写法2.将请求参数做处理
        d = request.get_json()
        print(d)
        print("request.json", request.json)
        print(type(d))

        print(d.get("username"))
        # 写法3.

        # get请求参数的解析和post的请求参数的解析不能混写，否则会报错
    else:

        args = request.args
        print(args)  # ImmutableMultiDict([('username', 'zz'), ('password', '123456')])
        # 将args转为字典
        print(args.to_dict())  # {'username': 'zz', 'password': '123456'}
        print("args--username", args.get("username"))

    return "请求成功"


"""
    strict_slashes 对URL最后的/符号是否严格校验
    /api/login
    /api/login/
    设置为false时，都能访问
"""


@app.route("/api/login", methods=["post"], strict_slashes=False)
def login():
    print(request.method)

    # 将数据转为字典
    data = request.get_json()
    print(data)
    print(type(data))

    username = data.get("username")
    password = data.get("password")

    """
        1.参数为空
        2.用户名密码正确
        3.用户密码错误
    """
    if username == "" or password == "":
        """
            可以用jsonify返回json数据
        """
        return jsonify({
            "code": "001",
            "msg": "username or password can not be null"
        })
    elif username == "zz" or password == "123456":
        return {
            "address": {
                "city": "changsha"
            },
            "httpstatus": 200,
            "info": {
                "age": 18,
                "name": "zz"
            },
            "msg": "success",
            "token": "12121212121212121212"

        }
    else:
        return {
            "code": "001",
            "msg": "用户名密码错误"
        }


@app.route("/api/getUserInfo", methods=["get"], strict_slashes=False)
def get_userinfo():
    token = request.headers.get("token")
    print(token)

    if token == "12121212121212121212":
        return {
            "httpstatus": 200,
            "data": [
                {
                    "userid": 17890,
                    "username": "zz",
                    "nikename": "liangliang",
                    "openid": "UUUUUUU",
                    "userbalance": 123.45,
                    "userpoints": 4567
                }
            ]
        }
    else:
        return {
            "code": "001",
            "msg": "登录超时"
        }


if __name__ == '__main__':
    # debug=True开启调试模式，修改代码自动重启
    # 0.0.0.0不限制访问的ip
    # 启动socket
    app.run(debug=True, host="0.0.0.0", port=8866)
