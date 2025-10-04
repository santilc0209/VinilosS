# 🎵 FastAPI CRUD - Sistema de Vinilos

Proyecto backend en **FastAPI + SQLAlchemy** que implementa un sistema CRUD completo para la gestión de:

- Usuarios
- Proveedores
- Vinilos
- Canciones
- Órdenes
- Reportes
- Carritos
- Playlists

Cada entidad cuenta con **4 métodos principales**:
- `GET` (todos)
- `GET/{id}` (por id)
- `POST` (crear)
- `PATCH` (actualizar)
- `DELETE` (eliminar)

---

## 🚀 Requisitos
- Python 3.10+
- Virtualenv
- SQLite (incluido por defecto)

---

## ⚙️ Instalación

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/TU_USUARIO/fastapi-vinilos.git
   cd fastapi-vinilos
Crear y activar entorno virtual:

bash
Copiar código
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
Instalar dependencias:

bash
Copiar código
pip install -r requirements.txt
▶️ Ejecutar el servidor
bash
Copiar código
uvicorn main:app --reload
Servidor corriendo en:
👉 http://127.0.0.1:8000
Documentación interactiva:
👉 http://127.0.0.1:8000/docs

📊 Poblar la Base de Datos
Ejecuta el script de semillas para generar 20 registros de prueba en cada tabla:

bash
Copiar código
python seed_data.py
📬 Uso en Postman
Se incluye colección CRUD para todas las tablas:

GET /tabla/ → lista todos

GET /tabla/{id} → trae por ID

POST /tabla/ → crea nuevo registro

PATCH /tabla/{id} → actualiza registro

DELETE /tabla/{id} → elimina registro

Ejemplo POST /usuarios/
json
Copiar código
{
  "nombre": "Santiago",
  "apellido": "López",
  "correo": "santi@gmail.com",
  "contraseña": "1234",
  "direccion": "Bogotá",
  "rol": "Cliente"
}
📂 Endpoints por entidad
Usuarios
GET /usuarios/

GET /usuarios/{id}

POST /usuarios/

PATCH /usuarios/{id}

DELETE /usuarios/{id}

Proveedores
GET /proveedores/

GET /proveedores/{id}

POST /proveedores/

PATCH /proveedores/{id}

DELETE /proveedores/{id}

Vinilos
GET /vinilos/

GET /vinilos/{id}

POST /vinilos/

PATCH /vinilos/{id}

DELETE /vinilos/{id}

Canciones
GET /canciones/

GET /canciones/{id}

POST /canciones/

PATCH /canciones/{id}

DELETE /canciones/{id}

Órdenes
GET /ordenes/

GET /ordenes/{id}

POST /ordenes/

PATCH /ordenes/{id}

DELETE /ordenes/{id}

Reportes
GET /reportes/

GET /reportes/{id}

POST /reportes/

PATCH /reportes/{id}

DELETE /reportes/{id}

Carritos
GET /carritos/

GET /carritos/{id}

POST /carritos/

PATCH /carritos/{id}

DELETE /carritos/{id}

Playlists
GET /playlists/

GET /playlists/{id}

POST /playlists/

PATCH /playlists/{id}

DELETE /playlists/{id}

🛠️ Tecnologías
FastAPI

SQLAlchemy

SQLite

Uvicorn

Faker (para generar datos falsos)
