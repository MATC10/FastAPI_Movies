from pydantic import BaseModel, Field
from typing import Optional, List

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