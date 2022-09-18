# import module
import tkinter as tk
from tkinter import* 
from PIL import ImageTk
from tkinter.ttk import*
import time
import login

# A class with init method    
class start_software:
    # init method or constructor   
    def main():
        global fp_root
        fp_root=Tk()
        fp_root.title("Smart Attendance System")
        fp_root.geometry("1300x750+100+25")
        fp_root.iconbitmap("images_software\\software_icon.ico")
        bg=PhotoImage(file="images_software/log.png")
        bg_image=Label(fp_root,image=bg).place(x=0,y=0,relwidth=1,relheight=1)
        start_software.bar() 
        fp_root.mainloop()

    # Define bar() function is used for loading bar and loading percentage         
    def bar():
        load = Progressbar(fp_root,orient= HORIZONTAL,length=1200,mode='determinate')
        load.place(x=50,y=690)
        for i in range(0,11):
            lbl=tk.Label(fp_root,text=f"Processing........................{10*i}%",font="Arial 13 bold",bg='#20242F',fg="white").place(x=540,y=715)
            load['value']=10*i
            fp_root.update_idletasks() 
            time.sleep(0.3)  
        fp_root.destroy()
        login.login_main()     

start_software.main()
