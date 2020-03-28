# coding:utf-8

from flask import Flask,current_app
import demo

# 创建flask的应用对象
# 其中__name__是一个变量，代表当前文件所在的模块的名字，即文件名
app = Flask(import_name=__name__,
            static_url_path="/fuck",# 访问静态资源的url前缀 默认是static
            static_folder='static',  # 静态文件的目录
            template_folder='templates', # 模版文件的目录 默认是templates
         )

# 配置参数的使用方式
# 1.使用配置文件
app.config.from_pyfile("config.cfg")  # 以当前模块的所在目录为根目录去寻找所在模块的名字

# 2.使用类的方式配置参数  优点：除了传递flask需要的参数 也可以配置自己需要的参数
class Config(object):
    DEBUG = True
    ITCAST = 'python'
app.config.from_object(Config)

# 3.直接操作config字典对象
app.config['DEBUG'] = True

# 绑定路由
@app.route("/")
def index():
    # "定义视图函数"
    # a = 1/0
    print(app.config.get('ITCAST')) # 直接从app中获取配置值
    print(current_app.config.get('ITCAST'))  # 从current——app代理人 中获取配置
    return "hello flask"



if __name__ == '__main__':

    # 启动flask程序
    app.run(
        host='0.0.0.0',  # 绑定ip地址和端口
        port=5000,
        debug=True
    )




