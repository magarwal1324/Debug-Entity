# import module
from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
import csv
from validate_email import validate_email
import Login
from connection import *
        
class Add_User:
    def __init__(self,add_user_root):
        self.window=add_user_root
        self.window.geometry("1300x750+100+25")
        self.window.title("Add User")
        self.window.iconbitmap("images\\software_icon.ico")
        self.window.resizable(0,0)
        # self.window.configure.lineargradient('#FEAC5E','#C779D0','#4BC0C8')

        self.fname_var = StringVar()
        self.lname_var = StringVar()
        self.department_var = StringVar()
        self.post_var = StringVar()
        self.email_var = StringVar()
        self.phn_no_var= StringVar()
        self.password_var = StringVar()
        
        backimg=ImageTk.PhotoImage(file="images/rgbg.jpg")
        back_img=Label(self.window,image=backimg).place(x=0,y=0,relwidth=1,relheight=1)

        f1img=ImageTk.PhotoImage(file="images/rg.jpg")
        f1_img=Label(self.window,image=f1img).place(x=250,y=50,height=650,width=300)
        lal1=Label(self.window,text='Get Started',font='Arial 20 bold',bg='#145860',fg='white').place(x=325,y=640) 

        frame1=Frame(self.window,bg='white').place(x=550,y=50,height=650,width=500)
        
        btn1=Button(self.window,text='Log In',font='Arial 10 bold',bg='blue',fg='white',bd=0,cursor='hand2',command=self.returnWindow).place(x=950,y=75)
        
        lbl2=Label(self.window,text='Register',font='Arial 20 bold',bg='white').place(x=600,y=130)    
        
        # Entry box's
        lbl3=Label(self.window,text='First Name',font='Arial 10 bold',bg='white').place(x=600,y=200)
        lbl4=Label(self.window,text='Last Name',font='Arial 10 bold',bg='white',bd=0).place(x=830,y=200)
        self.f_name=Entry(self.window,textvariable=self.fname_var,font="Arial 12",bg='lightgray')
        self.f_name.place(x=600,y=230,height=30,width=180)
        self.l_name=Entry(self.window,textvariable=self.lname_var,font="Arial 12",bg='lightgray')
        self.l_name.place(x=830,y=230,height=30,width=180)
        
        lbl5=Label(self.window,text='Department',font='Arial 10 bold',bg='white').place(x=600,y=280)
        lbl6=Label(self.window,text='Designation',font='Arial 10 bold',bg='white',bd=0).place(x=830,y=280)
        self.department=Entry(self.window,textvariable=self.department_var,font="Arial 12",bg='lightgray')
        self.department.place(x=600,y=310,height=30,width=180)
        self.post=Entry(self.window,textvariable=self.post_var,font="Arial 12",bg='lightgray')
        self.post.place(x=830,y=310,height=30,width=180)
        
        lbl7=Label(self.window,text='Email Id ',font='Arial 10 bold',bg='white',bd=0).place(x=600,y=360)
        lbl10=Label(self.window,text='Contact No. ',font='Arial 10 bold',bg='white',bd=0).place(x=830,y=360)
        self.email=Entry(self.window,textvariable=self.email_var,font="Arial 12",bg='lightgray')
        self.email.place(x=600,y=390,height=30,width=180)
        self.phn_no=Entry(self.window,textvariable=self.phn_no_var,font="Arial 12",bg='lightgray')
        self.phn_no.place(x=830,y=390,height=30,width=180)

        
        lbl8=Label(self.window,text='Password',font='Arial 10 bold',bg='white').place(x=600,y=440)
        lbl9=Label(self.window,text='Confirm Password',font='Arial 10 bold',bg='white',bd=0).place(x=830,y=440)
        self.password=Entry(self.window,textvariable=self.password_var,font="Arial 12",bg='lightgray',show="*")
        self.password.place(x=600,y=470,height=30,width=180)
        self.c_password=Entry(self.window,font="Arial 12",bg='lightgray',show="*")
        self.c_password.place(x=830,y=470,height=30,width=180)
        
        btn2=Button(self.window,text='Sign Up',font='Arial 15 bold',bg='blue',fg='white',bd=0,cursor='hand2',command=self.register_data).place(x=600,y=540,height=50,width=410)
        
        lbl10=Label(self.window,text='Already a Member?',font='Arial 10 bold',bg='white').place(x=600,y=610)
        btn3=Button(self.window,text='Log In',font='Arial 10 bold underline',fg='blue',bg='white',bd=0,cursor='hand2',command=self.returnWindow).place(x=965,y=610)
        
        self.window.mainloop()

    # Check email address is correct or not
    def email_validate(self):
        a=0
        valid = validate_email(self.email.get())
        if valid:
            a=1
        return(a)

    # Checking all entry fields and inserting data in database
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
                                                        self.phn_no_var.get(),
                                                        self.password_var.get()
                                ))
                            con.commit()
                            con.close()
                            messagebox.showinfo("Info","Registered")
                            self.returnWindow()  
                    else:
                        messagebox.showerror("Error","Please Enter Correct Department ")                      
                except:
                    messagebox.showerror("Error","Please Enter Correct Department ")        

            except Exception as e:
                messagebox.showerror("Error","Some Error Occured \nPlease Try Again After Sometime")
                print(e)

    # If login failed return to login page      
    def returnWindow(self):
        self.window.destroy()
        Login.login_main()

def add_user_main():
    global add_user_root
    add_user_root=Tk()
    obj=Add_User(add_user_root)
    add_user_root.mainloop()

