# import module
from tkinter import *
from typing import Type
import connection
from tkinter import ttk
from PIL import ImageTk
import Common_Requirements_File
import datetime
from calendar import monthrange
from tkinter import messagebox
import export_file_process

class current_monthly_view:
    def __init__(self,current_monthly_view_root):
        self.current_monthly_view_root = current_monthly_view_root
        self.current_monthly_view_root.title("Monthly View")

        self.reverse_image=PhotoImage(file="images/reverse.png")
        self.forward_image=PhotoImage(file="images/forward.png")
        self.capIcon = PhotoImage(file="images/export.png")

        self.now = datetime.datetime.now()
        self.day=self.now.day
        self.month=self.now.month
        self.year=self.now.year

        self.search_box()

        self.p_obj=Common_Requirements_File.Common_Requirements(self.current_monthly_view_root)
        self.p_obj.header()
        self.p_obj.left_nav_bar_setting()
        self.p_obj.right_nav_bar_setting()

    # function used for searching Month, Department & year wish attendance
    def search_box(self):
        frm = Frame(self.current_monthly_view_root,bg='white')
        frm.place(x=450,y=190,height=400,width=600)

        title1=Label(frm,text="Monthly Attendence",font=("Candara Light",35,"bold","underline"),fg="black",bg="white").pack(side=TOP)
        
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

    # process_data function used for getting data from entries
    def process_data(self):
        if self.dept.get()==self.dept_values[0] or self.cyear.get()==self.year_values[0]:
            messagebox.showerror("Error","Enter required values in the fields")
        else:
            self.year=self.dyear.get()
            selected_month=self.month_values.index(self.cmonth.get())+1
            if selected_month == self.now.month and int(self.dyear.get())==self.now.year:
                self.day=self.now.day
                self.month=selected_month
            else:
                self.month=selected_month
                self.day=monthrange(int(self.year),self.month)[1]

            self.make_tree()

    # function used for showing previous month attendence    
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

    # function used for showing next month attendence  
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
        try:       
            self.bottom_search_box(self.cyear.get(),self.dept.get(),self.cmonth.get(),self.dyear.get())

            yearLabel = Label(self.current_monthly_view_root,font="Arial 15",text=f"{self.month_values[self.month-1]} - {self.year}")
            yearLabel.place(x=670,y=75,height=60,width=164)

            # Button's for showing month wish attendence
            previous_btn = Button(self.current_monthly_view_root,image=self.reverse_image,command=self.show_previous_month_details)
            previous_btn.place(x=300,y=85,height=40,width=40)

            next_btn = Button(self.current_monthly_view_root,image=self.forward_image,command=self.show_next_month_details)
            next_btn.place(x=1174,y=85,height=40,width=40)

            self.tree=ttk.Treeview(self.current_monthly_view_root)
            self.tree.place(x=300,y=150,height=450,width=900)
            Scrollbar_x=ttk.Scrollbar(self.current_monthly_view_root,orient='horizontal',command=self.tree.xview)
            Scrollbar_y=ttk.Scrollbar(self.current_monthly_view_root,orient='vertical',command=self.tree.yview)
                    
            s = ttk.Style(self.current_monthly_view_root)
            s.theme_use("clam")
            s.configure(".", font=('Arial', 12))
            s.configure("Treeview.Heading", foreground="blue",font=('Arial', 11,"bold"),xscrollcommand=Scrollbar_x.set,yscrollcommand=Scrollbar_y.set)
                    
            Scrollbar_x.place(x=300,y=600,width=914)
            Scrollbar_y.place(x=1200,y=150,height=450)
            self.tree.config(xscrollcommand=Scrollbar_x.set)
            self.tree.config(yscrollcommand=Scrollbar_y.set)

            # Directing to Create & Insert month values            
            if self.month > self.now.month:
                if int(self.year) >= self.now.year:
                    self.make_column()
                else:
                    self.make_column()
                    self.insert_value()
            else:         
                self.make_column()
                self.insert_value()

            self.p_obj.close_search_frame()

        except Exception:
            pass
    
    # function for creating columns        
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
                self.tree.column("Registration Number", anchor="center")
                self.tree.heading("Registration Number", text="Registration Number")
            else:
                self.tree.column(i-1, anchor="center",width=70, minwidth=70)
                self.tree.heading(i-1, text=i-1)

    # export_table function used for make montly excel sheet
    def export_table(self):         
        exported_file_name=f"{self.current_monthly_view_root.title()}-{self.month_values[self.month-1]}-{self.year}"
        status,file_location=export_file_process.save(self.tree["columns"],self.excel_data,exported_file_name)
        if status=="done":
            messagebox.showinfo("Information",f"File exported successfully to the following location in your device:\n{file_location}")
        elif status=="not done":
            messagebox.showerror("Error","Some error occured, file not exported")
        elif status=="not data available":
            messagebox.showinfo("Information","No data available to export\nPlease !! try with another criteria")

    # Fetching month & date
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
        self.excel_data=[]
        cur = connection.connection()
        cur.execute("select distinct(s.registration_number) from student_details s left join attendance_details a on a.registration_number=s.registration_number where s.department=%s and s.year=%s order by s.registration_number",(self.dept.get(),self.cyear.get()))
        self.rows = cur.fetchall()
        j=1
        val=[]
        for row in self.rows:
            for i in range (self.day+2):
                if i == 0:
                    val.append(j)
                elif i == 1:
                    val.append(row[0])
                else:
                    date = self.give_me_date(i)

                    cur = connection.connection()
                    cur.execute("select attandance from attendance_details where registration_number=%s and date= %s",(row[0],date))
                    x = cur.fetchall()
                    if len(x)==0:
                        val.append("NA")
                    else:
                        val.append(x[0][0])

            self.excel_data.append(tuple(val))  
            self.tree.insert('','end',values=tuple(val)) 
            j+=1
            val.clear()

        export_btn=Button(self.current_monthly_view_root,image=self.capIcon,text="EXPORT",cursor="hand2",font="bold 10",compound=LEFT,command=self.export_table) 
        export_btn.place(x=1385,y=710,width=100)   

    # Search for another month, department, year monthly attendence
    def bottom_search_box(self,cyear,cdept,cmonth,dyear):
        frm = Frame(self.current_monthly_view_root)
        frm.place(x=300,y=650,height=80,width=914)

        self.cyear = ttk.Combobox(frm, value=self.year_values,font="calibri 12",state='readonly') 
        self.cyear.place(width=150,height=30)
        self.cyear.current(self.year_values.index(cyear))

        self.dept = ttk.Combobox(frm, value=self.dept_values,font="calibri 12",state='readonly') 
        self.dept.place(x=253,width=150,height=30)
        self.dept.current(self.dept_values.index(cdept))

        self.cmonth = ttk.Combobox(frm, value=self.month_values,font="calibri 12",state='readonly')
        self.cmonth.place(x=506,width=150,height=30)
        self.cmonth.current(self.month_values.index(cmonth))
        
        self.dyear = ttk.Combobox(frm, value=self.dyear_values,font="calibri 12",state='readonly')
        self.dyear.place(x=761,width=150,height=30)
        self.dyear.current(self.dyear_values.index(int(dyear)))
        

        s_btn=Button(frm,bd=0,cursor="hand2",text="Search",fg="white",bg="gray",font=("times new roman",15,"bold"),activebackground="gray",activeforeground="white",command=self.process_data).place(x=370,y=45,width=176,height=30)

def current_monthly_view_main():
    current_monthly_view_root = Tk()
    obj=current_monthly_view(current_monthly_view_root)
    current_monthly_view_root.mainloop()

# current_monthly_view_main()