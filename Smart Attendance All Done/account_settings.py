# Import module
from tkinter import *
from tkinter import ttk 
from PIL import ImageTk
from connection import*
import datetime
import Common_Requirements_File
import set_user_credentials
from tkinter import messagebox
import Dashboard

class account_settings:
    def __init__(self,root_account_settings):

        self.root_account_settings = root_account_settings
        self.root_account_settings.title("Account Settings")
        self.frame1()
        self.username=set_user_credentials.set_username
        self.password=set_user_credentials.set_password

        self.p_obj=Common_Requirements_File.Common_Requirements(self.root_account_settings)
        self.p_obj.header()
        self.p_obj.left_nav_bar_setting()

    # Function used for back to dashboard page       
    def go_to_dashboard(self):
        self.root_current_attendance.destroy()
        Dashboard.Dashboard_Main()
    
    # Update form 
    def frame1(self):
        frm = Frame(self.root_account_settings,bg='white')
        frm.place(x=450,y=190,height=400,width=600)

        title1=Label(frm,text="Update Account",font=("Candara Light",35,"bold","underline"),fg="black",bg="white").pack(side=TOP)
        
        data_update_values=['Select','First_Name','Last_Name','Department','Designation','Email','Contact_Number','Password']

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

    def previous_details(self,event):
        if self.select_detatils.get() != "Select":
            cur=connection()
            cur.execute("select "+self.select_detatils.get()+" from teacher_details where email=%s and password=%s",(self.username,self.password))
            row=cur.fetchone()
            previoust_data=row[0]
            self.mystr.set(previoust_data) 
        else:    
            self.mystr.set("")

    # Update in database
    def update_details(self):
        if self.select_detatils.get()=="Select" or self.new_data.get()=="":
            messagebox.showerror("Error","All feilds are required")
        elif self.old_data.get()==self.new_data.get():
            messagebox.showerror("Error","You are updating the same thing")
        else:
            msg = messagebox.askquestion("Question","Do you surely need to update")
            if msg == 'yes':
                con = givi_me_connection()
                cur = con.cursor()
                cur.execute("update teacher_details set "+self.select_detatils.get()+" =%s where email=%s and password =%s",(self.new_data.get(),self.username,self.password))
                con.commit()
                messagebox.showinfo("Updated","Details Updated")
                self.p_obj.header()
                self.frame1()

def Account_Settings_Main():
    global root_account_settings
    root_account_settings=Tk()
    obj = account_settings(root_account_settings)
    root_account_settings.mainloop()

# Account_Settings_Main()


