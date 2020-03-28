import pymysql
pymysql.install_as_MySQLdb()
from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired



app = Flask(__name__)

class Config(object):
    SQLALCHEMY_DATABASE_URI = "mysql://root:5416149qqq@127.0.0.1:3306/author_book_py04"
    #SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@127.0.0.1:3306/db_python '
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    SECRET_KEY = "23RFEFJJ423K"

app.config.from_object(Config)

db = SQLAlchemy(app)

# 定义数据库模型类
class Author(db.Model):
    """作者表"""
    __tablename__ = "tbl_authors"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(32),unique=True)
    books = db.relationship("Book",backref="author")

class Book(db.Model):
    """书籍"""
    __tablename__ = "tbl_books"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),unique=True)
    author_id = db.Column(db.Integer,db.ForeignKey("tbl_authors.id"))


# 定义表单模型类
class AuthorBookForm(FlaskForm):
    """作者书籍表单模型类"""
    author_name = StringField(label=u"作者",validators=[DataRequired(u'作者必填')])
    book_name = StringField(label=u"书籍",validators=[DataRequired(u'书籍必填')])
    submit = SubmitField(label="保存")


@app.route("/",methods=["GET","POST"])
def index():
    # 创建表单对象
    form = AuthorBookForm()

    # 验证表单成功
    if form.validate_on_submit():
        author_name = form.author_name.data
        book_name = form.book_name.data
        # 保存数据库
        # 更新author对象
        author = Author(name=author_name)
        db.session.add(author)
        db.session.commit()
        # 更新book对象
        book = Book(name=book_name,author_id=author.id)
        db.session.add(book)
        db.session.commit()
        pass
    # 查询数据库
    authors_li = Author.query.all()
    print(authors_li)
    for item in authors_li:
        print(item.name)
    return render_template("author_book.html",authors = authors_li,form=form)


# 定义一个视图 用来删除书籍
# 前端按照json格式返回      {"book_id":x}
@app.route("/detele_book",methos=["POST"])
def delete_book():
    """删除数据"""
    # 提取参数
    reg_data = request.get_json()  #如果前端发送的请求体数据是json，get_json那么会解析成字典
    book_id = reg_data.get("book_id")
    #删除数据
    book = Book.query.get(book_id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for("index"))




if __name__ == "__main__":
    app.run(debug=True)

    # # 创建测试数据库
    # db.drop_all()
    # db.create_all()
    #
    # # 添加测试数据
    # au_zhang = Author(name="张三")
    # au_li = Author(name="李四")
    # au_wang = Author(name="王五")
    # au_zhao = Author(name="赵六")
    # db.session.add_all([au_zhang,au_li,au_wang,au_zhao])
    # db.session.commit()
    #
    # bk_yuwen = Book(name="语文",author_id=au_zhang.id)
    # bk_shuxue = Book(name="数学",author_id=au_li.id)
    # bk_yinyu = Book(name="英语",author_id=au_wang.id)
    # bk_huaxue = Book(name="化学",author_id=au_zhao.id)
    # db.session.add_all([bk_yuwen, bk_shuxue, bk_yinyu, bk_huaxue])
    # db.session.commit()



