# Import module
from tkinter import *
from tkinter import ttk 
import Common_Requirements_File
from PIL import ImageTk,Image
from tkinter import messagebox
from connection import *
import pymysql

class update_Student:
    def __init__(self,update_student_root):
        self.update_student_root = update_student_root
        self.update_student_root.title("Update Student")
        self.regno_var = StringVar()

        # self.update_student_frame()
        self.regno()

        p_obj=Common_Requirements_File.Common_Requirements(self.update_student_root)
        p_obj.header()
        p_obj.left_nav_bar_setting()
        p_obj.right_nav_bar_setting()

    # Search box
    def regno(self):
        self.frm = Frame(self.update_student_root,bg='white')
        self.frm.place(x=550,y=100,height=100,width=400)

        regno=Label(self.frm,text="Enter Registration Number : ",font=("times new roman",15),bg="white", fg="black").place(x=10,y=15)
        self.txt_frame=Entry(self.frm,font=("time new roman",15),bg="lightgrey",textvariable=self.regno_var).place(x=10,y=50,width=330)
        s_btn=Button(self.frm,bd=0,cursor="hand2" ,text="🔍",fg="green",bg="white",font=(15),activebackground="white",activeforeground="white",command=self.check_regno).place(x=350,y=50,width=30,height=25)

    # Checking search box value
    def check_regno(self):
        if self.regno_var.get()=="":
            messagebox.showerror("Error","Please Enter The Fields To Proceed")
        else:
            try:
                cur=connection()
                cur.execute("Select * from student_details where registration_number=%s",(self.regno_var.get()))
                self.rows = cur.fetchall()
                if len(self.rows) == 0:
                    self.not_found()
                    messagebox.showerror("Error","Sorry, We cannot find a student with this registration")
                else:
                    self.found_data(self.rows)
                    self.update_studet_frame(self.rows)
  
            except Exception as es :
                messagebox.showerror("Error",f"Error due to: {str(es)}")

    # Display searched details in frame
    def found_data(self,rows):
        self.found_frm = Frame(self.update_student_root,bg='white')
        self.found_frm.place(x=300,y=250,height=400,width=435)

        Label(self.found_frm,text=f"Student Details of {rows[0][0]}",font=("Candara Light",25,"bold","underline"),fg="black",bg='white').pack(side=TOP)
     
        Label(self.found_frm,text="Reg No. : ",font=("times new roman",15),bg="white", fg="black").place(x=20,y=95)
        Label(self.found_frm,text=f"{rows[0][0]}",font=("times new roman",14),bg="white", fg="black").place(x=140,y=95)

        Label(self.found_frm,text="Name : ",font=("times new roman",15),bg="white", fg="black").place(x=20,y=135)
        Label(self.found_frm,text=f"{rows[0][1]}",font=("times new roman",14),bg="white", fg="black").place(x=140,y=135)

        Label(self.found_frm,text="Department : ",font=("times new roman",15),bg="white", fg="black").place(x=20,y=175)
        Label(self.found_frm,text=f"{rows[0][2]}",font=("times new roman",14),bg="white", fg="black").place(x=140,y=175)

        Label(self.found_frm,text="Year : ",font=("times new roman",15),bg="white", fg="black").place(x=20,y=215)
        Label(self.found_frm,text=f"{rows[0][3]}",font=("times new roman",14),bg="white", fg="black").place(x=140,y=215)

        Label(self.found_frm,text="Date of Birth : ",font=("times new roman",15),bg="white", fg="black").place(x=20,y=255)
        Label(self.found_frm,text=f"{rows[0][4]}",font=("times new roman",14),bg="white", fg="black").place(x=140,y=255)

        Label(self.found_frm,text="Number : ",font=("times new roman",15),bg="white", fg="black").place(x=20,y=295)
        Label(self.found_frm,text=f"{rows[0][5]}",font=("times new roman",14),bg="white", fg="black").place(x=140,y=295)
        
        Label(self.found_frm,text="Email : ",font=("times new roman",15),bg="white", fg="black").place(x=20,y=335)
        Label(self.found_frm,text=f"{rows[0][6]}",font=("times new roman",14),bg="white", fg="black").place(x=140,y=335)

    def update_studet_frame(self,rows):
        frm_update = Frame(self.update_student_root,bg='white')
        frm_update.place(x=775,y=250,height=400,width=425)

        title1=Label(frm_update,text="Update student",font=("Candara Light",25,"bold","underline"),fg="black",bg="white").pack(side=TOP)
        
        data_update_values=['Select','Name','department','year','dob','contact','email']

        lal_select_detatils=Label(frm_update,text="Select Details To Change",font=("Goudy old style",15,"bold"),bg="white").place(x=25,y=80)
        self.select_detatils = ttk.Combobox(frm_update, value=data_update_values,font="calibri 12",state='readonly') 
        self.select_detatils .place(x=25,y=120,width=375,height=25)
        self.select_detatils .current(0)

        self.mystr = StringVar()

        lal_old_data=Label(frm_update,text="Previous Data",font=("Goudy old style",15,"bold"),bg="white").place(x=25,y=165)
        self.old_data = Entry(frm_update,font=("calibri",12, "bold"),fg="black",borderwidth=2,textvariable=self.mystr, state=DISABLED) 
        self.old_data.place(x=25,y=200,width=375,height=25)
        self.select_detatils.bind("<<ComboboxSelected>>", self.previous_details)


        lal_new_data=Label(frm_update,text="New Data",font=("Goudy old style",15,"bold"),bg="white").place(x=25,y=240)
        self.new_data = Entry(frm_update,font=("calibri",12),borderwidth=2) 
        self.new_data.place(x=25,y=280,width=375,height=25)
            
        s_btn=Button(frm_update,bd=0,cursor="hand2",text="Update",fg="white",bg="dimgray",font=("times new roman",20,"bold"),activebackground="gray",activeforeground="white",command=self.update_details).place(x=25,y=330,width=375,height=40)

    def previous_details(self,event):
        if self.select_detatils.get() != "Select":
            cur=connection()
            cur.execute("select "+self.select_detatils.get()+" from student_details where registration_number= %s ",(self.rows[0][0]))
            row=cur.fetchone()
            previoust_data=row[0]
            self.mystr.set(previoust_data)
        else:    
            self.mystr.set("")

    def update_details(self):
        if self.select_detatils.get()=="Select" or self.new_data.get()=="":
            messagebox.showerror("Error","All feilds are required")
        elif self.old_data.get() == self.new_data.get():
            messagebox.showerror("Error","You are trying to update the same details")
        else:
            msg = messagebox.askquestion("Question","Do you surely need to update")
            if msg == 'yes':
                con= givi_me_connection()
                cur = con.cursor()
                cur.execute("update student_details set "+self.select_detatils.get()+" =%s where registration_number= %s",(self.new_data.get(),self.regno_var.get()))
                con.commit()
                messagebox.showinfo("Updated","Details Updated")
                cur.execute("Select * from student_details where registration_number=%s",(self.regno_var.get()))
                rows = cur.fetchall()
                self.found_data(rows)
                self.update_studet_frame(self.rows)

    def not_found(self):
        self.not_frm = Frame(self.update_student_root,bg='#f0f0f0')
        self.not_frm.place(x=300,y=250,height=400,width=1200)

def update_student_main():
    update_student_root=Tk()
    obj = update_Student(update_student_root)
    update_student_root.mainloop()    