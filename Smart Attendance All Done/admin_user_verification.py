# import module
import builtins
from tkinter import *
from tkinter import messagebox
import Login
import Dashboard
btn_state_verification_box=0

def cancel_clicked():
    global btn_state_verification_box
    btn_state_verification_box=0
    vbox_root.destroy()
def on_closing():
    global btn_state_verification_box
    btn_state_verification_box=0
    vbox_root.destroy()

# Admin Verification box
def verification_admin_main(title):
    global vbox_root, admin_user, admin_pwd, page_title, btn_state_verification_box
    page_title = title
    vbox_root=Toplevel()
    vbox_root.title("Verification Box")
    vbox_root.geometry("300x180+600+285")
    vbox_root.resizable(0,0)
    btn_state_verification_box = vbox_root.winfo_exists()
    vbox_root.protocol("WM_DELETE_WINDOW", on_closing)

    capIcon = PhotoImage(file="images/information_icon.png")
    Label(vbox_root,text=" Admin Credintials",font='Arial 12',image=capIcon,compound=LEFT).pack()

    Label(vbox_root,text="Username:",font='Arial 10').place(x=30,y=50)
    admin_user=Entry(vbox_root,font='Arial 10',bg="lightgray")
    admin_user.place(x=110,y=50)
    admin_user.focus()

    Label(vbox_root,text="Password:",font='Arial 10').place(x=30,y=90)
    admin_pwd=Entry(vbox_root,font='Arial 10',bg="lightgray",show="*")
    admin_pwd.place(x=110,y=90)

    if title == "Login":
        btn1=Button(vbox_root,text="Submit",command=Login.admin_verified)
        btn1.place(x=90,y=130)
    if title == "Dashboard":
        btn1=Button(vbox_root,text="Submit",command=Dashboard.admin_verified)
        btn1.place(x=90,y=130)
    

    btn2=Button(vbox_root,text="Cancel" ,command=cancel_clicked)
    btn2.place(x=160,y=130)
    vbox_root.mainloop()
    