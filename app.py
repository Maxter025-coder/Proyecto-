from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Configuración de la conexión con MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="gestion_recursos_humanos"
)

# Ruta para ver la lista de empleados (Read)
@app.route('/empleados')
def empleados():
    cursor = db.cursor(dictionary=True)
    cursor.execute("""
        SELECT e.id_empleado, e.nombre, e.direccion, p.nombre AS puesto, e.salario 
        FROM empleados e 
        JOIN puestos p ON e.puesto_id = p.id_puesto
    """)
    empleados = cursor.fetchall()
    cursor.close()
    return render_template("empleados.html", empleados=empleados)

# Ruta para mostrar el formulario de agregar un empleado
@app.route('/empleado/nuevo', methods=['GET', 'POST'])
def agregar_empleado():
    cursor = db.cursor(dictionary=True)
    if request.method == 'POST':
        nombre = request.form['nombre']
        direccion = request.form['direccion']
        puesto_id = request.form['puesto_id']
        salario = request.form['salario']
        cursor.execute(
            "INSERT INTO empleados (nombre, direccion, puesto_id, salario) VALUES (%s, %s, %s, %s)", 
            (nombre, direccion, puesto_id, salario)
        )
        db.commit()
        cursor.close()
        return redirect(url_for('empleados'))
    
    cursor.execute("SELECT id_puesto, nombre FROM puestos")
    puestos = cursor.fetchall()
    cursor.close()
    return render_template("nuevo_empleado.html", puestos=puestos)

# Ruta para editar un empleado
@app.route('/empleado/<int:id_empleado>/editar', methods=['GET', 'POST'])
def editar_empleado(id_empleado):
    cursor = db.cursor(dictionary=True)
    if request.method == 'POST':
        nombre = request.form['nombre']
        direccion = request.form['direccion']
        puesto_id = request.form['puesto_id']
        salario = request.form['salario']
        cursor.execute(
            "UPDATE empleados SET nombre = %s, direccion = %s, puesto_id = %s, salario = %s WHERE id_empleado = %s",
            (nombre, direccion, puesto_id, salario, id_empleado)
        )
        db.commit()
        cursor.close()
        return redirect(url_for('empleados'))
    
    cursor.execute("SELECT * FROM empleados WHERE id_empleado = %s", (id_empleado,))
    empleado = cursor.fetchone()
    cursor.execute("SELECT id_puesto, nombre FROM puestos")
    puestos = cursor.fetchall()
    cursor.close()
    return render_template('editar_empleado.html', empleado=empleado, puestos=puestos)

# Ruta para eliminar un empleado
@app.route('/empleado/<int:id_empleado>/eliminar', methods=['POST'])
def eliminar_empleado(id_empleado):
    cursor = db.cursor()
    cursor.execute("DELETE FROM empleados WHERE id_empleado = %s", (id_empleado,))
    db.commit()
    cursor.close()
    return redirect(url_for('empleados'))

# Ruta de inicio para redirigir a la lista de empleados
@app.route('/')
def inicio():
    return redirect(url_for('empleados'))

if __name__ == '__main__':
    # Cambia host a '0.0.0.0' para acceso desde otros dispositivos en la misma red local
    app.run(host='0.0.0.0', port=5000, debug=True)




    

