from flask import Flask,session,g

# g和app一样是跨线程的全局变量(应用上下文)
# 每次进入视图函数的时候 g变量都会被清空
# g 在客户端发起一次request后 ，在本次request期间 ，所有代码只要出现了g，都可以访问到g里面的数据

app = Flask(__name__)

app.config["SECRET_KEY"] = "FDSFSD"

# flask 的session 默认把session数据保存到了前端cookie中

def fuck():
    print("fuck!",g.username)
    print(g.username)


@ app.route("/login")
def login():

    # 设置session数据
    session['name'] = "python"
    session['mobile'] = "13899999999"
    g.username = "zhangsan"
    fuck()
    return "login success"

@app.route("/index")
def index():
    # 获取session数据
    name = session.get("name")
    return "hello : %s"%name

if __name__ == "__main__":
    app.run(debug=True)

"""
关于request：
    request是一个线程局部变量，可以理解为 本来是一个局部变量 但是为某个用户的线程独有
    request = {
        线程a:{
        } 专门处理用户a的请求
        线程b:{
        } 专门处理用户b的请求
    }
"""