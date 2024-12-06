from fastapi import FastAPI, UploadFile, File, Form, Depends, HTTPException
from typing import Optional, List
from pydantic import BaseModel
import shutil
import os
import uuid
import orm.repo as repo #Funciones para hacer consultas a la DB
from sqlalchemy.orm import Session
from orm.config import generador_sesion #Generador de sesiones

#Creación del servidor 
app = FastAPI();

#Get para obtener la lista de alumnos
@app.get("/alumnos")
def lista_alumnos(sesion: Session=Depends(generador_sesion)):
    print("Api consultando lista de alumnos");
    return repo.lista_alumnos(sesion);

#Get para obtener alumno por id
@app.get("/alumnos/{id}")
def alumno_por_id(id: int, sesion: Session=Depends(generador_sesion)):
    print("Api consultando alumno por id");
    return repo.alumno_por_id(sesion, id);

#Get para obtener la lista de fotos
@app.get("/fotos")
def lista_fotos(sesion: Session=Depends(generador_sesion)):
    print("Api consultando lista de fotos");
    return repo.lista_fotos(sesion);

#Get para obtener foto por id
@app.get("/fotos/{id}")
def foto_por_id(id: int, sesion: Session=Depends(generador_sesion)):
    print("Api consultando foto por id");
    return repo.foto_por_id(sesion, id);

#Get para obtener la lista de las calificaciones
@app.get("/calificaciones")
def lista_calificaciones(sesion: Session=Depends(generador_sesion)):
    print("Api consultando lista de calificaciones");
    return repo.lista_calificaciones(sesion);

#Get para obtener calificacion por id
@app.get("/calificaciones/{id}")
def calificaciones_por_id(id: int, sesion: Session=Depends(generador_sesion)):
    print("Api consultandfo calificacion por id");
    return repo.calificacion_por_id(sesion, id);

#Get para obtener calificacion por id de alumno
@app.get("/alumnos/{id}/calificaciones")
def calificaciones_por_id_alumno(id: int, sesion: Session=Depends(generador_sesion)):
    print("Api consultando calificaciones por alumno ", id);
    return repo.calificaciones_por_id_alumno(sesion, id);

@app.get

@app.delete("/usuario/{id}")
def borrar_alumno(id: int, sesion: Session=Depends(generador_sesion)):
    repo.borrar_calificaciones_por_id_alumno(sesion, id);
    repo.borrar_fotos_por_id_alumno(sesion, id);
    repo.borra_alumno_por_id(sesion, id)
    return {"status_borrado", "ok"}