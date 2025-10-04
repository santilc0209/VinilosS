from pydantic import BaseModel
import enum

# -------- ENUM --------
class RolEnum(str, enum.Enum):
    cliente = "Cliente"
    proveedor = "Proveedor"
    administrador = "Administrador"
    trabajador = "Trabajador"

# -------- USUARIOS --------
class UsuarioBase(BaseModel):
    nombre: str
    apellido: str
    correo: str
    direccion: str
    rol: RolEnum

class UsuarioCreate(UsuarioBase):
    contraseña: str

class UsuarioOut(UsuarioBase):
    id_usuario: int
    class Config:
        from_attributes = True

# -------- PROVEEDORES --------
class ProveedorBase(BaseModel):
    nombre: str
    correo: str
    telefono: str

class ProveedorCreate(ProveedorBase):
    pass

class ProveedorOut(ProveedorBase):
    id_proveedor: int
    class Config:
        from_attributes = True
