import mysql.connector
class mydb:
    def __init__(self,host,user,password,database):
        self.mydb = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = database
        )
        self.mycursor = self.mydb.cursor()

    def selectdb(self,table):
        sql = f"SELECT * FROM {table}"
        self.mycursor.execute(sql)
        show = self.mycursor.fetchall()
        return show

    def insert(self,table,columns,values):
        sql = f"INSERT INTO {table} ({columns}) VALUES {values}"
        self.mycursor.execute(sql)
        self.mydb.commit()
        if self.mycursor.rowcount > 0:
            return True
        else:
            return False

    def deletedb(self,table,id_name,id):
        sql = f"DELETE FROM {table} WHERE {id_name} = {id}"
        self.mycursor.execute(sql)
        self.mydb.commit()
        if self.mycursor.rowcount > 0:
            return True
        else:
            return False

    def editdb(self,table,column,id_name,values,id):
        sql = f"UPDATE {table} SET {column} = {values} WHERE {id_name} = {id}"
        self.mycursor.execute(sql)
        self.mydb.commit()
        if self.mycursor.rowcount > 0:
            return True
        else:
            return False

shop1_db = mydb("localhost","root","1234","shop")
db1 = mydb("localhost","root","1234","golf21")

print(shop1_db.deletedb("orders","order_id",115))
print(db1.selectdb("list"))