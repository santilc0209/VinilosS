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
   git clone https://github.com/TU_USUARIO/fastapi-vinilos.git
   cd fastapi-vinilos

2. Crear y activar entorno virtual:
   python -m venv venv
   source venv/bin/activate   # Mac/Linux
   venv\Scripts\activate      # Windows

3. Instalar dependencias:
   pip install -r requirements.txt

---

## ▶️ Ejecutar el servidor

uvicorn main:app --reload

Servidor corriendo en:  
👉 http://127.0.0.1:8000  
Documentación interactiva:  
👉 http://127.0.0.1:8000/docs

---

## 📊 Poblar la Base de Datos

Ejecuta el script de semillas para generar 20 registros de prueba en cada tabla:

python seed_data.py

---

## 📬 Uso en Postman

Se incluye colección **CRUD** para todas las tablas:

- `GET /tabla/` → lista todos
- `GET /tabla/{id}` → trae por ID
- `POST /tabla/` → crea nuevo registro
- `PATCH /tabla/{id}` → actualiza registro
- `DELETE /tabla/{id}` → elimina registro

Ejemplo `POST /usuarios/`
{
  "nombre": "Santiago",
  "apellido": "López",
  "correo": "santi@gmail.com",
  "contraseña": "1234",
  "direccion": "Bogotá",
  "rol": "Cliente"
}

---

## 📂 Endpoints por entidad

Usuarios → /usuarios  
Proveedores → /proveedores  
Vinilos → /vinilos  
Canciones → /canciones  
Órdenes → /ordenes  
Reportes → /reportes  
Carritos → /carritos  
Playlists → /playlists  

---

## 🛠️ Tecnologías
- FastAPI
- SQLAlchemy
- SQLite
- Uvicorn
- Faker

---

## 👨‍💻 Autor
Santiago López Cative
