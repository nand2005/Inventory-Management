import os , random
import mysql.connector
from datetime import datetime


user = "admin"
database = "supermarket"
password = "bav"

db = mysql.connector.connect(
    user = user,
    host = 'localhost',
    database = database,
    password=password
    )

cur = db.cursor()

today = str(datetime.today()).split()[0]

try:
    cur.execute('SELECT MIN(DATE) FROM HISTORY')
    day_of_creation = cur.fetchone()[0]
    if day_of_creation is None:
        day_of_creation = '2020-01-01'
except :
    day_of_creation = '2020-01-01'


categories = ['cosmetics','food and beverages','dairy and poultry','hygiene','stationaries','others']
subcategrs = ['lipstick','face cream','powder','nail polish','hair colors']
products   = ['lakme enrich (brown)','maybelline matte red','swiss beuty pure red','faces e royal maroon','elle 18 glossy pink']

cart_details = {}


bill_contents = ['supermarket',
'call us: 9987674923',
'34/1000 old NH 47, edapally jnc,nethaji nagar,',
'edapally,kochi,kerala,682024,india',
'bill no :','date :','customer name :',
'phno :','product name','product id',
'price','qty','total'
]





#login
def check_admin(username,password):
    cur.execute("SELECT ADMIN_NAME,PASSWORD FROM ADMINS")
    for i,j in cur.fetchall():
        if username.lower()==i.lower() and password.lower()==j.lower():
            return True
    return False

def check_employee(username,password):
    cur.execute("SELECT EMPLOYEE_NAME,PASSWORD FROM EMPLOYEES")
    for i,j in cur.fetchall():
        if username.lower()==i.lower() and password.lower()==j.lower():
            return True
    return False






#products
def add_product(P_ID,P_NAME,CAT_ID,SUB_CAT_ID,STOCK,MRP):
    try:
        cur.execute('INSERT INTO PRODUCTS VALUES(%s,%s,%s,%s,%s,%s)',(P_ID,P_NAME,CAT_ID,SUB_CAT_ID,STOCK,MRP))
        db.commit()
        return True
    except:
        return False

def delete_product(PRODUCT_ID):
    try:
        cur.execute('DELETE FROM PRODUCTS WHERE PRODUCT_ID=%s',(PRODUCT_ID,))
        db.commit()
        return True
    except:
        return False

def search_product(PRODUCT_ID):
    try:
        cur.execute('SELECT * FROM PRODUCTS WHERE PRODUCT_ID=%s',(PRODUCT_ID,))
        return cur.fetchall()[0]
    except:
        pass

def update_product(FIELD,NEW_VALUE,ID):
    try:
        options=("category","sub category","product name","mrp","stock")

        if FIELD==options[0]:
            cur.execute("UPDATE PRODUCTS SET CATEGORY_ID=%s WHERE PRODUCT_ID=%s",(NEW_VALUE,ID))
        elif FIELD==options[1]:
            cur.execute("UPDATE PRODUCTS SET SUB_CATEGORY_ID=%s WHERE PRODUCT_ID=%s",(NEW_VALUE,ID))
        elif FIELD==options[2]:
            cur.execute("UPDATE PRODUCTS SET PRODUCT_NAME=%s WHERE PRODUCT_ID=%s",(NEW_VALUE,ID))
        elif FIELD==options[3]:
            cur.execute("UPDATE PRODUCTS SET MRP=%s WHERE PRODUCT_ID=%s",(NEW_VALUE,ID))
        elif FIELD==options[4]:
            cur.execute("UPDATE PRODUCTS SET STOCK=%s WHERE PRODUCT_ID=%s",(NEW_VALUE,ID))
        else:
            return 'invalid field'
        db.commit()
        return True
    except:
        return False




#employee
def add_employee(EMPLOYEE_ID,EMPLOYEE_NAME,PASSWORD):
    try:
        cur.execute('INSERT INTO EMPLOYEES VALUES(%s,%s,%s)',(EMPLOYEE_ID,EMPLOYEE_NAME,PASSWORD))
        db.commit()
        return True
    except:
        return False

def remove_employee(EMPLOYEE_ID):
    try:
        cur.execute('DELETE FROM EMPLOYEES WHERE EMPLOYEE_ID=%s',(EMPLOYEE_ID,))
        db.commit()
        return True
    except:
        return False

def search_employee(EMPLOYEE_ID):
    try:
        cur.execute('SELECT * FROM EMPLOYEES WHERE EMPLOYEE_ID=%s',(EMPLOYEE_ID,))
        return cur.fetchall()
    except:
        return False

def update_employee(FIELD,NEW_VALUE,ID):
    try:
        options=("id","name","password")

        if FIELD==options[2]:
            cur.execute("UPDATE EMPLOYEES SET PASSWORD=%s WHERE EMPLOYEE_ID=%s",(NEW_VALUE,ID))
        elif FIELD==options[1]:
            cur.execute("UPDATE EMPLOYEES SET EMPLOYEE_NAME=%s WHERE EMPLOYEE_ID=%s",(NEW_VALUE,ID))
        elif FIELD==options[0]:
            cur.execute("UPDATE EMPLOYEES SET EMPLOYEE_ID=%s WHERE EMPLOYEE_ID=%s",(int(NEW_VALUE),ID))
        else:
            return 'invalid field'
        db.commit()
        return True
    except:
        return False





#history
def fetch_by_dates(DATE_1,DATE_2):
    try:
        cur.execute("SELECT BILL_NO,PRODUCT_ID,QUANTITY,DATE FROM HISTORY WHERE DATE BETWEEN %s AND %s ORDER BY DATE",(DATE_1,DATE_2))
        return cur.fetchall()
    except:
        return False

def fetch_by_pid(PRODUCT_ID):
    try:
        cur.execute("SELECT BILL_NO,QUANTITY,DATE FROM HISTORY WHERE PRODUCT_ID=%s ORDER BY DATE",(PRODUCT_ID,))
        return cur.fetchall()
    except:
        return False

def fetch_by_bill(BILL_NO):
    try:
        q1 = "SELECT PRODUCT_NAME,PRODUCTS.PRODUCT_ID,QUANTITY FROM PRODUCTS,HISTORY WHERE PRODUCTS.PRODUCT_ID=HISTORY.PRODUCT_ID"
        cur.execute(q1+" AND BILL_NO=%s ORDER BY DATE",(BILL_NO,))
        return cur.fetchall()
    except:
        return False



#customer
def fetch_by_bill_v2(BILL_NO):
    try:
        cur.execute('SELECT CUSTOMER_NAME,PHONE_NO,DATE FROM CUSTOMER,HISTORY WHERE HISTORY.BILL_NO=CUSTOMER.BILL_NO AND HISTORY.BILL_NO=%s',(BILL_NO,))
        return cur.fetchall()
    except:
        return False


def fetch_by_customer(CUSTOMER_NAME,PHONE_NO):
    try:
        cur.execute('SELECT CUSTOMER.BILL_NO,DATE FROM CUSTOMER,HISTORY WHERE CUSTOMER.BILL_NO=HISTORY.BILL_NO AND CUSTOMER_NAME=%s AND PHONE_NO=%s',(CUSTOMER_NAME,PHONE_NO))
        return cur.fetchall()
    except:
        return False

def fetch_by_dates_v2(date_1,date_2):
    try:
        cur.execute("SELECT CUSTOMER.BILL_NO,CUSTOMER_NAME,PHONE_NO,DATE FROM CUSTOMER,HISTORY WHERE CUSTOMER.BILL_NO=HISTORY.BILL_NO AND DATE BETWEEN %s AND %s ORDER BY DATE",(date_1,date_2,))
        return cur.fetchall()
    except:
        return False











#GLOBAL EMPLOYEE
def generate_billno():
    """returns a unique bill number"""
    try:
        chars   = 'abcdefghijklmnopqrstuvwxyz0123456789'
        bill_no = ''

        cur.execute('SELECT BILL_NO FROM CUSTOMER')

        for _ in range(5):
            index = random.randint(0,35)
            bill_no += chars[index]

        for bills in cur.fetchall():
            if bill_no != bills[0] or bills is not None:
                return bill_no
            elif  bill_no == bills[0]:
                generate_billno()
    except:
        return "69420"
        
def update_subcategories(CATEGORY_NAME):
    cur.execute("SELECT SUB_CATEGORY_NAME FROM SUB_CATEGORIES,CATEGORIES WHERE CATEGORIES.CATEGORY_ID=SUB_CATEGORIES.CATEGORY_ID AND CATEGORY_NAME=%s",(CATEGORY_NAME,))
    return [element[0] for element in cur.fetchall()]
         

def update_products(SUB_CATEGORY_NAME):
    cur.execute("SELECT PRODUCT_NAME FROM PRODUCTS,SUB_CATEGORIES WHERE PRODUCTS.SUB_CATEGORY_ID=SUB_CATEGORIES.SUB_CATEGORY_ID and SUB_CATEGORY_NAME=%s",(SUB_CATEGORY_NAME,))
    return [element[0] for element in cur.fetchall()]

def pid_value(PRODUCT_NAME):
    cur.execute("SELECT PRODUCT_ID,STOCK FROM PRODUCTS WHERE PRODUCT_NAME=%s",(PRODUCT_NAME,))
    return cur.fetchone()

def add_item(pid,qty):
    """adds the item to the cart"""
    if pid in list(cart_details.keys()):
        del cart_details[pid]
    cur.execute("SELECT PRODUCT_NAME,MRP,STOCK FROM PRODUCTS WHERE PRODUCT_ID=%s",(pid,))
    pname , price , stock = cur.fetchall()[0]

    if int(stock)-int(qty)>=0:
        total = price*int(qty)
        price , total = str(price),str(total)
        sp1 = " "* (27-len(pname))
        sp2 = " "* (18-len(pid))
        sp3 = " "* (17-len(price))
        sp4 = " "* (15-len(str(qty)))
        sp5 = " "* 3

        row = f"{pname}{sp1}{pid}{sp2}{price}{sp3}{qty}{sp4}{total}\n"
        cart_details[pid] = row,qty,total
        return True
    return False

def save_customer(billno,cust_name,phno):
    try:
        cur.execute("INSERT INTO CUSTOMER VALUES(%s,%s,%s)",(billno,cust_name,int(phno)))
        return True
    except Exception as err:
        return err

def save_bill(bill_no,date,cart):
    try:
        products = cart.keys()
        for product in products:
            cur.execute("INSERT INTO HISTORY VALUES(%s,%s,%s,%s)",(bill_no,product,cart[product][1],date))
        return True
    except Exception as err:
        return err

def update_stock(cart):
    try:
        for pid in cart.keys():
            cur.execute('SELECT STOCK FROM PRODUCTS WHERE PRODUCT_ID=%s',(pid,))
            initial_stock = int(cur.fetchall()[0][0])
            qty = int(cart[pid][1])
            final_stock = initial_stock-qty
            cur.execute("UPDATE PRODUCTS SET STOCK=%s WHERE PRODUCT_ID=%s",(final_stock,pid))
        return True
    except Exception as err:
        return err

def check_stock():
    cur.execute("SELECT STOCK,PRODUCT_NAME FROM PRODUCTS")
    abt_to_finish = {}
    finished = []
    for stock , product_name in cur.fetchall():
        stock = int(stock)
        if 0 < stock < 10:
            abt_to_finish[product_name]=stock
        if stock == 0:
            finished.append(product_name)
    return abt_to_finish,finished

                              
def create_bill(bill_no,cust_name,phno,date,bill_contents,cart_details):
    '''creates a text file to represent a bill,had to make it unreadable to save space!'''
    try:
        os.mkdir("bills")
    except :
        pass
    
    total = 0
    spacing = " "*6

    b1 = ' '*36+'|'
    b2 = ' '*33+'|'
    b3 = ' '*22+'|'
    b4 = ' '*30+'|'
    b5 = '-'*85

    sp1,sp2,sp3,sp4    =  " "*38," "*33," "*17," "*21
    sp5,sp6,sp7,sp8    =  "="*85," "*60," "*54,"="*85
    sp9,sp10,sp11,sp12 =  " "*6," "*11," "*11," "*13

    f = open(f'bills/{bill_no}.txt','w+')
    f.writelines(['+'+b5+'+\n|'+sp1,bill_contents[0]+b1,'\n|'+sp2,bill_contents[1]+b2,'\n|'+sp3])
    f.writelines([bill_contents[2]+b3,'\n|'+sp4,bill_contents[3]+b4,'\n|'+sp5+'|\n|',bill_contents[4]])
    bill_pos = f.tell()
    f.writelines([sp6,bill_contents[5]])
    date_pos = f.tell()
    f.writelines(['          |'+'\n|',bill_contents[6]])
    name_pos = f.tell()
    f.writelines([sp7,bill_contents[7]])
    no_pos = f.tell()
    f.writelines(['          |\n|'+sp8+'|\n|'+spacing,bill_contents[8],sp9,bill_contents[9]])
    f.writelines([sp10,bill_contents[10],sp11,bill_contents[11],sp12,bill_contents[12]+'   |','\n|'+sp8+'|\n']) #product name

    for pid in cart_details.keys():
        element = str(cart_details[pid][0][:-1])
        border = ' '*( 85-len(element) ) + '|\n'
        f.writelines(['|'+' '*85+'|','\n','|',element+border])
        total += float(cart_details[pid][2])

    total = str(total)
    tspace= ' '*(10-len(total))
    f.writelines(['|'+' '*85+'|\n','+'+b5+'+\n','|Total' + ' '*70 +total+tspace+'|\n','|'+' '*85+'|\n','+'+b5+'+\n'])

    f.seek(bill_pos);f.write(bill_no);f.seek(date_pos);f.write(date)
    f.seek(name_pos);f.write(cust_name);f.seek(no_pos);f.write(phno)

    f.close()
    