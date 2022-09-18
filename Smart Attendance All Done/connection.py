# import module
import pymysql

# def givi_me_connection():
#     con = pymysql.connect(host="mysql-39194-0.cloudclusters.net",port=39194, user="admin",password="De3nXPLy", database="stm")
#     return con

# def connection():
#     con = pymysql.connect(host="mysql-39194-0.cloudclusters.net",port=39194, user="admin",password="De3nXPLy", database="stm")
#     cur = con.cursor()
#     return cur

# connection with database
def givi_me_connection():
    con = pymysql.connect(host="localhost", user="root",password="", database="stm")
    return con

def connection():
    con = pymysql.connect(host="localhost", user="root",password="", database="stm")
    cur = con.cursor()
    return cur
