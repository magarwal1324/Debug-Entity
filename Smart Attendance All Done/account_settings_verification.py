# import module
from tkinter import *
from tkinter import messagebox
import set_user_credentials
import account_settings
btn_state_account_verification_box=0

# Function for cancle verification
def cancel_clicked():
    global btn_state_account_verification_box
    btn_state_account_verification_box=0
    vbox_root.destroy()

# Define verify_user function used getting user input email and password 
def verifiy_user():
    global verify_status
    name=user.get()
    pswd=pwd.get()

    if name == "" or pswd =="":
        messagebox.showwarning("Warning","All feilds are required",parent= vbox_root)
    elif set_user_credentials.set_username==name and set_user_credentials.set_password==pswd: 
        cancel_clicked()
        back_page_root.destroy()
        account_settings.Account_Settings_Main()
    else:
        messagebox.showerror("Error","Wrong input",parent=vbox_root)

def on_closing():
    global btn_state_account_verification_box
    btn_state_account_verification_box=0
    vbox_root.destroy()

# creating verification box
def account_settings_verification_main(rt):
    global vbox_root, user, pwd, back_page_root,btn_state_account_verification_box
    back_page_root = rt
    vbox_root=Toplevel()
    vbox_root.title("Verification Box")
    vbox_root.geometry("300x180+700+285")
    vbox_root.resizable(0,0)
    btn_state_account_verification_box = vbox_root.winfo_exists()
    vbox_root.protocol("WM_DELETE_WINDOW", on_closing)

    capIcon = PhotoImage(file="images/information_icon.png")
    Label(vbox_root,text=" User Credintials",font='Arial 12',image=capIcon,compound=LEFT).pack()

    Label(vbox_root,text="Email:",font='Arial 10').place(x=30,y=50)
    user=Entry(vbox_root,font='Arial 10',bg="lightgray",width=25)
    user.place(x=100,y=50)
    user.focus()

    Label(vbox_root,text="Password:",font='Arial 10').place(x=30,y=90)
    pwd=Entry(vbox_root,font='Arial 10',bg="lightgray",show="*",width=25)
    pwd.place(x=100,y=90)

    btn1=Button(vbox_root,text="Submit",command=verifiy_user)
    btn1.place(x=95,y=130)  

    btn2=Button(vbox_root,text="Cancel" ,command=cancel_clicked)
    btn2.place(x=165,y=130)
    vbox_root.mainloop()
    
# verification_admin_main()
