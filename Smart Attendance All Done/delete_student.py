# import module
from tkinter import *
from tkinter import ttk 
import Common_Requirements_File
from PIL import ImageTk,Image,ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True 
from tkinter import messagebox
from connection import *
import pymysql
import os

class Delete_Students:
    def __init__(self,delete_student_root):
        self.delete_student_root = delete_student_root
        self.delete_student_root.title("Delete Student")
        self.regno_var = StringVar()
        self.x=StringVar()


        self.regno()

        p_obj=Common_Requirements_File.Common_Requirements(self.delete_student_root)
        p_obj.header()
        p_obj.left_nav_bar_setting()
        p_obj.right_nav_bar_setting()
  
    def regno(self):
        self.frm = Frame(self.delete_student_root,bg='white')
        self.frm.place(x=550,y=100,height=100,width=400)

        regno=Label(self.frm,text="Enter Registration Number : ",font=("times new roman",15),bg="white", fg="black").place(x=10,y=15)
        self.txt_frame=Entry(self.frm,font=("time new roman",15),bg="lightgrey",textvariable=self.regno_var).place(x=10,y=50,width=330)
        s_btn=Button(self.frm,bd=0,cursor="hand2" ,text="🔍",fg="green",bg="white",font=(15),activebackground="white",activeforeground="white",command=self.check_regno).place(x=350,y=50,width=30,height=25)

    # Getting students details
    def check_regno(self):
        if self.regno_var.get()=="":
            messagebox.showerror("Error","Please Enter The Fields To Proceed")
        else:
            try:
                cur=connection()
                self.m=cur.execute("Select * from student_details where registration_number=%s",(self.regno_var.get()))
                self.rows = cur.fetchall()
                if len(self.rows) == 0:
                    self.not_found()
                    messagebox.showerror("Error","Sorry, We cannot find a student with this registration")
                else:
                    self.found_data(self.rows)
            except Exception:
                messagebox.showerror("Error","Some Error Occured")
    
    # Display data in frame
    def found_data(self,rows):
        self.found_frm = Frame(self.delete_student_root,bg='white')
        self.found_frm.place(x=450,y=220,height=500,width=600)

        self.rec_data=self.rows[0][7]
        with open(f'student_images/{self.rows[0][0]}.jpg','wb') as f:
            f.write(self.rec_data)

        image = Image.open(f"student_images/{self.regno_var.get()}.jpg") 
        resize_image = image.resize((150, 125), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(resize_image) 
        label1 = Label(self.found_frm,image=img)
        label1.image = img
        label1.place(x=425,y=50,height=125,width=150)
        
        # Profile picture
        os.remove(f"student_images/{self.regno_var.get()}.jpg")

        Label(self.found_frm,text=f"Details of {rows[0][0]}",font=("Candara Light",25,"bold","underline"),fg="black",bg='white').place(x=30,y=20)
     
        Label(self.found_frm,text="Reg No. : ",font=("times new roman",18),bg="white", fg="black").place(x=20,y=100)
        Label(self.found_frm,text=f"{rows[0][0]}",font=("times new roman",18),bg="white", fg="black").place(x=200,y=100)

        Label(self.found_frm,text="Name : ",font=("times new roman",18),bg="white", fg="black").place(x=20,y=140)
        Label(self.found_frm,text=f"{rows[0][1]}",font=("times new roman",18),bg="white", fg="black").place(x=200,y=140)

        Label(self.found_frm,text="Year : ",font=("times new roman",18),bg="white", fg="black").place(x=20,y=180)
        Label(self.found_frm,text=f"{rows[0][3]}",font=("times new roman",18),bg="white", fg="black").place(x=200,y=180)

        Label(self.found_frm,text="Department : ",font=("times new roman",18),bg="white", fg="black").place(x=20,y=220)
        Label(self.found_frm,text=f"{rows[0][2]}",font=("times new roman",18),bg="white", fg="black").place(x=200,y=220)

        Label(self.found_frm,text="Date of Birth : ",font=("times new roman",18),bg="white", fg="black").place(x=20,y=260)
        Label(self.found_frm,text=f"{rows[0][4]}",font=("times new roman",18),bg="white", fg="black").place(x=200,y=260)

        Label(self.found_frm,text="Number : ",font=("times new roman",18),bg="white", fg="black").place(x=20,y=300)
        Label(self.found_frm,text=f"{rows[0][5]}",font=("times new roman",18),bg="white", fg="black").place(x=200,y=300)
        
        Label(self.found_frm,text="Email : ",font=("times new roman",18),bg="white", fg="black").place(x=20,y=340)
        Label(self.found_frm,text=f"{rows[0][6]}",font=("times new roman",18),bg="white", fg="black").place(x=200,y=340)
   
        # Delete Button
        del_btn=Button(self.found_frm,bd=0,cursor="hand2",text="Delete",fg="white",bg="Red",font=("times new roman",20,"bold"),activebackground="gray",activeforeground="white",command=self.delete_student).place(x=210,y=415,width=200,height=30)

    # Deleting data from database
    def delete_student(self):
        msg = messagebox.askquestion("Question",f"Do you surely want to Delete {self.rows[0][1]} ")
        if msg == 'yes':
            try:
                con =givi_me_connection()
                cur=con.cursor()
                cur.execute("Delete from student_details where registration_number=%s",(self.rows[0][0]))
                con.commit()
                messagebox.showinfo("Deleted","Deleted Sucessfully")
                self.regno_var.set('')
                self.update_screen()
            except Exception:
                messagebox.showerror("Error","Sorry Some Error Occured")

    # Refresh screen button
    def update_screen(self):
        self.found_frm = Frame(self.delete_student_root,bg='#f0f0f0')
        self.found_frm.place(x=450,y=220,height=500,width=600)

    def not_found(self):
        self.not_frm = Frame(self.delete_student_root,bg='#f0f0f0')
        self.not_frm.place(x=450,y=220,height=500,width=600)

def delete_student_main():
    delete_student_root=Tk()
    obj = Delete_Students(delete_student_root)
    delete_student_root.mainloop()  