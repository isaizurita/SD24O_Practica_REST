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

#SELECT * FROM app.fotos WHERE id_alumnos={id_al}
def foto_por_id(sesion: Session, id_foto: int):
    print("select * from app.fotos where id=", id_foto);
    return sesion.query(modelos.Foto).filter(modelos.Foto.id==id_foto).first();

#SELECT * FROM app.calificaciones
def lista_calificaciones(sesion: Session):
    print("select * from app.calificaciones");
    return sesion.query(modelos.Calificacion).all();

#SELECT * FROM app.calificaciones WHERE id={id_fo}
def calificacion_por_id(sesion: Session, id_calificacion: int):
    print("select * from app.calificaciones where id=", id_calificacion);
    return sesion.query(modelos.Calificacion).filter(modelos.Calificacion.id==id_calificacion).first();