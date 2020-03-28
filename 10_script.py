from flask import Flask
from flask_script import Manager   # 启动命令的管理类

app = Flask(__name__)

# 创建manage的管理对象
manager = Manager(app)


@app.route("/index")
def index():
    return "index page in manager"


if __name__ == "__main__":
    # 通过管理对象来启动flask
    manager.run()

    # 接下来在命令行输入  python3 10_script.py runserver -h 192.168.31.141 -p 8000