# import module
from connection import*

# Fetching data from database
def find_row(username,password):
    cur = connection()
    cur.execute("select * from teacher_details where email= %s and password= %s",(username,password))
    return(cur.fetchone())

def first_name(username,password):
    row=find_row(username,password)
    first_name=row[1]
    return(first_name)

def last_name(username,password):
    row=find_row(username,password)
    last_name=row[2]
    return(last_name)

def department(username,password):
    row=find_row(username,password)
    department=row[3]
    return(department)

def post(username,password):
    row=find_row(username,password)
    post=row[4]
    return(post)

def email(username,password):
    row=find_row(username,password)
    email=row[5]
    return(email)
