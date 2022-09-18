# import module
from tkinter import *
from PIL import ImageTk,Image,ImageFile
from tkinter import messagebox
import time as tm
from connection import*
import login
import admin_account_settings
import attendence
import AttendanceProject
from tkinter import ttk 
from datetime import datetime
import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
import pyttsx3
import pymysql
ImageFile.LOAD_TRUNCATED_IMAGES = True

# A class with init method
class Dashboard:
    # init method or constructor
    def __init__(self,root_dashboard):
        self.root_dashboard=root_dashboard
        self.root_dashboard.title("Dashboard")
        self.root_dashboard.geometry("1500x750+10+25")
        self.root_dashboard.resizable(0,0)
        self.root_dashboard.iconbitmap("images_software\\software_icon.ico")

        self.capIcon = PhotoImage(file="images_software/cap1.png")
        self.downIcon = PhotoImage(file="images_software/down.png")
        self.upIcon = PhotoImage(file="images_software/up.png")

        cur = connection()
        cur.execute("select username from admin_credential_camera ")
        self.admin_name= cur.fetchone()

        self.admin_area_header()
        self.right_nav_bar_setting()
        self.open_camera_frame()

    # Dashboard header
    def admin_area_header(self):
        # print("hi i am admin area")
        self.topFrame=Frame(self.root_dashboard,bg='white')
        self.topFrame.place(x=0,y=0,height=60,width=1500)

        tagBtn = Button(self.topFrame,text="   Welcome to Smart Attendence System",image=self.capIcon,font='Arial 15 bold',compound=LEFT,fg='black',bg='white',activebackground='white',cursor='hand2',bd=0)
        tagBtn.place(x=535,y=10)
        homeLabel = Label(self.topFrame,text=f"Hello, {self.admin_name[0]}", font='Arial 13',bg="white",fg='gray17',anchor="e")
        homeLabel.place(x=1245,y=15,width=200)

    # Function for taking attendence using camera and taking attendence using manually
    def open_camera_frame(self):
        now=datetime.now()
        print(now.day)
        self.dateframe=Frame(self.root_dashboard,bg='#a42d5c')
        self.dateframe.place(x=200,y=95,height=70,width=1100)

        datelbl = Label(self.dateframe,text=f"{now.date()} --- Attend Today To Achieve Tommorow", font='Arial 15',bg="#a42d5c",fg='white',anchor="e")
        datelbl.place(x=200,y=15,width=600)

        # Button's        
        login_btn1=Button(root_Dashboard,command=self.capture,bd=0,cursor="hand2",text="Take Attendence",fg="white",bg="#a42d5c",font=("times new roman",20)).place(x=200,y=200,width=450,height=50)
        login_btn2=Button(root_Dashboard,command=self.goTOManualAttendence,bd=0,cursor="hand2",text="Give Attendence Manually",fg="white",bg="#a42d5c",font=("times new roman",20)).place(x=850,y=200,width=450,height=50)

    # Define goTOManualAttendence function used for taking students attendence by inputing values in the input fields
    def goTOManualAttendence(self):
        Frame_take_attendence=Frame(self.root_dashboard,bg="#e1e2fa")
        Frame_take_attendence.place(x=525,y=300,height=400,width=450)

        title1=Label(Frame_take_attendence,text="Mark Attendence",font=("Candara Light",35,"bold","underline"),fg="black",bg="#e1e2fa").place(x=50,y=10)
        description1=Label(Frame_take_attendence,text="Attend Today Achieve Tommorow",font=("calibri",15,"bold"),fg="#a42d5c",bg="#e1e2fa").place(x=80,y=70)

        lal_reg_no=Label(Frame_take_attendence,text="Registration Number:",font=("Goudy old style",15,"bold"),fg="grey",bg="#e1e2fa").place(x=50,y=125)
        self.txt_regno=Entry(Frame_take_attendence,font=("calibri",15),bg="lightgray")
        self.txt_regno.place(x=50,y=155,width=350,height=35)

        attendence_values=['Select','Present','Absent']
        lal_attendence=Label(Frame_take_attendence,text="Mark Attendence:",font=("Goudy old style",15,"bold"),fg="grey",bg="#e1e2fa").place(x=50,y=200)
        self.attendence = ttk.Combobox(Frame_take_attendence, value=attendence_values,font="calibri 15",state='readonly') 
        self.attendence.place(x=50,y=230,width=350,height=35)
        self.attendence.current(0)


        login_btn=Button(Frame_take_attendence,command=self.mark_attendence_manually_register,bd=0,cursor="hand2",text="Mark Attendence",fg="white",bg="#a42d5c",font=("times new roman",20)).place(x=50,y=300,width=350,height=50)

    # Function used for updating students values in database
    def mark_attendence_manually_register(self):
        if self.txt_regno.get() == "" or self.attendence.get() =="Select":
            messagebox.showerror("Error","All fields are required")
        else:
            con = pymysql.connect(host="localhost", user="root",password="", database="stm")
            cur = con.cursor()
            cur.execute("select * from student_details where registration_number=%s",(self.txt_regno.get()))
            rows_student=cur.fetchall()
            if len(rows_student)>0:
                now = datetime.now()
                con = pymysql.connect(host="localhost", user="root",password="", database="stm")
                cur = con.cursor()
                cur.execute("select * from attendance_details where registration_number=%s and date=%s",(self.txt_regno.get(),  now.date()))
                rows=cur.fetchall()
                # print(rows)
                if len(rows)>0:
                    now = datetime.now()
                    con = pymysql.connect(host="localhost", user="root",password="", database="stm")
                    cur = con.cursor()
                    cur.execute("update attendance_details set attandance =%s where registration_number= %s",(self.attendence.get(),self.txt_regno.get()))
                    con.commit()
                    messagebox.showinfo("Updated","Details Updated")
                else:
                    now = datetime.now()
                    con = pymysql.connect(host="localhost", user="root",password="", database="stm")
                    cur = con.cursor()
                    cur.execute(("insert attendance_details set  registration_number=%s, attandance=%s , date=%s "),(self.txt_regno.get(),self.attendence.get(),now.date()))
                    con.commit()
                    messagebox.showinfo("Updated","Details Updated")
            else:
                messagebox.showerror("Error","Enter Valid Registration Number")

    # Directing to camera setup     
    def capture(self):
        # attendence.face_recognitions_main()
        AttendanceProject.face_recognitions_main()
        # print("success")

    # Options on header
    def get_options_right(self,title):
        opt = {
            'Account': self.goToAccountSettings,
            'Log Out': self.log_out         
        }

        if title == "Account Settings":
            opt["Account"]=None
        
        return opt
       
    def right_nav_bar_setting(self):
        self.btnState2=True    

        homeLabel_btn = Button(self.topFrame,image=self.downIcon,bg='white',bd=0,activebackground="white",cursor="hand2",command=self.right_switch)
        homeLabel_btn.place(x=1450,y=10)

        self.navRoot2 = Frame(self.root_dashboard,bg='#042954',height=120,width=150)
        self.navRoot2.place(x=1500,y=60)

        y= 0      
        options = self.get_options_right(self.root_dashboard.title()) 
        for i in options:
            Button(self.navRoot2,text=i,font='Arial 15',bg='#a42d5c',fg='white',activebackground='green',activeforeground='white',bd=2,command=options[i]).place(x=0,y=y,height=60,width=150)
            y += 60
   
    def right_switch(self):
        
        if self.btnState2 is True:

            self.navRoot2.place(x=1350,y=60)
            homeLabel_btn = Button(self.topFrame,image=self.upIcon,bg='white',bd=0,activebackground="white",cursor="hand2",command=self.right_switch)
            homeLabel_btn.place(x=1450,y=10)   
            self.btnState2 =  False
        
        else:

            self.navRoot2.place(x=1500,y=60)
            homeLabel_btn = Button(self.topFrame,image=self.downIcon,bg='white',bd=0,activebackground="white",cursor="hand2",command=self.right_switch)
            homeLabel_btn.place(x=1450,y=10)
            self.btnState2 = True

    # Back to login page
    def log_out(self):
        root_Dashboard.destroy()
        login.login_main()

    # Directing to account update page
    def goToAccountSettings(self):
        root_Dashboard.destroy()
        admin_account_settings.Admin_Account_Settings_Main()
 

def Dashboard_Main():
    global root_Dashboard
    root_Dashboard=Tk()
    obj = Dashboard(root_Dashboard)
    root_Dashboard.mainloop()

# Dashboard_Main()