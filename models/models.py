from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, Enum, ARRAY, DateTime
from sqlalchemy.orm import relationship
from config.database import Base
import enum
from datetime import datetime


class UserRole(enum.Enum):
    COMPRADOR = 'comprador'
    VENDEDOR = 'vendedor'


class PropertyType(enum.Enum):
    CASA = 'casa'
    APARTAMENTO = 'apartamento'
    FLAT = 'flat'
    TERRENO = 'terreno'


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True, nullable=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    role = Column(Enum(UserRole), default=UserRole.COMPRADOR)
    phone_number = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    properties = relationship("Property", back_populates="owner")


class Property(Base):
    __tablename__ = "properties"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), nullable=False)
    description = Column(String(300), nullable=False)
    price = Column(Float, nullable=False)
    property_type = Column(Enum(PropertyType))
    images = Column(ARRAY(String(255)))
    is_active = Column(Boolean, default=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="properties")
