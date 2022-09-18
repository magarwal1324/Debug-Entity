# import module
from tkinter import *
from PIL import ImageTk,Image,ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
from tkinter import messagebox
import set_user_credentials
import fetch_data
import Dashboard
import todays_attendance
import previous_attendance
import Login
import add_student
import account_settings_verification
import update_student
import monthly_view
import student_details
import delete_student
from connection import *
import os
import all_semester_average

# A class with init method
class Common_Requirements:
    # init method or constructor
    def __init__(self,root):
        self.root = root
        self.root.geometry("1500x750+10+25")
        self.root.resizable(0,0)
        self.root.iconbitmap("images\\software_icon.ico")
        self.image_Initialize() 
        self.username=set_user_credentials.set_username
        self.password=set_user_credentials.set_password
        self.name=fetch_data.first_name(self.username,self.password) 
        self.admin_name = set_user_credentials.admin_name
        self.search_student_var = StringVar()

    # getting images
    def image_Initialize(self):        
        self.openIcon = PhotoImage(file="images/open.png")
        self.closeIcon = PhotoImage(file="images/close.png")
        self.capIcon = PhotoImage(file="images/cap1.png")
        self.downIcon = PhotoImage(file="images/down.png")
        self.upIcon = PhotoImage(file="images/up.png")
        self.searchIcon=PhotoImage(file="images/search.png")
        self.navIcon = PhotoImage(file="images/navlbl.png")
        self.handIcon=PhotoImage(file="images/hand.png")

    # Function used for making navbar
    def header(self):
        account_settings_verification.btn_state_account_verification_box=0
        self.topFrame=Frame(self.root,bg='white')
        self.topFrame.place(x=0,y=0,height=60,width=1500)

        tagBtn = Button(self.topFrame,text="   Welcome to Smart Attendence System",image=self.capIcon,font='Arial 15 bold',compound=LEFT,fg='black',bg='white',activebackground='white',cursor='hand2',bd=0)
        if self.root.title() == "Students Details":
            tagBtn.place(x=535,y=10)
        else:
            tagBtn.place(x=150,y=10)

        if self.root.title() != "Students Details":
            search = Entry(self.topFrame,bg='lightgray',font="Arial 15",textvariable=self.search_student_var).place(x=900,y=15,height=30,width=250)
            search_btn = Button(self.topFrame,image=self.searchIcon,bd=0,bg="lightgray",activebackground="lightgray",cursor="hand2",command=self.search_student).place(x=1127,y=20,height=20,width=20)
        
        homeLabel = Label(self.topFrame,text=f"Hello, {self.name}", font='Arial 13',bg="white",fg='gray17',anchor="e")
        homeLabel.place(x=1245,y=15,width=200)

    def search_student(self):
        if self.search_student_var.get()=="":
            messagebox.showerror("Error","Please Enter The Fields To Proceed")
        else:
            try:
                self.search_btn_after_search.destroy()
                self.search_frame.destroy()
                self.search_frame_close.destroy()
                try:
                    reg_no=self.search_student_var.get()
                    cur=connection()
                    self.m=cur.execute("Select * from student_details where registration_number =%s",(self.search_student_var.get()))
                    self.rows = cur.fetchall()
                    if len(self.rows) == 0:
                        messagebox.showerror("error","Sorry, We cannot find a student with this registration")
                    else:
                        self.search_student_frame()
                except Exception as e:
                    print(e)
                    messagebox.showinfo("info","Sorry, Some Error Has Occured")
            except Exception:
                try:
                    cur=connection()
                    self.m=cur.execute("Select * from student_details where registration_number =%s",(self.search_student_var.get()))
                    self.rows = cur.fetchall()
                    if len(self.rows) == 0:
                        messagebox.showerror("error","Sorry, We cannot find a student with this registration")
                    else:
                        self.search_student_frame()
                except Exception as es:
                    print(es)
                    messagebox.showinfo("info","Sorry, Some Error Has Occured")

    def goToStudentsDetails_after_search(self,Event):
        self.root.destroy()
        student_details.student_details_main(self.rows[0][0])

    def search_student_frame(self):
        # global x
        # x = self.search_frame
        self.search_frame=Label(self.root,bg='lightgray')
        self.search_frame.place(x=900,y=50,height=120,width=250)
        try:
            self.search_frame.bind("<Button-1>", self.goToStudentsDetails_after_search)
        except Exception as es:
            print(es)

        self.rec_data=self.rows[0][7]
        
        with open(f'student_images/{self.rows[0][0]}.jpg','wb') as f:
            f.write(self.rec_data)

        image = Image.open(f"student_images/{self.search_student_var.get()}.jpg") 
        resize_image = image.resize((70, 80))
        img = ImageTk.PhotoImage(resize_image) 
        label1 = Label(self.search_frame,image=img)

        label1.image = img
        label1.place(x=10,y=15,height=90,width=80)
        label1.bind("<Button-1>", self.goToStudentsDetails_after_search)

        os.remove(f"student_images/{self.search_student_var.get()}.jpg")

        if self.rows[0][2] == "Computer Science and Technology":
            dept="CST"
        elif self.rows[0][2] == "Mechanical Engineering":
            dept="ME"
        elif self.rows[0][2] == "Civil Engineering":
            dept="CE"
        elif self.rows[0][2] == "Electrical Engineering":
            dept="EE"

        name_lbl = Label(self.search_frame,text=f"{self.rows[0][1]}",font='Arial 12 bold',fg='black',bg='lightgray',anchor="w",activebackground='lightgray')
        name_lbl.place(x=100,y=15,height=30,width=140)
        name_lbl.bind("<Button-1>", self.goToStudentsDetails_after_search)
        
        reg_no_lbl = Label(self.search_frame,text=f"{self.rows[0][0]}",font='Arial 12 bold',fg='black',bg='lightgray',anchor="w",activebackground='lightgray')
        reg_no_lbl.place(x=100,y=45,height=30,width=140)
        reg_no_lbl.bind("<Button-1>", self.goToStudentsDetails_after_search)

        dept_lbl = Label(self.search_frame,text=f"{dept}, {self.rows[0][3]}",font='Arial 12 bold',fg='black',bg='lightgray',anchor="w",activebackground='lightgray')
        dept_lbl.place(x=100,y=75,height=30,width=140)
        dept_lbl.bind("<Button-1>", self.goToStudentsDetails_after_search)

        self.search_btn_after_search = Button(self.topFrame,image=self.searchIcon,bd=0,bg="lightgray",activebackground="lightgray",cursor="hand2",command=self.search_student)
        self.search_btn_after_search.place(x=1097,y=20,height=20,width=20)
    
        self.search_frame_close=Button(self.root,text="❌",font='Calibri 15',bg='lightgray',fg='red',activeforeground='red',activebackground='lightgray',cursor='hand2',command=self.close_search_frame,bd=0)
        self.search_frame_close.place(x=1127,y=20,height=20,width=20)

    def close_search_frame(self):
        self.search_frame.destroy()
        self.search_btn_after_search.destroy()
        self.search_frame_close.destroy()
        self.search_student_var.set("")

    def admin_area_header(self):
        account_settings_verification.btn_state_account_verification_box=0
        self.topFrame=Frame(self.root,bg='white')
        self.topFrame.place(x=0,y=0,height=60,width=1500)

        tagBtn = Button(self.topFrame,text="   Welcome to Smart Attendence System",image=self.capIcon,font='Arial 15 bold',compound=LEFT,fg='black',bg='white',activebackground='white',cursor='hand2',bd=0)
        tagBtn.place(x=535,y=10)
        homeLabel = Label(self.topFrame,text=f"Hello, {self.admin_name}", font='Arial 13',bg="white",fg='gray17',anchor="e")
        homeLabel.place(x=1245,y=15,width=200)

    def get_options_left(self,title):
        opt = {

                'Dashboard': self.goToDashboard,
                "Today's Attendence": self.goToTodaysAttendance,
                'Previous Attendence': self.goToPreviousAttendance,
                'Monthly View':self.goToMonthlyView,
                'Add Student': self.goToAddStudent,
                'Student Details' : self.goToStudentsDetails,
                'Update Student': self.goToUpdateAccounts,
                'Delete Student' : self.goToDeleteStudent,
                'Semester Average' : self.goToAllSemesterAverage,
                'Log Out': self.logout         
            }
        if title == "Dashboard":
            opt["Dashboard"]=None
        elif title == "Today's Attendence":
            opt["Today's Attendence"]=None
        elif title == "Previous Attendence":
            opt["Previous Attendence"]=None
        elif title == "Add Student":
            opt["Add Student"]= None
        elif title=="Update Student":
            opt["Update Student"]=None
        elif title == "Monthly View":
            opt["Monthly View"] = None
        elif title=="Students Details":
            opt["Student Details"]=None
        elif title=="Delete Student":
            opt["Delete Student"]=None
        elif title=="Semester Average":
            opt["Semester Average"]=None

        return opt 

    def left_nav_bar_setting(self):
        
        self.btnState=False     

        openBtn=Button(self.topFrame,image=self.openIcon,bg='white',activebackground='white',cursor='hand2',bd=1,command=self.left_switch)
        openBtn.place(x=10,y=10)

        self.navRoot = Frame(self.root,bg='#042954',height=1000,width=250)
        self.navRoot.place(x=-250,y=0)
        Label(self.navRoot,image=self.navIcon,bg='white',borderwidth = 5,relief="ridge",fg='black',anchor='w').place(x=0,y=0,height=60,width=250)

        y= 60

        options = self.get_options_left(self.root.title())
        
        for i in options:
            Button(self.navRoot,text=i,font='Arial 15',bg='#042954',fg='white',activebackground='green',activeforeground='white',bd=2,command=options[i]).place(x=0,y=y,height=60,width=250)
            y += 60

        closeBtn = Button(self.navRoot,image=self.closeIcon,bg='white',activebackground='white',cursor='hand2',bd=1,command=self.left_switch)
        closeBtn.place(x=200,y=10)
   
    def left_switch(self):
        try:
            if self.btnState is True:

                for x in range(0,251,3):
                    self.navRoot.place(x=-x,y=0)
                    self.topFrame.update()

                self.btnState =  False
            
            else:
                for x in range(-250,0,3):
                    self.navRoot.place(x=x,y=0)
                    self.topFrame.update()

                self.btnState = True
        except Exception :
            m="no place"

    def get_options_right(self,title):
        opt = {
            'Account': self.goToAccountSettings,
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

    def goToDashboard(self):
        self.root.destroy()
        Dashboard.Dashboard_Main()

    def goToTodaysAttendance(self):
        self.root.destroy()
        todays_attendance.Todays_Attendance_Main()

    def goToPreviousAttendance(self):
        self.root.destroy()
        previous_attendance.Previous_Attendance_Main()

    def goToAddStudent(self):
        self.root.destroy()
        add_student.add_student_main()
  
    def goToUpdateAccounts(self):
        self.root.destroy()
        update_student.update_student_main()

    def goToDeleteStudent(self):
        self.root.destroy()
        delete_student.delete_student_main()

    def goToMonthlyView(self):
        self.root.destroy()
        monthly_view.current_monthly_view_main()

    def goToAccountSettings(self):
        if account_settings_verification.btn_state_account_verification_box==0:
            account_settings_verification.account_settings_verification_main(self.root)

    def goToStudentsDetails(self):
        self.root.destroy()
        student_details.student_details_main()

    def goToAllSemesterAverage(self):
        self.root.destroy()
        all_semester_average.all_semester_average_main()
