from flask import Flask,make_response,request

app = Flask(__name__)

@app.route("/set_cookie")
def set_cookie():
    resp = make_response("success")
    # 设置cookie必须先要创建response对象
    resp.set_cookie("Itcast","Python")
    resp.set_cookie("Itcast_1","Python_1")
    resp.set_cookie("Itcast_2","Python_2",max_age=3600) # 通过max age设置有效期  单位是s
    resp.headers["Set-Cookie"] = "Itcast_3=Python3"
    return resp

@app.route('/get_cookie')
def get_cookie():
    c = request.cookies.get("Itcast")
    return c

@app.route("/delete_cookie")
def delete_cookie():
    # 删除cookie
    resp = make_response("del success")
    resp.delete_cookie("Itcast_1")
    return resp




if __name__ == "__main__":
    app.run(debug=True)