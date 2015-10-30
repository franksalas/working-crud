from flask import Flask, render_template

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Order, Product

engine = create_engine('sqlite:///database.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

app = Flask(__name__)


@app.route('/')
@app.route('/hello/')
def orderlist():
	order = session.query(Order).first()
	products = session.query(Product).filter_by(order_id=order.id)
	output = ''
	for i in products:
		output += i.donorId
		output += '</br>'
		output += i.pCode
		output += '</br>'
		output += i.bType
		output += '</br>'
		output += i.pDate
		output += '</br>'
		output += i.pVol
		output += '</br>'

	return output



	# order = session.query(Order).filter_by(id=order_id).one()
	# products = session.query(Product).filter_by(order_id=order_id)
	# return render_template('menu.html', order=order, products=products)





if __name__ == '__main__':
	app.run(debug=True)
