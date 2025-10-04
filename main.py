from fastapi import FastAPI
import models, database
from routers import usuarios, proveedores

app = FastAPI(title="API Vinilos")

# Crear tablas en la BD
models.Base.metadata.create_all(bind=database.engine)

# Incluir rutas
app.include_router(usuarios.router)
app.include_router(proveedores.router)

@app.get("/")
def home():
    return {"message": "API funcionando correctamente 🚀"}
