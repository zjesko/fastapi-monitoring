from sqlalchemy import Column, ForeignKey, Integer, String

from server.database import Base


class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    address = Column(String)


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    acc_id = Column(Integer, ForeignKey("accounts.id"))
    credit = Column(Integer)
    debit = Column(Integer)