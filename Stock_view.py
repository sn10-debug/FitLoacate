from tkinter import *
from NSE_checker import analysis_Stock_exchange
from math import *
stocks_list=['HDFCBANK','ONGC','TRIVENI','TORENTPOWER','RELIANCE']
window=Tk()
Label2=Label(text='Monthly Return :')
Label3=Label(text='Quaterly Return :')
Label4=Label(text='Half Yearly Return :')
Label5=Label(text='Yearly Return :')
Label2.grid(row=0,column=2)
Label3.grid(row=1,column=2)
Label4.grid(row=2,column=2)
Label5.grid(row=3,column=2)
rate1=Label(text=0,bg='white')
rate2=Label(text=0,bg='white')
rate3=Label(text=0,bg='white')
rate4=Label(text=0,bg='white')
rate1.grid(row=0,column=3)
rate2.grid(row=1,column=3)
rate3.grid(row=2,column=3)
rate4.grid(row=3,column=3)


def file_checker():
    stock=Input1.get().upper()
    try:
        if stock in stocks_list:
            
            data=analysis_Stock_exchange(f'C:/Users/user/Desktop/javascript/15-Mapty/starter/Stocks-Data-NSE/Quote-Equity-{stock}-EQ-05-01-2021-to-05-01-2022.csv')
            rate1.config(text=format(data[0],'0.1f')+'%')
            rate2.config(text=format(data[1],'0.1f')+'%')
            rate3.config(text=format(data[2],'0.1f')+'%')
            rate4.config(text=format(data[3],'0.1f')+'%')
        else:
            raise ValueError('The Company does not exists on the Folder')
    except ValueError as error:
        print(error)
            
       


window.title('Stock Viewer')
window.minsize(height=1000,width=1000)
window.config(padx=60,pady=10,bg='white')
canvas1=Canvas(height=400,width=400)
image=PhotoImage(file='C:/Users/user/Desktop/javascript/15-Mapty\starter/Stocks-Data-NSE/img_2.png')
canvas1.create_image(200,200,image=image)
canvas1.grid(row=0,column=1,rowspan=4)
Label1=Label(text='Company Name :',font=('Courier',15,'bold'))
Input1=Entry(width=30)
Label1.grid(row=4,column=0)
Input1.grid(row=4,column=1)
button1=Button(width=30,text='Search',command=file_checker)
button1.grid(row=5,column=1)


















window.mainloop()