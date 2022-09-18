# import module
from tkinter import *
from tkinter import ttk
from typing import Set 
import Common_Requirements_File
from PIL import ImageTk,Image,ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
from tkinter import messagebox
from connection import *
import os
from datetime import *
import student_monthly_attendence
import student_semesterly_average

class student_details:
    def __init__(self,student_details_root,no):
        self.student_details_root = student_details_root
        self.student_details_root.title("Students Details")
        self.regno_var = StringVar()
        self.the_number=StringVar()
        if no != False: 
            self.the_number = no
            self.regno(self.the_number)
            self.filter()
        else:
            self.regno()

        p_obj=Common_Requirements_File.Common_Requirements(self.student_details_root)
        p_obj.header()
        p_obj.left_nav_bar_setting()
        p_obj.right_nav_bar_setting()
    
    # Search box 
    def regno(self,the_number=""):
        self.frm = Frame(self.student_details_root,bg='white')
        self.frm.place(x=550,y=100,height=100,width=400)

        regno=Label(self.frm,text="Enter Registration Number : ",font=("times new roman",15),bg="white", fg="black").place(x=10,y=15)
        self.txt_frame=Entry(self.frm,font=("time new roman",15),bg="lightgrey",textvariable=self.regno_var)
        self.txt_frame.insert(END, the_number)
        self.txt_frame.place(x=10,y=50,width=330)
        s_btn=Button(self.frm,bd=0,cursor="hand2" ,text="🔍",fg="green",bg="white",font=(15),activebackground="white",activeforeground="white",command=self.filter).place(x=350,y=50,width=30,height=25)

    def filter(self):
        self.the_number=self.regno_var.get()
        self.check_regno(self.the_number)
    
    # Function used for fetching data from database
    def check_regno(self,registration_number):
        if student_monthly_attendence.btn_state_monthly_view==1:
            student_monthly_attendence.btn_state_monthly_view=0
            student_monthly_attendence.student_monthly_attendence_root.destroy()

        if student_semesterly_average.btn_state_semesterly_view==1:
            student_semesterly_average.btn_state_semesterly_view=0
            student_semesterly_average.student_semersterly_average_root.destroy()

        if registration_number=="":
            self.not_found()
            messagebox.showerror("Error","Please Enter The Fields To Proceed")
        else:
            try:
                cur=connection()
                self.m=cur.execute("Select * from student_details where registration_number=%s",(registration_number))
                self.rows = cur.fetchall()
                if len(self.rows) == 0:
                    self.not_found()
                    messagebox.showerror("Error","Sorry, We cannot find a student with this registration")
                else:
                    self.found_data(self.rows)
                    self.attendance_view()
            except Exception as es :
                messagebox.showerror("Error","Error Detected")
   
   # Display search data in frame
    def found_data(self,rows):
        self.found_frm = Frame(self.student_details_root,bg='white')
        self.found_frm.place(x=300,y=250,height=400,width=500)

        self.rec_data=self.rows[0][7]
        with open(f'student_images/{self.rows[0][0]}.jpg','wb') as f:
            f.write(self.rec_data)

        image = Image.open(f"student_images/{self.rows[0][0]}.jpg") 
        resize_image = image.resize((125, 100))
        img = ImageTk.PhotoImage(resize_image) 
        label1 = Label(self.found_frm,image=img)

        label1.image = img
        label1.place(x=340,y=30,height=105,width=130)

        os.remove(f"student_images/{self.regno_var.get()}.jpg")

        Label(self.found_frm,text=f"Student Details of {rows[0][0]}",font=("Candara Light",20,"bold","underline"),fg="black",bg='white').place(x=30,y=30)
     
        Label(self.found_frm,text="Reg No. : ",font=("arial",15),bg="white", fg="black").place(x=20,y=100)
        Label(self.found_frm,text=f"{rows[0][0]}",font=("arial",15),bg="white", fg="black").place(x=150,y=100)

        Label(self.found_frm,text="Name : ",font=("arial",15),bg="white", fg="black").place(x=20,y=140)
        Label(self.found_frm,text=f"{rows[0][1]}",font=("arial",15),bg="white", fg="black").place(x=150,y=140)

        Label(self.found_frm,text="Department : ",font=("arial",15),bg="white", fg="black").place(x=20,y=180)
        Label(self.found_frm,text=f"{rows[0][2]}",font=("arial",15),bg="white", fg="black").place(x=150,y=180)

        Label(self.found_frm,text="Year : ",font=("arial",15),bg="white", fg="black").place(x=20,y=220)
        Label(self.found_frm,text=f"{rows[0][3]}",font=("arial",15),bg="white", fg="black").place(x=150,y=220)

        Label(self.found_frm,text="Date of Birth : ",font=("arial",15),bg="white", fg="black").place(x=20,y=260)
        Label(self.found_frm,text=f"{rows[0][4]}",font=("arial",15),bg="white", fg="black").place(x=150,y=260)

        Label(self.found_frm,text="Number : ",font=("arial",15),bg="white", fg="black").place(x=20,y=300)
        Label(self.found_frm,text=f"{rows[0][5]}",font=("arial",15),bg="white", fg="black").place(x=150,y=300)
        
        Label(self.found_frm,text="Email : ",font=("arial",15),bg="white", fg="black").place(x=20,y=340)
        Label(self.found_frm,text=f"{rows[0][6]}",font=("arial",15),bg="white", fg="black").place(x=150,y=340)

    # Display the attendence details of current semester
    def attendance_view(self):
        self.attendance_view_frame = Frame(self.student_details_root,bg='white')
        self.attendance_view_frame.place(x=850,y=250,height=300,width=410)
        todays_date = date.today()

        if self.rows[0][3]=="1st Year":
            if todays_date.month>6:
                self.sem="1st Semester"
            else:
                self.sem="2nd Semester"
        elif self.rows[0][3] == "2nd Year":
            if todays_date.month>6:
                self.sem="3rd Semester"
            else:
                self.sem="4th Semester"
        elif self.rows[0][3] == "3rd Year":
            if todays_date.month>6:
                self.sem="5th Semester"
            else:
                self.sem="6th Semester"
            
        if self.sem=="1st Semester" or self.sem=="3rd Semester" or self.sem=="5th Semester":
            sem_start=7
        else:
            sem_start=1

        self.semester_present=0
        self.semester_absent=0
        self.semester_total=0
        self.semester_average_percentage='0.00%'

        cur=connection()
        for i in range(sem_start,todays_date.month+1):
            self.get_attendence_details_month=cur.execute("Select * from attendance_details where registration_number=%s and date like '%s-%%"+str(i)+"-%%'",(self.rows[0][0],todays_date.year))
            self.get_attendence_details_month_row = cur.fetchall()

            for attendence_measure in self.get_attendence_details_month_row:
                if attendence_measure[2]== "Present":
                    self.semester_present=self.semester_present+1 
                else:
                    self.semester_absent=self.semester_absent+1
                self.semester_total=self.semester_total+1

            if len(self.get_attendence_details_month_row)!=0:
                self.semester_average_percentage=(self.semester_present/self.semester_total)*100
                self.semester_average_percentage=round(self.semester_average_percentage,2)

        Label(self.attendance_view_frame,text="The Attendence Details Of \nCurrent Semester",font=("Candara Light",18,"bold","underline"),bg="white").place(x=55,y=30)
        Label(self.attendance_view_frame,text=f"Total Number Of Days\t     : {self.semester_total}",font="arial 15 ",bg="white").place(x=15,y=120)
        Label(self.attendance_view_frame,text=f"No. Of Days Present\t     : {self.semester_present}",font="arial 15 ",bg="white").place(x=15,y=150)
        Label(self.attendance_view_frame,text=f"No. Of Days Absent\t     : {self.semester_absent}",font="arial 15 ",bg="white").place(x=15,y=180)
        Label(self.attendance_view_frame,text=f"Average Semester Attendence    : {self.semester_average_percentage}",font="arial 15 ",bg="white").place(x=15,y=210)

        self.monthly_attendence_btn = Button(self.student_details_root,text="Monthly Attendence",font="arial 13 ",command=self.goToStudentMonthlyAttendence,bg="gray",activebackground="gray")
        self.monthly_attendence_btn.place(x=850,y=590,height=60,width=180)
        self.monthly_attendence_btn=Button(self.student_details_root,text="Semesterly Average",font="arial 13 ",bg="gray",command=self.goToStudentSemesterlyAverage,activebackground="gray")
        self.monthly_attendence_btn.place(x=1080,y=590,height=60,width=180)

    # To view student Monthly & Semesterly attendence view
    def goToStudentMonthlyAttendence(self):       
        if student_monthly_attendence.btn_state_monthly_view == 0:
            student_monthly_attendence.student_monthly_aatendence_main(self.rows[0][0])
    
    def goToStudentSemesterlyAverage(self):
        if student_semesterly_average.btn_state_semesterly_view == 0:
            student_semesterly_average.student_semersterly_average_main(self.rows[0][0])

    def not_found(self):
        self.not_frm = Frame(self.student_details_root,bg='#f0f0f0')
        self.not_frm.place(x=300,y=250,height=400,width=1260)

def student_details_main(no=False):
    student_monthly_attendence.btn_state_monthly_view=0
    student_semesterly_average.btn_state_semesterly_view=0
    student_details_root=Tk()
    obj = student_details(student_details_root,no)
    student_details_root.mainloop()  
