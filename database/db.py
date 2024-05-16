import pymysql
##import records

db_host = 'database-1.cdi6eaea22b2.us-east-1.rds.amazonaws.com'
db_user = 'admin'
db_passw = 'Admin123'
db_name = 'db_users'

def connectionSQL():
    try:
        connection = pymysql.connect(
            host = db_host,
            user = db_user,
            password = db_passw,
            database = db_name
            )
        print("succesfull connection to DB")
        return connection 
    except Exception as err:    
        print("Error conectando a la DB")
        return None 
        
def insert_records(id, name, category, price):
     query = "INSERT INTO users (id, name, lastname, birthday) VALUES ("+id+", '"+name+"','"+category+"','"+price+"')"
     try:
        connection = connectionSQL()
        if connection != None:
            cursor = connection.cursor()   
            cursor.execute(query)
            connection.commit()
            print("producto Agregado")
            return True
        else:
            print("error en agregar producto")
            return False
        
     except Exception as err:  ##Esto me faltó revalidarlo
        print ("error creating user",err)
        return False
        
def consult_records(id):
    query = "SELECT * FROM users WHERE id = " + id
    try:
        connection = connectionSQL()
        cursor = connection.cursor()
        if connection != None:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        else:
            print("error in the connection ")
            return None
    except Exception as err:
        print("error consulting the user", err)
        return None
        