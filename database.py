import mysql.connector
from mysql.connector import Error


class database:

    def __init__(self):
        self.conx=None
        self.connect_database()
        self.query = self.conx.cursor()

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
    
    def modify_data(self,insert_update_delete_input:str):
        self.query.execute(insert_update_delete_input)
        self.conx.commit()
        self.query.close()
        rowcount= self.query.rowcount
        print(rowcount)
    
db = database()

user=db.select_data("select * from tbldonor")
print(user)
