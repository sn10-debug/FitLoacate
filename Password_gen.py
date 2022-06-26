
from tkinter import *
from tkinter import messagebox
from turtle import width
import pyperclip
import json




# Function
def pass_gen():
    import random
    chars=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z']
    up=[]
    for i in chars:
        up.append(i.upper())
    chars.extend(up)
    chars.extend([str(i) for i in range(0,10)])
    chars.extend(['(',')','!','@','#','$','%','&','*'])
    pass1=''
    length=random.randint(10,17)
    for i in range(length):
        pass1+=random.choice(chars)
    Input3.delete(0,END)
    pyperclip.copy(pass1)
    # Copying the password to clipboard
    Input3.insert(END,pass1)    

def search():
    website=Input1.get().title()
    try:
        with open('data_pass.json') as file:
            data=json.load(file)
    except FileNotFoundError:
        print('You have\'nt started storing any data')
    else:

        try:
            data_info=data[website]
        except KeyError:
            messagebox.showinfo(title=website,message=f'You have not stored Credentials for this following website')
        else:
            Email=data_info['Email']
            Password=data_info['Password']
            messagebox.showinfo(title=website,message=f'Email:{Email}\nPassword:{Password}')


def adder():
    # data='|'.join([Input1.get(),Input2.get(),Input3.get()])
    data={
        Input1.get():{
            'Email':Input2.get(),
            'Password':Input3.get()
        }
    }
    
    # here data1 is only a boolean that is true or false when ok true and cancel it is false
    
    
    data1=True
    if Input1.get()=='' or Input2.get()=='' or Input3.get()=='':
        messagebox.showwarning(title='🤥🤥',message='Always try to fill valid information')
        data1=False
    if data1:
        data2=messagebox.askokcancel(title='Confirmation',message=f'Are you sure you want to Add the details ?\n Email:{Input2.get()}\n Password : {Input3.get()}')
        if data2:
            try:
                with open('data_pass.json',mode='r') as file:
                    data_file=json.load(file)
            except FileNotFoundError:
                with open('data_pass.json',mode='w') as file:
                    json.dump(data,file,indent=4)

            else:
                try:
                    if Input1.get() in data_file:
                        data3=data_file[Input1.get()]
                        if not data3==data[Input1.get()]:
                             messagebox.showinfo(title='Update',message=f'Your Data is Successfully updated for the web {Input1.get()} ')
                        else:
                            raise ValueError('The data already exits for this website')

                except ValueError as message_1:
                    messagebox.showinfo(title='Duplicacy',message=message_1) 
                else:
                    with open('data_pass.json',mode='w') as file:
                        data_file.update(data)
                        json.dump(data_file,file,indent=4)

            finally:    
                Input1.focus()
                Input1.delete(0,END)
                Input2.delete(0,END)
                Input2.insert(END,'nshakti.10@gmail.com')
                Input3.delete(0,END)



# UI 
window=Tk()
window.minsize(width=700,height=700)
window.config(padx=50,pady=50,bg='white')
window.title('Password Generator')

Canvas1=Canvas()
Canvas1.config(width=200,height=200)
image=PhotoImage(file='logo_2.png')
Canvas1.create_image(100,100,image=image)
Canvas1.grid(row=0,column=1)
Label_=Label(text='',font=('Aerial',30),bg='white')
Label_.grid(row=1,column=0)
Label1=Label(text='Website:',font=('Courier',10),bg='white')
Label1.grid(row=2,column=0)
Label2=Label(text='Email/Username:',font=('Courier',10),bg='white')
Label2.grid(row=3,column=0)
Label3=Label(text='Password:',font=('Courier',10),bg='white')
Label3.grid(row=4,column=0)
Input1=Entry(width=21)
Input1.focus()
Input1.grid(row=2,column=1)
# Columnspan is used to combine to columns
Button3=Button(text='Search',command=search,bg='white',width=13)
Button3.grid(row=2,column=2)
Input2=Entry(width=35)
Input2.insert(END,'nshakti.10@gmail.com')
Input2.grid(row=3,column=1,columnspan=2)
Input3=Entry(width=21)
Input3.grid(row=4,column=1)
Button1=Button(text='Generate Password',bg='white',command=pass_gen)
Button1.grid(row=4,column=2)
Button2=Button(text='Add',bg='white',width=36,command=adder)
Button2.grid(row=5,column=1,columnspan=2)






window.mainloop()
