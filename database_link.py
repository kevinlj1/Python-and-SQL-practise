import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = open("config.txt", "r").read(),
    database = "testscores"
)

def insert_data(name, ict, maths, chemistry):
    mycursor = mydb.cursor()

    sql = "INSERT INTO users (UserName, ICTScore, MathsScore, ChemistryScore) VALUES (%s, %s, %s, %s)"
    val = (name, ict, maths, chemistry)
    mycursor.execute(sql, val)
    mydb.commit()

    print(mycursor.rowcount, "record inserted.")

#Code above inserts a record into the database  

def fetch_data(name):
    mycursor = mydb.cursor()
    mycursor.execute(f"SELECT * FROM users WHERE userName = '{name}'")
    myresult = mycursor.fetchall()

    return myresult

#Code above returns a record from the database

