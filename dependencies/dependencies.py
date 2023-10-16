from fastapi import status, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from config.database import get_db
from schemas.schemas import TokenData
from util.auth_util import SECRET_KEY, ALGORITHM
from util.auth_util import get_user_by_email
from sqlalchemy.orm import Session
import jwt
from jwt.exceptions import JWTError

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user_by_email(db, email=token_data.username)
    if user is None:
        raise credentials_exception
    return user
