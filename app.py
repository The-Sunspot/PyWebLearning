from flask import Flask
from flask import url_for
app = Flask(__name__)#flask实例化
@app.route('/')#设置地址，一定/开头
@app.route('/home')#可以多个
def hi():
    return 'hi'
    
@app.route('/uesr/<name>')#可带变量
def hello(name):#返回值会被作为html解析
    return '<h2>Welcome to My Watchlist,'+name+'!</h2>'

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