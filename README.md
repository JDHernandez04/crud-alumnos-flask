# Práctica Técnica: Consumo de API REST - CRUD de Alumnos

Aplicación web desarrollada en **Python** con el microframework **Flask** para gestionar el catálogo de alumnos consumiendo el API REST de prueba.

## 🛠️ Tecnologías Utilizadas
* **Lenguaje:** Python 3.10+
* **Backend:** Flask (`requests` para el consumo HTTP y `python-dotenv` para variables de entorno).
* **Frontend:** HTML5, Jinja2 y Bootstrap 5.

## 🚀 Instrucciones de Instalación y Ejecución

1. **Clonar el repositorio:**
   ```bash
   git clone <url-de-tu-repositorio>
   cd crud-alumnos-flask

2. **Crear y activar entorno virtual**
    # En Windows:
    python -m venv venv
    venv\Scripts\activate

    # En macOS / Linux:
    python3 -m venv venv
    source venv/bin/activate

3. **Instalar dependencias**
    pip install -r requirements.txt

4. **Configurar variables de entorno**
    # Crear archivo .env basandose en el .env.example con su propio token
    API_TOKEN=tu_token_aqui
    FLASK_SECRET_KEY=mi_clave_secreta

5. **Ejecutar servidor de desarrollo**
    python app.py
    # Abre en el navegador: http://127.0.0.1:5000