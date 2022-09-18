# import module
from fetch_data import email
from tkinter import *
from tkinter import ttk 
from PIL import ImageTk
from connection import*
import datetime
import Common_Requirements_File
import set_user_credentials
from tkinter import messagebox
import Dashboard
import Admin_Area_File

class delete_teacher:
    def __init__(self,root_delete_teacher):
        self.root_delete_teacher = root_delete_teacher
        self.root_delete_teacher.title("Delete Teacher")
        self.username=set_user_credentials.set_username
        self.password=set_user_credentials.set_password
        self.backIcon=PhotoImage(file="images/back.png")

        self.id_var = StringVar()
        self.name_var = StringVar()
        self.dept_var= StringVar()
        self.phone_var = StringVar()
        self.mail_var = StringVar()
        self.search_var = StringVar()

        btn = Button(self.root_delete_teacher,text="            Go Back  ",image=self.backIcon ,compound=RIGHT,font= "Arial 15 bold", bg="#6600FF", fg="white",command=self.frame_back)
        btn.place(x=1280,y=80, height=40,width=200)

        btn = Button(self.root_delete_teacher,text="View All Teachers" ,font= "Arial 15 bold", bg="gray", fg="white",activebackground='gray',activeforeground='white',command=self.viewAllTeachers)
        btn.place(x=280,y=650, height=40,width=200)

        self.search_box()
        self.list_of_teachers()

        p_obj=Common_Requirements_File.Common_Requirements(self.root_delete_teacher)
        p_obj.admin_area_header()
        p_obj.right_nav_bar_setting()

    # Button for refresh page and view all teacher's
    def viewAllTeachers(self):
        self.update_screen()
        self.list_of_teachers()

    def frame_back(self):
        frm = Frame(self.root_delete_teacher)
        frm.place(x=1230,y=80,height=100,width=250)

        btn = Button(frm,text="Go To Admin Area    ",image=self.backIcon ,compound=RIGHT,font= "Arial 15 bold", bg="#6600FF", fg="white",command=self.go_to_admin)
        btn.place(x=10, height=40,width=240)

        btn1 = Button(frm,text="Go To User Area    ",image=self.backIcon ,compound=RIGHT,font= "Arial 15 bold", bg="#6600FF", fg="white",command=self.go_to_user)
        btn1.place(x=10, y=50, height=40,width=240)

    def go_to_user(self):
        self.root_delete_teacher.destroy()
        Dashboard.Dashboard_Main()

    def go_to_admin(self):
        self.root_delete_teacher.destroy()
        Admin_Area_File.Admin_Area_Main()
    
    # Search teacher with their mail id
    def search_box(self):
        frm = Frame(self.root_delete_teacher,bg='white')
        frm.place(x=60,y=80,height=100,width=634)   

        Email=Label(frm,text="Enter Teacher Mail ID:",font=("Goudy old style",18,"bold"),bg="white").place(x=30,y=10)
        self.email = ttk.Entry(frm,  textvariable=self.search_var,  font="calibri 15") 
        self.email.place(x=30,y=45,width=534,height=35)

        s_btn=Button(frm,bd=0,cursor="hand2",text="🔍",fg="PURPLE",bg="WHITE",font=("times new roman",18,"bold"),activebackground="gray",activeforeground="white",command=self.search).place(x=579,y=45,width=40,height=35)

    # Function for search
    def search(self):
        if self.search_var.get()=="":
            messagebox.showerror("Error","Please Enter before clicking ")
        else:
            cur=connection()
            q2 = self.email.get()
            cur.execute("SELECT teacher_id, First_Name, Last_Name, Department, Designation, Email, Contact_Number FROM teacher_details WHERE Email LIKE '%"+q2+"%'  ")
            rows = cur.fetchall()
            if len(rows)!=0:
                self.tree.delete(*self.tree.get_children()) 
                for row in rows:
                    self.tree.insert('','end',values=row)
                    self.update_screen() 
            
            else:
                messagebox.showerror("Error","Enter a write value")
                self.update_screen()

    # function for displaying all teacher's
    def list_of_teachers(self):
        cur = connection()
        cur.execute("select * from teacher_details")
        rows = cur.fetchall()

        self.tree=ttk.Treeview(self.root_delete_teacher)
        self.tree.place(x=60,y=210,height=400,width=620)
        Scrollbar_x=ttk.Scrollbar(self.root_delete_teacher,orient='horizontal',command=self.tree.xview)
        Scrollbar_y=ttk.Scrollbar(self.root_delete_teacher,orient='vertical',command=self.tree.yview)

        s = ttk.Style(self.root_delete_teacher)
        s.theme_use("clam")
        s.configure(".", font=('Arial', 12))
        s.configure("Treeview.Heading", foreground="blue",font=('Arial', 11,"bold"),xscrollcommand=Scrollbar_x.set,yscrollcommand=Scrollbar_y.set)
        
        Scrollbar_x.place(x=60,y=610,width=634)
        Scrollbar_y.place(x=680,y=210,height=400)
        self.tree.config(xscrollcommand=Scrollbar_x.set)
        self.tree.config(yscrollcommand=Scrollbar_y.set)

        self.tree["columns"]=("Teacher Id","First Name","Last Name","Department","Designation","Email","Contact Number")

        self.tree.column("Teacher Id",minwidth=100,width=100, anchor="center")
        self.tree.column("First Name",minwidth=100,width=100, anchor="center")
        self.tree.column("Last Name",minwidth=100, width=100,anchor="center")
        self.tree.column("Department", minwidth=300,width=300, anchor="center")
        self.tree.column("Designation",minwidth=100, width=100,anchor="center")
        self.tree.column("Email",minwidth=300, width=300,anchor="center")
        self.tree.column("Contact Number",minwidth=100, width=100,anchor="center")

        self.tree['show']='headings'

        self.tree.heading("Teacher Id", text="Teacher Id")
        self.tree.heading("First Name", text="First Name")
        self.tree.heading("Last Name", text="Last Name")
        self.tree.heading("Department", text="Department")
        self.tree.heading("Designation", text="Designation")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Contact Number", text="Contact Number")
        self.tree.bind("<ButtonRelease-1>",self.get_cursor)

        j=1
        for row in rows:
            self.tree.insert('','end',values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6])) 
            j+=1  
    
    # Define get_cursor function used for on one click you can see the full details of the clicked teacher
    def get_cursor(self,event):
        cursor_row=self.tree.focus()
        self.content=self.tree.item(cursor_row,'values')
        self.delete_frame()

    # Function used for displaying teacher details & deleting teacher details
    def delete_frame(self):
        self.found_frm = Frame(self.root_delete_teacher,bg='white',highlightbackground="gray", highlightthickness=1)
        self.found_frm.place(x=780,y=210,height=414,width=620)
     
        Label(self.found_frm,text="Teacher Details",font=("Candara Light",30,"bold","underline"),fg="black",bg='white').place(x=175,y=10)

        Label(self.found_frm,text="Name : ",font=("times new roman",18),bg="white", fg="black").place(x=20,y=80)
        Label(self.found_frm,text=f"{self.content[1]} {self.content[2]}",font=("times new roman",18),bg="white", fg="black").place(x=200,y=80)

        Label(self.found_frm,text="Department : ",font=("times new roman",18),bg="white", fg="black").place(x=20,y=120)
        Label(self.found_frm,text=f"{self.content[3]}",font=("times new roman",18),bg="white", fg="black").place(x=200,y=120)

        Label(self.found_frm,text="Designation : ",font=("times new roman",18),bg="white", fg="black").place(x=20,y=165)
        Label(self.found_frm,text=f"{self.content[4]}",font=("times new roman",18),bg="white", fg="black").place(x=200,y=165)

        Label(self.found_frm,text="Email : ",font=("times new roman",18),bg="white", fg="black").place(x=20,y=210)
        Label(self.found_frm,text=f"{self.content[5]}",font=("times new roman",18),bg="white", fg="black").place(x=200,y=210)

        Label(self.found_frm,text="Contact Number : ",font=("times new roman",18),bg="white", fg="black").place(x=20,y=255)
        Label(self.found_frm,text=f"{self.content[6]}",font=("times new roman",18),bg="white", fg="black").place(x=200,y=255)
   
        del_btn=Button(self.found_frm,bd=0,cursor="hand2",text="Delete",fg="white",bg="Red",font=("times new roman",20,"bold"),activebackground="gray",activeforeground="white",command=self.delete_teacher_data).place(x=210,y=350,width=200,height=30)

    # Delete techer from database
    def delete_teacher_data(self):
        msg = messagebox.askquestion("Question",f"Do you surely want to Delete {self.content[0]} {self.content[1]}")
        if msg == 'yes':
            con=givi_me_connection()
            cur = con.cursor()
            cur.execute("Delete from teacher_details where Email =%s",(self.content[5]))
            con.commit()
            messagebox.showinfo("Deleted","Deleted Sucessfully")
            self.list_of_teachers()
            self.update_screen()

    def update_screen(self):
        self.found_frm = Frame(self.root_delete_teacher,bg='#f0f0f0')
        self.found_frm.place(x=780,y=210,height=414,width=620)

    # def delete_data(self):
    #     frm1 = Frame(self.root_delete_teacher,bg='white')
    #     frm1.place(x=60,y=360,height=350,width=1380)

    #     # id=Label(frm1,text="ID:",font=("Goudy old style",15,"bold"),bg="white").place(x=20,y=10)
    #     # self.id = ttk.Entry(frm1, textvariable='id_var', font="calibri 18") 
    #     # self.id.place(x=30,y=40,width=450,height=35)

    #     Email=Label(frm1,text="Teacher Email Id:",font=("Goudy old style",15,"bold"),bg="white").place(x=30,y=10)
    #     self.mail = ttk.Entry(frm1, textvariable='mail_var' , font="calibri 18") 
    #     self.mail.place(x=30,y=40,width=1320,height=35)

    #     Name=Label(frm1,text="Name:",font=("Goudy old style",15,"bold"),bg="white").place(x=30,y=90)
    #     self.name = ttk.Entry(frm1, textvariable='name_var', font="calibri 18") 
    #     self.name.place(x=30,y=130,width=1320,height=35)

    #     dept=Label(frm1,text="Teacher Department:",font=("Goudy old style",15,"bold"),bg="white").place(x=30,y=180)
    #     self.dept = ttk.Entry(frm1, textvariable='dept_var', font="calibri 18") 
    #     self.dept.place(x=30,y=220,width=850,height=35)

    #     phone=Label(frm1,text="Contact Number:",font=("Goudy old style",15,"bold"),bg="white").place(x=30,y=270)
    #     self.phone = ttk.Entry(frm1, textvariable='phone_var', font="calibri 18") 
    #     self.phone.place(x=30,y=310,width=850,height=35)

    #     d_btn=Button(frm1,bd=0,cursor="hand2",text="Delete",fg="white",bg="Red",font=("times new roman",20,"bold"),activebackground="gray",activeforeground="white",command=self.delete).place(x=990,y=250,width=200,height=40)

    # Connection with database for delete teacher
    def delete(self):
        con=givi_me_connection()
        cur= con.cursor()
        selected_item=self.tree.selection()[0]
        print(self.tree.item(selected_item)['values'])
        uid=self.tree.item(selected_item)['values'][0]
        del_query="DELETE FROM teacher_details WHERE Email = %s "
        sel_data=(uid)
        cur.execute(del_query,sel_data)
        con.commit()
        self.delete(selected_item)
        messagebox.showinfo("Success")
    
def Delete_Teacher_Main():
    global root_account_settings
    root_delete_teacher=Tk()
    obj = delete_teacher(root_delete_teacher)
    root_delete_teacher.mainloop()
