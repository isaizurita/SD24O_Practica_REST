from fastapi import FastAPI, UploadFile, File, Form, Depends, HTTPException
from typing import Optional, List
from pydantic import BaseModel
import shutil
import os
import uuid
import orm.repo as repo #Funciones para hacer consultas a la DB
from sqlalchemy.orm import Session
from orm.config import generador_sesion #Generador de sesiones
import orm.esquemas as esquemas

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

#Get para obtener calificaciones por id de alumno
@app.get("/alumnos/{id}/calificaciones")
def calificaciones_por_id_alumno(id: int, sesion: Session=Depends(generador_sesion)):
    print("Api consultando calificaciones por alumno ", id);
    return repo.calificaciones_por_id_alumno(sesion, id);

#Get para obtener fotos por id de alumno
@app.get("/alumnos/{id}/fotos")
def fotos_por_id_alumno(id: int, sesion: Session=Depends(generador_sesion)):
    print("Api consultando fotos por alumno ", id);
    return repo.foto_por_id_alumno(sesion, id);


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


@app.delete("/alumnos/{id}")
def borrar_alumno(id: int, sesion: Session=Depends(generador_sesion)):
    repo.borrar_calificaciones_por_id_alumno(sesion, id);
    repo.borrar_fotos_por_id_alumno(sesion, id);
    repo.borra_alumno_por_id(sesion, id)
    return {"status_borrado", "ok"}

@app.delete("/fotos/{id}")
def borrar_foto(id: int, sesion: Session=Depends(generador_sesion)):
    repo.borra_foto_por_id(sesion, id);
    return {"status_borrado", "ok"}

@app.delete("/calicaciones/{id}")
def borrar_calificacion(id: int, sesion: Session=Depends(generador_sesion)):
    repo.borra_calificacion_por_id(sesion, id);
    return {"status_borrado", "ok"}

@app.delete("/alumnos/{id}/calificaciones")
def borrar_calificacion_por_id_alumno(id: int, sesion: Session=Depends(generador_sesion)):
    repo.borrar_calificaciones_por_id_alumno(sesion, id);
    return {"status_borrado":"ok"}

@app.delete("/alumnos/{id}/fotos")
def borrar_foto_por_id_alumno(id: int, sesion: Session=Depends(generador_sesion)):
    repo.borrar_fotos_por_id_alumno(sesion, id);
    return {"status_borrado":"ok"}

@app.put("/alumnos/{id}")
def actualizar_alumno(id: int, info_alumno: esquemas.AlumnoBase, sesion: Session=Depends(generador_sesion)):
    return repo.actualiza_alumno(sesion, id, info_alumno)

@app.put("/fotos/{id}")
def actualizar_foto(id: int, info_foto: esquemas.FotoBase, sesion: Session=Depends(generador_sesion)):
    return repo.actualiza_foto(sesion, id, info_foto)

@app.put("/calificaciones/{id}")
def actualizar_calificacion(id: int, info_cal: esquemas.CalificacionBase, sesion: Session=Depends(generador_sesion)):
    return repo.actualiza_calificacion(sesion, id, info_cal)

@app.post("/alumnos")
def guardar_alumno(alumno: esquemas.AlumnoBase, sesion: Session=Depends(generador_sesion)):
    print(alumno)
    return repo.guardar_alumno(sesion, alumno)

@app.post("/alumnos/{id}/calificaciones")
def guardar_calificacion(id: int, calificacion: esquemas.CalificacionBase, sesion: Session=Depends(generador_sesion)):
    return repo.guardar_calificacion(sesion, id, calificacion)

@app.post("/alumnos/{id}/fotos")
def guardar_foto(id: int, foto: esquemas.FotoBase, sesion: Session=Depends(generador_sesion)):
    return repo.guardar_foto(sesion, id, foto)