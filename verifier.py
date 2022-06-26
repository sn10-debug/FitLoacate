from tkinter import *
import re
import smtplib
import random
from tkinter import font
window=Tk()
window.minsize(height=1000,width=1000)
window.title('Verifier')
window.config(padx=50,pady=50)


# Verification


def name_v(x):
    name=x.split(' ')
    check=True
    for i in name:
        if len(i)<3:
            check=False
            break 
    if len(name)>1 and check:
        return True
    else:
        print('Invalid Name')
        return False

def Add_v(x):
    match1=re.compile('([sS]ector.?(No.|-).*[0-9]{1,2})')
    sector=list(match1.finditer(x))
    # print(sector)
    # print(sector[0].group(1))
    if len(sector)>=1:
        return True
    else:
        return False

def email_v(x):
    if re.match('[A-Za-z.0-9_]+@[A-Za-z]+.(ac)?.?(in|com|edu)',x):
        # print('Valid')
        return True
    else:
        return False
    

Add_v('B-104 Sector No. 8 Kalamboli')
email_v('nshakti.10@gmail.com')


def city_v(x):
    if len(x)>=3:
        return True
    else:
        return False

def verify_otp():
    message1=f'Subject:Order Confirmation\n\nDear {name_user}\nYour Order is confirmed'
    if Otp.get()==otp:
        print('Order Placed')
        Frame2.grid_forget()
        confirmation=Label(text=message1,font=('Courier',20,'bold'))
        confirmation.pack(side='top')
        official_mail='atlantamodel2@yahoo.com'
        with smtplib.SMTP('smtp.mail.yahoo.com') as connection:
        
            connection.starttls()
            connection.login(official_mail,password='zaotoiacxnyulqao')
            connection.sendmail(from_addr=official_mail,to_addrs=email_user,msg=message1)

    else:
        print('Incorrect Otp')

def generate_otp(email,Address,Name,Product):
    global otp,email_user,name_user
    email_user=email
    name_user=Name
    otp=''.join([str(random.randint(0,9)) for _ in range(6)])
    message1=f'Subject:Order Details\n\nYou are among the people who have the great ability to choose a right product.\nThank you {Name} for choosing WorkDone\nProduct Details:{Product}\nProduct will be delivered to \n{Address}\n.To confirm the order,enter the otp on the application. Your otp is {otp}'
    official_mail='atlantamodel2@yahoo.com'
    with smtplib.SMTP('smtp.mail.yahoo.com') as connection:
    
        connection.starttls()
        connection.login(official_mail,password='zaotoiacxnyulqao')
        connection.sendmail(from_addr=official_mail,to_addrs=email,msg=message1)


def verify():
    Address=' '.join(Input2.get('1.0',END).split('\n'))
    Name=Input1.get()
    email=Input4.get()

    
    if name_v(Name) and Add_v(Address) and email_v(email) and city_v(Input3.get()):
        generate_otp(email,Input2.get('1.0',END),Name,Input5.get())
        Frame1.grid_forget()
        Frame2.grid(row=0,column=0)
        
    else:
        Error=Label(Frame1,text='Invalid Information',font=('Courier',20,'bold'))
        Error.grid(row=7,column=2)





# Form

Frame1=Frame()
Title=Label(Frame1,text='WorkDone',font=('Courier',40,'bold'),fg='green')
Name=Label(Frame1,text='Name ',font=('Courier',20,'bold'))
Input1=Entry(Frame1,width=40,font=('Courier',20,'bold'))
Address=Label(Frame1,text='Address ',font=('Courier',20,'bold'))
Input2=Text(Frame1,height=5,width=40,font=('Courier',20,'bold'))
City=Label(Frame1,text='City ',font=('Courier',20,'bold'))
Input3=Entry(Frame1,width=40,font=('Courier',20,'bold'))
Email=Label(Frame1,text='Email ID ',font=('Courier',20,'bold'))
Input4=Entry(Frame1,width=40,font=('Courier',20,'bold'))
Medicine=Label(Frame1,text='Medicine Name ',font=('Courier',20,'bold'))
Input5=Entry(Frame1,width=40,font=('Courier',20,'bold'))
Title.grid(row=0,column=0,columnspan=3)
Name.grid(row=1,column=0)
Input1.grid(row=1,column=2)
Input1.focus()
Address.grid(row=2,column=0)
Input2.grid(row=2,column=2)
City.grid(row=3,column=0)
Input3.grid(row=3,column=2)
Email.grid(row=4,column=0)
Input4.grid(row=4,column=2)
Button1=Button(Frame1,text='Place Order',command=verify,font=('Courier',20,'bold'))
Medicine.grid(row=5,column=0)
Input5.grid(row=5,column=2)
for i in range(1,6):
    word=Label(Frame1,text=' : ',font=('Courier',20,'bold'))
    word.grid(row=i,column=1)
Button1.grid(row=6,column=2)
Frame1.grid(row=0,column=0)

Frame2=Frame()
Title2=Label(Frame2,text='WorkDone',font=('Courier',40,'bold'),fg='green')
Notify=Label(Frame2,text='Check your email id for your otp and to confirm the order enter the otp',font=('Courier',20,'bold'))
Otp=Entry(Frame2,width=40,font=('Courier',20,'bold'))
Button2=Button(Frame2,text='Submit',font=('Courier',20,'bold'),command=verify_otp)
Title2.grid(row=0,column=0)
Notify.grid(row=1,column=0)
Otp.grid(row=2,column=0)
Button2.grid(row=3,column=0)

# Frame1.grid(row=0,column=0)



window.mainloop()
