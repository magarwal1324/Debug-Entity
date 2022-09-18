# import module
from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
from validate_email import validate_email
from connection import *
import Dashboard

class login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1300x750+100+25")
        self.root.iconbitmap("images_software\\software_icon.ico")
        self.root.resizable(False,False)

        self.showPassword=PhotoImage(file="images_software/showPwd.png")
        self.hidePassword=PhotoImage(file="images_software/hidePwd.png")

        self.username_var = StringVar()
        self.pwd_var = StringVar()

        self.bg=ImageTk.PhotoImage(file="images_software/login_background.png")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        # self.signup_frame() 
        self.login_frame()

    # Admin login frame
    def login_frame(self):
        # Set Geometry
        Frame_signup=Frame(self.root,bg="#e1e2fa")
        Frame_signup.place(x=375,y=175,height=400,width=550)
        
        # Frame title and geometry
        title1=Label(Frame_signup,text="Log In Here",font=("Candara Light",35,"bold","underline"),fg="black",bg="#e1e2fa").place(x=170,y=10)
        description1=Label(Frame_signup,text="Admin Login Area",font=("calibri",15,"bold"),fg="#a42d5c",bg="#e1e2fa").place(x=200,y=70)

        # Input field for Email Id
        lal_user=Label(Frame_signup,text="Username:",font=("Goudy old style",15,"bold"),fg="grey",bg="#e1e2fa").place(x=50,y=125)
        self.txt_user=Entry(Frame_signup,textvariable=self.username_var,font=("calibri",15),bg="lightgray")
        self.txt_user.place(x=50,y=155,width=450,height=35)

        # Input field for password
        lal_pwd=Label(Frame_signup,text="Password:",font=("Goudy old style",15,"bold"),fg="grey",bg="#e1e2fa").place(x=50,y=200)
        self.txt_pwd=Entry(Frame_signup,textvariable=self.pwd_var,font=("calibri",15),bg="lightgray")
        self.txt_pwd.place(x=50,y=230,width=450,height=35)
        self.txt_pwd.default_show_val = self.txt_pwd['show']
        self.txt_pwd['show'] = "*"

        # Button's
        show1_password = Button(self.txt_pwd,command=self.show_password,image=self.hidePassword,bd=0,bg="lightgray",activebackground="lightgray",cursor="hand2").place(x=415,y=5)
        login_btn=Button(Frame_signup,command=self.login,bd=0,cursor="hand2",text="Log In",fg="white",bg="#a42d5c",font=("times new roman",20)).place(x=50,y=300,width=450,height=50)

    # Function for Show & Hide Password
    def show_password(self):
        if self.txt_pwd['show']=="*":
            self.txt_pwd['show'] = ""
            show1_password = Button(self.txt_pwd,command=self.show_password,image=self.showPassword,bd=0,bg="lightgray",activebackground="lightgray",cursor="hand2").place(x=415,y=5)
        else:
            self.txt_pwd['show'] = "*"
            hide_password = Button(self.txt_pwd,command=self.show_password,image=self.hidePassword,bd=0,bg="lightgray",activebackground="lightgray",cursor="hand2").place(x=415,y=5)

    # Function for check login field's
    def login(self):
        if self.txt_user.get() == "" or self.txt_pwd.get() == "":
            messagebox.showerror("Error","All feilds are required",parent= self.root)
        else:
            try:
                cur = connection()
                cur.execute("select * from admin_credential_camera where username= %s and Password= %s",(self.txt_user.get(),self.txt_pwd.get()))
                row= cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","Invalid Username Or Password",parent= self.root)
                else:
                    root_Login.destroy()                    
                    Dashboard.Dashboard_Main()
                    # self.login_frame2()

            except Exception as es:
                print(es)
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)

def login_main():
    global root_Login
    root_Login=Tk()
    # admin_user_verification.btn_state_verification_box=0
    obj=login(root_Login)
    root_Login.mainloop()

# login_main()
