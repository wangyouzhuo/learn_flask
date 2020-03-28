# coding:utf-8

from flask import Flask,current_app,redirect,url_for
from werkzeug.routing import BaseConverter


# 创建flask的应用对象
# 其中__name__是一个变量，代表当前文件所在的模块的名字，即文件名
app = Flask(import_name=__name__)


# 转换器语法
#@app.route("/goods/<int:goods_id>")
@app.route("/goods/<goods_id>")  # 不加类型的话 默认为字符串
def goods_detail(goods_id):
    return "goods detail page : {}".format(goods_id)


"""
    万能转换器
"""
# 1.自定义转换器
class RegexConverter(BaseConverter):
    def __init__(self,url_map,regex):
        super().__init__(map=url_map)
        self.regex = regex
    def to_python(self,value):
        #在这个可以对value进行一些操作#
        # value是正则后提取的数据
        print("to_python方法被调用:",value)
        return str(int(value)+1)
    def to_url(self,value):
        # 把视图中的数据转化到url中
        # 使用url_for的时候 这个方法被调用
        print("to_url方法被调用:",value)
        return str(int(value)-10)

# 2.将自定义转换器添加到flask应用中
app.url_map.converters["re"] = RegexConverter

# 3.使用转换器 来实现手机号的传递
@app.route("/send/<re(r'1[34578]\d{9}'):mobile>")
def send_sms(mobile):
    print("send_sms")
    return "send sms to %s"%mobile

# 4.万能转换器的复用案例:只需要配置 转换器类re 和 正则表达式
@app.route("/call/<re(r'1[34758]\d{3}'):mobile>")
def call_tel(mobile):
    return "call {}".format(mobile)



"""
    普通转换器
"""
# 定义转换器的类
class MobileConverter(BaseConverter):
    def __init__(self,url_map):
        super().__init__(url_map)
        self.regex = r'1[34578]\d{9}'
# 定义转换器的名字
app.url_map.converters['mobile'] = MobileConverter
# 使用转换器定义视图函数
@app.route("/sends/<mobile:mobile_number>")
def sends_sms(mobile_number):
    return "send sms to %s"%mobile_number


@app.route("/index")
def index():
    # /send/
    url = url_for("send_sms",mobile="13899999195")
    print(url)
    return redirect(url)

if __name__ == '__main__':

    print(app.url_map)

    # 启动flask程序
    app.run(
        debug=True
    )




