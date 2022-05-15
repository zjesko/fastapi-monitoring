from pydantic import BaseModel


class AccountIn(BaseModel):
    first_name: str
    last_name: str
    address: str


class Account(AccountIn):
    id: int

    class Config:
        orm_mode = True


class TransactionIn(BaseModel):
    acc_id: int
    credit: int
    debit: int


class Transaction(TransactionIn):
    id: int

    class Config:
        orm_mode = True
