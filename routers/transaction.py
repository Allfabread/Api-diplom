from datetime import datetime
from typing import List
from math import ceil

from fastapi import APIRouter, HTTPException
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import func
from sqlalchemy.orm import aliased

from security import hash_password, encode_jwt, decode_jwt, check_password
from db import depends_db, TransactionCreate, Transaction
from helpers import get_user_by_token


transactions_router = APIRouter(tags=['Transaction'])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/transaction/create')


@transactions_router.post('/transaction/create')
def create_transaction(data: TransactionCreate, token: str = Depends(oauth2_scheme), session = Depends(depends_db)):
    user = get_user_by_token(token, session)
    new_transaction = Transaction(
        user_id = user.id,
        check_id = data.check_id,
        amount = data.amount,
        transaction_type = data.transaction_type,
        category = data.category,
        timestamp = data.timestamp,
        comment = data.comment
    )
    session.add(new_transaction)
    session.commit()
    return "Транзакция добавленна!"