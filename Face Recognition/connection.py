# import module
import pymysql

# Connection with database
def connection():
    con = pymysql.connect(host="localhost", user="root",password="", database="stm")
    cur = con.cursor()
    return cur