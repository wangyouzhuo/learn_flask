# coding:utf-8

from flask import Flask,current_app,redirect,url_for

# 创建flask的应用对象
# 其中__name__是一个变量，代表当前文件所在的模块的名字，即文件名
app = Flask(import_name=__name__,
         )

# 绑定路由
@app.route("/")
def index():
    return "hello flask"

# 通过method来限定访问方式
@app.route('/post_only',methods=["POST","GET"])
def post_only():
    return "post only page"

# 如果两个hello的请求方式相同  则会执行hello one 而不执行hello two
# 如果method不同 则视情况判定
@app.route("/hello",methods=['POST'])
def hello():
    return "hello one"

@app.route("/hello",methods=['GET'])
def hello_2():
    return "hello two"

# 多个装饰器映射到同一个视图函数
@app.route("/hi1")
@app.route("/hi2")
def hi():
    return "hi page"

@app.route("/login")
def login():
    # 使用url——for  通过 视图函数名字 找到 路径url
    # 尽量采用这种写法
    url = url_for("index")
    return redirect(url)




if __name__ == '__main__':

    print(app.url_map)

    # 启动flask程序
    app.run(
        # host='0.0.0.0',  # 绑定ip地址和端口
        # port=5000,
        debug=True
    )




