from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from utils.jwt_manager import create_token
from schemas.user import User


router_login= APIRouter()


    
    
@router_login.post('/login', tags=['auth'])
def login(user: User):
    if user.login == 'admin' and user.password == 'admin':
        token: str = create_token(user.model_dump())
        return JSONResponse(status_code=status.HTTP_200_OK, content=token)

