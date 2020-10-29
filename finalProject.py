from flask import Flask,render_template,request,url_for,redirect
from data import dataSearch
from ytTimes import watch_times
from Shopee import Shopee
app = Flask(__name__)

@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method=='POST':
        return redirect(url_for('index'))
    return render_template('index.html')

@app.route("/<data>", methods=['GET']) 
def Search(data): 
    return dataSearch(data)

@app.route('/status', methods=['GET', 'POST'])
def status():
    if request.method=='POST':
        return redirect(url_for('status2'))
    return render_template('status.html')

@app.route('/image', methods=['GET', 'POST'])
def image():
    if request.method=='POST':
        return redirect(url_for('index'))
    return render_template('image.html')

@app.route('/statistics', methods=['GET', 'POST'])
def statistics():
    if request.method=='POST':
        return redirect(url_for('index'))
    return render_template('statistics.html')

@app.route('/shopping',methods=['GET','POST'])
def shopping():
    if request.method=='POST':
        return redirect(url_for('index'))
    return render_template('shopping.html')

@app.route('/shopping/<data>', methods=['GET','POST'])
def shop(data):
    return Shopee(data)

@app.route("/status2")
def status2():
    return render_template('status2.html')

if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True      
    app.jinja_env.auto_reload = True
    app.debug = True
    app.run()

