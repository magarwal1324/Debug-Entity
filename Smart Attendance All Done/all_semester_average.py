# import module
from tkinter import *
from typing import Type
from connection import *
from tkinter import ttk
from PIL import ImageTk
import Common_Requirements_File
from datetime import *
from calendar import monthrange
from tkinter import messagebox
from dateutil.relativedelta import relativedelta
import export_file_process

# A class with init method
class all_semester_average:
    # init method or constructor
    def __init__(self,all_semester_average_root):
        self.all_semester_average_view_root = all_semester_average_root
        self.all_semester_average_view_root.title("Semester Average")
        self.capIcon = PhotoImage(file="images/export.png")

        self.now = datetime.now()
        self.day=self.now.day
        self.month=self.now.month
        self.year=self.now.year


        self.search_box()

        self.p_obj=Common_Requirements_File.Common_Requirements(self.all_semester_average_view_root)
        self.p_obj.header()
        self.p_obj.left_nav_bar_setting()
        self.p_obj.right_nav_bar_setting()

    def search_box(self):
        frm = Frame(self.all_semester_average_view_root,bg='white')
        frm.place(x=450,y=190,height=400,width=600)

        title1=Label(frm,text="Semesterly Average",font=("Times New Roman",30,"bold","underline"),fg="black",bg="white").pack(side=TOP,pady=20)
        
        self.dept_values=['Enter the Department','Computer Science And Technology','Civil Engineering','Electrical Engineering','Mechanical Engineering']
        self.year_values=['Enter the Year','1st Year','2nd Year','3rd Year']
        

        lal_year=Label(frm,text="Year:",font=("Goudy old style",16,"bold"),bg="white").place(x=50,y=110)
        self.cyear = ttk.Combobox(frm, value=self.year_values,font="calibri 12",state='readonly') 
        self.cyear.place(x=50,y=140,width=500,height=30)
        self.cyear.current(0)

        lal_dept=Label(frm,text="Department:",font=("Goudy old style",16,"bold"),bg="white").place(x=50,y=200)
        self.dept = ttk.Combobox(frm, value=self.dept_values,font="calibri 12",state='readonly') 
        self.dept.place(x=50,y=230,width=500,height=30)
        self.dept.current(0)

            
        s_btn=Button(frm,bd=0,cursor="hand2",text="Search",fg="white",bg="gray",font=("times new roman",20,"bold"),activebackground="gray",activeforeground="white",command=self.process_data).place(x=50,y=320,width=500,height=50)

    def process_data(self):
        if self.dept.get()==self.dept_values[0] or self.cyear.get()==self.year_values[0]:
            messagebox.showerror("Error","Enter required values in the fields")
        else:
            self.make_tree()

    # Display data in table   
    def make_tree(self):
        try:
            self.bottom_search_box(self.cyear.get(),self.dept.get())

            yearLabel = Label(self.all_semester_average_view_root,bg='dimgray',font="Arial 18 bold",fg="White",text=f"Semesterly Average of {self.cyear.get()} - {self.dept.get()}")
            yearLabel.place(x=300,y=75,height=70,width=914)


            self.tree=ttk.Treeview(self.all_semester_average_view_root)
            self.tree.place(x=300,y=150,height=450,width=900)
            Scrollbar_x=ttk.Scrollbar(self.all_semester_average_view_root,orient='horizontal',command=self.tree.xview)
            Scrollbar_y=ttk.Scrollbar(self.all_semester_average_view_root,orient='vertical',command=self.tree.yview)
                    
            s = ttk.Style(self.all_semester_average_view_root)
            s.theme_use("clam")
            s.configure(".", font=('Arial', 12))
            s.configure("Treeview.Heading", foreground="blue",font=('Arial', 11,"bold"),xscrollcommand=Scrollbar_x.set,yscrollcommand=Scrollbar_y.set)
                    
            Scrollbar_x.place(x=300,y=600,width=914)
            Scrollbar_y.place(x=1200,y=150,height=450)
            self.tree.config(xscrollcommand=Scrollbar_x.set)
            self.tree.config(yscrollcommand=Scrollbar_y.set)

            todays_date = date.today()
            self.sem=""
            self.sem_no=""
            self.student_year=self.cyear.get()
            if self.student_year=="1st Year":
                if todays_date.month>6:
                    self.sem="1st Semester"
                    self.sem_no=1
                else:
                    self.sem="2nd Semester"
                    self.sem_no=2
            elif self.student_year == "2nd Year":
                if todays_date.month>6:
                    self.sem="3rd Semester"
                    self.sem_no=3
                else:
                    self.sem="4th Semester"
                    self.sem_no=4
            elif self.student_year == "3rd Year":
                if todays_date.month>6:
                    self.sem="5th Semester"
                    self.sem_no=5
                else:
                    self.sem="6th Semester"
                    self.sem_no=6

                    
            self.make_column()
            self.insert_value()

            self.p_obj.close_search_frame()
        except Exception:
            pass
            
    def make_column(self):
        for i in range (self.sem_no+2):
            if i == 0:
                self.tree["columns"] = self.tree["columns"] + ("slno")
            elif i == 1:
                self.tree["columns"] = self.tree["columns"] + ("Registration Number",)
            else:
                self.tree["columns"] = self.tree["columns"] + (f"SEM - {i-1}",)

        self.tree['show']='headings'


        for i in range (self.sem_no+2):
            if i == 0:
                self.tree.column("slno", anchor="center",width=50, minwidth=50)
                self.tree.heading("slno", text="Sl/No")
            elif i == 1:
                self.tree.column("Registration Number", anchor="center")
                self.tree.heading("Registration Number", text="Registration Number")
            else:
                self.tree.column(f"SEM - {i-1}", anchor="center",width=70, minwidth=100)
                self.tree.heading(f"SEM - {i-1}", text=f"SEM - {i-1}")
  
    def getSemValues(self,registration_number):      
        cur = connection()
        reg_no=registration_number
        cur.execute("select year from student_details where registration_number=%s",(reg_no))
        student_year = cur.fetchall()
        now = datetime.now()
        current_month = now.month
        current_year=now.year

        student_sem=""
        sem_ending=""

        semesters={}

        if current_month>=1 and current_month<=6:
            if student_year[0][0] == "1st Year":
                student_sem=2
            elif student_year[0][0] == "2nd Year":
                student_sem=4
            elif student_year[0][0] == "3rd Year":
                student_sem=6

            sem_ending=str(current_year)+"-06-31"

        elif current_month>=7 and current_month<=12:
            if student_year[0][0] == "1st Year":
                student_sem=1
            elif student_year[0][0] == "2nd Year":
                student_sem=3
            elif student_year[0][0] == "3rd Year":
                student_sem=5
                    
            sem_ending=str(current_year)+"-12-31"

        sem_ending=datetime. strptime(sem_ending, '%Y-%m-%d').date()
        sem_month_dates={1:["-07-01","-12-31"],2:["-01-01","-06-30"],3:["-07-01","-12-31"],4:["-01-01","-06-30"],5:["-07-01","-12-31"],6:["-01-01","-06-30"]}
        for i in reversed(range(student_sem)):
            sem_starting=sem_ending + relativedelta(months=-6) 
            sem_starting_year=str(sem_starting).split("-")
            sem_starting_date= sem_starting_year[0]+sem_month_dates[i+1][0]
            sem_ending_date= sem_starting_year[0]+sem_month_dates[i+1][1]
            semesters[i+1] = [sem_starting_date, sem_ending_date]
            sem_ending=(datetime. strptime(sem_starting_date, '%Y-%m-%d').date())
            
        sem_avg={}
        for sem in semesters:
            try:
                cur.execute("select count(attandance) from attendance_details where registration_number=%s and attandance=%s and date between %s AND %s",(reg_no,"Present",semesters.get(sem)[0],semesters.get(sem)[1]))
                total_present_days_of_student = cur.fetchall()
                cur.execute("select count(date) from attendance_details where registration_number=%s and date between %s AND %s",(reg_no,semesters.get(sem)[0],semesters.get(sem)[1]))
                total_w_days_of_student=cur.fetchall()
                avg = (total_present_days_of_student[0][0]/total_w_days_of_student[0][0])*100
                sem_avg[sem]=str(round(avg,2))+"%"
            except:
                sem_avg[sem]="NA"
        self.semester_average=sem_avg

    def export_table(self):         
        exported_file_name=f"{self.all_semester_average_view_root.title()}-{self.cyear.get()}-{self.dept.get()}"
        status,file_location=export_file_process.save(self.tree["columns"],self.excel_data,exported_file_name)
        if status=="done":
            messagebox.showinfo("Information",f"File exported successfully to the following location in your device:\n{file_location}")
        elif status=="not done":
            messagebox.showerror("Error","Some error occured, file not exported")
        elif status=="not data available":
            messagebox.showinfo("Information","No data available to export\nPlease !! try with another criteria")

    def insert_value(self):
        self.excel_data=[]
        cur = connection()
        cur.execute("select distinct(s.registration_number) from student_details s left join attendance_details a on a.registration_number=s.registration_number where s.department=%s and s.year=%s order by s.registration_number",(self.dept.get(),self.cyear.get()))
        self.rows = cur.fetchall()
        j=1
        val=[]
        for row in self.rows:
            for i in range (self.sem_no+2):
                if i == 0:
                    val.append(j)
                elif i == 1:
                    val.append(row[0])
                else:                   
                    self.getSemValues(row[0])
                    val.append(self.semester_average[i-1])

            self.excel_data.append(tuple(val)) 
            self.tree.insert('','end',values=tuple(val)) 
            j+=1
            val.clear()

        export_btn=Button(self.all_semester_average_view_root,image=self.capIcon,text="EXPORT",font="bold 10",compound=LEFT,command=self.export_table) 
        export_btn.place(x=1385,y=710,width=100) 

    def bottom_search_box(self,cyear,cdept):
        frm = Frame(self.all_semester_average_view_root)
        frm.place(x=300,y=650,height=80,width=914)

        self.cyear = ttk.Combobox(frm, value=self.year_values,font="calibri 12",state='readonly') 
        self.cyear.place(width=150,height=30)
        self.cyear.current(self.year_values.index(cyear))

        self.dept = ttk.Combobox(frm, value=self.dept_values,font="calibri 12",state='readonly') 
        self.dept.place(x=761,width=150,height=30)
        self.dept.current(self.dept_values.index(cdept))      

        s_btn=Button(frm,bd=0,cursor="hand2",text="Search",fg="white",bg="gray",font=("times new roman",15,"bold"),activebackground="gray",activeforeground="white",command=self.process_data).place(x=370,y=45,width=176,height=30)

def all_semester_average_main():
    all_semester_average_root = Tk()
    obj=all_semester_average(all_semester_average_root)
    all_semester_average_root.mainloop()

# all_semester_average_main()