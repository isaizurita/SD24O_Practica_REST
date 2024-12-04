#La clase base de las clases modelos
#Los modelos o clases modelo son las clases que mapean a las tablas
from orm.config import BaseClass
#Importar de SQAlchemy los tipos de datos que usan las tablas
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Float
#Para calcular la hora actual
import datetime

class Alumnos(BaseClass):
    __tablename__="alumnos"
    id=Column(Integer,primary_key=True)
    nombre=Column(String(100))
    edad=Column(Integer)
    domicilio=Column(String(100))
    carrera=Column(String(100))
    trimestre=Column(String(100))
    email=Column("email",String(100))
    password=Column(String(100))
    fecha_registro=Column(DateTime(timezone=True),default=datetime.datetime.now)

class Calificaciones(BaseClass):
    __tablename__="calificaciones"
    id=Column(Integer,primary_key=True)
    id_alumno=Column(Integer, ForeignKey(Alumnos.id))
    uea=Column(String(100))
    calificacion=Column(String(100))

class Fotos(BaseClass):
    __tablename__="fotos"
    id=Column(Integer,primary_key=True)
    id_alumno=Column(Integer, ForeignKey(Alumnos.id))
    titulo=Column(String(100))
    descripcion=Column(String(100))
    ruta=Column(String(100))



