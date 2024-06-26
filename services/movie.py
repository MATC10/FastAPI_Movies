from models.movie import Movie as MovieModel
from schemas.movie import Movie

class MovieService():
    def __init__(self, db) -> None:
        self.db = db
        
    def get_movies(self):
        result = self.db.query(MovieModel).all()
        return result
    
    def get_movie(self, id: int):
        result = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        return result
    
    def get_movies_by_title_and_category(self, title:str, category:str):
        result = self.db.query(MovieModel).filter(MovieModel.title == title and MovieModel.category == category).all()
        return result
    
    def create_movie(self, movie:Movie):
        new_movie = MovieModel(**movie.model_dump()) #EN EL CASO DE CREAR OBJETO NUEVO **
        self.db.add(new_movie)
        self.db.commit()
        return
    
    def put_movie(self, id: int, data:Movie):
            movie = self.db.query(MovieModel).filter(MovieModel.id == id).first()

            # Obtén todos los campos del modelo Movie
            fields = [f for f in MovieModel.__table__.columns.keys()]

            for field in fields:
                # Si el campo está en data, actualízalo. Si no, establece el campo en None.
                setattr(movie, field, data.model_dump().get(field, None))

            self.db.commit()
            return
    
    def delete_movie(self, id: int):
        self.db.query(MovieModel).filter(MovieModel.id == id).delete()
        self.db.commit()
        
    def patch_movie(self, id: int, data:Movie):
        movie = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        for key, value in data.model_dump().items():
            setattr(movie, key, value)
        self.db.commit()
        return
        