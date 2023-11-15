# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 23:03:20 2023

@author: Daniela
"""


import datetime
import os
from peewee import *



# Verifica si el archivo existe
if os.path.exists('peliculas.db'):
    # Si existe, es eliminado
    os.remove('peliculas.db')
    
    
db = SqliteDatabase('peliculas.db')


class Actor(Model):
    nombre = CharField(max_length=120,unique=True)
    nacionalidad = CharField(max_length=120)

    class Meta:
        database = db

class Genero(Model):
    nombre = CharField(max_length=120)

    class Meta:
        database = db

class Productora(Model):
    nombre = CharField(max_length=120,unique=True)
    pais = CharField(max_length=120)
    
    class Meta:
        database = db
        
  
class Pelicula(Model):
    titulo = CharField(max_length=120, index=True)
    fecha_estreno = DateField()
    fecha_alta = DateField(default=datetime.datetime.now)
    actores = ManyToManyField(Actor, backref='peliculas')
    generos = ManyToManyField(Genero, backref='peliculas')
    productora = ForeignKeyField(Productora, backref='peliculas')

    class Meta:
        database = db


    
    
db.connect()
db.create_tables([Actor,
                  Genero,
                  Productora,
                  Pelicula,
                  Pelicula.actores.get_through_model(),
                  Pelicula.generos.get_through_model()]
                 )



actor_1 = Actor.create(nombre='Brad Pitt', nacionalidad='estadounidense')
actor_2 = Actor.create(nombre='Leonardo DiCaprio',nacionalidad='estadounidense')
actor_3 = Actor.create(nombre='Ryan Reynolds', nacionalidad='estadounidense')
#modificar
actor_3.nacionalidad = 'canadiense'
actor_3.save()
actor_4 = Actor.create(nombre='Sandra Bullock', nacionalidad='estadounidense')
actor_5 = Actor.create(nombre='Kate Winslet', nacionalidad='británica')



genero_1 = Genero.create(nombre='Ciencia Ficción')
genero_2 = Genero.create(nombre='Fantasía')
genero_3 = Genero.create(nombre='Comedia')
genero_4 = Genero.create(nombre='Romance')

productora_1 = Productora.create(nombre="20th Century Studios",pais="USA")
productora_2 = Productora.create(nombre="Touchstone Pictures", pais="USA")
productora_3 = Productora.create(nombre="Paramount Pictures",pais="USA")


pelicula_1 = Pelicula.create(titulo='Titanic', fecha_estreno=datetime.date(1998, 1, 1), productora=productora_1)
pelicula_1.autores = [actor_2, actor_5]
pelicula_1.generos = [genero_4]

pelicula_2 = Pelicula.create(titulo='La propuesta', fecha_estreno=datetime.date(2009, 6, 19), productora=productora_2)
pelicula_2.autores = [actor_3, actor_4]
pelicula_2.generos = [genero_3, genero_4]

pelicula_3 = Pelicula.create(titulo='Deadpool', fecha_estreno=datetime.date(2016, 2, 11), productora=productora_1)
pelicula_3.autores = [actor_3]
pelicula_3.generos = [genero_2, genero_3]


actores = Actor.select()


for a in actores:
    print(f"Actor: {a.nombre}")