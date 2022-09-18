# import module
from tkinter import *
from tkinter import ttk 
from PIL import ImageTk
from connection import*
import datetime
import Common_Requirements_File
import Dashboard

class current_attendance:
    def __init__(self,root_current_attendance,attendance_of):

        self.root_current_attendance = root_current_attendance
        self.root_current_attendance.title("Current Attendence")
        self.attendance_of=attendance_of
        # print(self.attendance_of)

        self.tree_view()

        p_obj=Common_Requirements_File.Common_Requirements(self.root_current_attendance)
        p_obj.header()
        p_obj.left_nav_bar_setting()
        p_obj.right_nav_bar_setting()

    # Back to dashboard         
    def go_to_dashboard(self):
        self.root_current_attendance.destroy()
        Dashboard.Dashboard_Main()

    # Function used for viewing table
    def tree_view(self):
        now = datetime.datetime.now()
        yearLabel = Label(self.root_current_attendance,bg='dimgray',font="Arial 18 bold",text=f"{self.attendance_of} - {now.strftime('%Y-%m-%d')}",fg="White")
        yearLabel.place(x=73,y=140,height=70,width=1370)

        # Fetching data 
        cur = connection()
        cur.execute("select s.department , s.year , s.registration_number, s.Name, a.attandance from student_details s left join attendance_details a on a.registration_number=s.registration_number where a.date=%s and a.attandance=%s order by s.department,s.year,s.registration_number",(now.strftime('%Y-%m-%d'),self.attendance_of))
        rows = cur.fetchall()

        # Table for attendence view
        tree=ttk.Treeview(self.root_current_attendance)
        tree.place(x=73,y=250,height=450,width=1354)
        Scrollbar_x=ttk.Scrollbar(self.root_current_attendance,orient='horizontal',command=tree.xview)
        Scrollbar_y=ttk.Scrollbar(self.root_current_attendance,orient='vertical',command=tree.yview)
        
        s = ttk.Style(self.root_current_attendance)
        s.theme_use("clam")
        s.configure(".", font=('Arial', 12))
        s.configure("Treeview.Heading", foreground="blue",font=('Arial', 11,"bold"),xscrollcommand=Scrollbar_x.set,yscrollcommand=Scrollbar_y.set)
        
        Scrollbar_x.place(x=73,y=700,width=1370)
        Scrollbar_y.place(x=1429,y=250,height=450)
        tree.config(xscrollcommand=Scrollbar_x.set)
        tree.config(yscrollcommand=Scrollbar_y.set)


        tree["columns"]=("slno","Department","Year","Registration Number","Name","Attendance")

        tree.column("slno", width=100, minwidth=100, anchor="center")
        tree.column("Department",width=350, minwidth=350, anchor="center")
        tree.column("Year", width=150, minwidth=150, anchor="center")
        tree.column("Registration Number", minwidth=250, anchor="center")
        tree.column("Name", width=250, minwidth=250, anchor="center")
        tree.column("Attendance", width=250, minwidth=250, anchor="center")

        tree['show']='headings'

        tree.heading("slno", text="Slno")
        tree.heading("Department", text="Department")
        tree.heading("Year", text="Year")
        tree.heading("Registration Number", text="Registration Number")
        tree.heading("Name", text="Student Name")
        tree.heading("Attendance", text="Attendence")

        # Putting data in each rows
        j=1
        for row in rows:
            tree.insert('','end',values=(j,row[0],row[1],row[2],row[3],row[4])) 
            j+=1  

def Current_Attendance_Main(attendance_of):
    global root_current_attendance
    # year = '2nd Year'
    # department = 'Electrical Engineering'
    root_current_attendance=Tk()
    obj = current_attendance(root_current_attendance,attendance_of)
    root_current_attendance.mainloop()
# Current_Attendance_Main("Absent")