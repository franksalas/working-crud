from flask import Flask, render_template, url_for

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Order, Product

engine = create_engine('sqlite:///database.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

app = Flask(__name__)

# SHOW ALL ORDERS


@app.route('/')
@app.route('/order/')
def showOrder():
    order = session.query(Order).all()
    # return "This page will show all my orders"
    return render_template('order.html', order=order)


@app.route('/order/<int:order_id>/')
@app.route('/order/<int:order_id>/product/')
def showProduct(order_id):
    order = session.query(Order).filter_by(id=order_id).one()
    product = session.query(Product).filter_by(
        order_id=order_id).all()
    return render_template('menu.html', product=product, order=order)
    # return 'This page is the menu for restaurant %s' % restaurant_id


@app.route('/order/<int:order_id>/')
def orderlist(order_id):
	order = session.query(Order).filter_by(id=order_id).one()
	products = session.query(Product).filter_by(order_id=order.id)
	return render_template('menu.html', order=order, products=products)


@app.route('/order/new/', methods=['GET', 'POST'])
def newOrder():
	return "page to CREATE new Order"


# @app.route('/order/<int:order_id>/new/', methods=['GET', 'POST'])
# def newProduct(order_id):
# 	return "page to CREATE new Product"


# @app.route('/order/<int:order_id>/<int:product_id>/edit/')
# def editProduct(order_id, product_id):
# 	return "page to EDIT product"


# @app.route('/order/<int:order_id>/<int:product_id>/delete/')
# def deleteProduct(order_id, product_id):
# 	return "page to DELETE Product"


if __name__ == '__main__':
	app.run(debug=True)
