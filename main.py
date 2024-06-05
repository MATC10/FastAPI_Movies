from fastapi import FastAPI, Body, Path, Query
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()
app.version = '0.0.1'

class Movie(BaseModel):
    id: Optional[int] = None # id será opcional y a la vez de tipo entero, por defecto es None
    title: str = Field(min_length=5, max_length=15)
    overview: str = Field(min_length=5, max_length=30)
    year: int = Field(le=2025)
    rating: float = Field(ge =1, le=10)
    category: str = Field(min_length=5, max_length=20)
    
    # Dentro de la clase Movie creamos esta clase para poner los valores 'default' y no ponerlos en los atributos
    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "title": "Mi pelicula",
                "overview": "Descripción de la película",
                "year": 2024,
		        "rating": 5.5,
		        "category": "Acción"

            }
        }
    

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

@app.get('/movies', tags=['movies'])
def get_movies():
    return movies

@app.get('/movies/{movie_id}', tags=['movies'])
def get_movie(movie_id: int = Path(ge=1, le=10000)):
    for item in movies:
        if item['id'] == movie_id:
            return item
    return []

@app.get('/movies/', tags=['movies'])
def get_movies_by_title_and_category(title:str, category:str = Query(min_length=5, max_length=20)):
    return [ item for item in movies if item['title'] == title and item['category'] == category]

@app.post('/movies', tags=['movies'])
def create_movie(movie: Movie):
    movies.append(movie)
    return movies

@app.put('/movies/{movie_id}', tags=['movies'])
def put_movie(id:int, movie:Movie):
    for item in movies:
        if item['id'] == id:
            item['title'] = movie.title
            item['overview'] = movie.overview
            item['year'] = movie.year
            item['rating'] = movie.rating
            item['category'] = movie.category
            return movies
        
@app.delete('/movies/{movie_id}', tags=['movies'])
def delete_movie(id:int):
    for item in movies:
        if item['id'] == id:
            movies.remove(item)
            return movies