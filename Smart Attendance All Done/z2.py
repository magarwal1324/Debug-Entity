from  tkinter import *
from calendar import monthrange
import datetime
from tkinter import ttk
from PIL import ImageTk
import pymysql
import connection
import export_file_process
from tkinter import messagebox
btn_state_monthly_view=0

class student_monthly_attendence:
    def __init__(self,student_monthly_attendence_root,reg_no):
        global title1
        self.student_monthly_attendence_root=student_monthly_attendence_root
        self.student_monthly_attendence_root.title("Student Monthly Attendence")
        self.student_monthly_attendence_root.geometry("600x300+30+55")
        self.student_monthly_attendence_root.resizable(0,0)
        self.student_monthly_attendence_root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.month_values=['January','February','March','April','May','June','July','August','September','October','November','December']
        self.reg_no=reg_no

        self.reverse_image=PhotoImage(file="images/reverse.png")
        self.forward_image=PhotoImage(file="images/forward.png")

        self.now = datetime.datetime.now()
        self.day=self.now.day
        self.month=self.now.month
        self.year=self.now.year

        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        self.get_attendence_details_student=cur.execute("Select * from student_details where registration_number=%s ",(reg_no))
        self.get_attendence_details_student_row = cur.fetchall()
        self.registration_number=self.get_attendence_details_student_row[0][0]
        self.student_department=self.get_attendence_details_student_row[0][2]
        self.student_year=self.get_attendence_details_student_row[0][3]

        self.make_tree()

    def on_closing(self):
        global student_monthly_attendence_root,btn_state_monthly_view
        btn_state_monthly_view=0
        student_monthly_attendence_root.destroy()
        
    def search_box(self):
        global title1
        frm = Frame(self.current_monthly_view_root,bg='white')
        frm.place(x=450,y=190,height=400,width=600)

        title1=Label(frm,text="Monthly Attendance",font=("Candara Light",35,"bold","underline"),fg="black",bg="white").pack(side=TOP)
        
        self.dept_values=['Enter the Department','Computer Science And Technology','Civil Engineering','Electrical Engineering','Mechanical Engineering']
        self.year_values=['Enter the Year','1st Year','2nd Year','3rd Year']
        self.month_values=['January','February','March','April','May','June','July','August','September','October','November','December']
        self.dyear_values=[i for i in range(1947,self.year+1)]


        lal_user=Label(frm,text="Year:",font=("Goudy old style",16,"bold"),bg="white").place(x=50,y=70)
        self.cyear = ttk.Combobox(frm, value=self.year_values,font="calibri 12",state='readonly') 
        self.cyear.place(x=50,y=100,width=500,height=30)
        self.cyear.current(0)

        lal_pwd=Label(frm,text="Department:",font=("Goudy old style",16,"bold"),bg="white").place(x=50,y=150)
        self.dept = ttk.Combobox(frm, value=self.dept_values,font="calibri 12",state='readonly') 
        self.dept.place(x=50,y=180,width=500,height=30)
        self.dept.current(0)

        lal_date=Label(frm,text="Month:",font=("Goudy old style",16,"bold"),bg="white").place(x=50,y=245)
        self.cmonth = ttk.Combobox(frm, value=self.month_values,font="calibri 12",state='readonly')
        self.cmonth.place(x=130,y=245,height=30,width=150)
        self.cmonth.current(self.month-1)
        
        lal_dyear=Label(frm,text="Year:",font=("Goudy old style",16,"bold"),bg="white").place(x=340,y=245)
        self.dyear = ttk.Combobox(frm, value=self.dyear_values,font="calibri 12",state='readonly')
        self.dyear.place(x=400,y=245,height=30,width=150)
        self.dyear.current(len(self.dyear_values)-1)
            
        s_btn=Button(frm,bd=0,cursor="hand2",text="Search",fg="white",bg="gray",font=("times new roman",20,"bold"),activebackground="gray",activeforeground="white",command=self.process_data).place(x=50,y=320,width=500,height=50)
        
    def show_previous_month_details(self):
        if self.month==1:
            self.year=int(self.year)-1
            self.month=12
        else:
            self.month=self.month-1
            if self.month==self.now.month and int(self.year)==self.now.year:
                self.day=self.now.day
            else:
                self.day=monthrange(int(self.year),self.month)[1]

        self.make_tree()

    def show_next_month_details(self):
        if self.month == 12 and int(self.year)== self.now.year:
            False
        else:
            if self.month==12:
                    self.year=int(self.year)+1
                    self.month=1
            else:
                self.month=self.month+1
                if self.month==self.now.month and int(self.year)==self.now.year:
                    self.day=self.now.day
                else:
                    self.day=monthrange(int(self.year),self.month)[1]
            
            self.make_tree()
        
    def make_tree(self):
        yearLabel = Label(self.student_monthly_attendence_root,font="Arial 15",text=f"{self.month_values[self.month-1]} - {self.year}")
        yearLabel.place(x=150,y=50,height=40,width=300)

        previous_btn = Button(self.student_monthly_attendence_root,image=self.reverse_image,command=self.show_previous_month_details)
        previous_btn.place(x=50,y=50,height=40,width=40)

        next_btn = Button(self.student_monthly_attendence_root,image=self.forward_image,command=self.show_next_month_details)
        next_btn.place(x=520,y=50,height=40,width=40)

        

        self.tree=ttk.Treeview(self.student_monthly_attendence_root)
        self.tree.place(x=50,y=120,height=120,width=500)
        Scrollbar_x=ttk.Scrollbar(self.student_monthly_attendence_root,orient='horizontal',command=self.tree.xview)
        Scrollbar_y=ttk.Scrollbar(self.student_monthly_attendence_root,orient='vertical',command=self.tree.yview)
                
        s = ttk.Style(self.student_monthly_attendence_root)
        s.theme_use("clam")
        s.configure(".", font=('Arial', 12))
        s.configure("Treeview.Heading", foreground="blue",font=('Arial', 11,"bold"),xscrollcommand=Scrollbar_x.set,yscrollcommand=Scrollbar_y.set)
                
        Scrollbar_x.place(x=50,y=240,width=514)
        Scrollbar_y.place(x=550,y=120,height=134)
        self.tree.config(xscrollcommand=Scrollbar_x.set)
        self.tree.config(yscrollcommand=Scrollbar_y.set)

        if self.month > self.now.month:
            if int(self.year) >= self.now.year:
                self.make_column()
            else:
                self.make_column()
                self.insert_value()
        else:         
            self.make_column()
            self.insert_value()

    def export_table(self):         # this is change
        exported_file_name=f"{self.student_monthly_attendence_root.title()}-{self.month_values[self.month-1]}-{self.year}"
        status,file_location=export_file_process.save(self.tree["columns"],self.excel_data,exported_file_name)
        if status=="done":
            messagebox.showinfo("Information",f"File exported successfully to the following location in your device:\n{file_location}")
        elif status=="not done":
            messagebox.showerror("Error","Some error occured, file not exported")
        elif status=="not data available":
            messagebox.showinfo("Information","No data available to export\nPlease !! try with another criteria")

    def make_column(self):
        for i in range (self.day+2):
            if i == 0:
                self.tree["columns"] = self.tree["columns"] + ("slno")
            elif i == 1:
                self.tree["columns"] = self.tree["columns"] + ("Registration Number",)
            else:
                self.tree["columns"] = self.tree["columns"] + (i-1,)

        self.tree['show']='headings'

        for i in range (self.day+2):
            if i == 0:
                self.tree.column("slno", anchor="center",width=50, minwidth=50)
                self.tree.heading("slno", text="Sl/No")
            elif i == 1:
                self.tree.column("Registration Number", anchor="center",width=165, minwidth=165)
                self.tree.heading("Registration Number", text="Registration Number")
            else:
                self.tree.column(i-1, anchor="center",width=100, minwidth=100)
                self.tree.heading(i-1, text=i-1)
        

    def give_me_date(self,i):
        self.date=''
        if len(str(i))==1:
            if len(str(self.month))==1:
                self.date=str(self.year)+"-0"+str(self.month)+"-0"+str(i-1)
            else:
                self.date=str(self.year)+"-"+str(self.month)+"-0"+str(i-1)
        else:
            if len(str(self.month))==1:
                if str(i)=='10' :
                    self.date=str(self.year)+"-0"+str(self.month)+"-0"+str(i-1)
                else:
                    self.date=str(self.year)+"-0"+str(self.month)+"-"+str(i-1)
            else:
                if str(i)=='10' :
                    self.date=str(self.year)+"-0"+str(self.month)+"-0"+str(i-1)
                else:
                    self.date=str(self.year)+"-"+str(self.month)+"-"+str(i-1)  

        return self.date; 

    def insert_value(self):
        self.excel_data=[]  # this is change
        self.rows=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015]
        # self.rows.append(self.registration_number)
        j=1
        val=[]
        for row in self.rows:
            for i in range (self.day+2):
                if i == 0:
                    val.append(j)
                elif i == 1:
                    val.append(row)
                else:
                    date = self.give_me_date(i)

                    cur = connection.connection()
                    cur.execute("select attandance from attendance_details where registration_number=%s and date= %s",(row,date))
                    x = cur.fetchall()
                    if len(x)==0:
                        val.append("NA")
                    else:
                        val.append(x[0][0])

            
            self.excel_data.append(tuple(val))  # this is change
            self.tree.insert('','end',values=tuple(val)) 
            j+=1
            val.clear()

        export_btn=Button(self.student_monthly_attendence_root,text="EXPORT",command=self.export_table) # this is change
        export_btn.place(x=530,y=10,width=60)   # this is change

def student_monthly_aatendence_main(reg_no):
    global student_monthly_attendence_root,btn_state_monthly_view
    # btnstate=True
    student_monthly_attendence_root=Toplevel()
    btn_state_monthly_view = student_monthly_attendence_root.winfo_exists()
    obj=student_monthly_attendence(student_monthly_attendence_root,reg_no)
    student_monthly_attendence_root.mainloop()


student_monthly_aatendence_main(1001)