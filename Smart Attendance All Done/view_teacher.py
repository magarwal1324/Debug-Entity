# import module
from tkinter import *
import Common_Requirements_File
from tkinter import ttk 
from connection import*
import Dashboard
import Admin_Area_File
from PIL import ImageTk

class Admin_View_Teacher:
    def __init__(self,admin_view_teacher_root):
        self.admin_view_teacher_root =admin_view_teacher_root
        self.admin_view_teacher_root.title("View Teacher")
        self.backIcon=PhotoImage(file="images/back.png")
        self.capIcon = PhotoImage(file="images/cap1.png")

        btn = Button(self.admin_view_teacher_root,text="            Go Back  ",image=self.backIcon ,compound=RIGHT,font= "Arial 15 bold", bg="#6600FF", fg="white",command=self.frame_back)
        btn.place(x=1280,y=80, height=40,width=200)

        p_obj=Common_Requirements_File.Common_Requirements(self.admin_view_teacher_root)
        p_obj.admin_area_header()
        self.view_teacher()

    # Displaying full teacher's details in table
    def view_teacher(self):
        cur = connection()
        cur.execute("select * from teacher_details order by Department")
        rows = cur.fetchall()
        yearLabel = Label(self.admin_view_teacher_root,bg='dimgray',font="Arial 18 bold",text="Teacher Details",fg="White")
        yearLabel.place(x=376,y=140,height=70,width=800)

        tree=ttk.Treeview(self.admin_view_teacher_root)
        tree.place(x=73,y=250,height=450,width=1354)
        Scrollbar_x=ttk.Scrollbar(self.admin_view_teacher_root,orient='horizontal',command=tree.xview)
        Scrollbar_y=ttk.Scrollbar(self.admin_view_teacher_root,orient='vertical',command=tree.yview)
        
        s = ttk.Style(self.admin_view_teacher_root)
        s.theme_use("clam")
        s.configure(".", font=('Arial', 12))
        s.configure("Treeview.Heading", foreground="blue",font=('Arial', 11,"bold"),xscrollcommand=Scrollbar_x.set,yscrollcommand=Scrollbar_y.set)
        
        Scrollbar_x.place(x=73,y=700,width=1370)
        Scrollbar_y.place(x=1429,y=250,height=450)
        tree.config(xscrollcommand=Scrollbar_x.set)
        tree.config(yscrollcommand=Scrollbar_y.set)

        tree["columns"]=("slno","Teacher Id","First Name","Last Name","Department","Designation","Contact Number","Email")

        tree.column("slno", width=50, minwidth=50, anchor="center")
        tree.column("Teacher Id",width=150, minwidth=150, anchor="center")
        tree.column("First Name",width=150, minwidth=150, anchor="center")
        tree.column("Last Name", width=125, minwidth=125, anchor="center")
        tree.column("Department", minwidth=325, anchor="center")
        tree.column("Designation", width=150, minwidth=125, anchor="center")
        tree.column("Contact Number", width=150, minwidth=150, anchor="center")
        tree.column("Email", width=350, minwidth=350, anchor="center")

        tree['show']='headings'

        tree.heading("slno", text="Slno")
        tree.heading("Teacher Id", text="Teacher Id")
        tree.heading("First Name", text="First Name")
        tree.heading("Last Name", text="Last Name")
        tree.heading("Department", text="Department")
        tree.heading("Designation", text="Designation")
        tree.heading("Contact Number", text="Contact Number")
        tree.heading("Email", text="email")

        j=1
        for row in rows:
            tree.insert('','end',values=(j,row[0],row[1],row[2],row[3],row[4],row[6],row[5])) 
            j+=1  

    def frame_back(self):
        frm = Frame(self.admin_view_teacher_root)
        frm.place(x=1230,y=80,height=100,width=250)

        btn = Button(frm,text="Go To Admin Area    ",image=self.backIcon ,compound=RIGHT,font= "Arial 15 bold", bg="#6600FF", fg="white",command=self.go_to_admin)
        btn.place(x=10, height=40,width=240)

        btn1 = Button(frm,text="Go To User Area    ",image=self.backIcon ,compound=RIGHT,font= "Arial 15 bold", bg="#6600FF", fg="white",command=self.go_to_user)
        btn1.place(x=10, y=50, height=40,width=240)

    def go_to_user(self):
        self.admin_view_teacher_root.destroy()
        Dashboard.Dashboard_Main()

    def go_to_admin(self):
        self.admin_view_teacher_root.destroy()
        Admin_Area_File.Admin_Area_Main()

def admin_view_teacher_main():
    admin_view_teacher_root=Tk()
    obj=Admin_View_Teacher(admin_view_teacher_root)
    admin_view_teacher_root.mainloop()

# admin_view_teacher_main()