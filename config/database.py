import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base #esto servirá para manipular todas las tablas de mi bd

sqlite_file_name = '../database.sqlite'
base_dir = os.path.dirname(os.path.realpath(__file__)) #esto me lee este directorio: database.py

database_url = f'sqlite:///{os.path.join(base_dir, sqlite_file_name)}'

engine = create_engine(database_url, echo=True) #echo es para que muestre en consola lo que pasa en la bd

Session = sessionmaker(bind=engine)

Base = declarative_base()