# import module
from tkinter import *
from datetime import *
from tkinter import ttk
from connection import *
from dateutil.relativedelta import relativedelta
btn_state_semesterly_view=0

class student_semesterly_attendence:
    def __init__(self,student_semersterly_average_root,reg_no):
        self.student_semersterly_average_root=student_semersterly_average_root
        self.student_semersterly_average_root.title("Student Semesterly Average")
        self.student_semersterly_average_root.geometry("600x300+30+445")
        self.student_semersterly_average_root.iconbitmap("images\\software_icon.ico")
        self.student_semersterly_average_root.resizable(0,0)
        self.student_semersterly_average_root.configure(bg='lightgray')
        self.student_semersterly_average_root.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.now = datetime.now()
        self.day=self.now.day
        self.month=self.now.month
        self.year=self.now.year

        self.reg_no=reg_no

        # connecting to database
        cur=connection()
        self.get_attendence_details_student=cur.execute("Select * from student_details where registration_number=%s ",(reg_no))
        self.get_attendence_details_student_row = cur.fetchall()
        self.registration_number=self.get_attendence_details_student_row[0][0]
        self.student_year=self.get_attendence_details_student_row[0][3]

        self.year_values=['Enter the Year','1st Year','2nd Year','3rd Year']
        self.month_values=['January','February','March','April','May','June','July','August','September','October','November','December']
       
        self.frame_display()
    
    # Defining frame_display function is for diplaying student's Semester attendence as per current semester 
    def frame_display(self):
        todays_date = date.today()
        self.sem=""
        self.sem_no=""
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

        self.tree=ttk.Treeview(self.student_semersterly_average_root)
        self.tree.place(x=50,y=120,height=120,width=500)
        Scrollbar_x=ttk.Scrollbar(self.student_semersterly_average_root,orient='horizontal',command=self.tree.xview)
        Scrollbar_y=ttk.Scrollbar(self.student_semersterly_average_root,orient='vertical',command=self.tree.yview)
                
        s = ttk.Style(self.student_semersterly_average_root)
        s.theme_use("clam")
        s.configure(".", font=('Arial', 12))
        s.configure("Treeview.Heading", foreground="blue",font=('Arial', 11,"bold"),xscrollcommand=Scrollbar_x.set,yscrollcommand=Scrollbar_y.set)
                
        Scrollbar_x.place(x=50,y=240,width=514)
        Scrollbar_y.place(x=550,y=120,height=134)
        self.tree.config(xscrollcommand=Scrollbar_x.set)
        self.tree.config(yscrollcommand=Scrollbar_y.set)

        Label(self.student_semersterly_average_root,text="Semesterly Average",font=("Candara Light",24,"bold","underline"),bg='lightgray').place(x=160,y=30)

        self.make_column()
        self.insert_value()
                
    def make_column(self):
        for i in range (self.sem_no+2):
            if i == 0:
                self.tree["columns"] = self.tree["columns"] + ("slno")
            elif i == 1:
                self.tree["columns"] = self.tree["columns"] + ("Registration Number",)
            else:
                self.tree["columns"] = self.tree["columns"] + (i-1,)

        self.tree['show']='headings'


        for i in range (self.sem_no+2):
            if i == 0:
                self.tree.column("slno", anchor="center",width=50, minwidth=50)
                self.tree.heading("slno", text="Sl/No")
            elif i == 1:
                self.tree.column("Registration Number", anchor="center")
                self.tree.heading("Registration Number", text="Registration Number")
            else:
                self.tree.column(i-1, anchor="center",width=70, minwidth=100)
                self.tree.heading(i-1, text=f"SEM - {i-1}")

    def getSemValues(self):      
        cur = connection()
        reg_no=self.registration_number
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

    def insert_value(self):
        self.rows=[]
        self.rows.append(self.registration_number)
        j=1
        val=[]
        for row in self.rows:
            for i in range (self.sem_no+2):
                if i == 0:
                    val.append(j)
                elif i == 1:
                    val.append(self.registration_number)
                else:                   
                    for i in range(1,self.sem_no+1):
                        self.getSemValues()
                        val.append(self.semester_average[i])
            self.tree.insert('','end',values=tuple(val)) 
            j+=1
            val.clear()

    def on_closing(self):
        global student_semersterly_average_root,btn_state_semesterly_view
        btn_state_semesterly_view=0
        student_semersterly_average_root.destroy()
        
def student_semersterly_average_main(reg_no):
    global student_semersterly_average_root,btn_state_semesterly_view
    student_semersterly_average_root=Toplevel()
    btn_state_semesterly_view = student_semersterly_average_root.winfo_exists()
    obj=student_semesterly_attendence(student_semersterly_average_root,reg_no)
    student_semersterly_average_root.mainloop()
