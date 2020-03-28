# coding: utf-8

from flask import Flask,request


app = Flask(__name__)



@app.route("/index",methods=['GET','POST'])
# 127.0.0.1:5000/index?city=shenzhen&country=china
def index():
    # request中包含了前端发送过来的所有请求信息
    # requesu.form可以直接提取请求体中的表单格式数据，是一个类字典的对象
    # form和data用来提取请求体数据
    name = request.form.get("name","default_name")
    age = request.form.get("age","defualt_age")
    print(request.data)
    name_list = request.form.getlist("name")  #如果form中一个key对应两个value 可以通过这种方法提取
    print(name_list)

    # args用来提取url当中的参数（查询字符串）
    city = request.args.get('city')
    country = request.args.get('country')
    return "hello,name={} , age={} , city={} , counrty={}".format(name,age,city,country)

# 把不同的请求方式做到同一个视图函数中
def register():
    if request.method == 'GET':
        return
    if request.method == 'POST':
        return

if __name__ == "__main__":
    app.run(debug=True)
