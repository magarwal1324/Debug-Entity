# import module
from tkinter import *
from tkcalendar import Calendar 
from tkinter import ttk 
from PIL import ImageTk
import Common_Requirements_File
import previous_attendance_details
from tkinter import messagebox

class previous_attendance:
    def __init__(self,root_todays_attendance):

        self.root_previous_attendance = root_previous_attendance
        self.root_previous_attendance.title("Previous Attendence")

        self.previousDate = StringVar()
        self.left_frame()
        self.date_Picker()


        p_obj=Common_Requirements_File.Common_Requirements(self.root_previous_attendance)
        p_obj.header()
        p_obj.left_nav_bar_setting()
        p_obj.right_nav_bar_setting()

    # Input box for entering Department & Year
    def left_frame(self):
        frm = Frame(self.root_previous_attendance,bg='white')
        frm.place(x=60,y=190,height=400,width=600)

        title1=Label(frm,text="Previous's Attendence",font=("Candara Light",35,"bold","underline"),fg="black",bg="white").pack(side=TOP)
        
        dept_values=['Enter the Department','Computer Science And Technology','Civil Engineering','Electrical Engineering','Mechanical Engineering']
        year_values=['Enter the Year','1st Year','2nd Year','3rd Year']

        lal_user=Label(frm,text="Year:",font=("Goudy old style",18,"bold"),bg="white").place(x=50,y=90)
        self.year = ttk.Combobox(frm, value=year_values,font="calibri 12",state='readonly') 
        self.year.place(x=50,y=130,width=500,height=25)
        self.year.current(0)

        lal_pwd=Label(frm,text="Department:",font=("Goudy old style",18,"bold"),bg="white").place(x=50,y=160)
        self.dept = ttk.Combobox(frm, value=dept_values,font="calibri 12",state='readonly') 
        self.dept.place(x=50,y=200,width=500,height=25)
        self.dept.current(0)

        lal_date=Label(frm,text="Date:",font=("Goudy old style",18,"bold"),bg="white").place(x=50,y=230)
        self.date = Entry(frm,textvariable=self.previousDate,font=("calibri",12),borderwidth=2) 
        self.date.place(x=50,y=270,width=500,height=25)
            
        s_btn=Button(frm,bd=0,cursor="hand2",text="Search",fg="white",bg="gray",font=("times new roman",20,"bold"),activebackground="gray",activeforeground="white",command=self.pick).place(x=50,y=320,width=500,height=50)

    # Getting values from input field           
    def pick(self):
        dept_values=['Computer Science And Technology','Civil Engineering','Electrical Engineering','Mechanical Engineering']
        year_values=['1st Year','2nd Year','3rd Year']
        dept_name=self.dept.get()
        pDate=self.date.get()
        year=self.year.get()

        if dept_name in dept_values and year in year_values and pDate!="":
            # self.root.after_cancel(after_time)
            self.root_previous_attendance.destroy()
            previous_attendance_details.Previous_Attendance_Details_Main(year,dept_name,pDate)
        elif pDate=="":
            messagebox.showerror("Error","All feilds are required")
        else:
            messagebox.showerror("Error","Enter correct values in the fields")

    # Date will automatically put in data field when click Get Date in the given calendar
    def grad_date(self): 
        self.date.delete(0, 'end')
        self.date.insert(0, self.cal.get_date())

    # Calender
    def date_Picker(self):
        dateFrame=Frame(self.root_previous_attendance,bd=1,relief="solid",bg='#D1D5D8')
        dateFrame.place(x=840,y=190,height=400,width=600)

        lal_setDate=Label(dateFrame,text="Select the date from the calendar",font=("arial",16,"bold"),bg="#D1D5D8").place(height=40,width=597)

        self.cal = Calendar(dateFrame, selectmode = 'day', year = 2021, month = 1, day = 1,date_pattern='y-mm-dd') 
        self.cal.place(x=50,y=40,height=300,width=500) 


        btnDate=Button(dateFrame, text = "Get Date",fg="white",bg="#9c9c9c",font=("times new roman",14,"bold"),activebackground="#9c9c9c",activeforeground="white", command = self.grad_date) 
        btnDate.place(x=50,y=348,width=500,height=40)

def Previous_Attendance_Main():
    global root_previous_attendance
    root_previous_attendance=Tk()
    obj = previous_attendance(root_previous_attendance)
    root_previous_attendance.mainloop()
# Previous_Attendance_Main()