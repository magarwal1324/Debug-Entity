# import module
from tkinter import *
import Common_Requirements_File
import Dashboard
import admin_account_settings
import admin_add_user
import view_teacher
import delete_teacher

# A class with init method
class Admin_Area:
    def __init__(self,root):
        self.root_admin_area=root
        self.root_admin_area.title("Admin Area")
        self.backIcon=PhotoImage(file="images/back.png")
        self.capIcon = PhotoImage(file="images/cap1.png")
        self.add_teacher = PhotoImage(file="images/add_teacher.png")
        self.teacher = PhotoImage(file="images/teacher.png")
        self.deleteteacher = PhotoImage(file="images/delete_teacher.png")
        self.accountsetting = PhotoImage(file="images/admin_account_setting.png")  
        
        btn = Button(self.root_admin_area,text="Go To User Area    ",image=self.backIcon ,compound=RIGHT,font= "Arial 15 bold", bg="#6600FF", fg="white",command=self.go_to_user)
        btn.place(x=1240,y=80, height=40,width=240)

        self.admin_area_frame1()

        # import sidebar
        p_obj=Common_Requirements_File.Common_Requirements(self.root_admin_area)
        p_obj.admin_area_header()

    # Back to dashboard page    
    def go_to_user(self):
        self.root_admin_area.destroy()
        Dashboard.Dashboard_Main()

    # create button's Add Teacher, Delete Teacher, View Teacher & Account Settings
    def admin_area_frame1(self):
        btn = Button(self.root_admin_area,text="Add Teacher",image=self.add_teacher,compound=TOP,font= "Arial 20 bold", bg="#BE975B", fg="white",command=self.goToAddTeacher)
        btn.place(x=400,y=125, height=250,width=300)

        btn1 = Button(self.root_admin_area,text="Delete Teacher",image=self.deleteteacher,compound=TOP,font= "Arial 20 bold", bg="#BE975B", fg="white",command=self.goToDeleteTeacher)
        btn1.place(x=800,y=125, height=250,width=300)

        btn2 = Button(self.root_admin_area,text="View Teacher",image=self.teacher,compound=TOP,font= "Arial 20 bold", bg="#B9975B", fg="white",command=self.goToViewTeacher)
        btn2.place(x=400,y=425, height=250,width=300)

        btn3 = Button(self.root_admin_area,text="Account Settings",image=self.accountsetting,compound=TOP,font= "Arial 20 bold", bg="#B9975B", fg="white",command=self.goToAdminAccountSettings)
        btn3.place(x=800,y=425, height=250,width=300)

    # Directing to their pages
    def goToViewTeacher(self):
        self.root_admin_area.destroy()
        view_teacher.admin_view_teacher_main()

    def goToAddTeacher(self):
        self.root_admin_area.destroy()
        admin_add_user.admin_add_user_main()

    def goToAdminAccountSettings(self):
        self.root_admin_area.destroy()
        admin_account_settings.Admin_Account_Settings_Main()

    def goToDeleteTeacher(self):
        self.root_admin_area.destroy()
        delete_teacher.Delete_Teacher_Main()

def Admin_Area_Main():
    root_admin_area=Tk()
    obj = Admin_Area(root_admin_area)
    root_admin_area.mainloop()


