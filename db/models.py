from datetime import datetime

from sqlalchemy import Column, Integer, String, Enum, DateTime, Boolean, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(70), unique=True)
    hashed_password = Column(String(100))
    created = Column(DateTime, default=datetime.now)
    verification = Column(Boolean, default=False)

class Check(Base):
    __tablename__ = 'checks'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    name = Column(String(30))
    currency = Column(String(100))
    balance = Column(Float, default=0)
    image = Column(String(100))
    color = Column(String(100))

class Transaction(Base):
    __tablename__ = 'transactions'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    check_id = Column(Integer, ForeignKey('checks.id'))
    amount = Column(Float)
    transaction_type = Column(String(50))
    category = Column(String(50))
    timestamp = Column(DateTime)
    comment = Column(String(255))
