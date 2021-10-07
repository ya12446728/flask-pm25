#from _typeshed import FileDescriptor
from datetime import datetime
from flask import Flask
from flask.templating import render_template
from scrape.pm25 import get_pm25
import json

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return 'Hello word!'

@app.route('/test')
def test():
    name = "ian"
    time = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
    return render_template('index.html',data={
        'name' : name,
        'time' : time
    })
@app.route('/echarts')
def echarts():
    return render_template('eacharts.html')
@app.route('/stock')
def stock():
    time = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
    stocks=[
        {'分類': '日經指數', '指數': '22,920.30'},
        {'分類': '韓國綜合', '指數': '2,304.59'},
        {'分類': '香港恆生', '指數': '25,083.71'},
        {'分類': '上海綜合', '指數': '3,380.68'}
    ]

    return render_template('stack.html',**locals())

@app.route('/pm25')
def pm25():
    time = datetime.now().strftime('%Y-%m-%d %H-%M-%S')

    cols,datas = get_pm25()
    return render_template('pm25.html',**locals())

@app.route('/pm25-data', methods= ['GET','POST'])
def get_pm25_json():
    col,datas = get_pm25()

    site = [data[1] for data in datas]
    pm25 = [data[2] for data in datas]

    data = {'col':col ,'site' : site , 'pm25' :pm25}

    return json.dumps(data,ensure_ascii=False)

@app.route('/sum/x=<x>&y=<y>')
def get_sum(x,y):
    return f'ttoal:{eval(x)+eval(y)}'


@app.route('/today/<string:name>') 
def getToday(name):
    from datetime import datetime
    print(datetime.now())
    return name +" "+datetime.now().strftime('%Y-%m-%d %H-%M-%S')




if __name__== '__main__':
    app.run(debug=True)