# import module
from tkinter import *
import Common_Requirements_File
import Dashboard
import Admin_Area_File
from PIL import ImageTk
from tkinter import messagebox
from validate_email import validate_email
from connection import *

class Admin_Add_User:
    def __init__(self,admin_add_user_root):
        self.admin_add_user_root=admin_add_user_root
        self.admin_add_user_root.title("Add Teacher")
        self.backIcon=PhotoImage(file="images/back.png")
        self.capIcon = PhotoImage(file="images/cap1.png")

        self.fname_var = StringVar()
        self.lname_var = StringVar()
        self.department_var = StringVar()
        self.post_var = StringVar()
        self.email_var = StringVar()
        self.password_var = StringVar()
        self.ph_no_var = StringVar()
        self.c_password_var = StringVar()

        # Button for going back to Admin page or Dashboard page
        btn = Button(self.admin_add_user_root,text="            Go Back  ",image=self.backIcon ,compound=RIGHT,font= "Arial 15 bold", bg="#6600FF", fg="white",command=self.frame_back)
        btn.place(x=1280,y=80, height=40,width=200)

        p_obj=Common_Requirements_File.Common_Requirements(self.admin_add_user_root)
        p_obj.admin_area_header()
        self.add_user_frame()

    # create option's for going back
    def frame_back(self):
        frm = Frame(self.admin_add_user_root)
        frm.place(x=1230,y=80,height=100,width=250)

        btn = Button(frm,text="Go To Admin Area    ",image=self.backIcon ,compound=RIGHT,font= "Arial 15 bold", bg="#6600FF", fg="white",command=self.go_to_admin)
        btn.place(x=10, height=40,width=240)

        btn1 = Button(frm,text="Go To User Area    ",image=self.backIcon ,compound=RIGHT,font= "Arial 15 bold", bg="#6600FF", fg="white",command=self.go_to_user)
        btn1.place(x=10, y=50, height=40,width=240)

    # Function for going back to their pages
    def go_to_user(self):
        self.admin_add_user_root.destroy()
        Dashboard.Dashboard_Main()

    def go_to_admin(self):
        self.admin_add_user_root.destroy()
        Admin_Area_File.Admin_Area_Main()

    # create form for adding new teacher's
    def add_user_frame(self):
        frm = Frame(self.admin_add_user_root,bg='white')
        frm.place(x=450,y=125,height=550,width=600)

        lbl2=Label(frm,text='Register Teacher',font='Arial 20 bold',bg='white').place(x=190,y=30)    
        
        lbl3=Label(frm,text='First Name',font='Arial 11 bold',bg='white').place(x=20,y=110)
        lbl4=Label(frm,text='Last Name',font='Arial 11 bold',bg='white',bd=0).place(x=300,y=110)
        self.f_name=Entry(frm,textvariable=self.fname_var,font="Arial 12 bold",bg='lightgray')
        self.f_name.place(x=20,y=140,height=30,width=260)
        self.l_name=Entry(frm,textvariable=self.lname_var,font="Arial 12 bold",bg='lightgray')
        self.l_name.place(x=300,y=140,height=30,width=260)

        lbl5=Label(frm,text='Department',font='Arial 11 bold',bg='white').place(x=20,y=190)
        lbl6=Label(frm,text='Designation',font='Arial 11 bold',bg='white',bd=0).place(x=300,y=190)
        self.department=Entry(frm,textvariable=self.department_var,font="Arial 12 bold",bg='lightgray')
        self.department.place(x=20,y=220,height=30,width=260)
        self.post=Entry(frm,textvariable=self.post_var,font="Arial 12 bold",bg='lightgray')
        self.post.place(x=300,y=220,height=30,width=260)

        lbl7=Label(frm,text='Email Id',font='Arial 11 bold',bg='white',bd=0).place(x=20,y=270)
        self.email=Entry(frm,textvariable=self.email_var,font="Arial 12 bold",bg='lightgray')
        self.email.place(x=20,y=300,height=30,width=260)
        lbl10=Label(frm,text='Contact Number',font='Arial 11 bold',bg='white',bd=0).place(x=300,y=270)
        self.phn_no=Entry(frm,textvariable=self.ph_no_var,font="Arial 12 bold",bg='lightgray')
        self.phn_no.place(x=300,y=300,height=30,width=260)

        lbl8=Label(frm,text='Password',font='Arial 11 bold',bg='white').place(x=20,y=350)
        lbl9=Label(frm,text='Confirm Password',font='Arial 11 bold',bg='white',bd=0).place(x=300,y=350)
        self.password=Entry(frm,textvariable=self.password_var,font="Arial 12 bold",bg='lightgray',show="*")
        self.password.place(x=20,y=380,height=30,width=260)
        self.c_password=Entry(frm,font="Arial 12",bg='lightgray',show="*",textvariable=self.c_password_var)
        self.c_password.place(x=300,y=380,height=30,width=260)

        btn2=Button(frm,text='Sign Up',font='Arial 15 bold',bg='gray',fg='white',bd=0,cursor='hand2',command=self.register_data).place(x=20,y=460,height=50,width=540)

    # validate email correct or not
    def email_validate(self):
        a=0
        valid = validate_email(self.email.get())
        if valid:
            a=1
        return(a)

    # Checking input details and putting data in database
    def register_data(self):
        email_validate_check=self.email_validate()
        if self.f_name.get()=="" or self.l_name.get()=="" or self.department.get()=="" or self.post.get()=="" or self.email.get()=="" or self.password.get()=="" or self.c_password.get()=="":
            messagebox.showerror("Error","All fields are required")
        elif email_validate_check!=1:
            messagebox.showerror("Error","Email doesnot exists")
        elif len(self.password.get()) < 8 or len(self.password.get()) > 16:
            messagebox.showerror("Error","The Password Should Be Between 8 to 16 characters")
        elif self.password.get()!=self.c_password.get():
            messagebox.showerror("Error","password not match")
        else:           
            try:
                try:
                    import random 
                    t_code = random.randrange(100,999)
                    self.teacher_id_var=None
                    if self.department.get()=="Computer Science And Technology":
                        self.teacher_id_var=f"CSTAIEMP{t_code}"
                    elif self.department.get()=="Mechanical Engineering":
                        self.teacher_id_var=f"MEAIEMP{t_code}"
                    elif self.department.get()=="Electrical Engineering":
                        self.teacher_id_var=f"EEAIEMP{t_code}"
                    elif self.department.get()=="Civil Engineering":
                        self.teacher_id_var=f"CEAIEMP{t_code}"
                    elif self.department.get()=="Admin":
                        self.teacher_id_var=f"ADAIEMP{t_code}"
                    if self.teacher_id_var!= None:
                        con= givi_me_connection()
                        cur=con.cursor()
                        cur.execute("select * from teacher_details where Email=%s",self.email.get())
                        row = cur.fetchone()
                        if row!= None:
                            messagebox.showerror("Error","User Already Registered")
                        else:
                            cur.execute("insert into teacher_details values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                        self.teacher_id_var,
                                                        self.fname_var.get(),
                                                        self.lname_var.get(),
                                                        self.department_var.get(),
                                                        self.post_var.get(),
                                                        self.email_var.get(),
                                                        self.phn_no.get(),
                                                        self.password_var.get()
                                ))
                            con.commit()
                            con.close()
                            messagebox.showinfo("Info","Registered")
                            print(self.fname_var.get())
                            self.fname_var.set("")
                            self.lname_var.set("")
                            self.department_var.set("")
                            self.post_var.set("")
                            self.email_var.set("")
                            self.ph_no_var.set("")
                            self.password_var.set("")
                            self.c_password_var.set("")
                    else:
                        messagebox.showerror("Error","Please Enter Correct Department ")                      
                except:
                    messagebox.showerror("Error","Please Enter Correct Department ")        

            except Exception as e:
                messagebox.showerror("Error","Some Error Occured \nPlease Try Again After Sometime")
       
def admin_add_user_main():
    admin_add_user_root=Tk()
    obj=Admin_Add_User(admin_add_user_root)
    admin_add_user_root.mainloop()

# admin_add_user_main()