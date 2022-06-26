

# from email.mime import image
import smtplib
import pandas
email2='atlantamodel1@gmail.com'
email1='atlantamodel2@yahoo.com'
# connection=smtplib.SMTP('smtp.gmail.com')
# # 'smtp.gmail.com' denotes the location of the gmail smtp server

# # tls means transport layer security

# connection.starttls()
# connection.login(email1,'9321513030')
# connection.sendmail(email1,email2,msg='How are you ?')
# connection.close()
# In this way we sent the email to the another person
# generally mails with no subject are considered as spam

# connection=smtplib.SMTP('smtp.gmail.com')
# connection.starttls()
# connection.login(email1,'9321513030')
# connection.sendmail(email1,email2,msg='Subject:Automate\n\nThis mail is send from computer.')
# connection.close()

# if we dont want to close manually
# with smtplib.SMTP('smtp.gmail.com') as connection:
#     connection.starttls()
#     connection.login(email1,'9321513030')
#     connection.sendmail(email1,email2,msg='Subject:Automate\n\nHey this is Atlanta1.\nWelcome to WorkDone Group')
    
# with smtplib.SMTP('smtp.mail.yahoo.com') as connection:
#     connection.starttls()
#     connection.login(email1,'tgshybypzxuqemuu')
#     connection.sendmail(email1,email2,msg='Subject:Automate\n\nHey this is Atlanta1.\nWelcome to WorkDone Group')

# In yahoo you have to generate an app password for this to work

# Datetime Module
import datetime as din
current_date=din.datetime.now()
print(current_date)
# This returns the current date but it also has some attributes
year=current_date.year
month=current_date.month
date=current_date.day
day=current_date.weekday()

print(year,month,day)
print(type(year),type(month),type(day))

# This prints year month of today
# Here year and month and day are integers
# now it is tuesday it is returning 1 because monday is 0

date1=din.datetime(year=2003,month=1,day=1)
print(date1)
# In this way we created our won date like in javascript

# with open('././starting_letter_1.txt') as file:
#     file.seek(7)
#     print(file.read())
#     print(file.tell())
#     file.seek(0)
#     print(file.read())


# date2=din.datetime()

# with smtplib.SMTP('smtp.mail.yahoo.com') as connection:
#     if day==0:
#         with open('./birthday/quotes.txt') as file:
#             quotes=file.readlines()
#         quote1=random.choice(quotes).split('-')
#         connection.starttls()
#         connection.login('atlantamodel2@yahoo.com','zgrpfjhabjkypnib')
#         connection.sendmail('atlantamodel2@yahoo.com','atlantamodel1@gmail.com',msg=f'Subject:Monday Coffee\n\n{quote1[0]}\n  -{quote1[1]}')

# invitation='''

# Dear [Name],
# Blow out the candles and make a wish! May all your wishes and dreams come true today on your birthday and throughout the year ahead.
# Wishes from,
# Shakti Santosh Nayak
# '''


# data=pandas.read_csv('./birthday/birth_list.csv')
# for (index,row) in data.iterrows():
#     if row.day==date and row.month==month:
#         member=row.Name.split(' ')[0]
#         message1=member.join(invitation.split('[Name]'))
#         with smtplib.SMTP('smtp.gmail.com') as connection:
#             email='atlantamodel1@gmail.com'
#             connection.starttls()
#             connection.login(email,'9321513030')
#             connection.sendmail(email,'atlantamodel2@gmail.com',msg='Subject:Birthday Wish\n\n'+message1)
 



# Making API requests


import requests
# data=requests.get(url='http://api.open-notify.org/iss-now.json')
# This link is called api endpoint that is the location of the external system


# 1XX means hold on
# 2XX means the request was successfull
# 3XX means go away that is we dont have access to the data
# 4XX means you screwed up that is the request for what we are making does not exists
# 5XX means the server is down or something is wrong by the website itself

# if data.status_code==200:
#     print(data.status_code)
#     print(data.json()) 
    # After calling json metthod on the response it will return the dictionary with all the dictionary in it like in javascript in the form of the object
# data.raise_for_status()

# This will raise an exception that is a error if we are unsuccessful at getting the data and when status code is 200 then it will do nothing


# data2=requests.get('https://api.kanye.rest')
# data2.raise_for_status()
# data2=data2.json()['quote']

# from tkinter import *

# window=Tk()
# window.minsize(height=1000,width=1000)
# window.title('Quotes')
# window.config(padx=50,pady=50)

# canvas1=Canvas(height=300,width=800,bg='yellow')
# quote1=canvas1.create_text(400,150,text='',font=('Courier',10,'bold'))

# canvas1.grid(row=0,column=0)

# def change():
#     data2=requests.get('https://api.kanye.rest')
#     data2.raise_for_status()
#     data2=data2.json()['quote']
#     quote=data2.split(' ')
#     new=[]
#     diff=11
#     for i in range(0,len(quote),diff):
#         if i+7<len(quote):
#             new.append(' '.join(quote[i:i+diff]))
#         else:
#             new.append(' '.join(quote[i:len(quote)]))
    




#     canvas1.itemconfigure(quote1,text='\n'.join(new),font=('Courier',15,'bold'))

# next=PhotoImage(file='./Birthday/2x/outline_navigate_next_black_24dp.png')
# Button1=Button(command=change,width=50,image=next)
# Button1.grid(row=1,column=0)

# change()

# window.mainloop()





# API Parameters

# We can get different form of data depending on what input we give






# print(data2)


response1=requests.get(url='http://api.open-notify.org/iss-now.json')

data=response1.json()

print(data)

# parameters={
#     'lat':18.007429,
#     'lng':74.780983,
#     'formatted':0
# }
# response2=requests.get(f"https://api.sunrise-sunset.org/json?lat=18.007429&lng=74.780983&formatted=0")
# response2.raise_for_status()
# data=response2.json()
# print(data)


# response2=requests.get('https://api.coinbase.com/v2/')
# response2.raise_for_status()
# data=response2.json()
# print(data)



