from math import ceil

from fastapi import APIRouter, HTTPException
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
from sqlalchemy import func, update

from security import hash_password, encode_jwt, decode_jwt, check_password
from db import depends_db, Check, CheckCreate, User
from helpers import get_user_by_token


checks_router = APIRouter(tags=['Check'])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/check/create')

@checks_router.post("/check/create")
def add_check(data: CheckCreate, token: str = Depends(oauth2_scheme), session = Depends(depends_db)):
    user = get_user_by_token(token, session)
    check = Check(
        user_id = user.id,
        name = data.name,
        currency = data.currency,
        balance = data.balance,
        image = data.image,
        color = data.color
    )
    session.add(check)
    session.commit()
    user.verification = True
    session.commit()
    token = encode_jwt({'id': user.id, 'verification': user.verification})
    return {'token': token}