import html
import random
from turtle import width
import requests
from tkinter import *

MAIN_COLOR='#375362'

response=requests.get('https://opentdb.com/api.php?amount=35&type=multiple')
data=response.json()
questions=data['results']
print(len(questions))


num_easy=len([i for i in questions if i['difficulty']=='easy'])
num_moderate=len([i for i in questions if i['difficulty']=='medium'])
num_hard=len([i for i in questions if i['difficulty']=='hard'])
print(num_easy+num_hard+num_moderate)
print(num_easy,num_moderate,num_hard)





class game:
    def __init__(self,questions):
        self.questions=questions
        self.score=0
        self.num=0

    def quest_gen(self):
        '''This will return a question'''
        global num_easy,num_moderate
        if len(self.questions)>0:
            if self.num<num_easy:
                easy_questions=[i for i in self.questions if i['difficulty']=='easy']
                question=random.choice(easy_questions)
                print(num_easy,num_moderate,num_hard)
                print(len(easy_questions))
                

            elif self.num<num_moderate+num_easy:
                moderate_questions=[i for i in self.questions if i['difficulty']=='medium']
                question=random.choice(moderate_questions)
                print(num_easy,num_moderate,num_hard)
              
                print(len(moderate_questions))
            else:
                hard_questions=[i for i in self.questions if i['difficulty']=='hard']
                question=random.choice(hard_questions)
                # print(hard_questions)
                print(num_easy,num_moderate,num_hard)
                print(len(hard_questions))
                
            
            self.questions.remove(question)
            
            self.num+=1
            return question
        else:
            print('Game Over')

            return curr_question
        
    def check(self,question,answer):
        if question["correct_answer"]==answer:
            self.score+=1
            Label1.config(text=f'Score : {self.score}',font=('Courier',15,'bold'))
            return True
        else:
            return False


game1=game(questions)

def ask_question():
    '''This will display a new question on screen'''
    global buttons
    canvas1.config(bg='white')
    if len(game1.questions)>0:
        global curr_question,options
        
        curr_question=game1.quest_gen()
        # print(curr_question)
        print(curr_question)
        Q=html.unescape(curr_question['question'])
        # Html unescape is use to replace the html entities with their real value

        canvas1.itemconfigure(question_disp,text=Q)
        options=[curr_question['correct_answer']]+curr_question['incorrect_answers']
        random.shuffle(options)
        options=[html.unescape(i) for i in options]
        
        for (k,v) in zip(buttons,options):
            k.config(text=quest(v))
    else:
        canvas1.itemconfigure(label1,text='')
        canvas1.itemconfigure(question_disp,text='The Game has come to an end !')
        for k in buttons:
            k.config(text='',state='disabled')
            k.grid_forget()

       


def btn_check(x):
    
    if game1.check(curr_question,x):
        canvas1.config(bg='green')
    else:
        canvas1.config(bg='red')
    window.after(1000,ask_question)

    # While using tkinter we cannot mess up with time
    

def check_1():
    btn_check(options[0])
    
def check_2():
    btn_check(options[1])
   
def check_3():
    btn_check(options[2])

def check_4():
    btn_check(options[3])
 
 



def quest(x):
    question_words=x.split(' ')
    actual_question=[]
    diff=3
    for i in range(0,len(question_words),diff):
        if i+7<len(question_words):
            y=question_words[i:i+diff]
            actual_question.append(' '.join(y)+'\n')
        else:
            y=question_words[i:len(question_words)]
            actual_question.append(' '.join(y)+'\n')
    return ''.join(actual_question)

window=Tk()
window.minsize(height=1000,width=1000)
window.title('Quiz')
window.config(padx=50,pady=100,bg=MAIN_COLOR)
Label1=Label(text='Score : 0',font=('Courier',15,'bold'),bg=MAIN_COLOR,fg='white')
Label1.grid(row=0,column=2)
canvas1=Canvas(height=400,width=700,highlightthickness=0)
label1=canvas1.create_text(200,50,text='Question :',font=('Courier',30,'bold'))

question_disp=canvas1.create_text(350,150,text='',font=('Courier',20,'italic'),fill=MAIN_COLOR,width=600)
canvas1.grid(row=1,column=0,columnspan=2)

Button1=Button(text='Option1',width=40,command=check_1)
Button1.grid(row=2,column=0)
Button2=Button(text='Option2',width=40,command=check_2)
Button2.grid(row=2,column=1)
Button3=Button(text='Option3',width=40,command=check_3)
Button3.grid(row=3,column=0)
Button4=Button(text='Option4',width=40,command=check_4)
Button4.grid(row=3,column=1)

buttons=[Button1,Button2,Button3,Button4]
ask_question()


# API endpoint comes before the question mark and the parameters comes after the question marks and parameters are separated with & 


window.mainloop()




        
