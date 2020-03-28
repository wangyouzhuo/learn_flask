from flask import Flask,request,abort,Response,make_response,jsonify
import json

app = Flask(__name__)

@app.route("/index")
def index():
    # json就是字符串
    data = {
        "name":"python",
        "age":10
    }
    # 1. 使用json方法
    # json.dumps : 字典 转 json字符串
    # json.loads : json字符串 转 字典
    json_str = json.dumps(data)
    return json_str,200,{"Content-type":"application/json"}
    # 2. 使用jsonify方法 帮助转为json数据并设置响应头content-type为application/json
    return jsonify(data)
    return jsonify(city="sz",country="china")

if __name__ == "__main__":
    app.run(debug=True)