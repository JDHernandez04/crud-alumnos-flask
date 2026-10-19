import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://panel360.mx/api/escolares/practica/v1"
TOKEN = os.getenv("API_TOKEN")

def get_headers():
    """Genera los encabezados de autenticación requeridos por el API."""
    return {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

def listar_alumnos(page=1, per_page=10, q=""):
    """Obtiene la lista paginada o filtrada de alumnos (GET /alumnos)."""
    params = {"page": page, "per_page": per_page}
    if q:
        params["q"] = q
    response = requests.get(f"{BASE_URL}/alumnos", headers=get_headers(), params=params)
    return response.status_code, response.json()

def obtener_alumno(alumno_id):
    """Obtiene el detalle de un alumno por su ID (GET /alumnos/{id})."""
    response = requests.get(f"{BASE_URL}/alumnos/{alumno_id}", headers=get_headers())
    return response.status_code, response.json()

def crear_alumno(datos):
    """Crea un alumno nuevo (POST /alumnos)."""
    response = requests.post(f"{BASE_URL}/alumnos", headers=get_headers(), json=datos)
    return response.status_code, response.json()

def actualizar_alumno(alumno_id, datos):
    """Reemplaza todos los datos de un alumno (PUT /alumnos/{id})."""
    response = requests.put(f"{BASE_URL}/alumnos/{alumno_id}", headers=get_headers(), json=datos)
    return response.status_code, response.json()

def eliminar_alumno(alumno_id):
    """Elimina un alumno (DELETE /alumnos/{id})."""
    response = requests.delete(f"{BASE_URL}/alumnos/{alumno_id}", headers=get_headers())
    # El código 204 (No Content) no devuelve cuerpo JSON
    if response.status_code == 204:
        return 204, {"success": True}
    return response.status_code, response.json()

def resetear_sandbox():
    """Restaura el sandbox a los 20 alumnos originales (POST /reset)."""
    response = requests.post(f"{BASE_URL}/reset", headers=get_headers())
    return response.status_code, response.json()