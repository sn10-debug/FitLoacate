
from tkinter import *
import random
import pandas
try:
    data=pandas.read_csv('C:/Users/user/Desktop/javascript/15-Mapty/starter/FlashCard/data/learn.csv')
except FileNotFoundError:
    data=pandas.read_csv('C:/Users/user/Desktop/javascript/15-Mapty/starter/FlashCard/data/french_words.csv')

info={}
French_words=[]
timer=''
num=0
for (index,row) in data.iterrows():
    info[row.French]=row.English
    French_words.append(row.French)

def eng_updater():
    eng=info[word]
    update('English',eng,card_2,'white')


def update(label,word,img,color1):
    
    Canvas1.itemconfigure(Label1,text=label,fill=color1)
    Canvas1.itemconfigure(Label2,text=word,fill=color1)
    Canvas1.itemconfig(canvas_back,image=img)

    
    
def fr_updater():
    global timer,num,word
    
    window.after_cancel(timer)
    word=random.choice(French_words)
    update('French',word,card_1,'black')
    timer=window.after(3000,eng_updater)
    num+=1
    
def ticker():
    global word
    fr_updater()
    French_words.remove(word)
    info1={'French':[],'English':[]}
    for i in French_words:
        info1['French'].append(i)
        info1['English'].append(info[i])
    data_new=pandas.DataFrame(info1)
    # data_new.to_csv('C:/Users/user/Desktop/javascript/15-Mapty/starter/FlashCard/data/learn.csv')
    # We can prevent the index by just writing
    data_new.to_csv('C:/Users/user/Desktop/javascript/15-Mapty/starter/FlashCard/data/learn.csv',index=False)

def crosser():
    fr_updater()








window=Tk()
win_back=PhotoImage(file='C:/Users/user/Desktop/javascript/15-Mapty/starter/FlashCard/images/card_back.png')
window.minsize(height=1000,width=1000)
window.config(padx=50,pady=50,bg='#A3DA8D')

Canvas1=Canvas(height=525,width=800,bg='white',highlightthickness=0)
card_1=PhotoImage(file='C:/Users/user/Desktop/javascript/15-Mapty/starter/FlashCard/images/card_front.png')
card_2=PhotoImage(file='C:/Users/user/Desktop/javascript/15-Mapty/starter/FlashCard/images/card_back.png')
# We need to declare this here because if we declare it in the function it will be lost and we know this window is looping through
canvas_back=Canvas1.create_image(400,262,image=card_1)
Canvas1.config(bg='#A3DA8D')


Label1=Canvas1.create_text(400,150,text='French',font=('Arial',40,'italic'))
word=random.choice(French_words)
Label2=Canvas1.create_text(400,263,text=word,font=('Arial',40,'bold'))
timer=window.after(10*1000,eng_updater)

Canvas1.grid(row=0,column=0,columnspan=3)


cross=PhotoImage(file='C:/Users/user\Desktop/javascript/15-Mapty/starter/FlashCard/images/wrong.png')
tick=PhotoImage(file='C:/Users/user\Desktop/javascript/15-Mapty/starter/FlashCard/images/right.png')

def checker():
    print('hello')
Button1=Button(command=crosser,image=cross,highlightthickness=0,bg='#A3DA8D')
Button1.grid(row=1,column=0)

Button2=Button(command=ticker,image=tick,highlightthickness=0,bg='#A3DA8D')
Button2.grid(row=1,column=2)



window.mainloop()

