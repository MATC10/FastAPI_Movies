from fastapi import Depends, Path, Query, status, APIRouter
from fastapi.responses import JSONResponse
from typing import Optional, List
from config.database import Session
from models.movie import Movie as MovieModel
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from services.movie import MovieService
from schemas.movie import Movie

router = APIRouter()



@router.get('/movies', tags=['movies'], response_model=List[Movie], status_code=status.HTTP_200_OK, dependencies=[Depends(JWTBearer())]) #USANDO STATUS
def get_movies() -> List[Movie]:
    db = Session()
    result = MovieService(db).get_movies()
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(result))

@router.get('/movies/{id}', tags=['movies'], response_model=Movie, status_code=status.HTTP_200_OK)
def get_movie(id: int = Path(ge=1, le=10000)) -> Movie:
    db = Session()
    result = MovieService(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=404, content={'message':'No encontrado'})
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(result))


@router.get('/movies/', tags=['movies'], response_model=List[Movie], status_code=status.HTTP_200_OK)
def get_movies_by_title_and_category(title:str, category:str = Query(min_length=5, max_length=20)) -> List[Movie]:
    db = Session()
    result = MovieService(db).get_movies_by_title_and_category(title, category)
    if not result:
        return JSONResponse(status_code=404, content={'message':'No encontrado'})
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(result))

@router.post('/movies', tags=['movies'], response_model=dict, status_code=200)
def create_movie(movie: Movie) -> dict:
    db = Session()
    MovieService(db).create_movie(movie)
    return JSONResponse(status_code=201, content={'message': 'Se ha registrado la película'})

@router.put('/movies/{id}', tags=['movies'], response_model=dict, status_code=200)
def put_movie(id:int, movie:Movie) -> dict:
    db = Session()
    result = MovieService(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=404, content={'message':'No encontrado'})
    
    MovieService(db).put_movie(id, movie)
        
    return JSONResponse(status_code=200, content={'message': 'Se ha modificado la película'})

@router.delete('/movies/{id}', tags=['movies'], response_model=dict, status_code=200)
def delete_movie(id:int) -> dict:
    db = Session()
    result = MovieService.get_movie(id)
    if not result:
        return JSONResponse(status_code=404, content={'message':'No encontrado'})
    MovieService.delete_movie(id)
    db.commit()
    return JSONResponse(status_code=200, content={'message': 'Se ha eliminado la película'})