# import module
from tkinter import *
from tkinter import ttk 
from PIL import ImageTk
import Common_Requirements_File
import todays_attendance_details
from tkinter import messagebox

class todays_attendance:
    def __init__(self,root_todays_attendance):

        self.root_todays_attendance = root_todays_attendance
        self.root_todays_attendance.title("Today's Attendence")
        self.frame1()

        p_obj=Common_Requirements_File.Common_Requirements(self.root_todays_attendance)
        p_obj.header()
        p_obj.left_nav_bar_setting()
        p_obj.right_nav_bar_setting()

    # Input box for entering Department & Year
    def frame1(self):
        frm = Frame(self.root_todays_attendance,bg='white')
        frm.place(x=450,y=190,height=400,width=600)

        title1=Label(frm,text="Today's Attendence",font=("Candara Light",35,"bold","underline"),fg="black",bg="white").pack(side=TOP)
        
        dept_values=['Enter the Department','Computer Science And Technology','Civil Engineering','Electrical Engineering','Mechanical Engineering']
        year_values=['Enter the Year','1st Year','2nd Year','3rd Year']

        lal_user=Label(frm,text="Year:",font=("Goudy old style",18,"bold"),bg="white").place(x=50,y=90)
        self.year = ttk.Combobox(frm, value=year_values,font="calibri 18",state='readonly') 
        self.year.place(x=50,y=130,width=500,height=35)
        self.year.current(0)
        lal_pwd=Label(frm,text="Department:",font=("Goudy old style",18,"bold"),bg="white").place(x=50,y=195)
        self.dept = ttk.Combobox(frm, value=dept_values,font="calibri 18",state='readonly') 
        self.dept.place(x=50,y=235,width=500,height=35)
        self.dept.current(0)
    
        s_btn=Button(frm,bd=0,cursor="hand2",text="Search",fg="white",bg="gray",font=("times new roman",20,"bold"),activebackground="gray",activeforeground="white",command=self.pick).place(x=50,y=320,width=500,height=50)

    # Getting values from input field         
    def pick(self):
        dept_values=['Computer Science And Technology','Civil Engineering','Electrical Engineering','Mechanical Engineering']
        year_values=['1st Year','2nd Year','3rd Year']
        dept_name=self.dept.get()
        year=self.year.get()
        if dept_name in dept_values and year in year_values:
            # self.root.after_cancel(after_time)
            self.root_todays_attendance.destroy()
            todays_attendance_details.Todays_Attendance_Details_Main(year,dept_name)
        else:
            # Warning box if any input missing
            messagebox.showerror("Error","Enter correct values in the fields")

def Todays_Attendance_Main():
    global root_todays_attendance
    root_todays_attendance=Tk()
    obj = todays_attendance(root_todays_attendance)
    root_todays_attendance.mainloop()
# Todays_Attendance_Main()