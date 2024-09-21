import mysql.connector


def create_connection(host, user, password, database):
    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        cursor = conn.cursor()
        print("Conexión a la base de datos establecida.")
        return conn, cursor
    except mysql.connector.Error as err:
        print(f"Error al conectar a la base de datos: {err}")
        exit(1)
