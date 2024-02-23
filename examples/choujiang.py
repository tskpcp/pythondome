#抽奖系统
from flask import Flask,render_template
from random import randint
app =Flask(__name__)
hro=['a','c','d','e','f','n','m','j']
@app.route('/index')
def index():
    return render_template('index.html',hro=hro)

@app.route('/choujiang')
def choujing():
    num=randint(0,len(hro)-1)
    return  render_template('index.html',hro=hro,h=hro[num])
app.run(debug=True)

