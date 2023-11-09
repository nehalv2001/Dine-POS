from tkinter import *
from tkinter import messagebox
import mysql.connector
import random
import tkinter  as tk
import time

top=Tk()
top.geometry("1270x690+0+0")
top.resizable(0,0)
top.configure(bg="cadetblue")
top.title("Dine POS")


#=======================================================================================

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()
var17=IntVar()
var18=IntVar()
var19=IntVar()
var20=IntVar()
var21=IntVar()
var22=IntVar()
var23=IntVar()
var24=IntVar()
var25=IntVar()

e_guj=StringVar()
e_pun=StringVar()
e_noo=StringVar()
e_man=StringVar()
e_soup=StringVar()
e_pav=StringVar()
e_bb=StringVar()
e_pizza=StringVar()
e_sw=StringVar()
e_burger=StringVar()
e_gsw=StringVar()
e_biryani=StringVar()
e_jira=StringVar()
e_sada=StringVar()
e_masala=StringVar()
e_mysore=StringVar()
e_chaas=StringVar()
e_pepsi=StringVar()
e_coke=StringVar()
e_sprite=StringVar()
e_sosyo=StringVar()
e_juice=StringVar()
e_mazza=StringVar()
e_shake=StringVar()

ServiceCharge=StringVar()
CostOfDrinks=StringVar()
CostOfDishes=StringVar()
Subtotal=StringVar()
Total=StringVar()
BillNumber=IntVar()

e_guj.set('0')
e_pun.set('0')
e_noo.set('0')
e_man.set('0')
e_soup.set('0')
e_pav.set('0')
e_bb.set('0')
e_pizza.set('0')
e_sw.set('0')
e_burger.set('0')
e_gsw.set('0')
e_biryani.set('0')
e_jira.set('0')
e_sada.set('0')
e_masala.set('0')
e_mysore.set('0')
e_chaas.set('0')
e_pepsi.set('0')
e_coke.set('0')
e_sprite.set('0')
e_sosyo.set('0')
e_juice.set('0')
e_mazza.set('0')
e_shake.set('0')
BillNumber.set('')


def guj():
    if var1.get()==1:
        e101.config(state=NORMAL)
        e101.delete(0,END)
        e101.focus()
    else:
        e101.config(state=DISABLED)
        e_guj.set('0')

def pun():
    if var2.get()==1:
        e102.config(state=NORMAL)
        e102.delete(0,END)
        e102.focus()
    else:
        e102.config(state=DISABLED)
        e_pun.set('0')

def noo():
    if var3.get()==1:
        e103.config(state=NORMAL)
        e103.delete(0,END)
        e103.focus()
    else:
        e103.config(state=DISABLED)
        e_noo.set('0')

def man():
    if var4.get()==1:
        e104.config(state=NORMAL)
        e104.delete(0,END)
        e104.focus()
    else:
        e104.config(state=DISABLED)
        e_man.set('0')

def soup():
    if var5.get()==1:
        e105.config(state=NORMAL)
        e105.delete(0,END)
        e105.focus()
    else:
        e105.config(state=DISABLED)
        e_soup.set('0')

def pav():
    if var6.get()==1:
        e106.config(state=NORMAL)
        e106.delete(0,END)
        e106.focus()
    else:
        e106.config(state=DISABLED)
        e_pav.set('0')

def bb():
    if var7.get()==1:
        e107.config(state=NORMAL)
        e107.delete(0,END)
        e107.focus()
    else:
        e107.config(state=DISABLED)
        e_bb.set('0')

def pizza():
    if var8.get()==1:
        e108.config(state=NORMAL)
        e108.delete(0,END)
        e108.focus()
    else:
        e108.config(state=DISABLED)
        e_pizza.set('0')

def sw():
    if var9.get()==1:
        e109.config(state=NORMAL)
        e109.delete(0,END)
        e109.focus()
    else:
        e109.config(state=DISABLED)
        e_sw.set('0')

def burger():
    if var10.get()==1:
        e110.config(state=NORMAL)
        e110.delete(0,END)
        e110.focus()
    else:
        e110.config(state=DISABLED)
        e_burger.set('0')

def gsw():
    if var12.get()==1:
        e112.config(state=NORMAL)
        e112.delete(0,END)
        e112.focus()
    else:
        e112.config(state=DISABLED)
        e_gsw.set('0')

def biryani():
    if var13.get()==1:
        e113.config(state=NORMAL)
        e113.delete(0,END)
        e113.focus()
    else:
        e113.config(state=DISABLED)
        e_biryani.set('0')

def jira():
    if var14.get()==1:
        e114.config(state=NORMAL)
        e114.delete(0,END)
        e114.focus()
    else:
        e114.config(state=DISABLED)
        e_jira.set('0')

def sada():
    if var15.get()==1:
        e115.config(state=NORMAL)
        e115.delete(0,END)
        e115.focus()
    else:
        e115.config(state=DISABLED)
        e_sada.set('0')

def masala():
    if var16.get()==1:
        e116.config(state=NORMAL)
        e116.delete(0,END)
        e116.focus()
    else:
        e116.config(state=DISABLED)
        e_masala.set('0')

def mysore():
    if var17.get()==1:
        e117.config(state=NORMAL)
        e117.delete(0,END)
        e117.focus()
    else:
        e117.config(state=DISABLED)
        e_mysore.set('0')

def chaas():
    if var18.get()==1:
        e201.config(state=NORMAL)
        e201.delete(0,END)
        e201.focus()
    else:
        e201.config(state=DISABLED)
        e_chaas.set('0')

def pepsi():
    if var19.get()==1:
        e202.config(state=NORMAL)
        e202.delete(0,END)
        e202.focus()
    else:
        e202.config(state=DISABLED)
        e_pepsi.set('0')

def coke():
    if var20.get()==1:
        e203.config(state=NORMAL)
        e203.delete(0,END)
        e203.focus()
    else:
        e203.config(state=DISABLED)
        e_coke.set('0')

def sprite():
    if var21.get()==1:
        e204.config(state=NORMAL)
        e204.delete(0,END)
        e204.focus()
    else:
        e204.config(state=DISABLED)
        e_sprite.set('0')

def sosyo():
    if var22.get()==1:
        e205.config(state=NORMAL)
        e205.delete(0,END)
        e205.focus()
    else:
        e205.config(state=DISABLED)
        e_sosyo.set('0')

def juice():
    if var23.get()==1:
        e206.config(state=NORMAL)
        e206.delete(0,END)
        e206.focus()
    else:
        e206.config(state=DISABLED)
        e_juice.set('0')

def mazza():
    if var24.get()==1:
        e207.config(state=NORMAL)
        e207.delete(0,END)
        e207.focus()
    else:
        e207.config(state=DISABLED)
        e_mazza.set('0')

def shake():
    if var25.get()==1:
        e208.config(state=NORMAL)
        e208.delete(0,END)
        e208.focus()
    else:
        e208.config(state=DISABLED)
        e_shake.set('0')

#============================================================================================

def totalcost():
    global PriceOfDrinks,PriceOfDishes,Subtotal,S1,T1,m
    if var1.get()!=0 or var2.get()!=0 or var3.get()!=0 or var4.get()!=0 or var5.get()!=0 or\
       var6.get()!=0 or var7.get()!=0 or var8.get()!=0 or var9.get()!=0 or var10.get()!=0 or\
       var12.get()!=0 or var13.get()!=0 or var14.get()!=0 or var15.get()!=0 or var16.get()!=0 or\
       var17.get()!=0 or var18.get()!=0 or var19.get()!=0 or var20.get()!=0 or var21.get()!=0 or\
       var22.get()!=0 or var23.get()!=0 or var24.get()!=0 or var25.get()!=0:

        item1=int(e_guj.get())
        item2=int(e_pun.get())
        item3=int(e_noo.get())
        item4=int(e_man.get())
        item5=int(e_soup.get())
        item6=int(e_pav.get())
        item7=int(e_bb.get())
        item8=int(e_pizza.get())
        item9=int(e_sw.get())
        item10=int(e_burger.get())
        item11=int(e_gsw.get())
        item12=int(e_biryani.get())
        item13=int(e_jira.get())
        item14=int(e_sada.get())
        item15=int(e_masala.get())
        item16=int(e_mysore.get())
        item17=int(e_chaas.get())
        item18=int(e_pepsi.get())
        item19=int(e_coke.get())
        item20=int(e_sprite.get())
        item21=int(e_sosyo.get())
        item22=int(e_juice.get())
        item23=int(e_mazza.get())
        item24=int(e_shake.get())

    PriceOfDrinks=(item17*20)+(item18*30)+(item19*30)+(item20*30)+(item21*30)+\
                  (item22*40)+(item23*30)+(item24*60)
    PriceOfDishes=(item1*80)+(item2*120)+(item3*110)+(item4*90)+(item5*70)+\
                  (item6*100)+(item7*130)+(item8*210)\
                  +(item9*95)+(item10*60)+(item11*110)+(item12*70)+(item13*80)+\
                  (item14*110)+(item15*100)+(item16*130)
    m=random.randrange(1111,9999)
    
    CostOfDrinks.set(str(PriceOfDrinks)+ '₹')
    CostOfDishes.set(str(PriceOfDishes)+ '₹')
    BillNumber.set(m)

    S1=PriceOfDrinks+PriceOfDishes
    Subtotal.set(str(S1)+ '₹')

    ServiceCharge.set('50₹')

    T1=PriceOfDishes+PriceOfDrinks+50
    Total.set(str(T1) + '₹')

#=========================================================================================

def receipt():
    global Billnumber,date
    if CostOfDrinks.get() != '' or CostOfDishes.get() != '':
        textReceipt.delete(1.0,END)
        Billnumber='BILL'+str(m)
        date=time.strftime('%d/%m/%Y')
        textReceipt.insert(END,'Receipt Ref:'+Billnumber+'\t\t\t'+date+'\n')
        textReceipt.insert(END,'***************************************************\n')
        textReceipt.insert(END,'Items\t\tQuntity \tCost(Rs)\n')
        textReceipt.insert(END,'***************************************************\n')
        if e_guj.get()!='0':
            textReceipt.insert(END,f'Gujarati Thali:\t\t{int(e_guj.get())}\t{int(e_guj.get())*80}\n')

        if e_pun.get()!='0':
            textReceipt.insert(END,f'Punjabi Thali:\t\t{int(e_pun.get())}\t{int(e_pun.get())*120}\n')

        if e_noo.get()!='0':
            textReceipt.insert(END,f'Chinese Noodles:\t\t{int(e_noo.get())}\t{int(e_noo.get())*110}\n')

        if e_man.get() != '0':
            textReceipt.insert(END, f'Manchurian:\t\t{int(e_man.get())}\t{int(e_man.get())*90}\n')

        if e_soup.get() != '0':
            textReceipt.insert(END, f'Chinese Soup:\t\t{int(e_soup.get())}\t{int(e_soup.get())*70}\n')

        if e_pav.get() != '0':
            textReceipt.insert(END, f'Pavbhaji:\t\t{int(e_pav.get())}\t{int(e_pav.get())*100}\n')

        if e_bb.get() != '0':
            textReceipt.insert(END, f'Butter Bhaji:\t\t{int(e_bb.get())}\t{int(e_bb.get())*130}\n')

        if e_pizza.get() != '0':
            textReceipt.insert(END, f'Pizza:\t\t{int(e_pizza.get())}\t{int(e_pizza.get())*210}\n')

        if e_sw.get() != '0':
            textReceipt.insert(END, f'Sandwich:\t\t{int(e_sw.get())}\t{int(e_sw.get())*95}\n')

        if e_burger.get() != '0':
            textReceipt.insert(END, f'Burger:\t\t{int(e_burger.get())}\t{int(e_burger.get())*60}\n')

        if e_gsw.get() != '0':
            textReceipt.insert(END, f'Grill-Sandwich:\t\t{int(e_gsw.get())}\t{int(e_gsw.get())*110}\n')

        if e_biryani.get() != '0':
            textReceipt.insert(END, f'Biryani:\t\t{int(e_biryani.get())}\t{int(e_biryani.get())*70}\n')

        if e_jira.get() != '0':
            textReceipt.insert(END, f'Jira-rice:\t\t{int(e_jira.get())}\t{int(e_jira.get())*80}\n')

        if e_sada.get() != '0':
            textReceipt.insert(END, f'Sada Dhosa:\t\t{int(e_sada.get())}\t{int(e_sada.get())*110}\n')

        if e_masala.get() != '0':
            textReceipt.insert(END, f'Masala Dhosa:\t\t{int(e_masala.get())}\t{int(e_masala.get())*100}\n')

        if e_mysore.get() != '0':
            textReceipt.insert(END, f'Mysore Dhosa:\t\t{int(e_mysore.get())}\t{int(e_mysore.get())*130}\n')

        if e_chaas.get() != '0':
            textReceipt.insert(END, f'Chaas:\t\t{int(e_chaas.get())}\t{int(e_chaas.get())*20}\n')

        if e_pepsi.get() != '0':
            textReceipt.insert(END, f'Pepsi:\t\t{int(e_pepsi.get())}\t{int(e_pepsi.get())*30}\n')

        if e_coke.get() != '0':
            textReceipt.insert(END, f'Coke:\t\t{int(e_coke.get())}\t{int(e_coke.get())*30}\n')

        if e_sprite.get() != '0':
            textReceipt.insert(END, f'Sprite:\t\t{int(e_sprite.get())}\t{int(e_sprite.get())*30}\n')

        if e_sosyo.get() != '0':
            textReceipt.insert(END, f'Sosyo:\t\t{int(e_sosyo.get())}\t{int(e_sosyo.get())*30}\n')

        if e_juice.get() != '0':
            textReceipt.insert(END, f'Juice:\t\t{int(e_juice.get())}\t{int(e_juice.get())*40}\n')

        if e_mazza.get() != '0':
            textReceipt.insert(END, f'Mazza:\t\t{int(e_mazza.get())}\t{int(e_mazza.get())*30}\n')

        if e_shake.get() != '0':
            textReceipt.insert(END, f'Shake:\t\t{int(e_shake.get())}\t{int(e_shake.get())*60}\n')

        textReceipt.insert(END,'***************************************************\n')
        if CostOfDrinks.get()!='0 Rs':
            textReceipt.insert(END,f'CostOfDrinks\t\t\t{PriceOfDrinks}Rs\n')
        if CostOfDishes.get() != '0 Rs':
            textReceipt.insert(END,f'CostOfDishes\t\t\t{PriceOfDishes}Rs\n')

        textReceipt.insert(END, f'Subtotal\t\t\t{S1}Rs\n')
        textReceipt.insert(END, f'ServiceCharge\t\t\t{50}Rs\n\n')
        textReceipt.insert(END, f'Total\t\t\t{T1}Rs\n\n')
        textReceipt.insert(END,'***************************************************\n')

    else:
        messagebox.showerror('Error','No Item Is selected')


#========================================================================================
def reset():
    textReceipt.delete(1.0,END)
    e_guj.set('0')
    e_pun.set('0')
    e_noo.set('0')
    e_man.set('0')
    e_soup.set('0')
    e_pav.set('0')
    e_bb.set('0')
    e_pizza.set('0')

    e_sw.set('0')
    e_burger.set('0')
    e_gsw.set('0')
    e_biryani.set('0')
    e_jira.set('0')
    e_sada.set('0')
    e_masala.set('0')
    e_mysore.set('0')

    e_chaas.set('0')
    e_pepsi.set('0')
    e_coke.set('0')
    e_sprite.set('0')
    e_sosyo.set('0')
    e_juice.set('0')
    e_mazza.set('0')
    e_shake.set('0')

    e101.config(state=DISABLED)
    e102.config(state=DISABLED)
    e103.config(state=DISABLED)
    e104.config(state=DISABLED)
    e105.config(state=DISABLED)
    e106.config(state=DISABLED)
    e107.config(state=DISABLED)
    e108.config(state=DISABLED)
    e109.config(state=DISABLED)

    e110.config(state=DISABLED)
    e114.config(state=DISABLED)
    e112.config(state=DISABLED)
    e113.config(state=DISABLED)
    e115.config(state=DISABLED)
    e116.config(state=DISABLED)
    e117.config(state=DISABLED)
    e201.config(state=DISABLED)
    e202.config(state=DISABLED)

    e203.config(state=DISABLED)
    e204.config(state=DISABLED)
    e205.config(state=DISABLED)
    e206.config(state=DISABLED)
    e207.config(state=DISABLED)
    e208.config(state=DISABLED)

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)
    var25.set(0)

    CostOfDrinks.set('')
    CostOfDishes.set('')
    ServiceCharge.set('')
    Subtotal.set('')
    Total.set('')
    BillNumber.set('')

#=============================================================================

def Exit():
    Exit=messagebox.askquestion("Confirm","Are you sure?")
    if Exit=='yes':
        top.destroy()
    return

#=============================================================================================

def Insert():
    billnumber=BillNumber.get()
    costofdishes=CostOfDishes.get()
    costofdrinks=CostOfDrinks.get()
    servicecharge=ServiceCharge.get()
    subtotal=Subtotal.get()
    total=Total.get()
    
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="restaurant_data"
    )

    mycursor = mydb.cursor()
    sql = "INSERT INTO data (Bill_Number,dishes_cost,drinks_cost,service_charge,subtotal,total) VALUES (%s,%s,%s,%s,%s,%s)"
    val = (billnumber,costofdishes,costofdishes,servicecharge,subtotal,total)
    
    mycursor.execute(sql,val)

    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

def Delete():
    billnumber=BillNumber.get()
    
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="restaurant_data"
    )

    mycursor = mydb.cursor()
    sql = "DELETE FROM data WHERE Bill_Number =%s"
    val = (billnumber,)
    
    mycursor.execute(sql,val)

    mydb.commit()
    print(mycursor.rowcount, "record Deleted.")
#======================================================================================
def drink_list():
    my_w = tk.Tk()
    my_w.geometry("750x80")
    my_w.configure(bg="navy")
    my_w.resizable(0,0)
    my_connect = mysql.connector.connect(
        host="localhost",
        user="root", 
        password="",
        database="restaurant_data"
    )

    my_conn = my_connect.cursor()

    my_conn.execute("SELECT * FROM drinks")
    d1frame= Frame(my_w,bg="grey",bd=10,relief=RIDGE)
    d1frame.pack(side = TOP)
    e=Label(d1frame,width=10,text='Chaas',borderwidth=2, relief='ridge',
            anchor='w',fg='navy',bg='cadetblue',font=("arial",10,"bold"))
    e.grid(row=0,column=0)
    e=Label(d1frame,width=10,text='Pepsi',borderwidth=2, relief='ridge',
            anchor='w',fg='navy',bg='cadetblue',font=("arial",10,"bold"))
    e.grid(row=0,column=1)
    e=Label(d1frame,width=10,text='Coke',borderwidth=2, relief='ridge',
            anchor='w',fg='navy',bg='cadetblue',font=("arial",10,"bold"))
    e.grid(row=0,column=2)
    e=Label(d1frame,width=10,text='Sprite',borderwidth=2, relief='ridge',
            anchor='w',fg='navy',bg='cadetblue',font=("arial",10,"bold"))
    e.grid(row=0,column=3)
    e=Label(d1frame,width=10,text='Sosyo',borderwidth=2, relief='ridge',
             anchor='w',fg='navy',bg='cadetblue',font=("arial",10,"bold"))
    e.grid(row=0,column=4)
    e=Label(d1frame,width=10,text='Juice',borderwidth=2, relief='ridge',
            anchor='w',fg='navy',bg='cadetblue',font=("arial",10,"bold"))
    e.grid(row=0,column=5)
    e=Label(d1frame,width=10,text='Mazza',borderwidth=2, relief='ridge',
            anchor='w',fg='navy',bg='cadetblue',font=("arial",10,"bold"))
    e.grid(row=0,column=6)
    e=Label(d1frame,width=10,text='Shake',borderwidth=2, relief='ridge',
            anchor='w',fg='navy',bg='cadetblue',font=("arial",10,"bold"))
    e.grid(row=0,column=7)
    i=1 
    for student in my_conn: 
        for j in range(len(student)):
            e = Entry(d1frame, width=10, fg='navy') 
            e.grid(row=i, column=j) 
            e.insert(END, student[j])
    i=i+1
    my_w.mainloop()

def dishes_list():
    my_w = tk.Tk()
    my_w.geometry("750x130")
    my_w.configure(bg="navy")
    my_w.resizable(0,0)
    my_connect = mysql.connector.connect(
        host="localhost",
        user="root", 
        password="",
        database="restaurant_data"
    )

    mycursor = my_connect.cursor()

    mycursor.execute("SELECT * FROM dishes")
    '''

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)'''

            
    d1frame= Frame(my_w,bg="grey",bd=10,relief=RIDGE)
    d1frame.pack(side = TOP)
    d2frame= Frame(my_w,bg="grey",bd=10,relief=RIDGE)
    d2frame.pack(side = TOP)
        
    e=Label(d1frame,width=10,text='Gujarati Thali',borderwidth=2, relief='ridge',
            anchor='w',fg='navy',bg='cadetblue',font=("arial",10,"bold"))
    e.grid(row=0,column=0)
    e=Label(d1frame,width=10,text='Punjabi Thali',borderwidth=2, relief='ridge',
            anchor='w',fg='navy',bg='cadetblue',font=("arial",10,"bold"))
    e.grid(row=0,column=1)
    e=Label(d1frame,width=10,text='Chinese Noodles',borderwidth=2, relief='ridge',
            anchor='w',fg='navy',bg='cadetblue',font=("arial",10,"bold"))
    e.grid(row=0,column=2)
    e=Label(d1frame,width=10,text='Manchurian',borderwidth=2, relief='ridge',
            anchor='w',fg='navy',bg='cadetblue',font=("arial",10,"bold"))
    e.grid(row=0,column=3)
    e=Label(d1frame,width=10,text='Chinese Soup',borderwidth=2, relief='ridge',
            anchor='w',fg='navy',bg='cadetblue',font=("arial",10,"bold"))
    e.grid(row=0,column=4)
    e=Label(d1frame,width=10,text='Pavbhaji',borderwidth=2, relief='ridge',
            anchor='w',fg='navy',bg='cadetblue',font=("arial",10,"bold"))
    e.grid(row=0,column=5)
    e=Label(d1frame,width=10,text='Butter Bhaji',borderwidth=2, relief='ridge',
            anchor='w',fg='navy',bg='cadetblue',font=("arial",10,"bold"))
    e.grid(row=0,column=6)
    e=Label(d1frame,width=10,text='Pizza',borderwidth=2, relief='ridge',
            anchor='w',fg='navy',bg='cadetblue',font=("arial",10,"bold"))
    e.grid(row=0,column=7)

    i=1 
    for student in mycursor: 
        for j in range(len(student)):
            e = Entry(d1frame, width=10, fg='navy') 
            e.grid(row=i, column=j) 
            e.insert(END, student[j])
    i=i+1
    

    mycursor2 = my_connect.cursor()

    mycursor2.execute("SELECT * FROM dishes_2")
    
    e=Label(d2frame,width=10,text='Sandwich',borderwidth=2, relief='ridge',
            anchor='w',fg='navy',bg='cadetblue',font=("arial",10,"bold"))
    e.grid(row=0,column=0)
    e=Label(d2frame,width=10,text='Grill Sandwich',borderwidth=2, relief='ridge',
            anchor='w',fg='navy',bg='cadetblue',font=("arial",10,"bold"))
    e.grid(row=0,column=1)
    e=Label(d2frame,width=10,text='Biryani',borderwidth=2, relief='ridge',
            anchor='w',fg='navy',bg='cadetblue',font=("arial",10,"bold"))
    e.grid(row=0,column=2)
    e=Label(d2frame,width=10,text='Jira-Rice',borderwidth=2, relief='ridge',
            anchor='w',fg='navy',bg='cadetblue',font=("arial",10,"bold"))
    e.grid(row=0,column=3)
    e=Label(d2frame,width=10,text='Sada Dhosa',borderwidth=2, relief='ridge',
            anchor='w',fg='navy',bg='cadetblue',font=("arial",10,"bold"))
    e.grid(row=0,column=4)
    e=Label(d2frame,width=10,text='Masala Dhosa',borderwidth=2, relief='ridge',
            anchor='w',fg='navy',bg='cadetblue',font=("arial",10,"bold"))
    e.grid(row=0,column=5)
    e=Label(d2frame,width=10,text='Mysore Dhosa',borderwidth=2, relief='ridge',
            anchor='w',fg='navy',bg='cadetblue',font=("arial",10,"bold"))
    e.grid(row=0,column=6)
    e=Label(d2frame,width=10,text='Burger',borderwidth=2, relief='ridge',
            anchor='w',fg='navy',bg='cadetblue',font=("arial",10,"bold"))
    e.grid(row=0,column=7)

    k=1 
    for student in mycursor2: 
        for q in range(len(student)):
            e = Entry(d2frame, width=10, fg='navy') 
            e.grid(row=k, column=q) 
            e.insert(END, student[q])
    k=k+1
        
    

    my_w.mainloop()


def bill():
    global Billnumber,date
    if CostOfDrinks.get() != '' or CostOfDishes.get() != '':
        textReceipt.delete(1.0,END)
        Billnumber='BILL'+str(m)
        date=time.strftime('%d/%m/%Y')
        textReceipt.insert(END,'Receipt Ref:'+Billnumber+'\t\t\t'+date+'\n')
        textReceipt.insert(END,'***************************************************\n')
        textReceipt.insert(END,'Items:\t\tQuntity \tCost(Rs)\n')
        textReceipt.insert(END,'***************************************************\n')
        if e_guj.get()!='0':
            textReceipt.insert(END,f'Gujarati Thali:\t\t{int(e_guj.get())}\t{int(e_guj.get())*80}\n')
        if e_pun.get()!='0':
            textReceipt.insert(END,f'Punjabi Thali:\t\t{int(e_pun.get())}\t{int(e_pun.get())*120}\n')
        if e_noo.get()!='0':
            textReceipt.insert(END,f'Chinese Noodles:\t\t{int(e_noo.get())}\t{int(e_noo.get())*110}\n')
        if e_man.get() != '0':
            textReceipt.insert(END, f'Manchurian:\t\t\t{int(e_man.get())}\t{int(e_man.get())*90}\n')
        if e_soup.get() != '0':
            textReceipt.insert(END, f'Chinese Soup:\t\t{int(e_soup.get())}\t{int(e_soup.get())*70}\n')
        if e_pav.get() != '0':
            textReceipt.insert(END, f'Pavbhaji:\t\t\t{int(e_pav.get())}\t{int(e_pav.get())*100}\n')
        if e_bb.get() != '0':
            textReceipt.insert(END, f'Butter Bhaji:\t\t{int(e_bb.get())}\t{int(e_bb.get())*130}\n')
        if e_pizza.get() != '0':
            textReceipt.insert(END, f'Pizza:\t\t\t{int(e_pizza.get())}\t{int(e_pizza.get())*210}\n')
        if e_sw.get() != '0':
            textReceipt.insert(END, f'Sandwich:\t\t\t{int(e_sw.get())}\t{int(e_sw.get())*95}\n')
        if e_burger.get() != '0':
            textReceipt.insert(END, f'Burger:\t\t\t{int(e_burger.get())}\t{int(e_burger.get())*60}\n')
        if e_gsw.get() != '0':
            textReceipt.insert(END, f'Grill-Sandwich:\t\t{int(e_gsw.get())}\t{int(e_gsw.get())*110}\n')
        if e_biryani.get() != '0':
            textReceipt.insert(END, f'Biryani:\t\t\t{int(e_biryani.get())}\t{int(e_biryani.get())*70}\n')
        if e_jira.get() != '0':
            textReceipt.insert(END, f'Jira-rice:\t\t\t{int(e_jira.get())}\t{int(e_jira.get())*80}\n')
        if e_sada.get() != '0':
            textReceipt.insert(END, f'Sada Dhosa:\t\t\t{int(e_sada.get())}\t{int(e_sada.get())*110}\n')
        if e_masala.get() != '0':
            textReceipt.insert(END, f'Masala Dhosa:\t\t{int(e_masala.get())}\t{int(e_masala.get())*100}\n')
        if e_mysore.get() != '0':
            textReceipt.insert(END, f'Mysore Dhosa:\t\t{int(e_mysore.get())}\t{int(e_mysore.get())*130}\n')
        if e_chaas.get() != '0':
            textReceipt.insert(END, f'Chaas:\t\t\t{int(e_chaas.get())}\t{int(e_chaas.get())*20}\n')
        if e_pepsi.get() != '0':
            textReceipt.insert(END, f'Pepsi:\t\t\t{int(e_pepsi.get())}\t{int(e_pepsi.get())*30}\n')
        if e_coke.get() != '0':
            textReceipt.insert(END, f'Coke:\t\t\t\t{int(e_coke.get())}\t{int(e_coke.get())*30}\n')
        if e_sprite.get() != '0':
            textReceipt.insert(END, f'Sprite:\t\t\t{int(e_sprite.get())}\t{int(e_sprite.get())*30}\n')
        if e_sosyo.get() != '0':
            textReceipt.insert(END, f'Sosyo:\t\t\t{int(e_sosyo.get())}\t{int(e_sosyo.get())*30}\n')
        if e_juice.get() != '0':
            textReceipt.insert(END, f'Juice:\t\t\t{int(e_juice.get())}\t{int(e_juice.get())*40}\n')
        if e_mazza.get() != '0':
            textReceipt.insert(END, f'Mazza:\t\t\t{int(e_mazza.get())}\t{int(e_mazza.get())*30}\n')
        if e_shake.get() != '0':
            textReceipt.insert(END, f'Shake:\t\t\t{int(e_shake.get())}\t{int(e_shake.get())*60}\n')
        textReceipt.insert(END,'***************************************************\n')
        if CostOfDrinks.get()!='0 Rs':
            textReceipt.insert(END,f'CostOfDrinks\t\t\t{PriceOfDrinks}Rs\n')
        if CostOfDishes.get() != '0 Rs':
            textReceipt.insert(END,f'CostOfDishes\t\t\t{PriceOfDishes}Rs\n')

        textReceipt.insert(END, f'Subtotal\t\t\t\t{S1}Rs\n')
        textReceipt.insert(END, f'ServiceCharge\t\t\t{50}Rs\n\n')
        textReceipt.insert(END, f'Total\t\t\t\t\t{T1}Rs\n')
        textReceipt.insert(END,'***************************************************\n')

        

        op=messagebox.askyesno("Save bill","Do you want t o save the Bill?")
        if op>0:
            bill_details=textReceipt.get('1.0',END)
            f1=open("BILL/"+(Billnumber)+".txt","w")
            f1.write(bill_details)
            f1.close()
            messagebox.showinfo("Saved",f"Bill no: {Billnumber} Saved Successfully")
        else:
            return

    



#=============================================================================================


Tframe= Frame(top,bg="navy",bd=10,relief=RIDGE)
Tframe.pack( side = TOP)

l12=Label(Tframe,text="Dine POS",height=4,
          width=62,font=("arial",25,"bold"),fg="navy",bg="cadetblue")
l12.grid(row=0,column=0)

#=======================================================================================
MLframe= Frame(top,bg="navy",bd=10,relief=RIDGE)
MLframe.pack(side = LEFT)

L3frame= Frame(MLframe,bg="cadetblue",bd=10,relief=RIDGE,width=150)
L3frame.pack(side = BOTTOM)

c301=Label(L3frame,text="Cost Of Drink\t",font=("arial",15,"bold"),fg="navy",
           bg="cadetblue")
c301.grid(row=0,column=0,sticky=W)

e301=Entry(L3frame,bd=3,width=26,textvariable=CostOfDrinks)
e301.grid(row=0,column=1,sticky=W)

c302=Label(L3frame,text="Cost Of Dishes\t",font=("arial",15,"bold"),fg="navy",
           bg="cadetblue")
c302.grid(row=1,column=0,sticky=W)

e302=Entry(L3frame,bd=3,width=26,textvariable=CostOfDishes)
e302.grid(row=1,column=1,sticky=W)

c307=Label(L3frame,text="Bill Number\t",font=("arial",15,"bold"),fg="navy",
           bg="cadetblue")
c307.grid(row=2,column=0,sticky=W)

e307=Entry(L3frame,bd=3,width=26,textvariable=BillNumber)
e307.grid(row=2,column=1,sticky=W)

c303=Label(L3frame,text="\tService Charge\t",font=("arial",15,"bold"),fg="navy",
           bg="cadetblue")
c303.grid(row=0,column=3,sticky=W)

e303=Entry(L3frame,bd=3,width=25,textvariable=ServiceCharge)
e303.grid(row=0,column=4,sticky=W)

c304=Label(L3frame,text="\tSub Total\t",font=("arial",15,"bold"),fg="navy",
           bg="cadetblue")
c304.grid(row=1,column=3,sticky=W)

e304=Entry(L3frame,bd=3,width=25,textvariable=Subtotal)
e304.grid(row=1,column=4,sticky=W)

c305=Label(L3frame,text="\tTotal\t",font=("arial",15,"bold"),fg="navy",
           bg="cadetblue")
c305.grid(row=2,column=3,sticky=W)

e305=Entry(L3frame,bd=3,width=25,textvariable=Total)
e305.grid(row=2,column=4,sticky=W)

b50=Button(L3frame,text="Dishes",command=dishes_list,font=("arial",15,"bold"),fg="navy",
           bg="cadetblue",bd="5")
b50.grid(row=3,column=1)

b51=Button(L3frame,text="Delete",command=Delete,font=("arial",15,"bold"),fg="navy",
           bg="cadetblue",bd="5")
b51.place(x=650,y=90)

b52=Button(L3frame,text="Insert",command=Insert,font=("arial",15,"bold"),fg="navy",
           bg="cadetblue",bd="5")
b52.grid(row=3,column=3)

b53=Button(L3frame,text="Print Bill",font=("arial",15,"bold"),fg="navy",
           bg="cadetblue",bd="5",command=bill)
b53.grid(row=3,column=0)

b54=Button(L3frame,text="Drinks",command=drink_list,font=("arial",15,"bold"),fg="navy",
           bg="cadetblue",bd="5")
b54.grid(row=3,column=2)

#=======================================================================================
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()
var17=IntVar()
var18=IntVar()
var19=IntVar()
var20=IntVar()
var21=IntVar()
var22=IntVar()
var23=IntVar()
var24=IntVar()
var25=IntVar()


Lframe= Frame(MLframe,bg="cadetblue",bd=10,relief=RIDGE)
Lframe.pack(side = LEFT)

c101=Checkbutton(Lframe,text="Gujarati Thali",variable=var1,onvalue=1,offvalue=0,
                 font=("arial",15,"bold"),fg="navy",bg="cadetblue",command=guj)
c101.grid(row=0,sticky=W)



e101=Entry(Lframe,bd=3,textvariable=e_guj)
e101.grid(row=0,column=1)

c102=Checkbutton(Lframe,text="Punjabi Thali",onvalue=1,offvalue=0,variable=var2,
                 font=("arial",15,"bold"),fg="navy",bg="cadetblue",command=pun)
c102.grid(row=1,sticky=W)

e102=Entry(Lframe,bd=3,textvariable=e_pun)
e102.grid(row=1,column=1)

c103=Checkbutton(Lframe,text="Chinese Noodles",onvalue=1,offvalue=0,variable=var3,
                 font=("arial",15,"bold"),fg="navy",bg="cadetblue",command=noo)
c103.grid(row=2,sticky=W)

e103=Entry(Lframe,bd=3,textvariable=e_noo)
e103.grid(row=2,column=1)

c104=Checkbutton(Lframe,text="Manchurian",onvalue=1,offvalue=0,variable=var4,
                 font=("arial",15,"bold"),fg="navy",bg="cadetblue",command=man)
c104.grid(row=3,sticky=W)

e104=Entry(Lframe,bd=3,textvariable=e_man)
e104.grid(row=3,column=1)

c105=Checkbutton(Lframe,text="Chinese Soup",onvalue=1,offvalue=0,variable=var5,
                 font=("arial",15,"bold"),fg="navy",bg="cadetblue",command=soup)
c105.grid(row=4,sticky=W)

e105=Entry(Lframe,bd=3,textvariable=e_soup)
e105.grid(row=4,column=1)

c106=Checkbutton(Lframe,text="Pav-Bhaji",onvalue=1,offvalue=0,variable=var6,
                 font=("arial",15,"bold"),fg="navy",bg="cadetblue",command=pav)
c106.grid(row=5,sticky=W)

e106=Entry(Lframe,bd=3,textvariable=e_pav)
e106.grid(row=5,column=1)

c107=Checkbutton(Lframe,text="Butter Bhaji",onvalue=1,offvalue=0,variable=var7,
                 font=("arial",15,"bold"),fg="navy",bg="cadetblue",command=bb)
c107.grid(row=6,sticky=W)

e107=Entry(Lframe,bd=3,textvariable=e_bb)
e107.grid(row=6,column=1)

c108=Checkbutton(Lframe,text="Pizza",onvalue=1,offvalue=0,variable=var8,
                 font=("arial",15,"bold"),fg="navy",bg="cadetblue",command=pizza)
c108.grid(row=7,sticky=W)

e108=Entry(Lframe,bd=3,textvariable=e_pizza)
e108.grid(row=7,column=1)

c109=Checkbutton(Lframe,text="Sand-Wich",onvalue=1,offvalue=0,variable=var9,
                 font=("arial",15,"bold"),fg="navy",bg="cadetblue",command=sw)
c109.grid(row=0,column=2,sticky=W)

e109=Entry(Lframe,bd=3,textvariable=e_sw)
e109.grid(row=0,column=3)

c110=Checkbutton(Lframe,text="Burger",onvalue=1,offvalue=0,variable=var10,
                 font=("arial",15,"bold"),fg="navy",bg="cadetblue",command=burger)
c110.grid(row=7,column=2,sticky=W)

e110=Entry(Lframe,bd=3,textvariable=e_burger)
e110.grid(row=7,column=3)

c112=Checkbutton(Lframe,text="Grill Sand-Wich",onvalue=1,offvalue=0,variable=var12,
                 font=("arial",15,"bold"),fg="navy",bg="cadetblue",command=gsw)
c112.grid(row=1,column=2,sticky=W)

e112=Entry(Lframe,bd=3,textvariable=e_gsw)
e112.grid(row=1,column=3)

c113=Checkbutton(Lframe,text="Biryani",onvalue=1,offvalue=0,variable=var13,
                 font=("arial",15,"bold"),fg="navy",bg="cadetblue",command=biryani)
c113.grid(row=2,column=2,sticky=W)

e113=Entry(Lframe,bd=3,textvariable=e_biryani)
e113.grid(row=2,column=3)

c114=Checkbutton(Lframe,text="Jira-Rice",onvalue=1,offvalue=0,variable=var14,
                 font=("arial",15,"bold"),fg="navy",bg="cadetblue",command=jira)
c114.grid(row=3,column=2,sticky=W)

e114=Entry(Lframe,bd=3,textvariable=e_jira)
e114.grid(row=3,column=3)

c115=Checkbutton(Lframe,text="Sada Dhosa",onvalue=1,offvalue=0,variable=var15,
                 font=("arial",15,"bold"),fg="navy",bg="cadetblue",command=sada)
c115.grid(row=4,column=2,sticky=W)

e115=Entry(Lframe,bd=3,textvariable=e_sada)
e115.grid(row=4,column=3)

c116=Checkbutton(Lframe,text="Masala Dhosa",onvalue=1,offvalue=0,variable=var16,
                 font=("arial",15,"bold"),fg="navy",bg="cadetblue",command=masala)
c116.grid(row=5,column=2,sticky=W)

e116=Entry(Lframe,bd=3,textvariable=e_masala)
e116.grid(row=5,column=3)

c117=Checkbutton(Lframe,text="Mysore Dhosa",onvalue=1,offvalue=0,variable=var17,
                 font=("arial",15,"bold"),fg="navy",bg="cadetblue",command=mysore)
c117.grid(row=6,column=2,sticky=W)

e117=Entry(Lframe,bd=3,textvariable=e_mysore)
e117.grid(row=6,column=3)

#==========================================================================================

L2frame= Frame(MLframe,bg="cadetblue",bd=10,relief=RIDGE)
L2frame.pack(side = RIGHT)

c201=Checkbutton(L2frame,text="Chaas",onvalue=1,offvalue=0,variable=var18,
                 font=("arial",15,"bold"),fg="navy",bg="cadetblue",command=chaas)
c201.grid(row=0,sticky=W)

e201=Entry(L2frame,bd=3,textvariable=e_chaas)
e201.grid(row=0,column=1)

c202=Checkbutton(L2frame,text="Pepsi",onvalue=1,offvalue=0,variable=var19,
                 font=("arial",15,"bold"),fg="navy",bg="cadetblue",command=pepsi)
c202.grid(row=1,sticky=W)

e202=Entry(L2frame,bd=3,textvariable=e_pepsi)
e202.grid(row=1,column=1)

c203=Checkbutton(L2frame,text="Coke",onvalue=1,offvalue=0,variable=var20,
                 font=("arial",15,"bold"),fg="navy",bg="cadetblue",command=coke)
c203.grid(row=2,sticky=W)

e203=Entry(L2frame,bd=3,textvariable=e_coke)
e203.grid(row=2,column=1)

c204=Checkbutton(L2frame,text="Sprite",onvalue=1,offvalue=0,variable=var21,
                 font=("arial",15,"bold"),fg="navy",bg="cadetblue",command=sprite)
c204.grid(row=3,sticky=W)

e204=Entry(L2frame,bd=3,textvariable=e_sprite)
e204.grid(row=3,column=1)

c205=Checkbutton(L2frame,text="Sosyo",onvalue=1,offvalue=0,variable=var22,
                 font=("arial",15,"bold"),fg="navy",bg="cadetblue",command=sosyo)
c205.grid(row=4,sticky=W)

e205=Entry(L2frame,bd=3,textvariable=e_sosyo)
e205.grid(row=4,column=1)

c206=Checkbutton(L2frame,text="Juice",onvalue=1,offvalue=0,variable=var23,
                 font=("arial",15,"bold"),fg="navy",bg="cadetblue",command=juice)
c206.grid(row=5,sticky=W)

e206=Entry(L2frame,bd=3,textvariable=e_juice)
e206.grid(row=5,column=1)

c207=Checkbutton(L2frame,text="Mazza",onvalue=1,offvalue=0,variable=var24,
                 font=("arial",15,"bold"),fg="navy",bg="cadetblue",command=mazza)
c207.grid(row=6,sticky=W)

e207=Entry(L2frame,bd=3,textvariable=e_mazza)
e207.grid(row=6,column=1)

c208=Checkbutton(L2frame,text="Shake",onvalue=1,offvalue=0,variable=var25,
                 font=("arial",15,"bold"),fg="navy",bg="cadetblue",command=shake)
c208.grid(row=7,sticky=W)

e208=Entry(L2frame,bd=3,textvariable=e_shake)
e208.grid(row=7,column=1)

#==============================================================================================

MRframe= Frame(top,bg="navy",bd=10,relief=RIDGE)
MRframe.pack(side = RIGHT)

Rframe= Frame(MRframe,bg="navy",bd=10,relief=RIDGE)
Rframe.pack(side = TOP)

DK=""

def press(num):
    global DK
    DK = DK + str(num)
    equation.set(DK)
    
def equalpress():
    global DK
    total=str(eval(DK))
    equation.set(total)
    DK = ""

def clear():
    global DK
    DK = ""
    equation.set("")

    

equation=StringVar()
ce1=Entry(Rframe,bd="3",textvariable=equation)
ce1.grid(row=0,columnspan=5,ipadx=94,ipady=5)

b11=Button(Rframe,text="1",command=lambda: press(1),
           fg="black",bg="cadetblue",bd="5", height=1,width=7,font="arial 11 bold")
b11.grid(row=1,column=1)

b12=Button(Rframe,text="2",command=lambda: press(2),
           fg="black",bd="5",bg="cadetblue", height=1,width=7,font="arial 11 bold")
b12.grid(row=1,column=2)

b13=Button(Rframe,text="3",command=lambda: press(3),
           fg="black",bd="5", bg="cadetblue",height=1,width=7,font="arial 11 bold")
b13.grid(row=1,column=3)

b31=Button(Rframe,text="+",command=lambda: press("+"),
           fg="black",bd="5", bg="cadetblue",height=1,width=7,font="arial 11 bold")
b31.grid(row=1,column=4)

b14=Button(Rframe,text="4",command=lambda: press(4),
           fg="black",bd="5", bg="cadetblue",height=1,width=7,font="arial 11 bold")
b14.grid(row=2,column=1)

b15=Button(Rframe,text="5",command=lambda: press(5),
           fg="black",bd="5", height=1,width=7,font="arial 11 bold")
b15.grid(row=2,column=2)

b16=Button(Rframe,text="6",command=lambda: press(6),
           fg="black",bd="5", height=1,width=7,font="arial 11 bold")
b16.grid(row=2,column=3)

b32=Button(Rframe,text="-",command=lambda: press("-"),
           fg="black",bd="5", bg="cadetblue",height=1,width=7,font="arial 11 bold")
b32.grid(row=2,column=4)

b17=Button(Rframe,text="7",command=lambda: press(7),
           fg="black",bd="5", bg="cadetblue",height=1,width=7,font="arial 11 bold")
b17.grid(row=3,column=1)

b18=Button(Rframe,text="8",command=lambda: press(8),
           fg="black",bd="5", height=1,width=7,font="arial 11 bold")
b18.grid(row=3,column=2)

b19=Button(Rframe,text="9",command=lambda: press(9),
           fg="black",bd="5", height=1,width=7,font="arial 11 bold")
b19.grid(row=3,column=3)

b33=Button(Rframe,text="*",command=lambda: press("*"),
           fg="black",bd="5", bg="cadetblue",height=1,width=7,font="arial 11 bold")
b33.grid(row=3,column=4)

b20=Button(Rframe,text="0",command=lambda: press(0),
           fg="black",bd="5",bg="cadetblue", height=1,width=7,font="arial 11 bold")
b20.grid(row=4,column=1)

b21=Button(Rframe,text="C",command=clear,
           fg="black",bd="5", bg="cadetblue",height=1,width=7,font="arial 11 bold")
b21.grid(row=4,column=2)

b22=Button(Rframe,text="=",command=equalpress,
           fg="black",bd="5", bg="cadetblue",height=1,width=7,font="arial 11 bold")
b22.grid(row=4,column=3)

b34=Button(Rframe,text="/",command=lambda: press("/"),
           fg="black",bd="5",bg="cadetblue", height=1,width=7,font="arial 11 bold")
b34.grid(row=4,column=4)
#=======================================================================================================

R3frame= Frame(MRframe,bg="navy",bd=10,relief=RIDGE)
R3frame.pack(side = TOP)

textReceipt= Text(R3frame,bd=4,font=('arial',12,'bold'),width=34,height=9,bg='white')
textReceipt.grid(row=0,column=0)

#========================================================================================================

R2frame= Frame(MRframe,bg="navy",bd=10,relief=RIDGE)
R2frame.pack(side = BOTTOM)

b51=Button(R2frame,text="Total",command=totalcost,
           fg="navy",bd="5",bg="cadetblue", height=1,width=5,font=("arial",15,"bold"))
b51.grid(row=1,column=1)

b52=Button(R2frame,text="Receipt",command=receipt,
           fg="navy",bd="5",bg="cadetblue",height=1,width=6,font=("arial",15,"bold"))
b52.grid(row=1,column=2)

b53=Button(R2frame,text="Reset",command=reset,
           fg="navy",bd="5", bg="cadetblue",height=1,width=5,font=("arial",15,"bold"))
b53.grid(row=1,column=3)

b54=Button(R2frame,text="Exit",command=Exit,
           fg="navy",bd="5",bg="cadetblue", height=1,width=5,font=("arial",15,"bold"))
b54.grid(row=1,column=4)

#====================================================================================================

top.mainloop()
