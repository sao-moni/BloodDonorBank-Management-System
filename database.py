import mysql.connector
from mysql.connector import Error


class database:

    def __init__(self):
        self.conx=None
        self.connect_database()
        self.query = self.conx.cursor(dict=True)

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

    def select_data(self,select_input:str):

        self.query.execute(select_input)
        results=self.query.fetchall()
        self.query.close()

        return results
    
    def insert_data(self,insert_input:str):

        self.query.execute(self.insert_data)
        results=self.query.commit()
        self.query.close()

        return results

