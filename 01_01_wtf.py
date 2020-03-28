from flask import Flask,render_template,redirect,url_for,session
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,EqualTo


app = Flask(__name__)

app.config['SECRET_KEY'] = "E23RNJSVDSNFDSNFF"


# 定义表单的模型类
class RejisterForm(FlaskForm):
    """自定义的注册表单模型类"""
    #                              名字      检验器
    # DataRequired:保证数据必须填写且非空
    username  = StringField(  label=u'用户名',validators=[DataRequired(u"用户名不能为空")])
    password  = PasswordField(label=u"密码",validators=[DataRequired(u'密码不能为空')])
    password2 = PasswordField(label=u"确认密码",validators=[DataRequired(u'确认密码不能为空'),EqualTo("password",u"两次密码不一致")])
    submit    = SubmitField(label = u'提交')

@app.route("/register",methods=["GET","POST"])
def register():
    form = RejisterForm()
    # 判断form中的数据是否合理
    # 如果form中的数据完全满足验证器，返回正，否则返回假
    if form.validate_on_submit():
        # 验证合格 接下来从form中提取数据
        uname = form.username.data
        pwd   = form.password.data
        pwd2  = form.password2.data
        print(uname,pwd,pwd2)
        session["user_name"] = uname
        return redirect(url_for("index"))
    return render_template("register.html",form=form)


@app.route("/index")
def index():
    user_name = session.get("user_name")
    return "hello %s"%user_name



if __name__ == '__main__':
    app.run(debug=True)