from flask import Flask,render_template,flash


app = Flask(__name__)

global flag

flag = True

app.config["SECRET_KEY"] = "ASFDQ2923UF9SCDS"


@app.route("/")
def index():
    global flag
    if flag is True:
        flash("hello1")
        flash("hello2")
        flash("hello3")
        flag = False
    return render_template("index_for_macro.html")  # 可复用的宏

if __name__ == "__main__":
    app.run(debug=True)