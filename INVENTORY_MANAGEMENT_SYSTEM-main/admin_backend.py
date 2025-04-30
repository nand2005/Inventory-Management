from tkinter import *
from backend import *
from tkinter import ttk
from tkinter import messagebox

fgc, bgc=("white","#182E52")

font_10 = ("cooper",10)
font_12 = ("cooper",12)
font_13 = ("cooper",13)
font_14 = ("cooper",14)
font_15 = ("cooper",15)
font_16 = ("cooper",16)
font_18 = ("cooper",18)
font_20 = ("cooper",20)


def widgetdestroyer(frame):
	"""removes all the widgets in the frame"""
	for widget in frame.winfo_children():
		widget.destroy()


#ADD PRODUCT FRAME
def productadd(showcase_frame):
	widgetdestroyer(showcase_frame)
	showcase_frame.config(text="Add Product")

	Label(showcase_frame,font=font_10,bg=bgc,fg=fgc,text='Enter MRP ').grid(row=5,column=0)
	Label(showcase_frame,font=font_10,bg=bgc,fg=fgc,text='Enter Stock').grid(row=4,column=0)
	Label(showcase_frame,font=font_10,bg=bgc,fg=fgc,text='Enter Product ID').grid(row=0,column=0)
	Label(showcase_frame,font=font_10,bg=bgc,fg=fgc,text='Enter Category ID').grid(row=2,column=0)
	Label(showcase_frame,font=font_10,bg=bgc,fg=fgc,text='Enter Sub-Category').grid(row=3,column=0)
	Label(showcase_frame,font=font_10,bg=bgc,fg=fgc,text='Enter Product Name').grid(row=1,column=0)

	IDinput    = Entry(showcase_frame,width=24,font=font_10,justify=CENTER)
	catinput   = Entry(showcase_frame,width=24,font=font_10,justify=CENTER)
	mrpinput   = Entry(showcase_frame,width=24,font=font_10,justify=CENTER)
	nameinput  = Entry(showcase_frame,width=24,font=font_10,justify=CENTER)
	stockinput = Entry(showcase_frame,width=24,font=font_10,justify=CENTER)
	subcatinput= Entry(showcase_frame,width=24,font=font_10,justify=CENTER)

	IDinput.grid(row=0,column=1)
	mrpinput.grid(row=5,column=1)
	catinput.grid(row=2,column=1)
	nameinput.grid(row=1,column=1)
	stockinput.grid(row=4,column=1)	
	subcatinput.grid(row=3,column=1)

	def add():
		try:
			MRP=mrpinput.get()
			name=nameinput.get()
			ID=int(IDinput.get())
			stock=stockinput.get()
			category=catinput.get()
			subcat=subcatinput.get()
								
			if add_product(ID,name,category,subcat,stock,MRP):
				messagebox.showinfo('Added','Product Details Added Successfully !')
			else:
				messagebox.showerror('Error','couldnt add the product')
		except:
			messagebox.showerror('Error','Please Check What You Have Entered !')

	Add_Employee_Button=Button(showcase_frame,text='   Add   ',font=font_10,command=add,bg=bgc,fg=fgc).grid(row=7,column=0)

#SEARCH PRODUCT FRAME
def productsearch(showcase_frame):
	widgetdestroyer(showcase_frame)
	showcase_frame.config(text='Search Product')
		
	Label(showcase_frame,text='Enter Product ID',font=font_10,bg=bgc,fg=fgc).grid(row=0,column=0)
	Product_input=Entry(showcase_frame,width=24,font=font_10,justify=CENTER)
	Product_input.grid(row=0,column=1)

	def search():
		try:
			ID=Product_input.get()
			product_info=search_product(ID)
			try:
				price_info="MRP : "+str(product_info[5])
				stock_info="Stock : "+str(product_info[4])+"\n"
				cat_info  ="Category : "+str(product_info[2])+"\n"
				id_info   ="Product_ID   : "+str(product_info[0])+"\n"
				name_info ="Product_name : "+str(product_info[1])+"\n"
				scat_info ="Sub_Category : "+str(product_info[3])+"\n"
					
				text = id_info+name_info+cat_info+scat_info+stock_info+price_info

				messagebox.showinfo('Search result','Product Details\n\n'+text)
			except:
				messagebox.showerror('Error','No Product with Product_ID  '+str(ID)) 
		except:
			messagebox.showerror('Error','Please Check What You Have Entered !')

	showcase_Product_button=Button(showcase_frame,text='   Search   ',font=font_10,command=search,bg=bgc,fg=fgc).grid(row=1,column=0)

#DELETE PRODUCT FRAME
def productdel(showcase_frame):
	widgetdestroyer(showcase_frame)
	showcase_frame.config(text='Delete Product')

	Label(showcase_frame,text='Enter Product ID',font=font_10,bg=bgc,fg=fgc).grid(row=0,column=0)
	Delete_Product_input=Entry(showcase_frame,width=24,font=font_10,justify=CENTER)
	Delete_Product_input.grid(row=0,column=1)

	def delete():
		try:
			ID = int(Delete_Product_input.get())
			product_info=search_product(ID)
			try:
				price_info="MRP : "+str(product_info[5])
				stock_info="Stock : "+str(product_info[4])+"\n"
				cat_info  ="Category : "+str(product_info[2])+"\n"
				id_info   ="Product_ID   : "+str(product_info[0])+"\n"
				name_info ="Product_name : "+str(product_info[1])+"\n"
				scat_info ="Sub_Category : "+str(product_info[3])+"\n"
					
				text = id_info+name_info+cat_info+scat_info+stock_info+price_info

				if messagebox.askyesno("Confirmation","Do you want to delete this product?\n\n"+text):
					if delete_product(ID):
						messagebox.showinfo('Deleted','Product Details Deleted Successfully !')
			except Exception as err:
				print(err)
				messagebox.showinfo('Try again','No Product with Product_ID '+str(ID))
		except:
			messagebox.showerror('Error','Please Check What You Have Entered !')

	Del_button=Button(showcase_frame,text='   Delete   ',font=font_10,command=delete,bg=bgc,fg=fgc).grid(row=1,column=0)

#UPDATE PRODUCT DETAILS FRAME
def productupdate(showcase_frame):
	widgetdestroyer(showcase_frame)
	showcase_frame.config(text='Update Product')

	options=("category","sub category","product name","mrp","stock")

	Label(showcase_frame,font=font_10,bg=bgc,fg=fgc,text='Enter Product ID').grid(row=1,column=0)
	Label(showcase_frame,font=font_10,bg=bgc,fg=fgc,text='Enter field to update').grid(row=0,column=0)
	Label(showcase_frame,font=font_10,bg=bgc,fg=fgc,text='Enter new value for the field').grid(row=2,column=0)

	ID_input=Entry(showcase_frame,width=28,font=font_10,justify=CENTER)
	Field_input=ttk.Combobox(showcase_frame,value=options,font=("black",12),justify=CENTER)
	New_Value_input=Entry(showcase_frame,width=28,font=font_10,justify=CENTER)

	ID_input.grid(row=1,column=1)
	Field_input.grid(row=0,column=1)
	New_Value_input.grid(row=2,column=1)

	def update():
		try:
			field = Field_input.get()
			value = New_Value_input.get()
			Id    = int(ID_input.get())
			if update_product(field,value,Id):
				messagebox.showinfo('Updated','Product Details Updated Successfully !')
		except:
			messagebox.showerror('Error','Please Check What You Have Entered !')

	Update_Button=Button(showcase_frame,text='   Update   ',font=font_10,command=update,bg=bgc,fg=fgc).grid(row=3,column=0)

#PRODUCTS
def products(root):
	widgetdestroyer(root)	
	showcase_frame=LabelFrame(root,bd=3,width=600,bg=bgc,fg=fgc,font=font_12)

	Add_Button   =Button(root,font=font_13,bg=bgc,fg=fgc,height=2,width=13,text='Add Product',command=lambda:productadd(showcase_frame)).place(x=300,y=6)
	Delete_Button=Button(root,font=font_13,bg=bgc,fg=fgc,width=13,height=2,text='Delete Product',command=lambda:productdel(showcase_frame)).place(x=155,y=6)
	Search_Button=Button(root,font=font_13,bg=bgc,fg=fgc,width=13,height=2,text='Search Product',command=lambda:productsearch(showcase_frame)).place(x=10,y=6)
	Change_Details_Button=Button(root,font=font_13,width=13,bg=bgc,fg=fgc,height=2,text='Change details',command=lambda:productupdate(showcase_frame)).place(x=445,y=6)

	showcase_frame.place(x=10,y=100)





#ADD EMPLOYEE FRAME
def empadd(showcase_frame):
	widgetdestroyer(showcase_frame)
	showcase_frame.config(text='Add Employee')
		
	Label(showcase_frame,font=font_10,bg=bgc,fg=fgc,text='Enter Employee ID').grid(row=0,column=0)
	Label(showcase_frame,font=font_10,bg=bgc,fg=fgc,text='Enter Employee Name').grid(row=1,column=0)
	Label(showcase_frame,font=font_10,bg=bgc,fg=fgc,text='Enter Employees Password ').grid(row=2,column=0)

	IDinput=Entry(showcase_frame,width=24,font=font_10,justify=CENTER)
	passinput=Entry(showcase_frame,width=24,font=font_10,justify=CENTER)
	nameinput=Entry(showcase_frame,width=24,font=font_10,justify=CENTER)

	IDinput.grid(row=0,column=1)
	nameinput.grid(row=1,column=1)
	passinput.grid(row=2,column=1)

	def add():
		try:
			ID=int(IDinput.get())
			name=nameinput.get()
			password=passinput.get()
			if add_employee(ID,name,password):
				messagebox.showinfo('Added','Employee Details Added Successfully !')
			else:
				messagebox.showerror("error","could'nt add the employee")
		except:
			messagebox.showerror('Error','Please Check What You Have Entered !')

	Add_Employee_Button=Button(showcase_frame,text='   Add   ',font=font_10,command=add,bg=bgc,fg=fgc).grid(row=3,column=0)

#SEARCH EMPLOYEE FRAME
def searchemp(showcase_frame):
	widgetdestroyer(showcase_frame)
	showcase_frame.config(text='Search Employee')
		
	Label(showcase_frame,text='Enter Employee ID',font=font_10,bg=bgc,fg=fgc).grid(row=0,column=0)
	Emp_input=Entry(showcase_frame,width=24,font=font_10,justify=CENTER)
	Emp_input.grid(row=0,column=1)

	def search():
		try:
			ID=Emp_input.get()
			emplist=search_employee(ID)
			try:
				text='E_ID     : '+str(emplist[0][0])+'\nE_name   : '+emplist[0][1]+'\nPassword : '+emplist[0][2]
				messagebox.showinfo('Search result','Employee Details\n\n'+text)
			except :
				messagebox.showerror('Error','No Such Employee !')
		except:
			messagebox.showerror('Error','Please Check What You Have Entered !')

	showcase_emp_button=Button(showcase_frame,text='   Search   ',font=font_10,command=search,bg=bgc,fg=fgc).grid(row=1,column=0)

#DELETE EMPLOYEE FRAME
def empdel(showcase_frame):
	widgetdestroyer(showcase_frame)
	showcase_frame.config(text='Delete Employee')

	Label(showcase_frame,text='Enter Employee ID',font=font_10,bg=bgc,fg=fgc).grid(row=0,column=0)
	Delete_Emp_input=Entry(showcase_frame,width=24,font=font_10,justify=CENTER)
	Delete_Emp_input.grid(row=0,column=1)

	def delete():
		try:
			ID = int(Delete_Emp_input.get())
			info=search_employee(ID)
			try:
				text='E_ID     : '+str(info[0][0])+'\nE_name   : '+info[0][1]+'\nPassword : '+info[0][2]
				if messagebox.askyesno("Confirmation","Do you want to delete this employee?\n\n"+text):
					if remove_employee(ID):
						messagebox.showinfo('Deleted','Employee Details Deleted Successfully !')
			except:
				messagebox.showinfo('Deleted','No Employee with E_ID '+str(ID))
		except:
			messagebox.showerror('Error','Please Check What You Have Entered !')

	Del_button=Button(showcase_frame,text='   Delete   ',font=font_10,command=delete,bg=bgc,fg=fgc).grid(row=1,column=0)

#UPDATE EMPLOYEE DETAILS FRAME
def empupdate(showcase_frame):
	widgetdestroyer(showcase_frame)		
	showcase_frame.config(text='Update Employee')

	options=("id","name","password")

	Label(showcase_frame,font=font_10,bg=bgc,fg=fgc,text='Enter Employee ID').grid(row=1,column=0)
	Label(showcase_frame,font=font_10,bg=bgc,fg=fgc,text='Enter filed to update').grid(row=0,column=0)
	Label(showcase_frame,font=font_10,bg=bgc,fg=fgc,text='Enter new value for the field').grid(row=2,column=0)

	ID_input=Entry(showcase_frame,width=28,font=font_10,justify=CENTER)
	Field_input=ttk.Combobox(showcase_frame,value=options,font=("black",12),justify=CENTER)
	New_Value_input=Entry(showcase_frame,width=28,font=font_10,justify=CENTER)

	ID_input.grid(row=1,column=1)
	Field_input.grid(row=0,column=1)
	New_Value_input.grid(row=2,column=1)

	def update():
		try:
			field = Field_input.get()
			value = New_Value_input.get()
			Id    = int(ID_input.get())
			if messagebox.askyesno('Confirmation','Are you sure you want to update the values ?'):
				update_employee(field,value,Id)
				messagebox.showinfo('Updated','Employee Details Updated Successfully !')
		except:
			messagebox.showerror('Error','Please Check What You Have Entered !')

	Update_Button=Button(showcase_frame,text='   Update   ',font=font_10,command=update,bg=bgc,fg=fgc).grid(row=3,column=0)

#EMPLOYEE
def emps(root):
	widgetdestroyer(root)
	showcase_frame=LabelFrame(root,bd=3,width=600,bg=bgc,fg=fgc,font=font_12)

	Search_Button = Button(root,font=font_13,bg=bgc,fg=fgc,height=2,text='Search Employee',command=lambda:searchemp(showcase_frame)).place(x=10,y=6)
	Delete_Button = Button(root,font=font_13,bg=bgc,fg=fgc,height=2,text='Delete Employee',command=lambda:empdel(showcase_frame)).place(x=160,y=6)	
	Add_Button    = Button(root,font=font_13,bg=bgc,fg=fgc,height=2,text='Add Employee',command=lambda:empadd(showcase_frame)).place(x=305,y=6)
	Change_Details_Button=Button(root,font=font_13,bg=bgc,fg=fgc,height=2,text='Change details',command=lambda:empupdate(showcase_frame)).place(x=433,y=6)

	showcase_frame.place(x=10,y=100)






def textboxes(frame,no):
	"""creates text boxes to display results in a formatted way"""
	widgetdestroyer(frame)
	w1,w2,w3,w4=no

	def yview(*args):
		text_box1.yview(*args)
		text_box2.yview(*args)
		text_box3.yview(*args)
		text_box4.yview(*args)

	scroll_bar = Scrollbar(frame)
	text_box1  = Text(frame,height=21,width=w1,bg=bgc,fg=fgc,bd=1,
		yscrollcommand=scroll_bar.set,font=font_15)
	text_box2  = Text(frame,height=21,width=w2,bg=bgc,fg=fgc,bd=1,
		yscrollcommand=scroll_bar.set,font=font_15)
	text_box3  = Text(frame,height=21,width=w3,bg=bgc,fg=fgc,bd=1,
		yscrollcommand=scroll_bar.set,font=font_15)
	text_box4  = Text(frame,height=21,width=w4,bg=bgc,fg=fgc,bd=1,
		yscrollcommand=scroll_bar.set,font=font_15)

	text_box1.pack(side=LEFT)
	text_box2.pack(side=LEFT)
	text_box3.pack(side=LEFT)
	text_box4.pack(side=LEFT)

	scroll_bar.pack(side=RIGHT,fill="y")
	scroll_bar.config(command=yview)

	return text_box1,text_box2,text_box3,text_box4



def display_for_datespan(frame,date1,date2):
	widgetdestroyer(frame)
	textbox1,textbox2,textbox3,textbox4=textboxes(frame,(12,12,12,12))
	sep = "\n"+"="*11+"\n"
	data  = fetch_by_dates(date1,date2)

	textbox1.insert(END," "*2 +"bill number" + sep)
	textbox2.insert(END," "*3 +"product id" + sep)
	textbox3.insert(END," "*5 +"quantity" + sep)
	textbox4.insert(END," "*7 +"date" + sep)

	for row in data:
		bill_no,pid,qty,date = row

		textbox1.insert(END," "*5 + bill_no  +"\n")
		textbox2.insert(END," "*7 + str(pid) +"\n")
		textbox3.insert(END," "*9 + str(qty) +"\n")
		textbox4.insert(END," "*2 + str(date)+"\n")

def display_for_billnumber(frame,bill_no):
	widgetdestroyer(frame)
	textbox1,textbox2,textbox3,textbox4=textboxes(frame,(22,12,12,0))
	sep1 = "\n"+"="*20+"\n"
	sep2 = "\n"+"="*11+"\n"
	data = fetch_by_bill(bill_no)

	textbox1.insert(END," "*8 + "product name"+ sep1)
	textbox2.insert(END," "*3 + "product id"+ sep2)
	textbox3.insert(END," "*5 + "quantity"+ sep2)

	for row in data:
		pname,pid,qty = row
		pid = str(pid)
		qty = str(qty)

		textbox1.insert(END," "*5 + pname+"\n")
		textbox2.insert(END," "*7 + pid+"\n")
		textbox3.insert(END," "*9 + qty+"\n")

def display_for_products(frame,pid):
	textbox1,textbox2,textbox3,textbox4=textboxes(frame,(16,16,16,0))
	sep = "\n"+"="*14+"\n"
	data = fetch_by_pid(pid)

	textbox1.insert(END," "*6 + "bill number" + sep)
	textbox2.insert(END," "*7 + "quantity" + sep)
	textbox3.insert(END," "*10 + "date" + sep)

	for row in data:
		bill_no,qty,date = row

		textbox1.insert(END," "*9 + bill_no+"\n")
		textbox2.insert(END," "*11 + str(qty)+"\n")
		textbox3.insert(END," "*6 + str(date)+"\n")


def display_for_date(frame,date1,date2):
	widgetdestroyer(frame)
	records  = fetch_by_dates_v2(date1,date2)
	textbox1,textbox2,textbox3,textbox4=textboxes(frame,(7,17,12,12))

	sep1 = "\n"+"="*6+"\n"
	sep2 = "\n"+"="*15+"\n"
	sep3 = "\n"+"="*11+"\n"
	sep4 = "\n"+"="*9+"\n"

	textbox1.insert(END," "*2 +"Bill no" + sep1)
	textbox2.insert(END," "*0 +"Customer Name" + sep2)
	textbox3.insert(END," "*0 +"Phone Number" + sep3)
	textbox4.insert(END," "*5 +"Date" +sep4)

	for row in records:
		bill_no,customer_name,phone_no,date = row

		textbox1.insert(END,bill_no+"\n")
		textbox2.insert(END,customer_name+"\n")
		textbox3.insert(END,str(phone_no)+"\n")
		textbox4.insert(END,str(date)+"\n")

def display_for_customer(frame,customer_name,phone_no):
	widgetdestroyer(frame)
	records=fetch_by_customer(customer_name,phone_no)
	textbox1,textbox2,textbox3,textbox4=textboxes(frame,(16,16,16,0))
	l=0
	sep= "\n"+"="*14+"\n"
	sep1= "\n"+"="*14+"\n"

	textbox1.insert(END," "*9+"Index" + sep1)
	textbox2.insert(END," "*10+"Bill no" + sep)
	textbox3.insert(END," "*10 +"Date" + sep)

	for row in records:
		l+=1
		bill_no,date = row
		textbox1.insert(END," "*10 + str(l)+"\n")
		textbox2.insert(END," "*9  + bill_no+"\n")
		textbox3.insert(END," "*5  + str(date)+"\n")

def display_for_billno(frame,bill_no):
	widgetdestroyer(frame)
	textbox1,textbox2,textbox3,textbox4=textboxes(frame,(16,16,16,0))
	sep = "\n"+"="*14+"\n"

	textbox1.insert(END," "*2 + "Customer Name" + sep)
	textbox2.insert(END," "*4 + "Phone Number" + sep)
	textbox3.insert(END," "*9 + "Date" + sep)

	for row in fetch_by_bill_v2(bill_no):
		customer_name,phone_no,date = row

		textbox1.insert(END,customer_name+"\n")
		textbox2.insert(END," "*4 + str(phone_no)+"\n")
		textbox3.insert(END," "*6 + str(date)+"\n")



def bill_no(frame):
    widgetdestroyer(frame)
   
    text="*Enter bill number to search and display\ninformation of the transaction"

    Label(frame,fg=fgc,bg=bgc,font=font_14,text=text).place(x=0,y=0)
    Label(frame,fg=fgc,bg=bgc,font=font_14,text="Bill number :").place(x=0,y=160)

    bill_no=Entry(frame,width=10,fg=fgc,bg=bgc,font=font_16,bd=1)
    
    btn_search=Button(frame,text="search",fg=fgc,bg=bgc,font=font_16,bd=1,command=lambda:display_for_billnumber(frame,bill_no.get()))
    btn_search.place(x=10,y=300)
    bill_no.place(x=120,y=160)

def datespan_func(frame):
    widgetdestroyer(frame)
    text="*Enter date interval to get information\nof transactions made during that time"
    date = str(datetime.today()).split()[0]

    Label(frame,fg=fgc,bg=bgc,font=font_14,text=text).place(x=0,y=0)
    Label(frame,fg=fgc,bg=bgc,font=font_14,text="From:").place(x=0,y=160)
    Label(frame,fg=fgc,bg=bgc,font=font_14,text="To:").place(x=260,y=160)

    date_from = Entry(frame,width=10,fg=fgc,bg=bgc,font=font_14,bd=1)
    date_to   = Entry(frame,width=10,fg=fgc,bg=bgc,font=font_14,bd=1)
    date_from.insert(END,day_of_creation)
    date_to.insert(END,date)

    btn_search=Button(frame,text="search",fg=fgc,bg=bgc,font=font_16,bd=1,command=lambda:display_for_datespan(frame,date_from.get(),date_to.get()))

    date_from.place(x=60,y=160)
    date_to.place(x=300,y=160)
    btn_search.place(x=10,y=300)

def product_func(frame):
    widgetdestroyer(frame)
    text="*Enter Product ID of the required product\nto get information of its sales"

    Label(frame,fg=fgc,bg=bgc,font=font_14,text=text).place(x=0,y=0)
    Label(frame,fg=fgc,bg=bgc,font=font_14,text="Product Id:").place(x=0,y=160)

    product=Entry(frame,width=10,fg=fgc,bg=bgc,font=font_14,bd=1)
    product.place(x=100,y=160)

    btn_search=Button(frame,text="search",fg=fgc,bg=bgc,font=font_16,bd=1,command=lambda:display_for_products(frame,product.get()))
    btn_search.place(x=10,y=300)

def clear_history():
	proceed = messagebox.askyesno('confirmation','are you sure you want to clear transaction history?!')
	if proceed:
		cur.execute("DELETE FROM HISTORY")
		db.commit()
		messagebox.showinfo('info','all transaction history was cleared')

def clear_customer():
	proceed = messagebox.askyesno('confirmation','are you sure you want to clear customer history?!')
	if proceed:
		cur.execute("DELETE FROM CUSTOMER")
		db.commit()
		messagebox.showinfo('info','all transaction history was cleared')


def date_func(frame):
	widgetdestroyer(frame)
	text="*Enter date interval to get information of customer's\nwho purchased during that time"
	date = str(datetime.today()).split()[0]

	Label(frame,fg=fgc,bg=bgc,font=font_14,text=text).place(x=0,y=0)
	Label(frame,fg=fgc,bg=bgc,font=font_14,text="From:").place(x=0,y=200)
	Label(frame,fg=fgc,bg=bgc,font=font_14,text="To:").place(x=260,y=200)

	date_from = Entry(frame,width=10,fg=fgc,bg=bgc,font=font_14,bd=1)
	date_to   = Entry(frame,width=10,fg=fgc,bg=bgc,font=font_14,bd=1)
	date_from.insert(END,day_of_creation)
	date_to.insert(END,date)

	btn_search = Button(frame,text="search",fg=fgc,bg=bgc,font=font_16,bd=1,command=lambda:display_for_date(frame,date_from.get(),date_to.get()))

	date_from.place(x=60,y=200)
	date_to.place(x=300,y=200)
	btn_search.place(x=10,y=300)

def search_customer(frame):
	widgetdestroyer(frame)
	text="*Enter the customer name and phone number to\nsearch and display information of the customer"

	Label(frame,fg=fgc,bg=bgc,font=font_14,text=text).place(x=0,y=0)	
	Label(frame,fg=fgc,bg=bgc,font=font_14,text='Customer Name:').place(x=0,y=200)
	Label(frame,fg=fgc,bg=bgc,font=font_14,text='Phone Number:').place(x=0,y=250)

	cust_input   = Entry (frame,fg=fgc,bg=bgc,font=font_14,bd=1,width=10)
	custph_input = Entry (frame,fg=fgc,bg=bgc,font=font_14,bd=1,width=10)
	btn_search   = Button(frame,fg=fgc,bg=bgc,font=font_16,bd=1,text="search",command=lambda:display_for_customer(frame,cust_input.get(),custph_input.get()))

	cust_input.place(x=150,y=200)
	custph_input.place(x=150,y=250)
	btn_search.place(x=10,y=300)

def search_bill(frame):
	widgetdestroyer(frame)
	text="*Enter bill number to search and display\nthe information of the customer"

	Label(frame,fg=fgc,bg=bgc,font=font_14,text=text).place(x=0,y=0)
	Label(frame,fg=fgc,bg=bgc,font=font_14,text='Bill Number:').place(x=0,y=200)
	
	bill_input=Entry (frame,fg=fgc,bg=bgc,font=font_14,bd=1,width=10)
	btn_search=Button(frame,fg=fgc,bg=bgc,font=font_16,bd=1,text="search",command=lambda:display_for_billno(frame,bill_input.get()))

	bill_input.place(x=120,y=200)
	btn_search.place(x=10,y=300)


def customer(root):
	widgetdestroyer(root)
	showcase_frame = LabelFrame(root,bg=bgc,height=500,width=550,bd=3)
	showcase_frame.place(x=20,y=120)

	btn_r = Button(root,fg=fgc,bg=bgc,font=font_20,bd=1,text="clear",command=clear_customer)
	btn_s = Button(root,fg=fgc,bg=bgc,font=font_20,bd=1,text="date",command=lambda:date_func(showcase_frame))
	btn_c = Button(root,fg=fgc,bg=bgc,font=font_20,bd=1,text="customer",command=lambda:search_customer(showcase_frame))
	btn_b = Button(root,fg=fgc,bg=bgc,font=font_20,bd=1,text='Bill no',command=lambda:search_bill(showcase_frame))

	btn_r.place(x=470,y=20)
	btn_s.place(x=20,y=20)
	btn_c.place(x=140,y=20)
	btn_b.place(x=320,y=20)

def history(root):
    widgetdestroyer(root)
    showcase_frame = LabelFrame(root,bg=bgc,height=500,width=550,bd=3)
    showcase_frame.place(x=20,y=120)

    btn_h = Button(root,fg=fgc,bg=bgc,font=font_20,bd=1,text="clear",command=clear_history)
    btn_p = Button(root,fg=fgc,bg=bgc,font=font_20,bd=1,text="product",command=lambda:product_func(showcase_frame))
    btn_b = Button(root,fg=fgc,bg=bgc,font=font_20,bd=1,text="bill number",command=lambda:bill_no(showcase_frame))
    btn_d = Button(root,fg=fgc,bg=bgc,font=font_20,bd=1,text="date span",command=lambda:datespan_func(showcase_frame))

    btn_d.place(x=20,y=20)
    btn_b.place(x=175,y=20)
    btn_p.place(x=345,y=20)
    btn_h.place(x=470,y=20)