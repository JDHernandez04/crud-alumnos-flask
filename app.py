import os
from flask import Flask, render_template, request, redirect, url_for, flash
import api_service as api

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "dev_secret_key")

@app.route("/")
def index():
    page = request.args.get("page", 1, type=int)
    q = request.args.get("q", "").strip()
    
    status, respuesta = api.listar_alumnos(page=page, per_page=10, q=q)
    
    if status == 200 and respuesta.get("success"):
        data = respuesta.get("data", {})
        return render_template(
            "index.html",
            alumnos=data.get("alumnos", []),
            total=data.get("total", 0),
            page=data.get("page", 1),
            total_pages=data.get("total_pages", 1),
            q=q
        )
    else:
        error_msg = respuesta.get("error", "Error al conectar con el API. Verifica tu token.")
        flash(error_msg, "danger")
        return render_template("index.html", alumnos=[], total=0, page=1, total_pages=1, q=q)

@app.route("/alumnos/nuevo", methods=["GET", "POST"])
def nuevo_alumno():
    if request.method == "POST":
        datos = {
            "matricula": request.form.get("matricula", "").strip().upper(),
            "curp": request.form.get("curp", "").strip().upper(),
            "paterno": request.form.get("paterno", "").strip().upper(),
            "materno": request.form.get("materno", "").strip().upper(),
            "nombre": request.form.get("nombre", "").strip().upper()
        }
        
        status, respuesta = api.crear_alumno(datos)
        
        if status == 201 and respuesta.get("success"):
            flash("¡Alumno registrado exitosamente!", "success")
            return redirect(url_for("index"))
        else:
            # Capturamos el mensaje principal y el diccionario de errores (si es 422)
            error_msg = respuesta.get("error", "No se pudo crear el alumno.")
            errores_campo = respuesta.get("errores", {})
            flash(error_msg, "danger")
            return render_template("form.html", accion="Crear", alumno=datos, errores=errores_campo)
            
    return render_template("form.html", accion="Crear", alumno={}, errores={})

@app.route("/alumnos/<int:alumno_id>/editar", methods=["GET", "POST"])
def editar_alumno(alumno_id):
    if request.method == "POST":
        datos = {
            "matricula": request.form.get("matricula", "").strip().upper(),
            "curp": request.form.get("curp", "").strip().upper(),
            "paterno": request.form.get("paterno", "").strip().upper(),
            "materno": request.form.get("materno", "").strip().upper(),
            "nombre": request.form.get("nombre", "").strip().upper()
        }
        
        status, respuesta = api.actualizar_alumno(alumno_id, datos)
        
        if status == 200 and respuesta.get("success"):
            flash("¡Datos del alumno actualizados correctamente!", "success")
            return redirect(url_for("index"))
        else:
            error_msg = respuesta.get("error", "Error al actualizar los datos.")
            errores_campo = respuesta.get("errores", {})
            flash(error_msg, "danger")
            datos["id"] = alumno_id
            return render_template("form.html", accion="Editar", alumno=datos, errores=errores_campo)

    # Si es petición GET, consultamos los datos actuales del alumno
    status, respuesta = api.obtener_alumno(alumno_id)
    if status == 200 and respuesta.get("success"):
        alumno = respuesta["data"]["alumno"]
        return render_template("form.html", accion="Editar", alumno=alumno, errores={})
    else:
        flash(respuesta.get("error", "Alumno no encontrado."), "warning")
        return redirect(url_for("index"))

@app.route("/alumnos/<int:alumno_id>/eliminar", methods=["POST"])
def eliminar_alumno(alumno_id):
    status, respuesta = api.eliminar_alumno(alumno_id)
    if status == 204:
        flash("Alumno eliminado correctamente.", "success")
    else:
        flash(respuesta.get("error", "Error al intentar eliminar el alumno."), "danger")
    return redirect(url_for("index"))

@app.route("/reset", methods=["POST"])
def reset_sandbox():
    status, respuesta = api.resetear_sandbox()
    if status == 200 and respuesta.get("success"):
        flash("El sandbox se ha restaurado a los 20 alumnos de ejemplo.", "info")
    else:
        flash("No se pudo restaurar el sandbox.", "danger")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True, port=5000)