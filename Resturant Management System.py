import mysql.connector as connector
import math
from tkinter import *

root = Tk()
root.title("DBMS PBL")
#root.configure(bg="Black")
root['background']='#036B76'
root.geometry("1400x900")


#Value Holders
lgvalue = StringVar()
lg2value = StringVar()
menuvalue = StringVar()

#Frames
Label_name = Frame(root, bg="grey", borderwidth=4, relief=RAISED, height=60, width=60,pady=10,background="grey")
#lgf1.pack(pady=5,side=TOP)
Label_name.grid(row=1,column=1,padx=2,pady=2)

#Title
title = Label(Label_name, text="Restaurant Management System", relief=GROOVE,font=('Times', 40))
title.grid()

lgf1 = Frame(root, bg="grey", borderwidth=4, relief=RAISED, height=60, width=60,pady=10)
#lgf1.pack(pady=5,side=TOP)
lgf1.grid(sticky=N)


ls = Label(lgf1, text="Enter Database password", relief=GROOVE)
ls.grid()
lsentry = Entry(lgf1,textvariable=lgvalue,show="*")
lsentry.grid(row=0, column=3)

    
#Function for login1
def login():
    passwd=''
    passwd=lgvalue.get()
    if passwd == 'root':
        lgr=Label(lgf1, text="Logged in Database Successfully")
        lgr.grid()
        global con
        con = connector.connect(host='localhost', port='3306',
                            user='root', password=passwd)
        login2()
        b2=Button(lgf2,text="submit",command=login2,background="blue",fg='White')
        b2.grid(row=3, column=3)
    
    
    else:
        lgw=Label(lgf1, text="Log in into Database Unsuccessfully")
        lgw.grid()

#Function for login2
def login2():
    #System Password
    global lgf2
    lgf2 = Frame(root, bg="grey", borderwidth=4, relief=RAISED, height=100, width=100,pady=10)
#lgf2.pack(pady=5,side=TOP)
    lgf2.grid(row=2,column=2,padx=2,pady=2,sticky=N)
    passwd2=''
    ls2r=Label(lgf2, text="Enter System Security password", relief=GROOVE)
    ls2r.grid(row=0, column=3)
    ls2entry = Entry(lgf2,textvariable=lg2value,show="*")
    ls2entry.grid(row=0, column=5)
        
    passwd2=ls2entry.get()
    if  passwd2=='abc123':
        lg2r=Label(lgf2, text="Logged in System Successfully")
        lg2r.grid(row=2, column=5)
        global c
        c = con.cursor()
        c.execute('show databases')
        dl = c.fetchall()  # Fetched all databases in this variable
        dl2 = []
        for i in dl:
            dl2.append(i[0])

        if 'pbldb' in dl2:
            sql = 'use pbldb'
            c.execute(sql)
        else:
            sql1 = '''create database pbldb'''
            c.execute(sql1)
            sql2 = '''use pbldb'''
            c.execute(sql2)
            sql3 = '''create table Dish(DishName varchar(100),Cost integer,CookName varchar(50))'''
            c.execute(sql3)
            #sql4 = '''create table Orders(DishName varchar(100),Cost integer,Date varchar(100),Customer varchar(50))'''
            sql4 = '''create table Orders(DishName varchar(100),Date varchar(100),Customer varchar(50),Cost integer)'''
            c.execute(sql4)
            sql5 = '''create table Cook(Name varchar(100),Aadhar varchar(14),Dishes varchar(20),Salary integer,DOJ varchar(20))'''
            c.execute(sql5)
            sql6 = '''create table Expenditure(Type varchar(100),Cost integer,Date varchar(20))'''
            c.execute(sql6)
            con.commit()
            print("Done")

        mainmenu()    
    else:
            lg2w=Label(lgf2, text="Logged in System Failure", relief=GROOVE)
            lg2w.grid(row=2, column=5)
            
        
#Options for Menu
def options():

    choice=menuvalue.get()
    while True:
        if choice == '1':
            Dish()
            break
        elif choice == '2':
            Cook()
            break
        elif choice == '3':
            NewOrder()
            break
        elif choice == '4':
            NetIncome()
            break
        elif choice == '5':
            Expenditure()
            break
        elif choice == '6':
            root.destroy()
            break
        
        else:
            print("\n********* Thank You *********** \n")
            break



def mainmenu():
    mmf = Frame(root, bg="grey", borderwidth=4, relief=RAISED, height=200, width=100,pady=10)
    #mmf.pack(pady=5,side=TOP)
    mmf.grid(row=2,column=1,padx=2,pady=2)
    welcome_label= Label(mmf, text="WELCOME TO VIIT CANTEEN", relief=GROOVE)
    dishes_label= Label(mmf, text="1) DISHES",border=5,relief=RIDGE)
    cooks_label = Label(mmf, text="2) COOKS",border=5,relief=RIDGE)
    orders_labels = Label(mmf, text="3) ORDERS",border=5,relief=RIDGE)
    NetIncome_label = Label(mmf, text="4) INCOME",border=5,relief=RIDGE)
    Expenditure_label = Label(mmf, text="5) EXPENDITURE",border=5,relief=RIDGE)
    exit_label = Label(mmf, text="6) EXIT",border=5,relief=RIDGE)
        #Pack text for our form
    welcome_label.grid(row=3, column=2,pady=5)
    dishes_label.grid(row=5, column=2)
    cooks_label.grid(row=7, column=2)
    orders_labels.grid(row=9, column=2)
    NetIncome_label.grid(row=11, column=2)
    Expenditure_label.grid(row=13, column=2)
    exit_label.grid(row=15, column=2)
    ls2 = Label(mmf, text="Select Option",relief= SUNKEN)
    ls2.grid(row=17, column=2,pady=5)
    lsentry2 = Entry(mmf,textvariable=menuvalue)
    lsentry2.grid(row=19, column=2)
    menubutton=Button(mmf,text="submit",command=options,background="blue",fg='White')
    menubutton.grid(row=20, column=2,pady=5)

b1=Button(lgf1,text="submit",command=login,background="blue",fg='White')
b1.grid(row=0, column=5)

def Cname():
    sql = "select Name , Dishes from Cook"
    c= con.cursor()
    c.execute(sql)
    d = c.fetchall()
    Available_Cook_label = Label(dishframe, text=("<---- Available Cooks ---->"),border=5,relief=RIDGE)
    Available_Cook_label.pack()
    print("<---- Available Cooks ---->")
    for i in d:
        Available_Cook_label2 = Label(dishframe, text=(str(i[0]), "---", str(i[1])),border=5,relief=RIDGE)
        Available_Cook_label2.pack()
        print(i[0], "---", i[1])
    return

def Dish():
    global dishframe
    dishframe = Frame(root, bg="grey", borderwidth=4, relief=RAISED, height=150, width=100,pady=10)
    dishframe.grid(row=4,column=1,pady=2,padx=2)
    global dish_input1
    global Dish_Name
    global Dish_Cost
    global Cooked_By
    global dish_input5

    dish_input1 = StringVar()
    Dish_Name = StringVar()
    Dish_Cost = StringVar()
    Cooked_By = StringVar()
    dish_input5 = StringVar()

    Dish_label1 = Label(dishframe, text="Dish :: 1. Add 2. Remove 3. Display :",relief= SUNKEN)
    #Dish_label1.grid(row=2, column=2,pady=5)
    Dish_label1.pack(pady=2)

    Dish_entry1 = Entry(dishframe,textvariable=dish_input1)
    #Dish_entry1.grid(row=4, column=2,pady=5)
    Dish_entry1.pack(pady=2)

    Dish_button=Button(dishframe,text="submit",command=dish_oprations,background="blue",fg='White')
    #Dish_button.grid(row=6, column=1)
    Dish_button.pack(pady=5)

    def clear_text():
            
            dishframe.destroy()

    Dish_reset_button=Button(dishframe,text="Reset",command=clear_text,background="red",fg='White')
    #Dish_reset_button.grid(row=6, column=3)
    Dish_reset_button.pack(pady=5)

def dish_oprations():
    choice = dish_input1.get()
    if choice == '1':

        Dish_Name_label = Label(dishframe, text="Dish Name : ",relief= SUNKEN)
        #Dish_Name_label.grid(row=8, column=2,pady=5)
        Dish_Name_label.pack(pady=2)
        Dish_Name_entry1 = Entry(dishframe,textvariable=Dish_Name)
        #Dish_Name_entry1.grid(row=10, column=2,pady=5)
        Dish_Name_entry1.pack(pady=2)

        Dish_Cost_label = Label(dishframe, text="Dish Cost: ",relief= SUNKEN)
        #Dish_Cost_label.grid(row=12, column=2,pady=5)
        Dish_Cost_label.pack(pady=2)
        Dish_Cost_entry1 = Entry(dishframe,textvariable=Dish_Cost)
        #Dish_Cost_entry1.grid(row=14, column=2,pady=5)
        Dish_Cost_entry1.pack(pady=2)

        Cname()

        Cooked_By_label = Label(dishframe, text="Cooked By: ",relief= SUNKEN)
        Cooked_By_label.pack(pady=2)
        #Cooked_By_label.grid(row=16, column=2,pady=5)
        Cooked_By_entry1 = Entry(dishframe,textvariable=Cooked_By)
        Cooked_By_entry1.pack(pady=2)
        #Cooked_By_entry1.grid(row=18, column=2,pady=5)


        def dish_oprations2():
            
            dn = Dish_Name.get()
            print(dn)
            dc = Dish_Cost.get()
            print(dc)
            
            cb = Cooked_By.get()
            data = (dn, dc, cb)
            sql = 'insert into Dish values(%s,%s,%s)'
            c = con.cursor()
            c.execute(sql, data)
            con.commit()
            Dish_data_label = Label(dishframe, text="Data Entered Successfully",relief= SUNKEN)
            # Dish_data_label.grid(row=22, column=2,pady=5)
            Dish_data_label.pack(pady=2)

            
        
        Dish_button2=Button(dishframe,text="submit",command=dish_oprations2,background="blue",fg='White')
        #Dish_button2.grid(row=20, column=1)
        Dish_button2.pack(pady=2)

    elif choice == '2':

        Dish_Name_label2 = Label(dishframe, text="Dish Name : ",relief= SUNKEN)
        #Dish_Name_label2.grid(row=8, column=2,pady=5)
        Dish_Name_label2.pack(pady=2)
        Dish_Name_entry2 = Entry(dishframe,textvariable=Dish_Name)
        # Dish_Name_entry2.grid(row=10, column=2,pady=5)
        Dish_Name_entry2.pack(pady=2)

        

        def remove_dish():
            dn = Dish_Name.get()
            data = (dn,) 
            sql = 'delete from Dish where DishName = %s' 
            c= con.cursor() 
            c.execute(sql,data) 
            con.commit() 
            Dish_data_label = Label(dishframe, text="Data Deleted Successfully",relief= SUNKEN)
            #Dish_data_label.grid(row=14, column=2,pady=5)
            Dish_data_label.pack(pady=2)
            print("Data Updated Successfully")

        Dish_button3=Button(dishframe,text="submit",command=remove_dish,background="blue",fg='White')
        #Dish_button3.grid(row=12, column=2)
        Dish_button3.pack(pady=2)

    elif choice == '3':
        print("\n") 
        sql = "select * from Dish" 
        c= con.cursor() 
        c.execute(sql) 
        d = c.fetchall() 
        for i in d:
            Dish_Name_label_i = Label(dishframe, text=(str(i[0]), "-", str(i[1]), "-", str(i[2])),relief= SUNKEN)
            #Dish_Name_label_i.grid(row=8, column=2,pady=5)
            Dish_Name_label_i.pack(pady=2)
            print(i[0], " -", i[1], "-", i[2]) 
        print("\n")
        Dish_Name_label = Label(dishframe, text="\n",relief= SUNKEN)
        #Dish_Name_label.grid(row=9, column=2,pady=5) 
        Dish_Name_label.pack(pady=2)
    else:
        mainmenu()   

## Code for COOKS
def Cook():
    global cookframe
    cookframe = Frame(root, bg="grey", borderwidth=4, relief=RAISED, height=150, width=100,pady=10)
    cookframe.grid(row=4,column=1,pady=2,padx=2)
    global Salary
    global Dishes
    global Aadhar
    global cook_name
    global DOJ
    global m_entry

    m_entry=StringVar()
    Salary=StringVar()
    Dishes = StringVar()
    Aadhar = StringVar()
    cook_name = StringVar()
    DOJ= StringVar()

    cook_label1 = Label(cookframe, text="Cook :: 1. Add 2. Remove 3. Display :",relief= SUNKEN)
    cook_label1.grid(row=2, column=2,pady=5)
    cook_entry1 = Entry(cookframe,textvariable=m_entry)
    cook_entry1.grid(row=4, column=2,pady=5)

    Dish_button=Button(cookframe,text="submit",command=cook_operation,background="blue",fg='White')
    Dish_button.grid(row=6, column=1)
    def reset_cook():
            #dishframe.delete(0, END)
            cookframe.destroy()

    Dish_reset_button=Button(cookframe,text="Reset",command=reset_cook,background="red",fg='White')
    Dish_reset_button.grid(row=6, column=3)

def cook_operation():
    choice = m_entry.get()
    if choice == '1':

        cook_name_label = Label(cookframe, text="Cook Name : ",relief= SUNKEN)
        cook_name_label.grid(row=8, column=2,pady=5)
        cook_name_entry1 = Entry(cookframe,textvariable=cook_name)
        cook_name_entry1.grid(row=9, column=2,pady=5)

        Aadhar_label = Label(cookframe, text="Aadhar : ",relief= SUNKEN)
        Aadhar_label.grid(row=10, column=2,pady=5)
        Aadhar_entry1 = Entry(cookframe,textvariable=Aadhar)
        Aadhar_entry1.grid(row=11, column=2,pady=5)

        Dishes_label = Label(cookframe, text="Dishes : ",relief= SUNKEN)
        Dishes_label.grid(row=12, column=2,pady=5)
        Dishes_entry1 = Entry(cookframe,textvariable=Dishes)
        Dishes_entry1.grid(row=13, column=2,pady=5)

        DOJ_label = Label(cookframe, text="DOJ Y/M/D : ",relief= SUNKEN)
        DOJ_label.grid(row=14, column=2,pady=5)
        DOJ_entry1 = Entry(cookframe,textvariable=DOJ)
        DOJ_entry1.grid(row=15, column=2,pady=5)

        salary_label = Label(cookframe, text="Salary: ",relief= SUNKEN)
        salary_label.grid(row=16, column=2,pady=5)
        salary_entry1 = Entry(cookframe,textvariable=Salary)
        salary_entry1.grid(row=17, column=2,pady=5)

        def cook_operation2():
            cn = cook_name.get()
            ca = Aadhar.get()
            d = Dishes.get()
            s = Salary.get()
            doj = DOJ.get()
            data = (cn,ca,d,s,doj)
            sql = 'insert into Cook values(%s,%s,%s,%s,%s)'
            c = con.cursor() 
            c.execute(sql,data) 
            con.commit()
            cook_data_label = Label(cookframe, text="Data Entered Successfully",relief= SUNKEN)
            cook_data_label.grid(row=18, column=2,pady=5)
            print("Data Entered Successfully")

        cook_button2=Button(cookframe,text="submit",command=cook_operation2,background="blue",fg='White')
        cook_button2.grid(row=20, column=1)

        def clear_text1():
            cook_name_entry1.delete(0, END)
            Aadhar_entry1.delete(0, END)
            Dishes_entry1.delete(0, END)
            DOJ_entry1.delete(0, END)
            salary_entry1.delete(0, END)
        
        cook_reset_button=Button(cookframe,text="Reset",command=clear_text1,background="red",fg='White')
        cook_reset_button.grid(row=20, column=3)

    elif choice == '2':
        Cook_Name_label2 = Label(cookframe, text="Cook Name : ",relief= SUNKEN)
        Cook_Name_label2.grid(row=8, column=2,pady=5)
        Cook_Name_entry2 = Entry(cookframe,textvariable=cook_name)
        Cook_Name_entry2.grid(row=10, column=2,pady=5)

        Aadhar_Name_label2 = Label(cookframe, text="Aadhar : ",relief= SUNKEN)
        Aadhar_Name_label2.grid(row=12, column=2,pady=5)
        Aadhar_Name_entry2 = Entry(cookframe,textvariable=Aadhar)
        Aadhar_Name_entry2.grid(row=14, column=2,pady=5)

        def remove_cook():
            cn = cook_name.get()
            ca = Aadhar.get() 
            data = (cn,ca) 
            sql = 'delete from Cook where Name = %s and Aadhar = %s' 
            c=con.cursor() 
            c.execute(sql,data) 
            con.commit() 
            print("Data Updated Successfully")
            ab_label = Label(cookframe, text="Data Removed Successfully",relief= SUNKEN)
            ab_label.grid(row=16, column=2,pady=5)
            print("Data Entered Successfully")

        remove_cook_button3=Button(cookframe,text="submit",command=remove_cook,background="blue",fg='White')
        remove_cook_button3.grid(row=15, column=2)


    elif choice == '3':
        sql = "select * from cook" 
        c= con.cursor() 
        c.execute(sql) 
        d = c.fetchall() 
        for i in d:
            cook_Name_label_i = Label(cookframe, text=(str(i[0]), "-", str(i[1]), "-", str(i[2]),"-",str(i[3]),"-",str(i[4])),relief= SUNKEN)
            cook_Name_label_i.grid(row=8, column=2,pady=5)
            
            #print("\n",i[0], "-" ,i[1], "-" ,i[2], "-" ,i[3], "-" ,i[4],"\n") 
            
    else:
            options()


def NewOrder():
    global neworderframe
    neworderframe = Frame(root, bg="grey", borderwidth=4, relief=RAISED, height=150, width=100,pady=10)
    neworderframe.grid(row=4,column=1,pady=2,padx=2)
    global Date
    global Customer_Name
    global cost2  
    global Dish_Name2

    Date =StringVar()
    Customer_Name =StringVar()
    cost2 = StringVar()
    Dish_Name2= StringVar()

    sql = "select * from Dish"
    c= con.cursor() 
    c.execute(sql) 
    d = c.fetchall() 
    NewOrder_label1 = Label(neworderframe, text="Available Dishes :",relief= SUNKEN)
    #NewOrder_label1.grid(row=2, column=2,pady=5)
    NewOrder_label1.pack()
    NewOrder_label2 = Label(neworderframe, text=" NAME ----- COST ----- COOK ",relief= SUNKEN)
    NewOrder_label2.pack()
    #NewOrder_label2.grid(row=3, column=2,pady=5)
    #print("\n Available Dishes : \n")
    #print("NAME ----- COST ----- COOK ----- ")
    for i in d:
        NewOrder_label_i = Label(neworderframe, text=(str(i[0]), "-", str(i[1]), "-", str(i[2]),"-"),relief= SUNKEN)
        #NewOrder_label_i.grid(row=8, column=2,pady=5)
        NewOrder_label_i.pack()

        print(i[0],"-",i[1],"-",i[2],"-") 
    print("\n") 

    Date_label2 = Label(neworderframe, text="Date : ",relief= SUNKEN)
    #Date_label2.grid(row=11, column=2,pady=5)
    Date_label2.pack(pady=5)
    Date_entry2 = Entry(neworderframe,textvariable=Date)
    #Date_entry2.grid(row=12, column=2,pady=5)
    Date_entry2.pack()

    Customer_Name_label = Label(neworderframe, text="Customer Name : ",relief= SUNKEN)
    Customer_Name_label.pack(pady=5)
    Customer_Name_entry2 = Entry(neworderframe,textvariable=Customer_Name)
    Customer_Name_entry2.pack()

    Dish_Name_label2 = Label(neworderframe, text="Dish Name : ",relief= SUNKEN)
    Dish_Name_label2.pack(pady=5)
    Dish_Name_label2_entry2 = Entry(neworderframe,textvariable=Dish_Name2)
    Dish_Name_label2_entry2.pack()

    cost2_label2 = Label(neworderframe, text="Cost : ",relief= SUNKEN)
    cost2_label2.pack(pady=5)
    cost2_label2_entry2 = Entry(neworderframe,textvariable=cost2)
    cost2_label2_entry2.pack()

    def reset_neworder():
            neworderframe.destroy()
    

    def NewOrder_operations():
        sql = "select DishName, Cost from Dish" 
        c = con.cursor() 
        c.execute(sql) 
        d = c.fetchall() 

        dt = Date.get() 
        cn = Customer_Name.get() 
        lis = Dish_Name2.get()
        cost = cost2.get()
        
        data = (lis,dt,cn,cost) 
        sql = 'insert into Orders values(%s,%s,%s,%s)' 
        c = con.cursor() 
        c.execute(sql,data) 
        con.commit() 
        #print("Total Amount : ",tc, "Rs")
        print("Data Entered Successfully") 
        neworder_data_label = Label(neworderframe, text="Data Entered Successfully",relief= SUNKEN)
        neworder_data_label.pack()
        
    
    NewOrder_button=Button(neworderframe,text="submit",command=NewOrder_operations,background="blue",fg='White')
    NewOrder_button.pack(pady=5)
    neworder_reset_button=Button(neworderframe,text="Reset",command=reset_neworder,background="red",fg='White')
    neworder_reset_button.pack(pady=5)
    

def NetIncome():
    global netincomeframe
    netincomeframe = Frame(root, bg="grey", borderwidth=4, relief=RAISED, height=150, width=100,pady=10)
    netincomeframe.grid(row=4,column=1,pady=2,padx=2)
    def reset_netincome():
            netincomeframe.destroy()

    c= con.cursor() 
    sql = 'select Cost from Orders' 
    c.execute(sql) 
    d = c.fetchall() 
    oi = 0         #order income 
    for i in d:
        oi = oi + i[0] 
    print("Total Income from Orders : ",oi, "Rs") 
    netincome_data_label = Label(netincomeframe, text="Total Income from Orders : Rs", relief= SUNKEN)
    netincome_data_label.pack(pady=5)
    netincome_data_label2 = Label(netincomeframe, text=oi, relief= SUNKEN)
    netincome_data_label2.pack(pady=5)

    netincome_reset_button=Button(netincomeframe,text="Reset",command=reset_netincome,background="red",fg='White')
    netincome_reset_button.pack(pady=5)

def Expenditure():
    global expenditureframe
    expenditureframe = Frame(root, bg="grey", borderwidth=4, relief=RAISED, height=150, width=100,pady=10)
    expenditureframe.grid(row=4,column=1,pady=2,padx=2)
    entry1=StringVar()
    Type= StringVar()
    Cost3= StringVar()
    Date= StringVar()


    Expenditure_label1 = Label(expenditureframe, text="Expenditure:: 1)BILL ENTRY 2)SHOW BILLS",relief= SUNKEN)
    #NewOrder_label1.grid(row=2, column=2,pady=5)
    Expenditure_label1.pack(pady=5)
    Expenditure_entry2 = Entry(expenditureframe,textvariable=entry1)
    Expenditure_entry2.pack(pady=5)


    def reset_exp():
            expenditureframe.destroy()
    
    def expenditure_operation():
        choice = entry1.get()
        if choice == '1':
                Type_label1 = Label(expenditureframe, text="Type: ",relief= SUNKEN)
                #NewOrder_label1.grid(row=2, column=2,pady=5)
                Type_label1.pack(pady=5)
                Type_entry2 = Entry(expenditureframe,textvariable=Type)
                Type_entry2.pack(pady=5)

                Cost_label1 = Label(expenditureframe, text="Cost: ",relief= SUNKEN)
                #NewOrder_label1.grid(row=2, column=2,pady=5)
                Cost_label1.pack(pady=5)
                Cost_entry2 = Entry(expenditureframe,textvariable=Cost3)
                Cost_entry2.pack(pady=5)

                Date_label1 = Label(expenditureframe, text="Date(D/M/Y) : ",relief= SUNKEN)
                #NewOrder_label1.grid(row=2, column=2,pady=5)
                Date_label1.pack(pady=5)
                Date_entry2 = Entry(expenditureframe,textvariable=Date)
                Date_entry2.pack(pady=5)

                def operation():
                    t = Type.get()
                    c = Cost3.get()
                    d = Date.get()
                    data = (t,c,d) 
                    sql = 'insert into Expenditure values(%s,%s,%s)' 
                    c = con.cursor()
                    c.execute(sql,data) 
                    con.commit() 
                    print("Data Entered Successfully")
                    exp_label1 = Label(expenditureframe, text="Data Entered Successfully",relief= SUNKEN)
                    exp_label1.pack(pady=5)
                Expenditureop_button=Button(expenditureframe,text="submit",command=operation,background="blue",fg='White')
                Expenditureop_button.pack(pady=5)

        elif choice == '2':
            c = con.cursor()
            sql = 'select * from Expenditure' 
            c.execute(sql)
            d = c.fetchall() 
            Expenditure_label2 = Label(expenditureframe, text=" TYPE ----- COST ----- DATE ",relief= SUNKEN)
            Expenditure_label2.pack()
            for i in d:
                print(i)
                exp_label2 = Label(expenditureframe, text=i,relief= SUNKEN)
                exp_label2.pack(pady=5)                   
    Expenditure_button=Button(expenditureframe,text="submit",command=expenditure_operation,background="blue",fg='White')
    Expenditure_button.pack(pady=5)
    Expenditure_reset_button=Button(expenditureframe,text="Reset",command=reset_exp,background="red",fg='White')
    Expenditure_reset_button.pack(pady=5)

root.mainloop()

