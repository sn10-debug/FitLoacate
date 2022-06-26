from tkinter import *

MAIN_COLOUR='#FFC600'
window=Tk()
window.minsize(height=1000,width=1000)
window.title('WorkDone')
window.config(padx=50,pady=50,bg=MAIN_COLOUR)
import os
def set1():
    os.environ.__setitem__('hello','hello value')
    # print(os.environ.get('hello'))


from verify_func import verify

import random
import json
class Details:
    def __init__(self,name,email,number):
        self.Name=name
        self.Email_id=email
        self.Phone_Number=number
        self.Address=self.address_gen()
        self.store()

    def address_gen(self):
        letters='a b c d e f g h i j k l m n o p q r s t u v x y z'.split(' ')
        symbols=letters+[i.upper() for i in letters]+[str(i) for i in range(10)]+['$','#']
        address=[random.choice(symbols) for _ in range(12)]
        return ''.join(address)
        
    def store(self):
        data={
                    self.Address:{
                        'Name':self.Name,
                        'Emaid ID':self.Email_id,
                        'Phone Number':self.Phone_Number
                    }
                }
        try:
            with open('user_info.json') as file:
                existing_info=json.load(file)
            
        except FileNotFoundError:
            with open('user_info.json',mode='w') as file:
                json.dump(data,file,indent=4)
        else:
            file=open('user_info.json',mode='w')
            existing_info.update(data)
            json.dump(existing_info,file,indent=4)



def click():
    if verify(Input1.get(),Input4.get(),Input2.get()):
        Details(Input1.get(),Input2.get(),Input4.get())




Label1=Label(text='Name',font=('Courier',20,'bold'),bg=MAIN_COLOUR)
Input1=Entry(width=25,font=('Courier',20,'bold'))
Label1.grid(row=0,column=0)
Input1.grid(row=0,column=2)
Label2=Label(text='Email ID',font=('Courier',20,'bold'),bg=MAIN_COLOUR)
Input2=Entry(width=25,font=('Courier',20,'bold'))
Label2.grid(row=1,column=0)
Input2.grid(row=1,column=2)
Label3=Label(text='Address',font=('Courier',20,'bold'),bg=MAIN_COLOUR)
Input3=Text(width=25,height=5,font=('Courier',20,'bold'))
Label4=Label(text='Phone Number',font=('Courier',20,'bold'),bg=MAIN_COLOUR)
Input4=Entry(width=25,font=('Courier',20,'bold'))
Label3.grid(row=2,column=0)
Input3.grid(row=2,column=2)
Label4.grid(row=3,column=0)
Input4.grid(row=3,column=2)
Labels=[Label1,Label2,Label3,Label4]
for i in Labels:
    i.config(padx=20,pady=20)
for i in range(len(Labels)):
    Labelx=Label(text=' : ',font=('Courier',20,'bold'),bg=MAIN_COLOUR)
    Labelx.grid(row=i,column=1)
Button1=Button(text='Create',font=('Courier',20,'bold'),command=click)
Button1.grid(row=4,column=2)

        
            
        



        
    


window.mainloop()


