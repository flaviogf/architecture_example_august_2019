from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from easyagro.extensions import db


class Budget(db.Model):
    uid = Column(String(36),
                 primary_key=True)
    name = Column(String(250),
                  nullable=False)
    email = Column(String(250),
                   nullable=False)
    total = Column(Float,
                   nullable=False)
    items = relationship('BudgetItem')


class BudgetItem(db.Model):
    uid = Column(String(36),
                 primary_key=True)
    name = Column(String(250),
                  nullable=False)
    quantity = Column(Integer,
                      nullable=False)
    price = Column(Float,
                   nullable=False)
    total = Column(Float,
                   nullable=False)
    budget_uid = Column(String(36),
                        ForeignKey('budget.uid'))


class DeliveryType:
    name = Column(String(250),
                  primary_key=True)
    value = Column(Float,
                   nullable=False)
