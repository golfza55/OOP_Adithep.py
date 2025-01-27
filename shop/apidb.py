import database
mycursor = database.mydb.cursor()

#----------------------------------------------------------------#
def selectdb(table):
    sql = f"SELECT * FROM products"
    mycursor.execute(sql)
    show = mycursor.fetchall()
    return show
#print(selectdb("users"))

#----------------------------------------------------------------#


product_id = 10
product_name = "test"
description = "noob"
price = 500
stock = 20 
def insert_products(product_id,product_name,description,price,stock):
    sql = "INSERT INTO products VALUES (%s,%s,%s,%s,%s)"
    val_sql = (product_id,product_name,description,price,stock)
    mycursor.execute(sql,val_sql)
    database.mydb.commit() 
    if mycursor.rowcount > 0:
        return True
    else:
        return False
#print(insert_products('test',5000,50))


#----------------------------------------------------------------#


def deleteadb(table,id_name,id):
    sql = f"DELETE FROM  product WHERE product_id = 2"
    val_sql = (id)
    mycursor.execute(sql,valsql)
    database.mydb.commit()
    if mycursor.rowcount > 0:
         return True
    else:
         return False
#print(deletedo('users','id_user',2))



def edintdb(table,column,id_name,id,val):
sql = f"UPDATE {table} SET {column} = %s WHERE {id_name} = %s "
val_sql = (val,id)
mycursor.execute(sql,val_sql)
database.mydb.commit()   
if mycursor.rowcount > 0:
    return True
else:
    return False
print(edintdb('product',"name_product","id_product",1,"lauwa"))
