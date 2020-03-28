from flask import Flask,request,abort,Response,make_response

app = Flask(__name__)


@app.route("/index")
def index():
    # # 使用元组 自定义响应信息：响应体；状态码；响应头
    # # 1. 响应头可以是列表
    return "index page",400,[("Itcast","python"),("city","shenzhen")]

    # # 2. 响应头可以是字典
    return "index page",400,{"Itcast":"python","city":"shenzhen"}

    # # 3. 状态码可以是非标准的自定义的东西
    return "index page",666,{"Itcast":"python","city":"shenzhen"}
    return "index page","666 itcast status",{"Itcast":"python","city":"shenzhen"}

    # # 4. 可以只传递状态码和响应头
    return "index page","666 itcast status"

    # 5. 可以通过make response来构造响应信息
    resp = make_response("index page 2")  # 前端显示的内容
    resp.status = "999 itcast"  # 状态码
    resp.headers["city"] = "sz" # 响应头
    return resp








if __name__ == "__main__":
    app.run(debug=True)