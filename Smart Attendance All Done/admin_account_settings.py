# import module
from tkinter import *
from tkinter import ttk 
from PIL import ImageTk
from connection import *
import datetime
import Common_Requirements_File
import set_user_credentials
from tkinter import messagebox
import Dashboard
import Admin_Area_File

class admin_account_settings:
    def __init__(self,root_admin_account_settings):
        self.root_admin_account_settings = root_admin_account_settings
        self.root_admin_account_settings.title("Admin Account Settings")
        self.frame1()
        self.username=set_user_credentials.set_username
        self.password=set_user_credentials.set_password
        self.backIcon=PhotoImage(file="images/back.png")

        btn = Button(self.root_admin_account_settings,text="            Go Back  ",image=self.backIcon ,compound=RIGHT,font= "Arial 15 bold", bg="#6600FF", fg="white",command=self.frame_back)
        btn.place(x=1280,y=80, height=40,width=200)

        p_obj=Common_Requirements_File.Common_Requirements(self.root_admin_account_settings)
        p_obj.admin_area_header()

    def frame_back(self):
        frm = Frame(self.root_admin_account_settings)
        frm.place(x=1230,y=80,height=100,width=250)

        btn = Button(frm,text="Go To Admin Area    ",image=self.backIcon ,compound=RIGHT,font= "Arial 15 bold", bg="#6600FF", fg="white",command=self.go_to_admin)
        btn.place(x=10, height=40,width=240)

        btn1 = Button(frm,text="Go To User Area    ",image=self.backIcon ,compound=RIGHT,font= "Arial 15 bold", bg="#6600FF", fg="white",command=self.go_to_user)
        btn1.place(x=10, y=50, height=40,width=240)

    def go_to_user(self):
        self.root_admin_account_settings.destroy()
        Dashboard.Dashboard_Main()

    def go_to_admin(self):
        self.root_admin_account_settings.destroy()
        Admin_Area_File.Admin_Area_Main()

    # Update form
    def frame1(self):
        frm = Frame(self.root_admin_account_settings,bg='white')
        frm.place(x=450,y=190,height=400,width=600)

        title1=Label(frm,text="Update Account",font=("Candara Light",35,"bold","underline"),fg="black",bg="white").pack(side=TOP)
        
        data_update_values=['Select','username','password']

        # Select category User id or Password which you want to update 
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

    # Function used for showing current details after selecting which one you wanna update
    def previous_details(self,event):
        if self.select_detatils.get() != "Select":
            cur=connection()
            cur.execute("select "+self.select_detatils.get()+" from admin_credentials")
            row=cur.fetchone()
            previoust_data=row[0]
            self.mystr.set(previoust_data)
        else:    
            self.mystr.set("")

    # Update new data
    def update_details(self):

        if self.select_detatils.get()=="Select" or self.new_data.get()=="":
            messagebox.showerror("Error","All feilds are required")
        else:
            msg = messagebox.askquestion("Question","Do you surely need to update")
            if msg == 'yes':
                con = givi_me_connection()
                cur = con.cursor()
                cur.execute("update admin_credentials set "+self.select_detatils.get()+" =%s ",(self.new_data.get()))
                con.commit()
                messagebox.showinfo("Updated","Details Updated")

def Admin_Account_Settings_Main():
    global root_account_settings
    root_admin_account_settings=Tk()
    obj = admin_account_settings(root_admin_account_settings)
    root_admin_account_settings.mainloop()
