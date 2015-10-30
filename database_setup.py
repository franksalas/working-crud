
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

#########################
# sqlalchemy components #
# configuation          #
# class                 #
# Table                 #
# Mapper                #
#########################

Base = declarative_base()


class Order(Base):
	__tablename__ = 'order'
	id = Column(Integer, primary_key = True)
	number = Column(Integer, nullable = False)


class Product(Base):
	__tablename__ = 'product'
	id = Column(Integer, primary_key = True)
	donorId = Column(String(10), nullable = False)
	pCode = Column(String(10), nullable = False)
	bType = Column(String(5), nullable = False)
	pDate = Column(String(10), nullable = False)
	pVol = Column(String(3), nullable = False)
	order_id = Column(Integer, ForeignKey('order.id'))
	order = relationship(Order)


########## insert at end of file #######

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
