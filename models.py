from sqlalchemy import Column, Integer, String, Float, Enum, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
import enum

class RolEnum(str, enum.Enum):
    cliente = "Cliente"
    proveedor = "Proveedor"
    administrador = "Administrador"
    trabajador = "Trabajador"

# ---------- USUARIOS ----------
class Usuario(Base):
    __tablename__ = "usuarios"
    id_usuario = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    apellido = Column(String)
    correo = Column(String, unique=True)
    contraseña = Column(String)
    direccion = Column(String)
    rol = Column(Enum(RolEnum))

# ---------- PROVEEDORES ----------
class Proveedor(Base):
    __tablename__ = "proveedores"
    id_proveedor = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    correo = Column(String)
    telefono = Column(String)

# ---------- VINILOS ----------
class Vinilo(Base):
    __tablename__ = "vinilos"
    id_vinilo = Column(Integer, primary_key=True, index=True)
    titulo = Column(String)
    artista = Column(String)
    precio = Column(Float)
    stock = Column(Integer)

# ---------- CANCIONES ----------
class Cancion(Base):
    __tablename__ = "canciones"
    id_cancion = Column(Integer, primary_key=True, index=True)
    titulo = Column(String)
    duracion = Column(Float)
    artista = Column(String)
    genero = Column(String)

# ---------- ORDENES ----------
class Orden(Base):
    __tablename__ = "ordenes"
    id_orden = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"))
    total = Column(Float)
    estado = Column(String)

# ---------- REPORTES ----------
class Reporte(Base):
    __tablename__ = "reportes"
    id_reporte = Column(Integer, primary_key=True, index=True)
    titulo = Column(String)
    descripcion = Column(String)
    fecha = Column(String)

# ---------- CARRITOS ----------
class Carrito(Base):
    __tablename__ = "carritos"
    id_carrito = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"))
    total = Column(Float)

# ---------- PLAYLISTS ----------
class Playlist(Base):
    __tablename__ = "playlists"
    id_playlist = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"))
