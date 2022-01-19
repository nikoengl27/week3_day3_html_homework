from flask import render_template
from app import app
from models.orderlist import orders

@app.route('/orders')
def index():
    return render_template('index.html', title='New Orders', newOrders= orders, count=0)

@app.route('/orders/<number>')
def one_order(number):
    return render_template('order.html', title='Order', order= orders[int(number)])
