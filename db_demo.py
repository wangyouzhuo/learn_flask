from flask import Flask
from flask_sqlalchemy  import SQLAlchemy
from sqlalchemy import or_
from sqlalchemy import func

app = Flask(__name__)

# 进行数据库参数配置

class Config(object):
    SQLALCHEMY_DATABASE_URL = "mysql://root:mysql@127.0.0.1:3306/db_python04"

    SQLALCHEMY_TRACK_MODIFICATIONS = True

app.config.from_object(Config)

# 创建数据库工具sqlalchemy对象

db = SQLAlchemy(app)  # 这样就可以自动从app中提取数据库参数进行配置

# 创建数据库模型类
class Role(db.Model):
    """用户角色表/身份表"""
    __tablename__ = "tbl_roles"
    id = db.Column(db.Integer,primary_key=True)  # 设置一个整型的主键 默认为自增
    name = db.Column(db.String(32), unique=True)

    users = db.relationship("User",backref="role")  # 当从role访问users时，访问的是哪个模型类的对象呢？User
    # backref 相当于给role添加了一个新的属性    接下来通过某个user的user.role，就可以直接拿到那条记录，而不是记录的id
    # Role.users 建立了Role和User的关联


class User(db.Model):
    """用户表"""
    __tablename__ = "tbl_users"  # 指明 数据库的表名
    id       = db.Column(db.Integer,primary_key=True)  # 设置一个整型的主键 默认为自增
    name     = db.Column(db.String(64),unique=True)
    email    = db.Column(db.String(128),unique=True)
    password = db.Column(db.String(64),nullable=False)
    role_id = db.Column(db.Integer,db.ForeignKey("tbl_roles.id"))  # 可以实现：从user找到role





@app.route("/")
def index():
    return "index page"


if __name__ == "__main__":

    # 通过db的方式清楚数据库里面的所有数据
    db.drop_all()

    # 创建表
    db.create_all()  # 这样就会创建role表和user表

    # 创建对象
    role1 = Role(name="admin")
    #session记录对象任务
    db.session.add(role1)
    # 提交任务到数据库
    db.session.commit()

    # 创建对象
    role2 = Role(name="stuf")
    #session记录对象任务
    db.session.add(role2)
    # 提交任务到数据库
    db.session.commit()

    # 一次性添加多条数据
    us1 = User(name="wang",email="wang@163.com",password="123456",role_id=role1.id)
    us2 = User(name="zhang",email="zhang@163.com",password="111111",role_id=role2.id)
    db.session.add_all([us1,us2])
    db.session.commit()

    # 查询
    li = Role.query.all()
    first = Role.query.first()
    a = Role.query.get(2)  #根据主键进行查询 primary_key = 2

    li = db.session.query(Role).all()

    # 过滤查询
    b = User.query.filter_by(name="wang",role="1").all()
    c = User.query.filter(User.name=="wang",User.role_id==1).first()

    # 使用 或逻辑 进行过滤
    d = User.query.filter(or_(User.name=="wang",User.email.endswith("163.com")))

    e = User.query.filter().offset(2).limit(2).order_by(User.id.asc()).all()
    # offset 偏移：从第几个开始取   limit：取n个    order_by排序

    db.session.query(User.role_id,func.count(User.role_id)).group_by(User.role_id).all()  # 分组查询

    # 关联查询
    #从role表中查询role表匹配到的user
    f = Role.query.get(1).users[0].name

    # 关联查询
    #从user表查询role
        #方法一
    target_id = User.query.get(1).role_id
    Role.query.get(target_id)
        #方法二
    user = User.query.get(1)
    user.role

    # 对查询出来的结果直接进行修改
    User.query.filter_by(name="zhou").update({"name":"python","email":"123@qq.com"})
    db.session.commit()

    #删除
    user = User.query.get(3)
    db.session.delete(user)


    app.run(debug=True)