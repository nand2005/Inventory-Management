from tkinter import *
from tkinter import ttk, messagebox
from admin_backend import *
from PIL import ImageTk, Image
from employee import billing_area

logs = []
censored_pd = ""  # Define censored_pd initially to avoid reference before assignment error


def login():
    global root
    root = Tk()
    root.geometry("350x600")
    root.config(bg="white")
    root.title("Login")
    root.resizable(0, 0)

    values = ("ADMIN", "EMPLOYEE", "DEVELOPER")

    pic = Image.open(
        'C:/Users/User/Downloads/INVENTORY_MANAGEMENT_SYSTEM-main/INVENTORY_MANAGEMENT_SYSTEM-main/assets/user.png').resize(
        (120, 120))
    icon = ImageTk.PhotoImage(pic)
    role = ttk.Combobox(root, value=values, font=("black", 12))

    Label(root, image=icon, bd=0).place(x=120, y=70)
    Label(root, text="Username", font=("black", 12), bg="white").place(x=10, y=285)
    Label(root, text="Password", font=("black", 12), bg="white").place(x=10, y=325)

    name = Entry(root, width=16, fg="black", bg="white", font=("black", 12))
    password = Entry(root, width=16, fg="black", bg="white", font=("black", 12), show="*")
    btn_login = Button(root, text="Login", fg="black", bg="white", font=("black", 12), bd=2,
                       command=lambda: call(name.get(), password.get(), role.get()))

    role.place(x=130, y=240)
    name.place(x=130, y=285)
    password.place(x=130, y=325)
    btn_login.place(x=270, y=365)

    root.mainloop()


def admin(root):
    global S_Button, E_Button, H_Button, P_Button
    widgetdestroyer(root)
    root.title('Administration')
    root.geometry('750x660')
    root.configure(bg="white")

    oldemp1 = Image.open('C:/Users/User/Downloads/INVENTORY_MANAGEMENT_SYSTEM-main/INVENTORY_MANAGEMENT_SYSTEM-main/assets/emp.png')
    oldemp2 = Image.open('C:/Users/User/Downloads/INVENTORY_MANAGEMENT_SYSTEM-main/INVENTORY_MANAGEMENT_SYSTEM-main/assets/product.png')
    oldemp3 = Image.open('C:/Users/User/Downloads/INVENTORY_MANAGEMENT_SYSTEM-main/INVENTORY_MANAGEMENT_SYSTEM-main/assets/history.png')
    oldemp4 = Image.open('C:/Users/User/Downloads/INVENTORY_MANAGEMENT_SYSTEM-main/INVENTORY_MANAGEMENT_SYSTEM-main/assets/search.jpg')

    newemp1 = oldemp1.resize((120, 120))
    newemp2 = oldemp2.resize((120, 120))
    newemp3 = oldemp3.resize((120, 120))
    newemp4 = oldemp4.resize((120, 120))

    emp_pic = ImageTk.PhotoImage(newemp1)
    product_pic = ImageTk.PhotoImage(newemp2)
    history_pic = ImageTk.PhotoImage(newemp3)
    showcase_pic = ImageTk.PhotoImage(newemp4)

    frame1 = LabelFrame(root, text='Options', font=("black", 13), height=660, width=125, bg="white", fg="black")
    frame2 = LabelFrame(root, bd=3, height=660, width=610, bg="white", fg="black")

    E_Button = Button(frame1, bg="white", fg="black", bd=5, image=emp_pic, command=lambda: emps(frame2))
    H_Button = Button(frame1, bg="white", fg="black", bd=5, image=history_pic, command=lambda: history(frame2))
    P_Button = Button(frame1, bg="white", fg="black", bd=5, image=product_pic, command=lambda: products(frame2))
    S_Button = Button(frame1, bg="white", fg="black", bd=5, image=showcase_pic, command=lambda: customer(frame2))

    S_Button.image = showcase_pic
    E_Button.image = emp_pic
    H_Button.image = history_pic
    P_Button.image = product_pic

    Label(frame1, font=("black", 13), bg="white", fg="black", text='Products').grid(row=3, column=0)
    Label(frame1, font=("black", 13), bg="white", fg="black", text='Employees').grid(row=1, column=0)
    Label(frame1, font=("black", 13), bg="white", fg="black", text='Sales History').grid(row=5, column=0)
    Label(frame1, font=("black", 13), bg="white", fg="black", text='Search Customer').grid(row=7, column=0)

    frame1.place(x=0, y=0)
    frame2.place(x=140, y=10)
    E_Button.grid(row=0, column=0)
    P_Button.grid(row=2, column=0)
    H_Button.grid(row=4, column=0)
    S_Button.grid(row=6, column=0)


def window(root):
    global l3
    widgetdestroyer(root)

    root.title("Database")
    root.geometry("510x250")
    root.config(bg="white")
    root.iconbitmap("C:/Users/User/Downloads/INVENTORY_MANAGEMENT_SYSTEM-main/INVENTORY_MANAGEMENT_SYSTEM-main/assets/database.ico")

    text1 = f"user : {user} "
    text2 = "password : " + censored_pd
    text3 = "database : " + database
    text4 = "query to be executed :"

    l1 = Label(root, text=text1, font=("black", 12), fg="black", bg="white")
    l2 = Label(root, text=text2, font=("black", 12), fg="black", bg="white")
    l3 = Label(root, text=text3, font=("black", 12), fg="black", bg="white")
    l4 = Label(root, text=text4, font=("black", 12), fg="black", bg="white")

    query = Entry(root, width=40, font=("cooper", 16), fg="black", bg="white")

    btn_logs = Button(root, text="Logs", font=("black", 16), fg="black", bg="white", command=show_logs)
    btn_clear = Button(root, text="Clear", font=("black", 16), fg="black", bg="white", command=lambda: clear(query))
    btn_exc = Button(root, text="Execute", font=("black", 16), fg="black", bg="white", command=lambda: execute(query))

    l1.place(x=10, y=10)
    l2.place(x=10, y=30)
    l3.place(x=10, y=50)
    l4.place(x=10, y=100)
    query.place(x=10, y=130)
    btn_exc.place(x=380, y=200)
    btn_logs.place(x=200, y=200)
    btn_clear.place(x=10, y=200)


def clear(text_box):
    text_box.delete(0, END)


def show_logs():
    index = 0
    display_string = ""
    for querry in logs:
        index += 1
        display_string += f"{index}) {querry}\n"
        if index % 5 == 0:
            messagebox.showinfo("logs", display_string)
            display_string = ""
    if len(display_string):
        messagebox.showinfo("logs", display_string)


def execute(query):
    try:
        global logs
        code = query.get().upper()
        logs.append(code)

        if "SELECT" in code or "DESCRIBE" in code or "SHOW" in code:
            cur.execute(code)
            display_string = ""
            limit = 50

            for row in cur.fetchall():
                for elt in row:
                    display_string += str(elt) + ' '
                display_string += '\n'
                limit -= 1
                if limit == 0:
                    messagebox.showinfo("information", display_string)
                    display_string = ""
                    limit = 50

            messagebox.showinfo("information", display_string)

        elif "USE" in code:
            l3.config(text="database : " + code.split()[1].lower())
            cur.execute(code)
            messagebox.showinfo("info", "query executed successfully!")

        else:
            cur.execute(code)
            messagebox.showinfo("info", "query executed successfully!")

    except Exception as error:
        messagebox.showerror("ERROR!", error)


def call(username, password, role):

    if role == "ADMIN":
        if check_admin(username, password):
            admin(root)
        else:
            messagebox.showerror("login error", "invalid username or password")

    elif role == "EMPLOYEE":
        if check_employee(username, password):
            billing_area(root)
        else:
            messagebox.showerror("login error", "invalid username or password")

    elif role == "DEVELOPER":
        if check_admin(username, password):
            window(root)
        else:
            messagebox.showerror("login error", "invalid username or password")

    else:
        messagebox.showerror("Error", "Choose option")


login()
