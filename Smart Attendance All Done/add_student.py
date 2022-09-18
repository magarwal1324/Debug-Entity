# import module
from connection import *
from tkinter import *
from tkinter import ttk 
import Common_Requirements_File
import Dashboard
import Admin_Area_File
from PIL import ImageTk,Image
from tkinter import filedialog
from tkinter import messagebox
import csv
from validate_email import validate_email
import shutil 

class Add_Student:
    def __init__(self,add_student_root):
        self.add_student_root = add_student_root
        self.add_student_root.title("Add Student")
        self.add_student_frame()

        self.p_obj=Common_Requirements_File.Common_Requirements(self.add_student_root)
        self.p_obj.header()
        self.p_obj.left_nav_bar_setting()
        self.p_obj.right_nav_bar_setting()
    
    # Create from for adding new student's
    def add_student_frame(self):

        self.name_var = StringVar()
        self.roll_var = StringVar()
        self.department_var = StringVar()
        self.year_var = StringVar()
        self.phone_var = StringVar()
        self.email_var = StringVar()
        self.dob_var = StringVar()
        self.filename=''

        self.frm = Frame(self.add_student_root,bg='white')
        self.frm.place(x=450,y=100,height=620,width=600)
        title1=Label(self.frm,text="Add Student",font=("Candara Light",35,"bold","underline"),fg="black",bg="white").pack(side=TOP)

        # Upload Student profile photo from file
        s_btn=Button(self.frm,bd=0,cursor="hand2" ,text="Upload Photo",fg="white",bg="dimgray",font=("arial",10,"bold"),activebackground="gray",activeforeground="white",command=self.upload_student).place(x=250,y=80,width=100,height=30)

        f_name=Label(self.frm,text="Name ",font=("times new roman",15),bg="white", fg="black").place(x=22,y=150)
        self.txt_frame=Entry(self.frm,font=("time new roman",15),bg="lightgrey",textvariable=self.name_var).place(x=30,y=180,width=550)

        roll=Label(self.frm,text="Reg No.  ",font=("times new roman",15),bg="white", fg="black").place(x=22,y=230)
        self.txt_roll=Entry(self.frm,font=("time new roman",15),bg="lightgrey",textvariable=self.roll_var).place(x=30,y=260,width=250)

        self.dept_values=['Select','Computer Science and Technology','Electrical Engineering','Civil Engineering','Mechanical Engineering']
        self.year_values=['Select','1st Year','2nd Year','3rd Year']
 
        lal_select_dept=Label(self.frm,text="Department ",font=("times new roman",15),bg="white",fg='black').place(x=320,y=230)
        self.select_dept = ttk.Combobox(self.frm, value=self.dept_values,font="calibri 12",state='readonly',textvariable=self.department_var) 
        self.select_dept.place(x=320,y=260,width=250,height=25)
        self.select_dept.current(0)
        
        year=Label(self.frm,text="Year",font=("times new roman",15),bg="white",fg='black').place(x=22,y=310)
        self.year = ttk.Combobox(self.frm, value=self.year_values,font="calibri 12",state='readonly', textvariable=self.year_var) 
        self.year.place(x=30,y=340,width=250,height=25)
        self.year.current(0)

        dob=Label(self.frm,text="Date of Birth ",font=("times new roman",15),bg="white", fg="black").place(x=320,y=310)
        self.txt_dob=Entry(self.frm,font=("time new roman",15),textvariable=self.dob_var ,bg="lightgrey").place(x=320,y=340,width=250)

        phone=Label(self.frm,text="Phone ",font=("times new roman",15),bg="white", fg="black").place(x=30,y=390)
        self.txt_phone=Entry(self.frm,font=("time new roman",15),bg="lightgrey",textvariable=self.phone_var).place(x=30,y=420,width=550)

        email=Label(self.frm,text="Email ",font=("times new roman",15),bg="white", fg="black").place(x=30,y=470)
        self.txt_email=Entry(self.frm,font=("time new roman",15),bg="lightgrey",textvariable= self.email_var).place(x=30,y=500,width=550)

        submit_btn=Button(self.frm,bd=0,cursor="hand2",text="Submit",fg="white",bg="gray",font=("times new roman",20,"bold"),activebackground="gray",activeforeground="white",command=self.check_data).place(x=30,y=550,width=550,height=40)

    def check_data(self):       
        if self.name_var.get()=="" or self.roll_var.get()=="" or self.phone_var.get()=="" or self.email_var.get()=="" or self.department_var.get() == "Select" or self.year_var.get()=="Select" or self.dob_var.get()=="" or self.filename=="":
            messagebox.showerror("Error","All fields are required")
        else: 
            try:
                try:
                    con=givi_me_connection()
                    cur=con.cursor()
                    with open(self.filename,'rb') as f:
                        data = f.read()
                    cur.execute("insert into student_details values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                    self.roll_var.get(),
                                                    self.name_var.get(),                                        
                                                    self.department_var.get(),
                                                    self.year_var.get(),
                                                    self.dob_var.get(),
                                                    self.phone_var.get(),  
                                                    self.email_var.get(),
                                                    data
                    ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Info","Registered") 
                    
                    self.add_student_frame()       
                    self.p_obj.close_search_frame()

                except Exception as e:
                    messagebox.showerror("Error","Some Error Occured" + e)
                    print(e)
            except Exception:
                pass

    # Getting and uploading students profile photo asper Photo formate        
    def upload_student(self):
        self.filename = filedialog.askopenfilename(initialdir=":/downloads", title = "Select a file",filetypes=(("png files","*.png"),("jpg files","*.jpg"),("jpeg files","*.jpeg")))
        self.lbl_file_name= Label(self.frm,text=f"{self.filename}",font=("times new roman",8),bg="white", fg="black").place(x=170,y=110)

def add_student_main():
    add_student_root=Tk()
    obj = Add_Student(add_student_root)
    add_student_root.mainloop()