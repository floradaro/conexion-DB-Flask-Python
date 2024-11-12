import os
from flask_mysqldb import MySQL

mysql = MySQL()

app.config['MYSQL_HOST'] = os.getenv('MYSQLHOST', 'RAILWAY_PRIVATE_DOMAIN')
app.config['MYSQL_USER'] = os.getenv('MYSQLUSER', 'root')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQLPASSWORD', 'WMMsvicfJAYUoModynwlhAgjtbWkOaKt')
app.config['MYSQL_DB'] = os.getenv('MYSQLDATABASE', 'railway')
app.config['MYSQL_PORT'] = int(os.getenv('MYSQLPORT', 3306))

mysql.init_app(app)