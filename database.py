import mysql.connector

config = {
    'user': 'root',
    'password': 'UEtMHcrWSH8LSh0tjS4I',
    'host': 'containers-us-west-148.railway.app',
    'database': 'railway',
    'port': 5958  # Puerto predeterminado de MySQL
}
database = mysql.connector.connect(**config)

print('BBDD conectada!!')
