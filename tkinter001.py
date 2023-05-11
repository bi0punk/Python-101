from tkinter import *
import tkinter.messagebox as tsmg

root = Tk()
root.geometry("700x500")
root.title("Welcome To My Page")

def check():
    a = uname.get()
    b = pwd.get()
    c = cpwd.get()
    mix = a + "-" + b + "-" + c
    # Instead of Login.txt you should write your file name.
    with open("Login.txt", "r") as fi:
        d = fi.readlines()
    if b == c:
        if str(mix) in str(d):
            tsmg.showinfo("Welcome",f"Hello {a}, You Have SuccessFully Logged In")
        else:
            tsmg.showerror("Error","No User Found, Please Sign-Up First")
    else:
        tsmg.showerror("Error","Both Password Are Different")
    clear_entries()

def save():
    a = uname.get()
    b = pwd.get()
    c = cpwd.get()
    mix = a + "-" + b + "-" + c
    if a and b and c:
        with open("Login.txt", "r") as fi:
            d = fi.readlines()
        if str(mix) in str(d):
            tsmg.showerror("Error","You Already Have An Account, Please Login")
        elif str(a) in str(d):
            tsmg.showerror("Error","Username Already Exist")
        else:
            if b == c:
                with open("Login.txt", "a") as f:
                    f.write(f"{a}-{b}-{c}\n")
                tsmg.showinfo("Success","Your Account Has Been Created")
                clear_entries()
            else:
                tsmg.showerror("Error","Both Password Are Different")   
                clear_entries()

def clear_entries():
    uname.set("")
    pwd.set("")
    cpwd.set("")

uname = StringVar()
pwd = StringVar()
cpwd = StringVar()

f = Frame(root)
f.pack()
Label(f, text="Login To Continue", font="SegoeUI 18 bold", pady=10).pack()

f = Frame(root)
Label(f, text="Username", font="SegoeUI 14 bold", pady=5).pack()
Entry(f, textvariable=uname, font="SegoeUI 14 bold", borderwidth=5, relief=SUNKEN).pack(padx=5, pady=5)
Label(f, text="Password", font="SegoeUI 14 bold", pady=5).pack()
Entry(f, textvariable=pwd, font="SegoeUI 14 bold", borderwidth=5, relief=SUNKEN).pack(padx=5, pady=5)
Label(f, text="Conform-Password", font="SegoeUI 14 bold", pady=5).pack()
Entry(f, textvariable=cpwd, font="SegoeUI 14 bold", borderwidth=5, relief=SUNKEN).pack(padx=5, pady=5)
f.pack()

f = Frame(root)
Button(f, text="Login", font="SegoeUI 10 bold", command=check).pack(side=LEFT, pady=10, padx=10)
Button(f, text="Sign-Up", font="SegoeUI 10 bold", command=save).pack(side=LEFT, pady=10, padx=10)
f.pack()

f = Frame(root)
Label(f, text="Don't Have An Account Then Sign-Up", font="SegoeUI 14 bold", pady=5).pack()
f.pack()

root.mainloop()
