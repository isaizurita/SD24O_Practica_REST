from pydantic import BaseModel

#Esquema Alumno
class AlumnoBase(BaseModel):
    nombre:str
    edad:int
    domicilio:str
    carrera:str
    trimestre:str
    email:str
    password:str

#Esquema Calificación
class CalificacionBase(BaseModel):
    uea:str
    calificacion:str

#Esquema Foto
class FotoBase(BaseModel):
    titulo:str
    descripcion:str
    ruta:str