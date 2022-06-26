PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1


from tkinter import *
from turtle import fillcolor


# UI

window=Tk()
window.title('Pomodoro')
window.minsize(height=1000,width=1000)
window.config(padx=150,pady=50,bg='#FC997C')
# bg denotes the background colour



# in tkinter also a settimeout like function is available
def call(*a):
    for i in a:
        print(i)

# window.after(10000,call,'a','b','c')
# This will occur after 10 seconds and here also time is in miliseconds
# And this will be only available until the window is open

# the arguements written after the callback function are the arguements of the callback function

# Countdown timer
Minutes=WORK_MIN

Seconds=0
Check_mark=0
num=0
breaking=True
def counter2():
    global Check_mark,Minutes,Seconds,num,breaking
    if not breaking:
        if Minutes==0 and Seconds==0:
            num+=1
            
            
            if num%2==0:
                if num==8:
                    
                    res()
                else:
                    Minutes=WORK_MIN
                    Label1.config(text='Work Time',font=(FONT_NAME,50),bg='#FC997C',fg=GREEN)
                
            else:
                Check_mark+=1
                if Check_mark<=4:
                    Label3.config(text='✓'*Check_mark)
                    if num%7==0:
                        Label1.config(text='Long Break',font=(FONT_NAME,50),bg='#FC997C',fg=RED)
                        Minutes=LONG_BREAK_MIN
                    else:
                        Label1.config(text='Short Break',font=(FONT_NAME,50),bg='#FC997C',fg=PINK)
                        Minutes=SHORT_BREAK_MIN
                    
        if Seconds%60==0:
            Minutes-=1
            Seconds=60

        
        if len(str(Seconds))==1:
            canvas1.itemconfigure(text1,text=f'{Minutes} : 0{Seconds}',font=(FONT_NAME,20,'bold'))
        else:
            canvas1.itemconfigure(text1,text=f'{Minutes} : {Seconds}',font=(FONT_NAME,20,'bold'))
        


        Seconds-=1
        
        window.after(1000,counter2)
def counter():
    # In these way we update a element in the canvas
    global breaking
    breaking=not breaking
    Label1.config(text='Work Time',font=(FONT_NAME,50),bg='#FC997C',fg=GREEN)
    counter2()
def res():
    global Minutes,Seconds,Check_mark,num
    
    Minutes=WORK_MIN
    Seconds=0
    Check_mark=0
    num=0
    Label3.config(text='✓'*Check_mark)
    Label1.config(text='Timer',font=(FONT_NAME,50),bg='#FC997C',fg=GREEN)
    

def reset():
    global breaking
    res()
    breaking=not breaking

    canvas1.itemconfigure(text1,text=f'{WORK_MIN} : 00',font=(FONT_NAME,20,'bold'))






Label1=Label(text='Timer',font=(FONT_NAME,50),bg='#FC997C',fg=GREEN)
Label1.grid(row=0,column=1)

canvas1=Canvas(width=220,height=224,bg='#FFF1AF',highlightthickness=10)


# we can see a border when two different bg colour are applied so to avoid that we use it

image=PhotoImage(file='tomato.png')

# PhotoImage is a class which make a image element out of it like how we use img src in html

canvas1.create_image(120,112,image=image)
text1=canvas1.create_text(120,150,text=f'{WORK_MIN} : 00',font=(FONT_NAME,20,'bold'),fill='white')


# Fill is used to define the color

canvas1.grid(row=1,column=1)
Label2=Label(text='',bg='#FC997C',highlightthickness=0)
Label2.grid(row=2,column=0)

Button1=Button(text='Start',width=20,highlightthickness=10,font=(FONT_NAME),fg=RED,command=counter)

# fg is used to denote the text color
Button1.grid(row=3,column=0)
Button2=Button(text='Reset',width=20,highlightthickness=10,font=(FONT_NAME),fg=RED,command=reset)

Button2.grid(row=3,column=2)
Label3=Label(text='✓'*Check_mark,highlightthickness=0,bg='#FC997C',fg=GREEN,font=(10))
Label3.grid(row=4,column=1)


# Changing the type of data stored in the same variable is called dynamic typing



# We can use window.after_cancel() to cancel any event that was going occur after a certain time interval

window.mainloop()
