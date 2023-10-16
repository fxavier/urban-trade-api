from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from schemas.schemas import UserPublic
from sqlalchemy.orm import Session
from config.database import get_db
from repository import user_repository
from schemas.schemas import Token
from typing import Annotated
from api.auth.auth import get_current_user
# from util.auth_util import create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES, get_user_by_email, verify_password

router = APIRouter()

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[UserPublic, Depends(get_current_user)]


@router.get('/api/v1/me', response_model=UserPublic, status_code=status.HTTP_200_OK)
async def user(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail='Authentication Failed')
    return {"user": user}
