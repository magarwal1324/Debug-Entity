# import module
from tkinter import *
from tkinter import ttk 
from PIL import ImageTk
from connection import*
import datetime
import Common_Requirements_File
from datetime import date

class todays_attendance_details:
    def __init__(self,root_todays_attendance_details,year,department):

        self.root_todays_attendance_details = root_todays_attendance_details
        self.root_todays_attendance_details.title("Today's Attendence Details")
        self.year=year
        self.department=department

        self.tree_view()

        p_obj=Common_Requirements_File.Common_Requirements(self.root_todays_attendance_details)
        p_obj.header()
        p_obj.left_nav_bar_setting()
        p_obj.right_nav_bar_setting()

    # Fetching data & Displaying in table
    def tree_view(self):
        now = datetime.datetime.now()
        # Displaying title asper search
        yearLabel = Label(self.root_todays_attendance_details,bg='Black',font="Arial 15",text=f"{self.year} - {self.department} - {now.strftime('%Y-%m-%d')}",fg="White")
        yearLabel.place(x=320,y=90,height=80,width=864)

        cur = connection()
        cur.execute("select s.registration_number, s.Name, a.attandance from student_details s left join attendance_details a on a.registration_number=s.registration_number where s.department=%s and s.year= %s and a.date=%s order by s.registration_number",(self.department,self.year,now.strftime('%Y-%m-%d')))
        rows = cur.fetchall()
        # studentsPreesent = cur.execute("select * from attendance_details where attandance= %s",('Present'))  
        
        # Count's total number of students, Total number of students present, Total number of students Absent & displaying it
        present1=0
        absent=0
        for row in rows:
            if 'Present' in row[2]:
                present1+=1
            if 'Absent' in row[2]:
                absent+=1  

        labelData = Label(self.root_todays_attendance_details,bg='gray',font="Arial 13",text=f"Total number of students = {len(rows)}\t\tPresent = {present1}\tAbsent = {absent}",fg="White")
        labelData.place(x=320,y=200,height=40,width=864)

        # Display columns and table values
        tree=ttk.Treeview(self.root_todays_attendance_details)
        tree.place(x=320,y=250,height=450)
        Scrollbar_x=ttk.Scrollbar(self.root_todays_attendance_details,orient='horizontal',command=tree.xview)
        Scrollbar_y=ttk.Scrollbar(self.root_todays_attendance_details,orient='vertical',command=tree.yview)
        
        s = ttk.Style(self.root_todays_attendance_details)
        s.theme_use("clam")
        s.configure(".", font=('Arial', 12))
        s.configure("Treeview.Heading", foreground="blue",font=('Arial', 11,"bold"),xscrollcommand=Scrollbar_x.set,yscrollcommand=Scrollbar_y.set)
        
        Scrollbar_x.place(x=320,y=700,width=864)
        Scrollbar_y.place(x=1170,y=250,height=450)
        tree.config(xscrollcommand=Scrollbar_x.set)
        tree.config(yscrollcommand=Scrollbar_y.set)

        tree["columns"]=("slno","Registration Number","Name","Attendance")

        tree.column("slno", width=100, minwidth=100, anchor="center")
        tree.column("Registration Number", width=250, minwidth=250, anchor="center")
        tree.column("Name", width=250, minwidth=250, anchor="center")
        tree.column("Attendance", width=250, minwidth=250, anchor="center")

        tree['show']='headings'

        tree.heading("slno", text="Slno")
        tree.heading("Registration Number", text="Registration Number")
        tree.heading("Name", text="Student Name")
        tree.heading("Attendance", text="Attendence")

        j=1
        for row in rows:
            tree.insert('','end',values=(j,row[0],row[1],row[2])) 
            j+=1  

def Todays_Attendance_Details_Main(year,department):
    global root_todays_details_attendance
    # year = '2nd Year'
    # department = 'Electrical Engineering'
    root_todays_attendance_details=Tk()
    obj = todays_attendance_details(root_todays_attendance_details,year,department)
    root_todays_attendance_details.mainloop()
# Todays_Attendance_Details_Main("2nd Year","Electrical Engineering")