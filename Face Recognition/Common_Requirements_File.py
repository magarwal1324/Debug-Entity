# import module
from tkinter import *
from PIL import ImageTk,Image,ImageFile
from tkinter import messagebox
import Dashboard
from connection import *
import os

class Common_Requirements:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1500x750+10+25")
        self.root.resizable(0,0)
        self.root.iconbitmap("images_software\\software_icon.ico")
        self.image_Initialize() 

        self.admin_name = "h"

    def image_Initialize(self):        
        self.capIcon = PhotoImage(file="images_software/cap1.png")
        self.downIcon = PhotoImage(file="images_software/down.png")
        self.upIcon = PhotoImage(file="images_software/up.png")
        
    def admin_area_header(self):
        self.topFrame=Frame(self.root,bg='white')
        self.topFrame.place(x=0,y=0,height=60,width=1500)

        tagBtn = Button(self.topFrame,text="   Welcome to Smart Attendence System",image=self.capIcon,font='Arial 15 bold',compound=LEFT,fg='black',bg='white',activebackground='white',cursor='hand2',bd=0)
        tagBtn.place(x=535,y=10)
        homeLabel = Label(self.topFrame,text=f"Hello, {self.admin_name}", font='Arial 13',bg="white",fg='gray17',anchor="e")
        homeLabel.place(x=1245,y=15,width=200)
  
    def get_options_right(self,title):
        opt = {
            'Account': None,
            'Log Out': self.logout          
        }

        if title == "Account Settings":
            opt["Account"]=None
        
        return opt
        
    def right_nav_bar_setting(self):
        self.btnState2=True    

        homeLabel_btn = Button(self.topFrame,image=self.downIcon,bg='white',bd=0,activebackground="white",cursor="hand2",command=self.right_switch)
        homeLabel_btn.place(x=1450,y=10)

        self.navRoot2 = Frame(self.root,bg='#042954',height=120,width=150)
        self.navRoot2.place(x=1500,y=60)

        y= 0      
        options = self.get_options_right(self.root.title()) 
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

    def logout(self):
        msgbox = messagebox.askquestion("Exit",'Do you want to Log Out',icon='warning')
        if msgbox == 'yes':
            tota = self.root.title()
            self.root.destroy()
            Login.login_main()
            # if tota != "Dashboard":
            #     Dashboard.root_Dashboard.destroy()
