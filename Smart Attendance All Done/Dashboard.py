# import module
from tkinter import *
import Common_Requirements_File
from PIL import ImageTk
from tkinter import messagebox
import time as tm
import admin_user_verification
import account_settings_verification
import Admin_Area_File
import set_user_credentials
import current_attendance
import monthly_view
from connection import*
inital=[0,0,0,0]
import datetime

# A class with init method
class Dashboard:
    # init method or constructor
    def __init__(self,root_dashboard):
        self.root_dashboard=root_dashboard
        self.root_dashboard.title("Dashboard")
        self.presentIcon=PhotoImage(file="images/present.png")
        self.absentIcon=PhotoImage(file="images/absent.png")
        self.month_attendanceIcon=PhotoImage(file="images/monthly_attendance.png")
        self.admin_userIcon=PhotoImage(file="images/admin_user_icon.png")
        self.settingsIcon=PhotoImage(file="images/settings.png")
        self.handIcon=PhotoImage(file="images/hand.png")

        self.first_row()
        self.second_row()
        
        # import navbar & sidebar
        p_obj=Common_Requirements_File.Common_Requirements(self.root_dashboard)
        p_obj.header()
        p_obj.left_nav_bar_setting()
        p_obj.right_nav_bar_setting()
        # self.date_time()
        self.live()
    #     self.root_dashboard.bind("<ButtonRelease-1>",self.click_event)

    # def click_event(Self,event):
    #     Common_Requirements_File.

    # Present, Absent & Monthly view card view
    def first_row(self):
        x=105

        self.options = {
            self.presentIcon : ["Present","_________________________________________________________________",self.goToCurrentPresent],
            self.absentIcon : ["Absent","_________________________________________________________________",self.goToCurrentAbsent],
            self.month_attendanceIcon : ["Monthly View ","_________________________________________________________________",self.goToMonthlyView],
        }

        for i in self.options:
            shadow_frame = Frame(self.root_dashboard,bg="gray").place(x=(x+4),y=154,height=180,width=360)
            t_present = Frame(self.root_dashboard,bg='white')
            t_present.place(x=x,y=150,height=180,width=360)
            t_present_icon=Label(self.root_dashboard,image=i,relief="solid",bd=1).place(x=(x+20),y=115)
            t_present_lbl = Label(t_present,text=f"{self.options[i][0]}",font="Arial 15",bg="white",fg="#A8A8A8",anchor="e").place(x=210,y=10,width=130)
            t_present_line = Label(t_present,text=f"{self.options[i][1]}",bg="white",fg="#A8A8A8").place(x=20,y=100,width=320)
            t_present_view = Button(self.root_dashboard,text="Show All",image=self.handIcon,compound=LEFT,font="Arial 10 underline",bg="white",fg="blue",bd=0,activebackground='white',activeforeground='green',cursor='hand2',command=self.options[i][2]).place(x=(x+20),y=280)
            x+=465

    # Directing to present,absent & monthly_view pages
    def goToCurrentPresent(self):
        self.root_dashboard.destroy()
        current_attendance.Current_Attendance_Main("Present")

    def goToCurrentAbsent(self):
        self.root_dashboard.destroy()
        current_attendance.Current_Attendance_Main("Absent")

    def goToMonthlyView(self):
        self.root_dashboard.destroy()
        monthly_view.current_monthly_view_main()

    # Admin area & Account Settings card view
    def second_row(self):
        x=220

        self.options_second_row = {
            self.admin_userIcon : ["Admin Area","___________________________________________________________________________",self.add_user],
            self.settingsIcon : ["Account Settings","___________________________________________________________________________",self.account_settings]  
        }

        for i in self.options_second_row:
            shadow_frame = Frame(self.root_dashboard,bg="gray").place(x=(x+5),y=425,height=250,width=420)
            t_update = Frame(self.root_dashboard,bg='white')
            t_update.place(x=x,y=420,height=250,width=420)
            t_present_icon=Label(self.root_dashboard,image=i,relief="solid",bd=1).place(x=(x+75),y=380)
            t_present_lbl = Label(t_update,text=f"{self.options_second_row[i][0]}",font="Arial 15",bg="white",fg="#A8A8A8").place(x=20,y=135)
            t_present_line = Label(t_update,text=f"{self.options_second_row[i][1]}",bg="white",fg="#A8A8A8").place(x=20,y=170)
            t_settings_view = Button(self.root_dashboard,text="Click Here",image=self.handIcon,compound=LEFT,font="Arial 10 underline",bg="white",fg="blue",bd=0,activebackground='white',activeforeground='green',cursor='hand2',command=self.options_second_row[i][2]).place(x=(x+20),y=620)
            x+=640

    # Admin verfication for add new user's
    def add_user(self):
        if admin_user_verification.btn_state_verification_box==0:
            admin_user_verification.verification_admin_main(self.root_dashboard.title())

    # Loginer account settings
    def account_settings(self):
        if account_settings_verification.btn_state_account_verification_box==0:
            account_settings_verification.account_settings_verification_main(root_Dashboard)

    # live view of present & absent
    def live(self):
        global after_date_time
        global live1
        global live2
        now = datetime.datetime.now()
        cur=connection()
        cur.execute("select * from attendance_details where date=%s",(now.strftime('%Y-%m-%d')))
        rows = cur.fetchall()
        present1=0
        absent=0
        for row in rows:
            if 'Present' in row[2]:
                present1+=1
            if 'Absent' in row[2]:
                absent+=1  

        t_present_count = Label(self.root_dashboard,text=f"{present1}",font="Arial 20",bg="white",anchor="e").place(x=350,y=200,width=90)
        t_absentt_count = Label(self.root_dashboard,text=f"{absent}",font="Arial 20",bg="white",anchor="e").place(x=825,y=200,width=90)

def Dashboard_Deiconify():
    root_Dashboard.deiconify()

def dest():
    root_Dashboard.destroy()    

# Verify admin verfication box     
def admin_verified():
    admin_name=admin_user_verification.admin_user.get()
    admin_pwd=admin_user_verification.admin_pwd.get()
    cur = connection()
    cur.execute("select * from admin_credentials where username= %s and password= %s",(admin_name,admin_pwd))
    row= cur.fetchone()
    if admin_name=="" or admin_pwd=="":
        messagebox.showwarning("Warning","All feilds are required",parent= admin_user_verification.vbox_root)
    elif row != None: 
        admin_user_verification.cancel_clicked()
        root_Dashboard.destroy()
        set_user_credentials.admin_name = admin_name
        Admin_Area_File.Admin_Area_Main()
    else:
        messagebox.showerror("Error","Wrong input",parent= admin_user_verification.vbox_root)

def Dashboard_Main():
    account_settings_verification.btn_state_account_verification_box=0
    admin_user_verification.btn_state_verification_box=0
    global root_Dashboard
    root_Dashboard=Tk()
    obj = Dashboard(root_Dashboard)
    root_Dashboard.mainloop()

# Dashboard_Main()