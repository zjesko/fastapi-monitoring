import uvicorn
from typing import List
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException
from prometheus_fastapi_instrumentator import Instrumentator

from server import crud, models, schemas
from server.database import get_db, engine

# create models in db
models.Base.metadata.create_all(bind=engine)

# init app
app = FastAPI(title="Bank", docs_url="/")

# add prom middleware
@app.on_event("startup")
async def startup_event():
    Instrumentator().instrument(app).expose(app)


# routes
@app.get("/ping")
def ping():
    return {"ping": "pong"}

@app.get("/500")
def error():
    assert 0 == 1


@app.post("/accounts/", response_model=schemas.Account)
def create_account(account: schemas.AccountIn, db: Session = Depends(get_db)):
    return crud.create_account(db=db, account=account)


@app.get("/accounts/", response_model=List[schemas.Account])
def read_accounts(db: Session = Depends(get_db)):
    accounts = crud.get_accounts(db)
    return accounts


@app.get("/accounts/{account_id}", response_model=schemas.Account)
def read_account(account_id: int, db: Session = Depends(get_db)):
    account = crud.get_account(db, id=account_id)
    if account is None:
        raise HTTPException(status_code=404, detail="Account not found")
    return account


@app.get(
    "/accounts/{account_id}/transactions/", response_model=List[schemas.Transaction]
)
def get_transactions_by_account(account_id: int, db: Session = Depends(get_db)):
    return crud.get_transactions_by_acc(db=db, id=account_id)


@app.post("/transactions/", response_model=schemas.Transaction)
def create_transaction(
    transaction: schemas.TransactionIn, db: Session = Depends(get_db)
):
    return crud.create_transaction(db=db, transaction=transaction)


@app.get("/transactions/", response_model=List[schemas.Transaction])
def read_transactions(db: Session = Depends(get_db)):
    transactions = crud.get_transactions(db)
    return transactions


@app.get("/transactions/{transaction_id}", response_model=schemas.Transaction)
def read_transactions(transaction_id: int, db: Session = Depends(get_db)):
    transaction = crud.get_transaction(db, id=transaction_id)
    if transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return transaction


# run server
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8888, reload=True)
