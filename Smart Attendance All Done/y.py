from datetime import *
import pymysql
import random
randomabc=random.randint(1,7)

print("started")
x = ["2021-07-13"]
print(len(x))
for k in x:
    for i in range(1001,1062):
            if i==random.randint(1001,1062):
                con = pymysql.connect(host="localhost", user="root",password="", database="stm")
                cur = con.cursor()
                cur.execute("INSERT INTO attendance_details (registration_number,attandance,date) VALUES (%s,%s,%s);",(i,"Absent",k))
                con.commit()
            else:
                con = pymysql.connect(host="localhost", user="root",password="", database="stm")
                cur = con.cursor()
                cur.execute("INSERT INTO attendance_details (registration_number,attandance,date) VALUES (%s,%s,%s);",(i,"Present",k))
                con.commit()

print("Done")

# x = ["2019-07-01","2019-07-02","2019-07-03","2019-07-05","2019-07-08",]
# print("started")
# for k in x:
#     for i in range(1001,1061):
#         if i == 1007 or i == 1015 or i==1023 or i==1053 or i==1037 or i== 1041 or i == 1059 or i==1030 or i==1029 or i==1021:
#             con = pymysql.connect(host="localhost", user="root",password="", database="stm")
#             cur = con.cursor()
#             cur.execute("INSERT INTO attendance_details (registration_number,attandance,date) VALUES (%s,%s,%s);",(i,"Absent",k))
#             con.commit()
#         else:
#             con = pymysql.connect(host="localhost", user="root",password="", database="stm")
#             cur = con.cursor()
#             cur.execute("INSERT INTO attendance_details (registration_number,attandance,date) VALUES (%s,%s,%s);",(i,"Present",k))
#             con.commit()

# print("done")
