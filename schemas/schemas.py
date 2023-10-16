from pydantic import BaseModel
from typing import List, Optional
from enum import Enum
from datetime import datetime


class PropertyTypeEnum(Enum):
    CASA = "casa"
    APARTAMENTO = "apartamento"
    FLAT = "flat"
    TERRENO = "terreno"


class UserRole(Enum):
    COMPRADOR = 'comprador'
    VENDEDOR = 'vendedor'


class PropertieBase(BaseModel):
    title: str
    description: str
    price: float
    property_type: PropertyTypeEnum
    images: List[str]
    is_active: bool = True


class UserBase(BaseModel):
    name: str
    email: str
    role: UserRole = UserRole.COMPRADOR.value
    phone_number: Optional[str] = None
   # profile_picture: Optional[str] = None
    is_active: bool = True


class CreateUserRequest(UserBase):
    email: str
    password: str


class UserUpdate(UserBase):
    name: Optional[str]
    email: Optional[str]
    password: Optional[str]
    role: Optional[UserRole]
    is_active: Optional[bool]
    phone_number: Optional[str]
   # profile_picture: Optional[str]


class UserInDB(UserBase):
    id: int
    hashed_password: str
    created_at: datetime


class UserPublic(UserBase):
    id: int
    created_at: datetime


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
