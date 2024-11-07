import mysql.connector
database = mysql.connector.connect(
    #host = 'sql' cuando tengamos un hosting
    user = 'root',
    password = '',
    database = 'contactsdb'
)