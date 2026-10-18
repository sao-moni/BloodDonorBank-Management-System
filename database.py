import mysql.connector
from mysql.connector import Error
class database:
    def __init__(self):
        self.conx=None
        self.connect_database()
    def connect_database(self):
        try:
            self.conx = mysql.connector.connect(
                host="localhost",
                user="root",
                password="monirtk@12",
                database="blooddonorbank"
            )
            print("Connection with database is successful")
        except Error as e:
            print("Connect to Database Error")

    def query_database(self,query_input:str):
        query=self.conx.cursor(dictionary=True)
        query.execute(query_input)
        results=query.fetchall()
        query.close()
        return results
