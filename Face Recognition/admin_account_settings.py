# import module
from tkinter import *
from tkinter import ttk 
from PIL import ImageTk
from connection import *
import Dashboard
import datetime
import Common_Requirements_File
from tkinter import messagebox
import Dashboard
import login

class admin_account_settings:
    def __init__(self,root_admin_account_settings):
        self.root_admin_account_settings = root_admin_account_settings
        self.root_admin_account_settings.title("Admin Account Settings")
        self.root_admin_account_settings.geometry("1500x750+10+25")
        self.root_admin_account_settings.resizable(0,0)
        self.root_admin_account_settings.iconbitmap("images_software\\software_icon.ico")
        cur = connection()
        cur.execute("select username from admin_credential_camera ")
        self.admin_name= cur.fetchone()
        
        self.capIcon = PhotoImage(file="images_software/cap1.png")
        self.downIcon = PhotoImage(file="images_software/down.png")
        self.upIcon = PhotoImage(file="images_software/up.png")

        self.backIcon=PhotoImage(file="images_software/back.png")


        btn = Button(self.root_admin_account_settings,text="Go To Dashboard  ",image=self.backIcon ,compound=RIGHT,font= "Arial 15 bold", bg="#6600FF", fg="white",command=self.goToDashboard)
        btn.place(x=1230,y=80, height=40,width=250)

        # self.frame1()
        self.admin_area_header()
        self.right_nav_bar_setting()
        self.frame1()
    
    # Admin header
    def admin_area_header(self):
        self.topFrame=Frame(self.root_admin_account_settings,bg='white')
        self.topFrame.place(x=0,y=0,height=60,width=1500)

        tagBtn = Button(self.topFrame,text="   Welcome to Smart Attendence System",image=self.capIcon,font='Arial 15 bold',compound=LEFT,fg='black',bg='white',activebackground='white',cursor='hand2',bd=0)
        tagBtn.place(x=535,y=10)
        homeLabel = Label(self.topFrame,text=f"Hello, {self.admin_name[0]}", font='Arial 13',bg="white",fg='gray17',anchor="e")
        homeLabel.place(x=1245,y=15,width=200)

    def get_options_right(self,title):
        opt = {
            'Account': None,
            'Log Out': self.log_out         
        }

        if title == "Account Settings":
            opt["Account"]=None
        
        return opt
        
    def right_nav_bar_setting(self):
        self.btnState2=True    

        homeLabel_btn = Button(self.topFrame,image=self.downIcon,bg='white',bd=0,activebackground="white",cursor="hand2",command=self.right_switch)
        homeLabel_btn.place(x=1450,y=10)

        self.navRoot2 = Frame(self.root_admin_account_settings,bg='#042954',height=120,width=150)
        self.navRoot2.place(x=1500,y=60)

        y= 0      
        options = self.get_options_right(self.root_admin_account_settings.title()) 
        for i in options:
            Button(self.navRoot2,text=i,font='Arial 15',bg='#a42d5c',fg='white',activebackground='green',activeforeground='white',bd=2,command=options[i]).place(x=0,y=y,height=60,width=150)
            y += 60
   
    def right_switch(self):
        
        if self.btnState2 is True:

            self.navRoot2.place(x=1350,y=60)
            homeLabel_btn = Button(self.topFrame,image=self.upIcon,bg='white',bd=0,activebackground="white",cursor="hand2",command=self.right_switch)
            homeLabel_btn.place(x=1450,y=10)   
            self.btnState2 =  False
        
        else:

            self.navRoot2.place(x=1500,y=60)
            homeLabel_btn = Button(self.topFrame,image=self.downIcon,bg='white',bd=0,activebackground="white",cursor="hand2",command=self.right_switch)
            homeLabel_btn.place(x=1450,y=10)
            self.btnState2 = True


    def log_out(self):
        self.root_admin_account_settings.destroy()
        login.login_main()

    def goToDashboard(self):
        self.root_admin_account_settings.destroy()
        Dashboard.Dashboard_Main()

    # Update form
    def frame1(self):
        frm = Frame(self.root_admin_account_settings,bg='white')
        frm.place(x=450,y=190,height=400,width=600)

        title1=Label(frm,text="Update Account",font=("Candara Light",35,"bold","underline"),fg="black",bg="white").pack(side=TOP)
        
        data_update_values=['Select','username','Password']

        lal_select_detatils=Label(frm,text="Select Details To Change",font=("Goudy old style",18,"bold"),bg="white").place(x=50,y=80)
        self.select_detatils = ttk.Combobox(frm, value=data_update_values,font="calibri 12",state='readonly') 
        self.select_detatils .place(x=50,y=120,width=500,height=25)
        self.select_detatils .current(0)

        self.mystr = StringVar()

        lal_old_data=Label(frm,text="Previous Data",font=("Goudy old style",18,"bold"),bg="white").place(x=50,y=165)
        self.old_data = Entry(frm,font=("calibri",15, "bold"),fg="black",borderwidth=2,textvariable=self.mystr, state=DISABLED) 
        self.old_data.place(x=50,y=200,width=500,height=25)

        lal_new_data=Label(frm,text="New Data",font=("Goudy old style",18,"bold"),bg="white").place(x=50,y=240)
        self.new_data = Entry(frm,font=("calibri",12),borderwidth=2) 
        self.new_data.place(x=50,y=280,width=500,height=25)
            
        s_btn=Button(frm,bd=0,cursor="hand2",text="Update",fg="white",bg="dimgray",font=("times new roman",20,"bold"),activebackground="gray",activeforeground="white",command=self.update_details).place(x=50,y=330,width=500,height=50)
        self.select_detatils.bind("<<ComboboxSelected>>", self.previous_details)

    # Display already exist details in database
    def previous_details(self,event):
        if self.select_detatils.get() != "Select":
            cur=connection()
            cur.execute("select "+self.select_detatils.get()+" from admin_credential_camera")
            row=cur.fetchone()
            previoust_data=row[0]
            self.mystr.set(previoust_data)
        else:    
            self.mystr.set("")

    # Update values in database
    def update_details(self):

        if self.select_detatils.get()=="Select" or self.new_data.get()=="":
            messagebox.showerror("Error","All feilds are required")
        else:
            msg = messagebox.askquestion("Question","Do you surely need to update")
            if msg == 'yes':
                con = pymysql.connect(host="localhost", user="root",password="", database="stm")
                cur = con.cursor()
                cur.execute("update admin_credential_camera set "+self.select_detatils.get()+" =%s ",(self.new_data.get()))
                con.commit()
                messagebox.showinfo("Updated","Details Updated")

def Admin_Account_Settings_Main():
    root_admin_account_settings=Tk()
    obj = admin_account_settings(root_admin_account_settings)
    root_admin_account_settings.mainloop()
