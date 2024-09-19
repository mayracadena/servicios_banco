import psycopg2

class Database:
    def __init__(self):
        self.host = "localhost"
        self.database = "servicios_banco"
        self.user = "postgres"
        self.password = "123"
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            self.cursor = self.connection.cursor()
            print("Se conectó a la base de datos")
        except psycopg2.Error as e:
            print(f"Eror en la conexión a la base de datos {e}")

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Se desconectó la base de datos")

    def execute_query(self, query):
        try:
            self.cursor.execute(query)
            self.connection.commit()
            return self.cursor.fetchall()
        except psycopg2.Error as e:
            print(f"No se pudo ejecutar la consulta {e}")

    def __del__(self):
        self.disconnect()


# Crear una instancia de la clase Database
db = Database()

# Intentar establecer la conexión
db.connect()

# Cerrar la conexión
db.disconnect()