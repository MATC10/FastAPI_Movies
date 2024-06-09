from fastapi import FastAPI
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from routers.movie import router
from routers.user import router_login


app = FastAPI()
app.title = 'FastAPI de Miguel Ángel'
app.version = '0.0.1'

app.add_middleware(ErrorHandler)
app.include_router(router_login)
app.include_router(router)


Base.metadata.create_all(bind=engine) #aquí digo con qué motor para crear las tablas
    


movies = [
    {
        "id": 1,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que...",
        "year": "2009",
        "rating": 7.8,
        "category": "Acción"
    },
        {
        "id": 2,
        "title": "Avatar2",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que...",
        "year": "2009",
        "rating": 7.8,
        "category": "Acción"
    }
]


@app.get('/', tags=['home'])
def message():
    return '¡Hola mundo!'