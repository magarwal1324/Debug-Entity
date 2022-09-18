# Import Module
from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
from validate_email import validate_email
import admin_user_verification
import Dashboard
import set_user_credentials
import add_user
from connection import *
import random
import smtplib
from email.message import EmailMessage
from captcha.image import ImageCaptcha

# A class with init method
class login:
    # init method or constructor        
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1300x750+100+25")
        self.root.iconbitmap("images\\software_icon.ico")
        self.root.resizable(False,False)

        self.showPassword=PhotoImage(file="images/showPwd.png")
        self.hidePassword=PhotoImage(file="images/hidePwd.png")

        self.username_var = StringVar()
        self.pwd_var = StringVar()

        self.bg=ImageTk.PhotoImage(file="images/log_in_img.jpg")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        self.signup_frame() 
        self.login_frame()

    #Teacher's login frame
    def login_frame(self):
        # Set Geometry
        Frame_signup=Frame(self.root,bg="white")
        Frame_signup.place(x=575,y=150,height=450,width=550)

        # Frame title and geometry
        title1=Label(Frame_signup,text="Log In Here",font=("Candara Light",35,"bold","underline"),fg="black",bg="white").place(x=170,y=10)
        description1=Label(Frame_signup,text="Teacher Login Area",font=("calibri",15,"bold"),fg="#a42d5c",bg="white").place(x=200,y=70)

        # Input field for Email Id
        lal_user=Label(Frame_signup,text="Email:",font=("Goudy old style",15,"bold"),fg="grey",bg="white").place(x=50,y=125)
        self.txt_user=Entry(Frame_signup,textvariable=self.username_var,font=("calibri",15),bg="lightgray")
        self.txt_user.place(x=50,y=155,width=450,height=35)

        # Input field for password
        lal_pwd=Label(Frame_signup,text="Password:",font=("Goudy old style",15,"bold"),fg="grey",bg="white").place(x=50,y=215)
        self.txt_pwd=Entry(Frame_signup,textvariable=self.pwd_var,font=("calibri",15),bg="lightgray")
        self.txt_pwd.place(x=50,y=245,width=450,height=35)
        self.txt_pwd.default_show_val = self.txt_pwd['show']
        self.txt_pwd['show'] = "*"

        # Button's
        show1_password = Button(self.txt_pwd,command=self.show_password,image=self.hidePassword,bd=0,bg="lightgray",activebackground="lightgray",cursor="hand2").place(x=415,y=5)
        forget_btn=Button(Frame_signup,text='Forget Password?',font='Arial 10 bold',fg='#a42d5c',bg='white',bd=0,cursor='hand2',command = self.go_to_forgot_password).place(x=380,y=285)
        login_btn=Button(Frame_signup,command=self.login,bd=0,cursor="hand2",text="Log In",fg="white",bg="#a42d5c",font=("times new roman",20)).place(x=50,y=350,width=450,height=50)

    # Forgot password frame
    def go_to_forgot_password(self):
        # Set geometry
        Frame_forgot_password=Frame(self.root,bg="white")
        Frame_forgot_password.place(x=575,y=150,height=450,width=550)

        # Frame title and geometry
        title1=Label(Frame_forgot_password,text="Forgot Password",font=("Candara Light",35,"bold","underline"),fg="black",bg="white").place(x=75,y=10)

        # Input field for Email Id
        emaild=Label(Frame_forgot_password,text="Enter Email:",font=("Goudy old style",15,"bold"),fg="grey",bg="white").place(x=50,y=100)
        self.emailid_forgot=Entry(Frame_forgot_password,font=("calibri",15),bg="lightgray")
        self.emailid_forgot.place(x=50,y=130,width=450,height=35)

        # Send Otp button
        send_btn=Button(Frame_forgot_password,command=self.forget_password_check,bd=0,cursor="hand2",text="Send Otp To Your Email Address",fg="white",bg="#a42d5c",font=("times new roman",15)).place(x=50,y=200,width=450,height=50)

        # Input field for Otp
        lal_otp=Label(Frame_forgot_password,text="Enter OTP",font=("Goudy old style",15,"bold"),fg="grey",bg="white").place(x=50,y=265)
        self.txt_otp_forgot_pwd=Entry(Frame_forgot_password,font=("calibri",15),bg="lightgray")
        self.txt_otp_forgot_pwd.place(x=50,y=295,width=450,height=35)

        # Otp verification button
        Verify_btn=Button(Frame_forgot_password,command=self.forgot_otp_check,bd=0,cursor="hand2",text="Verify OTP",fg="white",bg="#a42d5c",font=("times new roman",20)).place(x=50,y=350,width=450,height=50)

    # Define forgot_otp_check function is used for checking correct Otp
    def forgot_otp_check(self):
        if str(self.txt_otp_forgot_pwd.get())==str(self.otp_forgot):
            self.frame_password_update()
        else:
            messagebox.showerror("Error","Enter Valid Otp")

    # Function for input field's for update password
    def frame_password_update(self):
        Frame_password_update=Frame(self.root,bg="white")
        Frame_password_update.place(x=575,y=150,height=450,width=550)

        title1=Label(Frame_password_update,text="New Password Area",font=("Candara Light",35,"bold","underline"),fg="black",bg="white").place(x=65,y=10)

        # Update new password feild's
        lal_user=Label(Frame_password_update,text="New Password:",font=("Goudy old style",15,"bold"),fg="grey",bg="white").place(x=50,y=125)
        self.new_password=Entry(Frame_password_update,font=("calibri",15),bg="lightgray")
        self.new_password.place(x=50,y=155,width=450,height=35)

        lal_pwd=Label(Frame_password_update,text="Confirm Password:",font=("Goudy old style",15,"bold"),fg="grey",bg="white").place(x=50,y=215)
        self.confirm_password=Entry(Frame_password_update,font=("calibri",15),bg="lightgray")
        self.confirm_password.place(x=50,y=245,width=450,height=35)

        login_btn=Button(Frame_password_update,command=self.update_forget_password,bd=0,cursor="hand2",text="Change Password",fg="white",bg="#a42d5c",font=("times new roman",20)).place(x=50,y=325,width=450,height=50)

    # Function for update password in database
    def update_forget_password(self):
        if self.new_password.get()=="" or self.confirm_password.get()=="":
            messagebox.showerror("Error","All Fields are required")
        elif str(self.new_password.get())==str(self.confirm_password.get()):
            con=givi_me_connection()
            cur=con.cursor()
            # print(self.emailid_forgot)
            # print(self.new_password.get())
            cur.execute("update teacher_details set password =%s where email=%s",(str(self.new_password.get()),str(self.email_id_forgot)))
            con.commit()
            messagebox.showinfo("info","Password has been successfully changed")
            self.login_frame()            
        elif len(self.new_password.get()) < 8 or len(self.new_password.get()) > 16:
            messagebox.showerror("Error","The Password Should Be Between 8 to 16 characters")
        else:
            messagebox.showerror("Error","Please Enter Correct Password")

    # Function for checking if email address is valid or not   
    def forget_password_check(self):
        cur=connection()
        cur.execute("Select * from teacher_details where Email =%s",(self.emailid_forgot.get()))
        rows=cur.fetchone()
        if rows!=None:
            self.email_id_forgot=self.emailid_forgot.get()
            self.otp_forgot = random.randrange(100000,1000000)
            self.forgot_otp_email()
        else:
            messagebox.showerror("Error","Enter Valid Email id")

    # Function for sending Otp to email
    def forgot_otp_email(self):
        subject =f"Smart Attendance Software Account {self.otp_forgot} is your verification code for secure access"
        # Message to be sent to email
        message=f"Hi,\nGreetings!\nYou are just a step away from accessing your Smart Attendance Software account \nWe are sharing a verification code to access your account.\nOnce you have verified the code, you'll be prompted to set a new password immediately. This is to ensure that only you have access to your account. \n\nYour OTP: {self.otp_forgot} \n\nBest Regards,\nTeam Smart Attendance Software"

        # Send email through SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('smartattendanceteam.official@gmail.com', 'smartattendance@team')
        email = EmailMessage()
        email['From'] = 'smartattendanceteam.official@gmail.com'
        email['To'] = str(self.email_id_forgot)
        email['Subject'] = subject
        email.set_content(message)
        server.send_message(email)
        messagebox.showinfo("OTP","OTP successfully send")

    def forget_password(self):
        Frame_forgot_password=Frame(self.root,bg="white")
        Frame_forgot_password.place(x=575,y=150,height=450,width=550)

        title1=Label(Frame_forgot_password,text="Find Your Account",font=("Candara Light",35,"bold","underline"),fg="black",bg="white").place(x=80,y=10)
        description1=Label(Frame_forgot_password,text="Please enter your valid details to find your account.",font=("calibri",14,"bold"),fg="#a42d5c",bg="white").place(x=70,y=70)

        lal_email=Label(Frame_forgot_password,text="Enter Your Email:",font=("Goudy old style",15,"bold"),fg="grey",bg="white").place(x=50,y=125)
        self.txt_email=Entry(Frame_forgot_password,textvariable=self.username_var,font=("calibri",15),bg="lightgray")
        self.txt_email.place(x=50,y=155,width=450,height=35)


        lal_pwd=Label(Frame_forgot_password,text="Password:",font=("Goudy old style",15,"bold"),fg="grey",bg="white").place(x=50,y=215)
        self.txt_pwd=Entry(Frame_forgot_password,textvariable=self.pwd_var,font=("calibri",15),bg="lightgray")
        self.txt_pwd.place(x=50,y=245,width=450,height=35)

    # Function for Show & Hide Password
    def show_password(self):
        if self.txt_pwd['show']=="*":
            self.txt_pwd['show'] = ""
            show1_password = Button(self.txt_pwd,command=self.show_password,image=self.showPassword,bd=0,bg="lightgray",activebackground="lightgray",cursor="hand2").place(x=415,y=5)
        else:
            self.txt_pwd['show'] = "*"
            hide_password = Button(self.txt_pwd,command=self.show_password,image=self.hidePassword,bd=0,bg="lightgray",activebackground="lightgray",cursor="hand2").place(x=415,y=5)

    # Generate Captcha
    def captcha_generator(self):       
        global captcha_code
        captcha_code = random.randrange(100000,1000000)
        image = ImageCaptcha()
        data = image.generate(str(captcha_code))
        image.write(str(captcha_code), 'out.png')
    
    # Function for verification of teacher's
    def login_frame2(self):
        self.captcha_generator()
     
        set_user_credentials.set_username = self.email
        set_user_credentials.set_password = self.password

        Frame_signup2=Frame(self.root,bg="white")
        Frame_signup2.place(x=575,y=150,height=450,width=550)
        
        self.outPng = PhotoImage(file="out.png")
        Label(Frame_signup2,image=self.outPng).place(x=50,y=115,height=60,width=200)

        # Recaptcha Generate Button
        resend_btn=Button(Frame_signup2,command=self.login_frame2,bd=0,cursor="hand2",text="↻",fg="white",bg="#a42d5c",font=("times new roman",20)).place(x=260,y=130,width=30,height=30)

        self.txt_captcha=Entry(Frame_signup2,font=("calibri",24),bg="lightgray")
        self.txt_captcha.place(x=300,y=115,width=200,height=60)

        title2=Label(Frame_signup2,text="Verify Here",font=("Candara Light",35,"bold","underline"),fg="black",bg="white").place(x=170,y=10)
        description2=Label(Frame_signup2,text="Verification Area",font=("calibri",15,"bold"),fg="#a42d5c",bg="white").place(x=200,y=70)

        # Button for Check Captcha send Otp to email address
        send_btn=Button(Frame_signup2,command=self.check_captcha,bd=0,cursor="hand2",text="Verify Captcha and Send OTP",fg="white",bg="#a42d5c",font=("times new roman",15)).place(x=50,y=200,width=450,height=50)

        lal_otp=Label(Frame_signup2,text="Enter OTP",font=("Goudy old style",15,"bold"),fg="grey",bg="white").place(x=50,y=265)
        self.txt_otp=Entry(Frame_signup2,font=("calibri",15),bg="lightgray")
        self.txt_otp.place(x=50,y=295,width=450,height=35)

        Verify_btn=Button(Frame_signup2,command=self.checkotp,bd=0,cursor="hand2",text="Verify OTP",fg="white",bg="#a42d5c",font=("times new roman",20)).place(x=50,y=350,width=450,height=50)

    # Check Captcha
    def check_captcha(self):
        if self.txt_captcha.get() == str(captcha_code):
            self.otp = random.randrange(100000,1000000)
            # print(self.otp)
            self.send_email()
        else:
            messagebox.showerror("Error","Enter Valid Captcha Code")
            self.login_frame2()

    # Send email after checking captcha
    def send_email(self):
        subject =f"Smart Attendance Software Account {self.otp} is your verification code for secure access"
        message=f"Hi,\nGreetings!\nYou are just a step away from accessing your Smart Attendance Software account\n\nYour OTP: {self.otp} \n\nBest Regards,\nTeam Smart Attendance Software"

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('smartattendanceteam.official@gmail.com', 'smartattendance@team')
        email = EmailMessage()
        email['From'] = 'smartattendanceteam.official@gmail.com'
        email['To'] = str(self.email)
        email['Subject'] = subject
        email.set_content(message)
        server.send_message(email)
        messagebox.showinfo("OTP","OTP successfully send")

    # After Verification of Otp redirecting to Dashboard page
    def checkotp(self):
        otp_verify=str(self.txt_otp.get())
        otp=str(self.otp)
        if otp_verify==otp:
            messagebox.showinfo("Success","Log In")
            self.root.destroy()
            Dashboard.Dashboard_Main()
        else:
            messagebox.showerror("Incorrect","Enter valid Data")

    # Function for get into adding new user         
    def signup_frame(self):
        Frame_login=Frame(self.root,bg="#a42d5c")
        Frame_login.place(x=175,y=150,height=450,width=450)

        title2=Label(Frame_login,text="Welcome",font=("Candara Light",50),fg="white",bg="#a42d5c").place(x=70,y=110)
        description2=Label(Frame_login,text="Attend today and achieve tomorrow",font=("calibri",15,"bold"),fg="white",bg="#a42d5c").place(x=45,y=190)

        signup_btn=Button(Frame_login,cursor="hand2",text="Add User",bd=0,bg="white",fg="black",font=("times new roman",20),command=self.add_user).place(x=75,y=350,width=250,height=50)

    # Verification box for admin
    def add_user(self):
        if admin_user_verification.btn_state_verification_box==0:
            admin_user_verification.verification_admin_main(self.root.title())

    # Function for check login field's
    def login(self):
        if self.txt_user.get() == "" or self.txt_pwd.get() == "":
            messagebox.showerror("Error","All feilds are required",parent= self.root)
        else:
            try:
                cur = connection()
                cur.execute("select * from teacher_details where Email= %s and Password= %s",(self.txt_user.get(),self.txt_pwd.get()))
                row= cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","Invalid Username Or Password",parent= self.root)
                else:
                    self.email=row[5]
                    self.password=row[7]
                    set_user_credentials.set_username = self.email
                    set_user_credentials.set_password = self.password
                    self.root.destroy()
                    Dashboard.Dashboard_Main()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)

# Verify admin box
def admin_verified():
    cur = connection()
    cur.execute("select * from admin_credentials where username= %s and password= %s",(admin_user_verification.admin_user.get(),admin_user_verification.admin_pwd.get()))
    row= cur.fetchone()
    admin_name=admin_user_verification.admin_user.get()
    admin_pwd=admin_user_verification.admin_pwd.get()
    if admin_name=="" or admin_pwd=="":
        messagebox.showwarning("Warning","All feilds are required",parent= admin_user_verification.vbox_root)
    elif row != None: 
        admin_user_verification.cancel_clicked()
        root_Login.destroy()
        add_user.add_user_main()
    else:
        messagebox.showerror("Error","Wrong input",parent= admin_user_verification.vbox_root)

def login_main():
    global root_Login
    root_Login=Tk()
    admin_user_verification.btn_state_verification_box=0
    obj=login(root_Login)
    root_Login.mainloop()

# login_main()
