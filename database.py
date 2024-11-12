import os
import MySQLdb  # Asegúrate de tener este paquete instalado

# Conexión a la base de datos usando las variables de entorno proporcionadas por Railway
database = MySQLdb.connect(
    host=os.getenv('MYSQLHOST', 'RAILWAY_PRIVATE_DOMAIN'),  # Host de la base de datos, por defecto usará el valor proporcionado
    user=os.getenv('MYSQLUSER', 'root'),  # Usuario de la base de datos, por defecto 'root'
    password=os.getenv('MYSQLPASSWORD', 'WMMsvicfJAYUoModynwlhAgjtbWkOaKt'),  # Contraseña proporcionada por Railway
    database=os.getenv('MYSQLDATABASE', 'railway'),  # Nombre de la base de datos proporcionado por Railway
    port=int(os.getenv('MYSQLPORT', 3306))  # Puerto de la base de datos, por defecto 3306
)