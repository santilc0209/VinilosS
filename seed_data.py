from database import SessionLocal, engine
import models
from faker import Faker
import random

# Crear BD y tablas
models.Base.metadata.create_all(bind=engine)
db = SessionLocal()
fake = Faker()

# ----------- USUARIOS -----------
roles = ["Cliente", "Proveedor", "Administrador", "Trabajador"]
usuarios = []
for i in range(20):
    user = models.Usuario(
        nombre=fake.first_name(),
        apellido=fake.last_name(),
        correo=f"usuario{i}@gmail.com",
        contraseña="1234",
        direccion=fake.city(),
        rol=random.choice(roles)
    )
    usuarios.append(user)
    db.add(user)

# ----------- PROVEEDORES -----------
proveedores = []
for i in range(20):
    proveedor = models.Proveedor(
        nombre=fake.company(),
        correo=f"proveedor{i}@empresa.com",
        telefono=fake.phone_number()
    )
    proveedores.append(proveedor)
    db.add(proveedor)

# ----------- VINILOS -----------
vinilos = []
for i in range(20):
    vinilo = models.Vinilo(
        titulo=fake.sentence(nb_words=3),
        artista=fake.name(),
        precio=round(random.uniform(50_000, 300_000), 2),
        stock=random.randint(5, 100)
    )
    vinilos.append(vinilo)
    db.add(vinilo)

# ----------- CANCIONES -----------
canciones = []
for i in range(20):
    cancion = models.Cancion(
        titulo=fake.catch_phrase(),
        duracion=round(random.uniform(2.5, 5.5), 2),
        artista=fake.name(),
        genero=random.choice(["Rock", "Pop", "Jazz", "Indie", "Reggaeton"])
    )
    canciones.append(cancion)
    db.add(cancion)

# ----------- ORDENES -----------
ordenes = []
for i in range(20):
    orden = models.Orden(
        id_usuario=random.randint(1, 20),
        total=round(random.uniform(100_000, 600_000), 2),
        estado=random.choice(["Pendiente", "Pagada", "Cancelada"])
    )
    ordenes.append(orden)
    db.add(orden)

# ----------- REPORTES -----------
reportes = []
for i in range(20):
    reporte = models.Reporte(
        titulo=f"Reporte #{i+1}",
        descripcion=fake.text(max_nb_chars=100),
        fecha=str(fake.date_this_year())
    )
    reportes.append(reporte)
    db.add(reporte)

# ----------- CARRITOS -----------
carritos = []
for i in range(20):
    carrito = models.Carrito(
        id_usuario=random.randint(1, 20),
        total=round(random.uniform(80_000, 300_000), 2)
    )
    carritos.append(carrito)
    db.add(carrito)

# ----------- PLAYLISTS -----------
playlists = []
for i in range(20):
    playlist = models.Playlist(
        nombre=f"Playlist {i+1}",
        id_usuario=random.randint(1, 20)
    )
    playlists.append(playlist)
    db.add(playlist)

# Confirmar cambios
db.commit()
db.close()

print("✅ Base de datos poblada con datos de ejemplo (20 registros por tabla).")
