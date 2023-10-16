from fastapi import FastAPI
from api.controllers import user_controller
from api.auth import auth
from config.database import engine, Base
from models import models

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title='API de Marketplace Imobiliaria',
    description='API de Marketplace Imobiliaria',
    version='0.0.1',
    docs_url='/',
    contact={
        'name': 'Xavier Francisco',
        'url': 'https://xavierfrancisco.com',
        'email': 'xavierfrancisco353@gmail.com',
    },
    license_info={
        'name': 'MIT License',
        'url': 'https://opensource.org/licenses/MIT',
    },
)

app.include_router(auth.router)
app.include_router(user_controller.router)
