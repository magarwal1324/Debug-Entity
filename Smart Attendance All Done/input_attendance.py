# import module
from tkinter import *
from tkinter import messagebox
import pymysql

class attendance:
    def __init__(self,root):
        self.root=root
        self.root.title("Accept Attendance")
        self.root.geometry("400x250")
        self.root.resizable(0,0)
        
        # Entry box
        lbl1=Label(self.root,text="Registration No. :",font="Arial 15").place(x=10,y=30)
        self.entry1=Entry(self.root,font="Arial 15")
        self.entry1.place(x=150,y=30,height=30,width=200)

        lbl2=Label(self.root,text="Attandance",font="Arial 15").place(x=10,y=80)
        self.entry2=Entry(self.root,font="Arial 15")
        self.entry2.place(x=150,y=80,height=30,width=200)

        lbl3=Label(self.root,text="Date",font="Arial 15").place(x=10,y=130)
        self.entry3=Entry(self.root,font="Arial 15")
        self.entry3.place(x=150,y=130,height=30,width=200)


        btn=Button(self.root,text="Submit",command=self.accept).place(x=150,y=180)

    # Insert data in database
    def accept(self):
        if self.entry1.get()=="" or self.entry2.get()=="" or self.entry3.get()=="" :
            messagebox.showerror("Error","All fields are required")
        else:
            con=pymysql.connect(host="localhost",user="root",password="",database="stm")
            cur=con.cursor()

            cur.execute(("Insert attendance_details set registration_number=%s , attandance=%s, date=%s"),(self.entry1.get(),self.entry2.get(),self.entry3.get()))

            con.commit()
            con.close()
            messagebox.showinfo("Info","Registered")         

def main():
    root=Tk()
    obj=attendance(root)
    root.mainloop()

main()