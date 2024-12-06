import orm.modelos as modelos
from sqlalchemy.orm import Session
from sqlalchemy import and_

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