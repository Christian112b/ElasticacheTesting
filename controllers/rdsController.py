import config 
import pandas as pd
import mysql.connector
from mysql.connector import Error



class rds():
    def __init__(self):

        self.host = config.RDS_HOST
        self.userdb = config.RDS_USER
        self.passdb = config.RDS_PASSWORD
        self.database = config.RDS_DATABASE

        self.connection = self.getConnection()

    def getConnection(self):
        try:
            # Conectar a la base de datos MySQL en RDS
            connection = mysql.connector.connect(
                host=self.host,
                user=self.userdb,
                password=self.passdb,
                database=self.database
            )

            return connection
        except Error as e:
            print(f"Error al conectar a RDS: {e}")
            return None


    def getQueryData(self, connection, query):
        if connection is not None:
            cursor = connection.cursor()
            try:
                cursor.execute(query)
                columns = [col[0] for col in cursor.description] 
                rows = cursor.fetchall()
                df = pd.DataFrame(rows, columns=columns)
                return df
            except Error as e:
                print(f"Error al ejecutar la consulta: {e}")
            finally:
                cursor.close()
        else:
            print("No hay conexión activa.")
            return None
    
        
    def closeConnection(self):
        if self.connection is not None:
            self.connection.close()
        else:
            print("No hay conexión activa para cerrar.")