from flask import Flask, render_template, request, redirect, url_for
import database as db

app = Flask(__name__)

@app.route('/')
def home():
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM users")
    myresult = cursor.fetchall()
    #vamos a convertir los datos a diccionario
    insertObject = []
    columnNames = [column[0] for column in cursor.description]
    for record in myresult:
        insertObject.append(dict(zip(columnNames, record)))
    cursor.close()
    return render_template('index.html', data=insertObject)

#Guardar usuarios
@app.route('/user', methods=['POST'])
def addUser():
    fullname = request.form.get('fullname')
    phone = request.form.get('phone')
    email = request.form.get('email')

    if fullname and phone and email:
        cursor = db.database.cursor()
        sql = "INSERT INTO users (fullname, phone, email) VALUES (%s, %s, %s)"
        data = (fullname, phone, email)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('home'))

@app.route('/delete/<string:id>')
def delete(id):
    cursor = db.database.cursor()
    sql = "DELETE FROM users WHERE id=%s"
    data = (id,)
    cursor.execute(sql, data)
    db.database.commit()
    return redirect(url_for('home'))

@app.route('/edit/<string:id>', methods=['POST'])
def edit(id):
    fullname = request.form.get('fullname')
    phone = request.form.get('phone')
    email = request.form.get('email')

    if fullname and phone and email:
        cursor = db.database.cursor()
        sql = "UPDATE users SET fullname =%s, phone= %s, email=%s WHERE id = %s"
        data = (fullname, phone, email, id)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
