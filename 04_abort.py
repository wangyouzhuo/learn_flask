from flask import Flask,request,abort,Response

app = Flask(__name__)

@app.route("/login",methods=["GET"])
def login():
    # name = request.form.get()
    # pwd = request.form.get()
    name = ""
    pwd = ""
    if name != 'zhangsan' or pwd != 'admin':
        # 使用abort函数可以立即终止视图函数的执行，并给前端返回特定的信息
        # 1.传递状态码信息 必须是标准的http状态码 比如404
        abort(404)
        # 2. 传递响应体信息
        resp = Response("login failed")
        abort(resp)
    return ""


# 自定义错误处理方法
@app.errorhandler(404)
def handle_404_error(err):
    # 这个视图函数的返回值 是前端用户最后看到的返回值
    return "出现404错误，错误信息：%s"%err

if __name__ == "__main__":
    app.run(debug=True)