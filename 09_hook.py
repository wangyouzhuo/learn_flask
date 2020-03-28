from flask import Flask,session,current_app,request,url_for

app = Flask(__name__)

@app.route("/index")
def index():
    print("index 被执行")
    a = 1/0
    return "index page"

@app.route("/hello")
def index():
    print("hello 被执行")
    a = 1/0
    return "hello page"


@app.before_first_request
def handle_before_first_request():
    """在第一次请求处理视图函数之前先被执行"""
    print("handle_before_first_request 被执行")

@app.before_request
def handle_before_request():
    """每次请求视图函数之前都被执行"""
    print("handle_before_request 被执行")

@app.after_request
def handle_after_request(response):
    """在每次请求视图函数之后都被执行,前提是视图函数没有出现异常"""
    print("handle_after_request 被执行")
    return response


@app.teardown_request
def handle_teardown_requeust(response):
    """无论视图函数是否出现异常 都被执行 (在error情况下执行此函数 需要关闭debug模式)"""
    print(request.path)
    if request == url_for("index"):  # 将钩子函数和视图函数绑定
        pass
    if request == url_for("hello"):
        pass
    print("handle_teardown_request 被执行")
    return response



if __name__ == "__main__":
    app.run()