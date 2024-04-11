from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/main_menu')
def main_menu():
    return render_template('main_menu.html')

@app.route('/dashboardlink')
def dashboard():
    return render_template('dashboard.html')

@app.route('/productlink')
def product():
    return render_template('product.html')

@app.route('/goods_receivelink')
def goods_receive():
    return render_template('goods_receive.html')

@app.route('/goods_issuelink')
def goods_issue():
    return render_template('goods_issue.html')

@app.route('/transferlink')
def transfer():
    return render_template('transfer.html')

@app.route('/balance_stocklink')
def balance_stock():
    return render_template('balance_stock.html')

@app.route('/reportlink')
def report():
    return render_template('report.html')

@app.route('/logoutlink')
def logout():
    return render_template('logout.html')

if __name__ == '__main__':
    app.run(debug=True)
