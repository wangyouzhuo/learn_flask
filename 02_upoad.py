from flask import Flask,request


app = Flask(__name__)

@app.route("/upload",methods=['POST'])
def upload():
    "接受前端传送过来的文件"
    file_obj = request.files.get('pic')
    if file_obj is None:
        #此时前端没有发送文件
        return "未上传文件"
    # # 将文件保存本地
    # # 1.创建一个文件
    # f = open("./demo.jpg","wb")
    # # 2. 从前端读取文件数据 并向本地文件写内容
    # data = file_obj.read()
    # f.write(data)
    # # 3. 关闭文件
    # f.close()

    #一种保存文件的简单方法
    file_obj.save("./demo1.png")
    return "上传成功"

if __name__ == '__main__':
    app.run(debug=True)