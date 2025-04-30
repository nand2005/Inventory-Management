from tkinter import *
from backend import *
from tkinter import ttk
from tkinter import messagebox


fgc, bgc=("white","#182E52")

font_10 = ("cooper",10)
font_11 = ("cooper",11)
font_12 = ("cooper",12)
font_13 = ("cooper",13)
font_14 = ("cooper",14)
font_18 = ("cooper",18)
font_20 = ("cooper",20)
font_25 = ("cooper",25)
font_30 = ("cooper",30)


def widgetdestroyer(frame):
    """destroys all the widgets in the frame"""
    for widget in frame.winfo_children():
        widget.destroy()



def payment(total,transaction_details):
    root=Toplevel()
    root.title("payment")
    root.geometry("300x180")
    root.config(bg=bgc)

    Label(root,fg=fgc,bg=bgc,font=font_20,text=f'Total : {total}').place(x=0,y=10)
    Label(root,fg=fgc,bg=bgc,font=font_14,text=f'amount recieved :').place(x=0,y=80)

    recieved_amt = Entry(root,width=5,fg=fgc,bg=bgc,font=font_14)
    btn_p =  Button(root,text=f'proceed',fg=fgc,bg=bgc,font=font_14,command=lambda:transaction(root,total,recieved_amt.get(),transaction_details))
    btn_p.place(x=210,y=140)
    recieved_amt.place(x=160,y=80)

    root.mainloop()

def transaction(root,total,rec_amt,transaction_details):
    bill_no,date,customer,history,stock = transaction_details

    widgetdestroyer(root)

    updated_table_bills = False
    updated_table_hist  = False
    updated_table_stock = False

    balance_amt = round(eval(f'{rec_amt}-{total}'),2)
    Label(root,fg=fgc,bg=bgc,font=font_12,text=f'Bill No : {bill_no}').place(x=0,y=5)
    Label(root,fg=fgc,bg=bgc,font=font_12,text=f'Date : {date}').place(x=160,y=5)

    if balance_amt>=0:
        updated_table_stock = stock[0](stock[1])
        updated_table_hist  = history[0](*history[1])
        updated_table_bills = customer[0](*customer[1])

        if updated_table_bills is True and updated_table_hist is True and updated_table_stock is True:
            db.commit()

            Label(root,fg=fgc,bg=bgc,font=font_14,text=f'balance : {balance_amt}').place(x=0,y=60)
            Label(root,fg=fgc,bg=bgc,font=font_11,text='transaction saved').place(x=0,y=90)
            Button(root,fg=fgc,bg=bgc,font=font_14,text=f'print bill',command=generate_bill).place(x=210,y=140)

        else:
            widgetdestroyer(root)
            def logs():
                text1 = f'updating table history...\nreturned  {updated_table_hist}\n\n'
                text2 = f'updating table bills...\nreturned  {updated_table_bills}\n\n'
                text3 = f'updating table stock...\nreturned  {updated_table_stock}\n\n'

                return messagebox.showerror("error logs",text1+text2+text3)

            Label(root,fg=fgc,bg=bgc,font=font_14,text='transaction failed!').place(x=70,y=70)
            Button(root,fg=fgc,bg=bgc,font=font_14,text=f'error logs',command=logs).place(x=200,y=140)
    else:
        widgetdestroyer(root)
        Label(root,fg=fgc,bg=bgc,font=font_14,text='transaction failed!').place(x=70,y=60)
        Label(root,fg=fgc,bg=bgc,font=font_11,text='insufficient amount to complete transaction!').place(x=0,y=90)





#CREATING THE WINDOW
def billing_area(root):
    widgetdestroyer(root)
    window_name   = "Billing"
    company_name  = "SuperMarket"

    root.title(window_name)
    root.config(bg = bgc)
    root.geometry(f"1210x810")
    root.iconbitmap("assets/icon_bill.ico")

    #Defining frames
    frame_customer_details = LabelFrame(root,text="Customer Details",
        bg=bgc,fg=fgc,height=120,width=1190,font=font_20,bd=5)
    frame_products = LabelFrame(root,text="Products",
        bg=bgc,fg=fgc,height=400,width=500,font=font_20,bd=5)
    frame_bill = LabelFrame(root,text="Bill",
        bg=bgc,fg=fgc,height=300,width=300,font=font_20,bd=5)
    frame_bill_options = LabelFrame(root,text="Billing Options",
        bg=bgc,fg=fgc,height=200,width=500,font=font_20,bd=5)
    frame_total = LabelFrame(root,text="Total",
        bg=bgc,fg=fgc,height=85,width=688,font=font_20,bd=5)

    #Defining labels
    heading            =   Label(root , text=company_name,fg=fgc,bg=bgc,font=font_30)
    label_total        =   Label(frame_total,text="Total",fg=fgc,bg=bgc,font=font_25)
    label_stock        =   Label(frame_products,fg=fgc,bg=bgc,font=font_10,text="stock:")
    label_product      =   Label(frame_products,fg=fgc,bg=bgc,font=font_20,text="Product:")
    label_catogory     =   Label(frame_products,fg=fgc,bg=bgc,font=font_20,text="Category:")
    label_quantity     =   Label(frame_products,fg=fgc,bg=bgc,font=font_20,text="Quantity:")
    label_product_id   =   Label(frame_products,fg=fgc,bg=bgc,font=font_20,text="Product Id:")
    label_sub_catogory =   Label(frame_products,fg=fgc,bg=bgc,font=font_20,text="Sub Catogory:")
    label_cust_phno    =   Label(frame_customer_details,fg=fgc,bg=bgc,font=font_20,text="Ph_No:")
    label_bill_no      =   Label(frame_customer_details,fg=fgc,bg=bgc,font=font_20,text="Bill No:")
    label_cust_name    =   Label(frame_customer_details,fg=fgc,bg=bgc,font=font_20,text="customer name:")
    label_date         =   Label(frame_customer_details,fg=fgc,bg=bgc,font=font_20,text="Date:")

    #defining entry boxes
    entry_total      = Entry(frame_total,fg=fgc,bg=bgc,font=font_25,bd=0,width=8)
    entry_stock      = Entry(frame_products,fg=fgc,bg=bgc,font=font_10,bd=0,width=3)
    entry_quantity   = Entry(frame_products,fg=fgc,bg=bgc,font=font_20,bd=3,width=18)
    entry_product_id = Entry(frame_products,fg=fgc,bg=bgc,font=font_20,bd=3,width=18)
    entry_bill_no    = Entry(frame_customer_details,fg=fgc,bg=bgc,font=font_20,bd=0,width=5 )
    entry_date       = Entry(frame_customer_details,fg=fgc,bg=bgc,font=font_20,bd=0,width=10 )
    entry_cust_name  = Entry(frame_customer_details,fg=fgc,bg=bgc,font=font_20,bd=2,width=15)
    entry_ph_no      = Entry(frame_customer_details,fg=fgc,bg=bgc,font=font_20,bd=2,width=10)

    #Defining Dropdown Boxes
    combo_products       = ttk.Combobox(frame_products,value=products , font=font_18)
    combo_categories     = ttk.Combobox(frame_products,value=categories,font=font_18)
    combo_sub_categories = ttk.Combobox(frame_products,value=subcategrs,font=font_18)

    #Defining Buttons
    btn_add    = Button(frame_products,fg=fgc,bg=bgc,font=font_20,bd=1,text="Add to Cart",command=add)
    btn_remove = Button(frame_products,fg=fgc,bg=bgc,font=font_20,bd=1,text="Remove From Cart",command=delete)
    btn_total  = Button(frame_bill_options,fg=fgc,bg=bgc,font=font_20,bd=1,text="Total",command=total)
    btn_clear  = Button(frame_bill_options,fg=fgc,bg=bgc,font=font_20,bd=1,text="Clear",command=clear)
    btn_bill   = Button(frame_bill_options,fg=fgc,bg=bgc,font=font_20,bd=1,text="Generate Bill",command=generate_bill)
    btn_exit   = Button(frame_bill_options,fg=fgc,bg=bgc,font=font_20,bd=1,text="       Exit       ",command=root.quit)

    combo_products.bind('<<ComboboxSelected>>', lambda event:refresh_pid(event,combo_products.get()))
    combo_categories.bind('<<ComboboxSelected>>', refresh_subcategories)
    combo_sub_categories.bind('<<ComboboxSelected>>', refresh_products)

    #heading
    heading.place(x=500,y=0)
    #CUSTOMER DETAILS
    label_bill_no.place(x=5,y=25)
    entry_bill_no.place(x=100,y=25)
    label_date.place(x=200,y=25)
    entry_date.place(x=280,y=25)
    entry_ph_no.place(x=1010,y=25)
    label_cust_name.place(x=450,y=25)
    entry_cust_name.place(x=650,y=25)
    label_cust_phno.place(x=910,y=25)
    #PRODUCT DETAILS
    btn_add.place(x=20,y=295)
    label_stock.place(x=5,y=255)
    entry_stock.place(x=50,y=257)
    btn_remove.place(x=220,y=295)
    label_catogory.place(x=5,y=5)
    label_product.place(x=5,y=105)
    label_quantity.place(x=5,y=215)
    combo_products.place(x=200,y=105)
    combo_categories.place(x=200,y=5)
    entry_quantity.place(x=200,y=215)
    label_product_id.place(x=5,y=160)
    label_sub_catogory.place(x=5,y=55)
    entry_product_id.place(x=200,y=160)
    combo_sub_categories.place(x=200,y=55)
    #BILLING OPTIONS
    btn_total.place(x=50,y=20)
    btn_bill.place(x=250,y=20)
    btn_clear.place(x=50,y=100)
    btn_exit.place(x=250,y=100)
    #TOTAL
    label_total.place(x=20,y=0)
    entry_total.place(x=520,y=0)
    #FRAMES
    frame_bill.place(x=510,y=180)
    frame_total.place(x=510,y=710)
    frame_products.place(x=10,y=180)
    frame_bill_options.place(x=10,y=595)
    frame_customer_details.place(x=10,y=50)

    globals().update(locals())

    text_boxes()
    template()
    inventory_check()
    entry_date.insert(END,today)
    entry_bill_no.insert(END,str(generate_billno()))

def text_boxes():
    global text_box1,text_box2,text_box3,text_box4,text_box5

    def yview(*args):
        text_box1.yview(*args)
        text_box2.yview(*args)
        text_box3.yview(*args)
        text_box4.yview(*args)
        text_box5.yview(*args)
            
    scroll_bar = Scrollbar(frame_bill)

    text_box1   = Text(frame_bill,height=21,width=18,bg=bgc,fg=fgc,bd=1,
        yscrollcommand=scroll_bar.set,font=("cooper",15))
    text_box2   = Text(frame_bill,height=21,width=12,bg=bgc,fg=fgc,bd=1,
        yscrollcommand=scroll_bar.set,font=("cooper",15))
    text_box3   = Text(frame_bill,height=21,width=10,bg=bgc,fg=fgc,bd=1,
        yscrollcommand=scroll_bar.set,font=("cooper",15))
    text_box4   = Text(frame_bill,height=21,width=8 ,bg=bgc,fg=fgc,bd=1,
        yscrollcommand=scroll_bar.set,font=("cooper",15))
    text_box5   = Text(frame_bill,height=21,width=10,bg=bgc,fg=fgc,bd=1,
        yscrollcommand=scroll_bar.set,font=("cooper",15))

    text_box1.pack(side=LEFT)
    text_box2.pack(side=LEFT)
    text_box3.pack(side=LEFT)
    text_box4.pack(side=LEFT)
    text_box5.pack(side=LEFT)

    scroll_bar.pack(side=RIGHT,fill="y")
    scroll_bar.config(command=yview)

def template():
    text_box1.delete("1.0",END)
    text_box2.delete("1.0",END)
    text_box3.delete("1.0",END)
    text_box4.delete("1.0",END)
    text_box5.delete("1.0",END)

    text_box1.insert(END,"PRODUCT NAME\n----------------------------\n\n")
    text_box2.insert(END,"PRODUCT ID\n------------------\n\n")
    text_box3.insert(END,"     MRP\n---------------\n\n")
    text_box4.insert(END,"  QTY\n------------\n\n")
    text_box5.insert(END,"TOTAL\n---------------\n\n")

def fill(row):
    contents = row.split()
    temp = ""

    sp1 = " "*7
    sp2 = " "*3
    sp3 = " "*4

    text_box2.insert(END,sp1 + contents[-4] + "\n")
    text_box3.insert(END,sp2 + contents[-3] + "\n")
    text_box4.insert(END,sp3 + contents[-2] + "\n")
    text_box5.insert(END,contents[-1] + "\n")

    for i in range(len(contents)-4):
        temp += contents[i] + " "

    text_box1.insert(END,temp + "\n")

def add():
    try:
        total_price = ''
        stk = entry_stock.get()
        pid = entry_product_id.get()
        qty = entry_quantity.get()

        if pid=='':
            return messagebox.showwarning("error","please select an item to add it into the cart")
        if int(qty)<1:
            return messagebox.showerror("Quantity","invalid value for quantity")
        if (int(stk)-int(qty))<0:
            return messagebox.showerror("stock","unable to add the item to the cart as qty exceeds what is in stock")

        temp = add_item(pid,qty)

        if temp is True:
            template()
            for product in cart_details.keys():
                fill(cart_details[product][0])
                total_price += cart_details[product][2] + "+"
            total_price = eval(total_price[:-1])
            entry_total.delete(0,END)
            entry_total.insert(END,str(total_price))

        else:
            messagebox.showwarning('stock','there is not enough stock as specified')
    except Exception as err:
        print(err)
        messagebox.showerror("Error",'error')

def delete():
    try:
        total_price = ''
        pid = entry_product_id.get()
        if pid in cart_details:
            del cart_details[pid]
        else:
            messagebox.showwarning("warning","the item you are trying to remove doesnt exist")
        template()
        for product in cart_details.keys():
            fill(cart_details[product][0])
            total_price += cart_details[product][2] + "+"
        try:
            entry_total.delete(0,END)
            total_price = eval(total_price[:-1])
            entry_total.insert(END,str(total_price))
        except :
            pass
        entry_total.delete(0,END)
        entry_total.insert(END,str(total_price))

    except Exception as err:
        print(err)
        text_box.delete('1.0',END)
        text_box.insert(END,temp)

def refresh_pid(event,pdt):
    try:
        pid ,stock = pid_value(pdt)
        entry_stock.delete(0,END)
        entry_quantity.delete(0,END)
        entry_product_id.delete(0,END)
        entry_stock.insert(END,stock)
        entry_quantity.insert(END,"1")
        entry_product_id.insert(END,pid)
    except Exception as err:
        print(err)

def refresh_subcategories(event):
    try:
        subcategrs = update_subcategories(combo_categories.get())
        combo_sub_categories.config(value=subcategrs)
        combo_sub_categories.current(0)
        refresh_products(event)
    except Exception as err:
        print(err)

def refresh_products(event):
    try:
        products = update_products(combo_sub_categories.get())
        combo_products.config(value=products)
        combo_products.current(0)
        refresh_pid(event,products[0])
    except Exception as err:
        print(err)

def clear():
    template()
    cart_details.clear()
    entry_ph_no.delete(0,END)
    entry_total.delete(0,END)
    entry_bill_no.delete(0,END)
    entry_cust_name.delete(0,END)
    entry_bill_no.insert(END,str(generate_billno()))

def total():
    try:
        date      = entry_date.get()
        phno      = entry_ph_no.get()
        total     = entry_total.get()
        bill_no   = entry_bill_no.get()
        cust_name = entry_cust_name.get()
        if len(cart_details)==0:
            return messagebox.showwarning("error","there is nothing in the cart")
        if cust_name == '' or phno == '':
            return messagebox.showerror("incomplete fields" , "please fill all the customer fields")
        
        customer_details = [bill_no,cust_name,phno]
        bill_details = [bill_no,date,cart_details]
        transaction_details = [bill_no,date,(save_customer,customer_details),(save_bill,bill_details),(update_stock,cart_details)]

        payment(total,transaction_details)

    except Exception as err:
        messagebox.showwarning("error",f"there appears to be an error,please try again\n\n({err})")

def generate_bill():
    try:
        date = today
        phno = entry_ph_no.get()
        bill_no = entry_bill_no.get()
        cust_name = entry_cust_name.get()
        if cust_name == '' or phno == '':
            return messagebox.showerror("incomplete fields" , "please fill all the customer fields")
        create_bill(bill_no,cust_name,phno,date,bill_contents,cart_details)
    except Exception as err:
        print(err)
        messagebox.showwarning("error" , err)

def inventory_check():
    abt_to_finish,finished = check_stock()
    if len(finished)!=0:
        text = "the following product's stock has expired:\n"
        for product in finished:
            text += product+"\n"
        messagebox.showerror("stock expired",text)
    if len(abt_to_finish)!=0:
        text = "the following product's stock is about to expire:\n"
        for product in abt_to_finish:
            text += product+f" (stock remaining {abt_to_finish[product]})\n"
        messagebox.showerror("stock",text)

