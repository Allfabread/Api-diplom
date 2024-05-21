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

class Check(Base):
    __tablename__ = 'checks'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    currency = Column(String(100))
    balance = Column(Float, default=0)

    

    
# class Category(Base):
#     __tablename__ = 'categories'
    
#     id = Column(Integer, primary_key=True)
#     name = Column(String(30))
#     icon = Column(String(70))


# class FreelancersCategory(Base):
#     __tablename__ = 'categories_of_freelancers'
    
#     id = Column(Integer, primary_key=True)
#     freelancer_id = Column(Integer, ForeignKey(f'{User.__tablename__}.id'))
#     category_id = Column(Integer, ForeignKey(f'{Category.__tablename__}.id'))


# class Task(Base):
#     __tablename__ = 'tasks'
    
#     id = Column(Integer, primary_key=True)
#     customer_id = Column(Integer, ForeignKey(f'{User.__tablename__}.id'))
#     category_id = Column(Integer, ForeignKey(f'{Category.__tablename__}.id'))
#     title = Column(String(50))
#     description = Column(String(500))
#     created = Column(DateTime, default=datetime.now)
    

# class Review(Base):
#     __tablename__ = 'reviews'
    
#     id = Column(Integer, primary_key=True)
#     to_id = Column(Integer, ForeignKey(f'{User.__tablename__}.id'))
#     from_id = Column(Integer, ForeignKey(f'{User.__tablename__}.id'))
#     created = Column(DateTime, default=datetime.now)
#     content = Column(String(150))
#     rating = Column(Integer) # 1 - 5


# class Message(Base):
#     __tablename__ = 'messages'
    
#     id = Column(Integer, primary_key=True)
#     to_id = Column(Integer, ForeignKey(f'{User.__tablename__}.id'))
#     from_id = Column(Integer, ForeignKey(f'{User.__tablename__}.id'))
#     content = Column(String(300))
#     created = Column(DateTime, default=datetime.now)
