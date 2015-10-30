from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Order, Product


engine = create_engine('sqlite:///database.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Menu for UrbanBurger
order1 = Order(number=1961)

session.add(order1)
session.commit()

product3 = Product(donorId = "W232978115", pCode = "E3098", bType = "O Neg",
pDate = "11/08/16", pVol = "222", order=order1)

session.add(product3)
session.commit()

product4 = Product(donorId = "W981816476", pCode = "E3899", bType = "O POS",
pDate = "11/08/16", pVol = "90", order=order1)

session.add(product4)
session.commit()

product2 = Product(donorId = "W209579390", pCode = "E3079", bType = "A Neg",
pDate = "09/18/06", pVol = "282", order=order1)

session.add(product2)
session.commit()

product4 = Product(donorId = "W224112201", pCode = "E3079", bType = "O POS",
pDate = "08/08/08", pVol = "92", order=order1)

session.add(product4)
session.commit()

product5 = Product(donorId = "W256288172", pCode = "E3099", bType = "B POS",
pDate = "01/08/14", pVol = "72", order=order1)

session.add(product5)
session.commit()

product6 = Product(donorId = "W454006961", pCode = "E3099", bType = "AB Neg",
pDate = "11/28/16", pVol = "292", order=order1)

session.add(product6)
session.commit()


# W454006961
# W256288172
# W803017579
# W092257573
# W927763027
# W377320222
# W224112201
# W867918179
# W209579390
# W591486314
# W548586623
# W981816476
# W911104873
# W327148744
# W063332833
# W279462960
# W892429280
# W232978115
# W454103621
# W618904552