import orm.modelos as modelos
from sqlalchemy.orm import Session
import orm.esquemas as esquemas

#SELECT * FROM app.alumnos
def lista_alumnos(sesion: Session):
    print("select * from app.alumnos");
    return sesion.query(modelos.Alumno).all();

#SELECT * FROM app.alumnos WHERE id={id_al}
def alumno_por_id(sesion: Session, id_alumno: int):
    print("select * from app.alumnos where id=", id_alumno);
    return sesion.query(modelos.Alumno).filter(modelos.Alumno.id==id_alumno).first();


#SELECT * FROM app.fotos
def lista_fotos(sesion: Session):
    print("select * from app.fotos");
    return sesion.query(modelos.Foto).all();

#SELECT * FROM app.fotos WHERE id={id_al}
def foto_por_id(sesion: Session, id_foto: int):
    print("select * from app.fotos where id=", id_foto);
    return sesion.query(modelos.Foto).filter(modelos.Foto.id==id_foto).first();

#SELECT * FROM app.fotos WHERE id_alumnos={id_al}
def foto_por_id_alumno(sesion: Session, id_alumno: int):
    print("select * from app.fotos where id=", id_alumno);
    return sesion.query(modelos.Foto).filter(modelos.Foto.id_alumno==id_alumno).all()


#SELECT * FROM app.calificaciones
def lista_calificaciones(sesion: Session):
    print("select * from app.calificaciones");
    return sesion.query(modelos.Calificacion).all();

#SELECT * FROM app.calificaciones WHERE id={id_fo}
def calificacion_por_id(sesion: Session, id_calificacion: int):
    print("select * from app.calificaciones where id=", id_calificacion);
    return sesion.query(modelos.Calificacion).filter(modelos.Calificacion.id==id_calificacion).first();

#SELECT * FROM app.calificaciones WHERE id_alumnos={id_al}
def calificaciones_por_id_alumno(sesion: Session, id_alumno: int):
    print("select * from app.calificaciones where id=", id_alumno);
    return sesion.query(modelos.Calificacion).filter(modelos.Calificacion.id_alumno==id_alumno).all()


#delete from app.fotos where id_alumno={id_alumno}
def borrar_fotos_por_id_alumno(sesion: Session, id_alumno: int):
    print("delete from app.fotos where id_alumno=", id_alumno);

    fotos_al=foto_por_id_alumno(sesion, id_alumno);

    if fotos_al is not None:
        for foto_alumno in fotos_al:
            sesion.delete(foto_alumno)
        sesion.commit()
        respuesta={
            "mensaje":"foto eliminada"
        }
        return respuesta

#delete from app.calificaciones where id_alumno={id_alumno}
def borrar_calificaciones_por_id_alumno(sesion: Session, id_alumno):
    print("delete from app.calificaciones where id_alumno=", id_alumno);

    calificaciones_al=calificaciones_por_id_alumno(sesion, id_alumno);

    if calificaciones_al is not None:
        for calificacion_alumno in calificaciones_al:
            sesion.delete(calificacion_alumno)
        sesion.commit();
        respuesta={
            "mensaje":"calificacion eliminada"
        }
        return respuesta

#delete from app.alumno where id=id_alumno
def borra_alumno_por_id(sesion: Session, id_alumno: int):
    print("delete from app.alumnos where id=", id_alumno);

    alumno=alumno_por_id(sesion, id_alumno)

    if alumno is not None:
        sesion.delete(alumno)
        sesion.commit()
    
    respuesta={
        "mensaje":"alumno eliminado"
    }
    return respuesta

#delete from app.fotos where id={id}
def borra_foto_por_id(sesion: Session, id_foto):
    print("delete from app.fotos where id=", id_foto);

    foto=foto_por_id(sesion, id_foto)

    if foto is not None:
        sesion.delete(foto)
        sesion.commit()
    
    respuesta={
        "mensaje":"foto eliminada"
    }
    return respuesta

#delete from app.calificaciones where id={id}
def borra_calificacion_por_id(sesion: Session, id_cal):
    print("delete from app.calificaciones where id=", id_cal);

    cal=calificacion_por_id(sesion, id_cal)

    if cal is not None:
        sesion.delete(cal)
        sesion.commit()
    
    respuesta={
        "mensaje":"calificación eliminada"
    }
    return respuesta

#PUT '/alumnos/{id}'
def actualiza_alumno(sesion: Session, id_alumno: int, alumno_esquema: esquemas.AlumnoBase):
    #Verificar que el alumno exista
    alumno_bd = alumno_por_id(sesion, id_alumno)
    if alumno_bd is not None:
        #Si existe, modificar la siguiente información
        alumno_bd.nombre = alumno_esquema.nombre
        alumno_bd.edad = alumno_esquema.edad
        alumno_bd.domicilio = alumno_esquema.domicilio
        alumno_bd.carrera = alumno_esquema.carrera
        alumno_bd.trimestre = alumno_esquema.trimestre
        alumno_bd.email = alumno_esquema.email
        alumno_bd.password = alumno_esquema.password
        #Confirmar los cambios
        sesion.commit()
        #Refrescar la base de datos
        sesion.refresh(alumno_bd)
        #Imprimir los nuevos datos
        print(alumno_esquema)
        return alumno_esquema
    else:
        respuesta={"mensaje":"No existe el alumno"}
        return respuesta

#PUT '/fotos/{id}'
def actualiza_foto(sesion: Session, id_foto: int, foto_esquema: esquemas.FotoBase):
    foto_bd = foto_por_id(sesion, id_foto)
    if foto_bd is not None:
        foto_bd.titulo = foto_esquema.titulo
        foto_bd.descripcion = foto_esquema.descripcion
        foto_bd.ruta = foto_esquema.ruta
        
        sesion.commit()
        sesion.refresh(foto_bd)
        print(foto_esquema)
        return foto_esquema
    
    else:
        respuesta={"mensaje":"No existe la foto"}
        return respuesta

#PUT '/calificaciones/{id}'
def actualiza_calificacion(sesion: Session, id_cal: int, cal_esquema: esquemas.CalificacionBase):
    cal_bd = calificacion_por_id(sesion, id_cal)
    if cal_bd is not None:
        cal_bd.uea = cal_esquema.uea
        cal_bd.calificacion = cal_esquema.calificacion
        
        sesion.commit()
        sesion.refresh(cal_bd)
        print(cal_esquema)
        return cal_esquema
    
    else:
        respuesta={"mensaje":"No existe la calificacion"}
        return respuesta

#POST '/alumnos'
def guardar_alumno(sesion: Session, alumno_esquema: esquemas.AlumnoBase):
    #Crear un nuevo objero de la clase modelo Alumno
    alumno_bd= modelos.Alumno()
    #Llenamos el nuevo objero con los parámetros que nos pasó el usuario
    alumno_bd.nombre = alumno_esquema.nombre
    alumno_bd.edad = alumno_esquema.edad
    alumno_bd.domicilio = alumno_esquema.domicilio
    alumno_bd.carrera = alumno_esquema.carrera
    alumno_bd.trimestre = alumno_esquema.trimestre
    alumno_bd.email = alumno_esquema.email
    alumno_bd.password = alumno_esquema.password
    #Insertar el nuevo objeto a la Base de Datos
    sesion.add(alumno_bd)
    #Confirmamos el cambio
    sesion.commit()
    #Hacemos un refresh
    sesion.refresh(alumno_bd)
    return alumno_bd

#POST '/alumnos/{id}/calificaciones
def guardar_calificacion(sesion: Session, alumno_id: int, cal_nueva: esquemas.CalificacionBase):
    # Verificar si el alumno existe utilizando alumno_por_id
    alumno = alumno_por_id(sesion, alumno_id)

    if not alumno:
        mensaje={"Mensaje":"Alumno no encontrado"}
        return mensaje

    else:
        # Crear un nuevo objeto de la clase modelo Compra
        cal_bd = modelos.Calificacion()
        # Llenar el nuevo objeto con los parámetros que nos pasó el usuario
        cal_bd.id_alumno = alumno_id
        cal_bd.uea = cal_nueva.uea
        cal_bd.calificacion = cal_nueva.calificacion

        # Insertar el nuevo objeto en la Base de Datos
        sesion.add(cal_bd)
        # Confirmar el cambio
        sesion.commit()
        # Hacer un refresh
        sesion.refresh(cal_bd)
        return cal_bd
    
#POST '/alumnos/{id}/fotos
def guardar_foto(sesion: Session, alumno_id: int, foto_nueva: esquemas.FotoBase):
    alumno = alumno_por_id(sesion, alumno_id)
    if not alumno:
        mensaje={"Mensaje":"Alumno no encontrado"}
        return mensaje
    else:
        foto_db = modelos.Foto()
        foto_db.id_alumno = alumno_id
        foto_db.titulo = foto_nueva.titulo
        foto_db.descripcion = foto_nueva.descripcion
        foto_db.ruta = foto_nueva.ruta
        sesion.add(foto_db)
        sesion.commit()
        sesion.refresh(foto_db)
        return foto_db