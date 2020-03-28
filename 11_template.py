from flask import Flask,request,url_for,render_template


app = Flask(__name__)

@app.route("/index")
def index():
    data = {
        "name":"python",
        "age":18,
        "my_dict":{"city":"shenzheng"},
        "my_list":[1,2,3,4,5],
        "my_int":0
    }
    # return render_template("index.html",name="python",age="8")
    return render_template("index.html",**data)


# 自定义过滤器
def list_step_2(li):
    return li[::2]
# 注册过滤器
app.add_template_filter(list_step_2,"li2")

# 自定义并注册过滤器
@app.template_filter("li3")
def list_step_3(li):
    return li[::3]




if __name__ == "__main__":
    app.run(debug=True)