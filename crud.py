from sqlalchemy.orm import Session
import models, schemas

# -------- CRUD USUARIOS --------
def get_usuarios(db: Session):
    return db.query(models.Usuario).all()

def get_usuario(db: Session, user_id: int):
    return db.query(models.Usuario).filter(models.Usuario.id_usuario == user_id).first()

def create_usuario(db: Session, usuario: schemas.UsuarioCreate):
    nuevo = models.Usuario(**usuario.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def delete_usuario(db: Session, user_id: int):
    usuario = get_usuario(db, user_id)
    if usuario:
        db.delete(usuario)
        db.commit()
    return usuario

def update_usuario(db: Session, user_id: int, datos: dict):
    usuario = get_usuario(db, user_id)
    if not usuario:
        return None
    for key, value in datos.items():
        setattr(usuario, key, value)
    db.commit()
    db.refresh(usuario)
    return usuario
