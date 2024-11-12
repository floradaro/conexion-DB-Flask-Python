import os
from flask import Flask, request, jsonify, render_template, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Configura la conexión a la base de datos usando variables de entorno
def get_db_connection():
    return mysql.connector.connect(
        host=os.environ.get('MYSQLHOST', 'railway.railway.internal'),  # Usamos 'MYSQLHOST' que es la variable de entorno para el host privado
        user=os.environ.get('MYSQLUSER', 'root'),  # 'MYSQLUSER' contiene el usuario de la base de datos
        password=os.environ.get('MYSQLPASSWORD', ''),  # 'MYSQLPASSWORD' contiene la contraseña
        database=os.environ.get('MYSQLDATABASE', 'railway'),  # 'MYSQLDATABASE' contiene el nombre de la base de datos
        port=int(os.environ.get('MYSQLPORT', 3306))
    )

@app.route('/')
def home():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    myresult = cursor.fetchall()
    # Convertir los datos a diccionario
    insertObject = []
    columnNames = [column[0] for column in cursor.description]
    for record in myresult:
        insertObject.append(dict(zip(columnNames, record)))
    cursor.close()
    conn.close()
    return render_template('index.html', data=insertObject)

# Guardar usuarios
@app.route('/user', methods=['POST'])
def addUser():
    fullname = request.form.get('fullname')
    phone = request.form.get('phone')
    email = request.form.get('email')

    if fullname and phone and email:
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO users (fullname, phone, email) VALUES (%s, %s, %s)"
        data = (fullname, phone, email)
        cursor.execute(sql, data)
        conn.commit()
        cursor.close()
        conn.close()
    return redirect(url_for('home'))

@app.route('/delete/<string:id>')
def delete(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "DELETE FROM users WHERE id=%s"
    data = (id,)
    cursor.execute(sql, data)
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('home'))

@app.route('/edit/<string:id>', methods=['POST'])
def edit(id):
    fullname = request.form.get('fullname')
    phone = request.form.get('phone')
    email = request.form.get('email')

    if fullname and phone and email:
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = "UPDATE users SET fullname=%s, phone=%s, email=%s WHERE id=%s"
        data = (fullname, phone, email, id)
        cursor.execute(sql, data)
        conn.commit()
        cursor.close()
        conn.close()
    return redirect(url_for('home'))

if __name__ == '__main__':
    # Establece el host a 0.0.0.0 y el puerto utilizando la variable de entorno 'PORT'
    app.run(debug=True, host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
