from sqlalchemy.orm import Session

from server import models, schemas


def get_account(db: Session, id: int):
    return db.query(models.Account).filter(models.Account.id == id).first()


def get_accounts(db: Session):
    return db.query(models.Account).all()


def get_transaction(db: Session, id: int):
    return db.query(models.Transaction).filter(models.Transaction.id == id).first()


def get_transactions_by_acc(db: Session, id: int):
    return db.query(models.Transaction).filter(models.Transaction.acc_id == id).all()


def get_transactions(db: Session):
    return db.query(models.Transaction).all()


def create_account(db: Session, account: schemas.AccountIn):
    db_account = models.Account(**account.dict())
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return db_account


def create_transaction(db: Session, transaction: schemas.TransactionIn):
    db_transaction = models.Transaction(**transaction.dict())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction
