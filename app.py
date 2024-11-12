from flask import Flask, request, jsonify, render_template
import os
import mysql.connector

app = Flask(__name__)

# Configuración de la base de datos
db_config = {
    'user': 'root',
    'password': 'gFnBMkOKsYoOlZbwNanXgUVKkmQkNrmU',
    'host': 'mysql.railway.internal',
    'database': 'railway'
}

def get_db_connection():
    conn = mysql.connector.connect(**db_config)
    return conn

@app.route('/')
def home():
    return render_template('index.html')

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
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get("PORT", 3306)))
