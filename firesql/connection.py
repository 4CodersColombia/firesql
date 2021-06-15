
from typing import Text
from sqlalchemy import create_engine

user = "root"
password = "Cxkxdy6PDvm5lcA2"
host = "34.68.161.48"
port = "3306"
database = "subi_db"

class Firesql():
    connection = None
    
    def connect_sql(self,host_name:str, user_name:str, user_password:str,db_name:str,port=3306):
        try:
            conn =create_engine(f"mysql+pymysql://{user_name}:{user_password}@{host_name}:{port}/{db_name}")
            self.connection= conn.connect() 
            print("Connection to MySQL DB successful")
        except Exception as e:
            print(f"The error '{e}' occurred")





if '__main__'==__name__:
    db = Firesql()
    db.connect_sql(host,user,password,database)
    db.execute(Text("CREATE TABLE some_table (x int, y int)"))
    db.commit()
