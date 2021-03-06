#体系结构
#venv为虚拟目录
#.flaskenv为全局变量
#.gitignore是忽略的git
#static是全部静态
#templates是默认模版路径
#app.py是默认程序入口
from flask import Flask #开始
from flask import url_for #返回函数的url
from flask import render_template #模版

#start-------------------------------------------------------------------------------------
app = Flask(__name__)#flask实例化
@app.route('/')#设置地址，一定/开头，可以多个
def hi():
    return 'hi'
#url带变量-----------------------------------------------------------------------------------
@app.route('/uesr/<name>')#可带变量
def hello(name):#返回值会被作为html解析
    return '<h2>Welcome to My Watchlist,'+name+'!</h2>'


#url_for-----------------------------------------------------------------------------------
@app.route('/urlfortest')
def test_url_for():#urlfor是函数->url的映射，调用时需要加上变量参数
    print(url_for('hi')) # 输出：/
    # 注意下面两个调用是如何生成包含 URL 变量的 URL 的
    print(url_for('hello', name='greyli')) # 输出：/user/greyli
    print(url_for('hello', name='peter')) # 输出：/user/peter
    print(url_for('test_url_for')) # 输出：/urlfortest
    # 下面这个调用传入了多余的关键字参数，它们会被作为查询字符串附加到 URL后面。
    print(url_for('test_url_for', num=2)) # 输出：/urlfortest?num=2
    return 'Test page'

#对于static的使用是这样的：url_for('static',filename='xx.xx')
#模版中可以直接使用urlfor等一些常见函数

#render模版--------------------------------------------------------------------------------
name = 'Grey Li'
movies = [
{'title': 'My Neighbor Totoro', 'year': '1988'},
{'title': 'Dead Poets Society', 'year': '1989'},
{'title': 'A Perfect World', 'year': '1993'},
{'title': 'Leon', 'year': '1994'},
{'title': 'Mahjong', 'year': '1996'},
{'title': 'Swallowtail Butterfly', 'year': '1996'},
{'title': 'King of Comedy', 'year': '1999'},
{'title': 'Devils on the Doorstep', 'year': '1999'},
{'title': 'WALL-E', 'year': '2008'},
{'title': 'The Pork of Music', 'year': '2012'},
]
@app.route('/in')
def index():
    return render_template('index.html',name=name,movies=movies)


#数据库--------------------------------
#sqlite3: cmd输入sqlite3 xx.db
#随便sql就可以了
#
from flask_sqlalchemy import SQLAlchemy
import os
#设置数据库路径
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False#关闭对模型修改的监控

db=SQLAlchemy(app)#db初始化

#表要继承Model
class User(db.Model): # 表名将会是 user（自动生成，小写处理）
    id = db.Column(db.Integer, primary_key=True) # 主键
    name = db.Column(db.String(20)) # 名字

class Movie(db.Model): # 表名将会是 movie
    id = db.Column(db.Integer, primary_key=True) # 主键
    title = db.Column(db.String(60)) # 电影标题
    year = db.Column(db.String(4)) # 电影年份
@app.route('/')
def index():
    user = User.query.first() #User.query.filter(user.id=="xxx").first()类似这样
    movies = Movie.query.all() # 读取所有电影记录
    return render_template('index.html', name=user.name, movies=movies)