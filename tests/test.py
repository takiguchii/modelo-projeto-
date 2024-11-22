import mysql.connector
from mysql.connector import Error

def connect_to_database():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="",
            password="",
            database=""
        )
        if conn.is_connected():
            print("Conectado ao banco com sucesso!")
            return conn
    except Error as e:
        print("Conexão falhou!")
        return None
    
def main():
    conn = connect_to_database()
    
if __name__ == "__main__":
    main()