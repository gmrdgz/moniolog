from pydantic import BaseModel

class BankAccount(BaseModel):
    id: str
    bank_name: str
    account_type: str
