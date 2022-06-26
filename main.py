# print('hello')
#     # print('Indentation Error')
# print('hello')
# table=input('What is Your Name ?/n')
# # here input is like prompt in javascript and it is also a synchronous type of code that is blocking type of code that is it blocks the execution of the other blocks of code.
# print('Hello '+table)

# y=input('Dear '+table +" , What is Your Company's Name ?/n")
# print("Your Company's Name is "+y)
# # print('hello')

# print('Your Company is '+input('How Old is your Company ?(Years)/n') +' Years Old')
# # here as the compiler comes on the above line then first it goes through print and then recognizes the first check_statement as a string and then it goes through input and immediately it executes it and as soon as it receives the input ,it returns the input in the code block of the print function and then it gets executed.
# print('The length of Your Name is :')
# print(len(table))

# a=input('a: ')
# b=input('b: ')
# table=a
# a=b
# b=table
# print('Values Interchanged')
# print('a: '+a)
# print('b: '+b)
# here in python also the rules for selecting a variable name is same as it should not start with a number and also there should not be space between the variable name and also the variable name should not be the name of a function.

# print('Welcome To Band Name Generator :')
# name=input("Enter the City's Name in which you Grew : /n ")
# pet_name=input("Enter Your Pet's Name : /n")
# print('Your Band Name can be ' +name+pet_name)
# print('The numbers are:')
# for(i) in range(0,10,2):
#     print(i)
    # here numbers will be printed in the range [0,10) with the difference of 2 and also the format over here is important and after colon that is after declaring the for loop
hello=''
# Boolean(hello)
a=10
b=a
print(id(a))#Here same memory as they are equal
print(id(b))
b=b+2
print(id(b))
A=10
B=10
print(id(A),id(B))
# Though you declared them separartely but they contain the same number so they have the same id.
print(bin(10))
#this is used convert the number into binary form and similarly it can also be used to convert into other formats as well that is hexadecimal and octadecimal
print(hex(10))#16 values 0-9 A,B,C,D,E,F
print(oct(10))#8 values 0-7
# 0x represent as hexadecimal
#0b represented as Binary
#0o represented as octadecimal

#Data Types
# The types of data are String,NUmbers,Boolean and this we have learnt in javascript
# print('Hello'[0])#This will print the first letter of the word and we know the strings are 0 Base.
#Extracting a Particular letter from the word is subscripting

# print('Hello'[-1])
# print(123_456_789);
#As we use to write bigg numbers with commas (',') but here we can use uderscore instead of commas because ',' for python will simply mean that it is separate element as we have learnt in javascript.
#Another data type is float which means number with decimal point.

# 4.14-Float
# len('Shakti') #len() is only made for strings and not for datac types
# len(2345) this is not made for numbers

# word_length=len('Shakti Santosh Nayak');
# print(type(word_length));
# Here type function is used to give the type of variable as 'typeOf' in javascript.
# Input_name_length=len(input('What is Your Name'))
# print('The length of your name is '+str(Input_name_length))
# we need convert the number into string because we know that we cannot do concatanation of string and int

# Total_Bill=int(input('Enter the Total Bill /n'))
# print(Total_Bill)
# num4=input('Enter a Two Digit Number /n');
# print(int(num4[0])+int(num4[1]));

print(type(6/3))#though this is a integer but this appears as a float
# input_Number1=input('Enter a Random Number /n');
# sum=0
# for i in range(0,len(input_Number1)):
#     sum=sum+int(input_Number1[i])

# print(sum)
print(3*(3+3)/3-3)


#Challenge

# height=float(input('Enter Your Height:/n'))
# weight=float(input('Enter Your Weight:/n'))
# print(type(height))
# BMI=round(weight/(height**2))#Here round is used to round off the number as Math.round in javascript
# print(round(weight/(height**2),2))#here we can decide the decimal to how much we want to round off
# print('Your BMI is '+str(BMI) +' kg/m^2')


football_goals=0

football_goals+=1#through these 1 will be directly added to the previous value of football_goals and this is also similar to javascripy
print('Football Goals = ' +str(football_goals))
print(8//3)#here dirrectly it will be converted into a integer and also it's type will be integer not foloat because we know that we get a result as float when we divide two numbers
# print(type(8//3)) int
# print(type(4/2)) float


#Challlenge

# Username=input('Please Enter Your good Name /n');
# Age=int(input('Please Enter your Age /n'))
# Grade=int(input('Please Enter your Grade /n'));#int always expects a decimal value
# print(f'Your Name is {Username} and you are {Age} years old and you are in Grade {Grade}');
# #the above sentence is like template literal which we used in javascrpit that is dynamically using the variable declared in the workspace without converting into a string because we know that incantation of two similar data type takes place


# print(f'You are left with {(90-Age)*365} days , {(90-Age)*52} weeks and {(90-Age)*12} months left if you are expecting that you are going to live 90')

#Tip Calculator

# Total_Bill=float(input('Enter Your Total Bill : $'))
# Percent_Tip=int(input('How much percentage would you like to give as a tip ? 10, 12 or 15 ? '))
# Split=int(input('How Many people to split the Bill ? '))
# Total_Bill+=(Total_Bill*Percent_Tip)/100
# print(f' Each person should pay ${round(Total_Bill/Split,2)}')

# height=int(input('Enter Your Height in cm : '));
# if height>=120:
#     print('You can ride the Rollercoaster.')
#  #here incantation for this code represents that it is under the if block  and if no space is left before then it will come under the if condition code block   
# else :
#     print('You have to grow taller before you ride.')


# num4=int(input('Enter a Number : '));
# if num4%2==0:
#     print('The number you have entered is even')
# else :
#     print('The number you entered is a odd')

# if height>=120 :
#     print('You can ride the rollercoaster')
#     age =int(input('Enter Your Age : '))
#     if age<=12:
#         print('You have to pay $5 for the ride')
#     elif age<=18:
#         print('You have to pay $7 for the ride')
#     else :
#         print('You have to pay $12 for the ride')

# else:
#     print('You have to grow Taller before you ride the rollercoaster')


#BMI 2.0 Coding Challenge

# height=float(input('Enter Your height in m : '));
# weight=float(input('Enter Your Mass in Kg : '));

# BMI=weight/(height**2)
# if BMI<=18.5 :
#     print(f'Your BMI is {round(BMI,2)}, You are UnderWeight.')
# elif BMI<=25 :
#      print(f'Your BMI is {round(BMI,2)}, You have a normal weight')
# elif BMI<=30  :
#     print(f'Your BMI is {round(BMI,2)}, You are slightly overweight')
# elif BMI<=35 :
#     print(f'Your BMI is {round(BMI,2)}, You are obese')
# else :
#     print(f'Your BMI is {round(BMI,2)}, You are clinically overweight')


# To check whether a year is a leap year not (Coding Challenge)

# year=int(input('Enter a Year that has to be checked : '))
# if year%4 == 0:
#     if year%100!=0:
#         print('The year is a Leap Year')
#     else :
#         if year%400==0:
#             print('The Year is a Leap Year')
#         else :
#             print('The year is not a Leap Year')   
# else :
#     print('The year is not a Leap Year')

# bill=0
# if height>=120 :
#     print('You can ride the rollercoaster')
#     age =int(input('Enter Your Age : '))
#     want_Photo=input('Do you want a Photo which captures your Amazing Moment ? Yes or No ? ')
#     if age<=12:
#         print('Chlid has to pay $5 for the ride')
#         bill=5
#     elif age<=18:
#         print('Youths have to pay $7 for the ride')
#         bill=7
#     elif not (age>=45 and age<=55) :
#         print('Adults have to pay $12 for the ride')
#         bill=12
        
#     if want_Photo=='Yes' and not (age>=45 and age<=55) :
#         bill+=3
#         print(f'Your Total Bill is ${bill}')
#     else :
#         print(f'Your Total Bill is ${bill}')    
# else:
#     print('You have to grow Taller before you ride the rollercoaster')

# print(format(22/7,'0.3f'))
# format function is like round function but it returns the number as a string


# Calculate Salary

# Basic_pay=float(input('Enter the Basic Pay : '))
# Salary=Basic_pay+Basic_pay*0.3+Basic_pay*0.8-Basic_pay*0.12
# print('The Salary is ' +str(Salary))

# Cost of settting a Lab

# No_Of_Computers=int(input('Number of Computer Purchased : '))
# Price_Computer=float(input('Price of one Computer : '))
# Price_Table=float(input('Enter the cost for each Table : '))
# Price_Chair=float(input('Enter the cost for each Chair :'))
# Total_cost_Equipment=No_Of_Computers*(Price_Computer+Price_Table+Price_Chair)
# Target_days=float(input('Enter the Number of days alloted for the completion of work : '))
# Hours_Work=float(input('Enter the hours for Labour to work : '))
# Cost_EachLabour=float(input('Enter The cost for each Labour : '))
# total_wage=0
# Hour_perDay=Hours_Work/Target_days
# if Hour_perDay >= 8 :
#     total_wage=No_Of_Computers*(Cost_EachLabour*8+(Cost_EachLabour*0.8)*(Hour_perDay-8))
# else :
#     total_wage=No_Of_Computers*Cost_EachLabour*Hour_perDay

# Total_cost=total_wage+Total_cost_Equipment
# print('The Total Cost for setting up a Lab is ' + str(Total_cost))


# hours=int(input('Enter the number of hours you browsed : '))
# minutes=float()



# s=float(input())
# n=float(input())
# k=int(input())
# t=float(input())
# p=float(input())
# Total_Distance=(4*n*t+ k*3.14*p)
# Total_Distance_km=Total_Distance/1000
# Total_Time=Total_Distance_km/s
# print(Total_Distance_km)
# print(Total_Time)



# print('Welcome to WorkDone Foody')
# Size_Pizza=input('What is the pizza size would you like to Order ? S,M or L ? : ')
# Cheese=input('Do you want to add Extra Cheese ? Y or N ? ')
# pepperoni=input('Do you want to add pepperoni to make your Pizza more Delicious ? Y or N ? ')
# bill=0

# if Size_Pizza=='S' :
#     bill+=15
#     print('Pizza 🍕: $15')

# elif Size_Pizza=='M' :
#     bill+=20
#     print('Pizza 🍕: $20')
# else :
#     bill+=25
#     print('Pizza 🍕: $25')

# if pepperoni=='Y':
#     if Size_Pizza=='S' :
#         bill+=2
#         print('+ pepperoni 🧂: $2 ')
#     else :
#         bill +=3
#         print('+ pepperoni 🧂: $3 ')    

# if Cheese=='Y':
#     bill+=1
#     print('+ Cheese 🧀: $1')

# print(f'Your Total Bill is ${bill}')

# Calculator hate

# name1=input('Enter Your Name : ')
# name2=input("Enter the other one's name : ")
# name1=name1.lower()
# name2=name2.lower()
# # Lower method is used to convert all the letters of the word into lower case
# # And count method is used to count the occurence of the letter in the particular word 
# true_letters=name1.count('t')+name1.count('r')+name1.count('u')+name1.count('e')+name2.count('t')+name2.count('r')+name2.count('u')+name2.count('e')
# hate_letters=name1.count('h')+name1.count('a')+name1.count('t')+name1.count('e')+name2.count('h')+name2.count('a')+name2.count('t')+name2.count('e') 

# score=int(str(true_letters)+str(hate_letters))

# if score <=10 or score>=90 :
#     print(f'Your score is {score}% and You both do not go together like coke and mentos ')
# elif score>=40 and score <=50 :
#     print(f'Your score is {score}% and You both cannot go together ')
# else :
#     print(f'Your score is {score}')

# print('Shakti Nayak'.lower())
# it doesn't matter whether there is a space it is same as javascript


# Treasure Challenge
# print('''                  _                      
#                  (_)                     
#   ___ _ __   __ _ _ _ __   ___  ___ _ __ 
#  / _ / '_ / / _` | | '_ / / _ // _ / '__|
# |  __/ | | | (_| | | | | |  __/  __/ |   
#  /___|_| |_|/__, |_|_| |_|/___|/___|_|   
#              __/ |                       
#             |___/  ''')
# print('''
# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."/` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/_____ /
# *******************************************************************************
# ''')
# print("""        ,,,,,,,,,,---''''---,,,,,,,,,,
#       --''''''''          ````][''''          ''''''''--
#                            _3'''':.
#  _                  .,---------------.
#  //    / _________./  |[__]| o   |J@"//__
#   //==o=========:;    |____|[IL__|''''/_/')
#      /            `'-,._____===/=_____.,-'
#                           /         /     ,
#                          '''''''''''''' 
#                      """)
# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure.") 
# step1=input('You are at a cross road , Where do yu want to go? Type "left" or "right" /n').lower()
# if step1=='left' :
#     step2=input('You come to a lake . There is an island in the middle of the lake. Type "wait" for a boat. Type "swim" to swim across /n' ).lower()
#     if step2=='wait':
#         step3=input('You arrive at the island unharmed. There is a house with 3 doors. One red , one yellow and one blue. Which colour do you choose ? /n').lower()
#         if step3=='red':
#            print('You are Burned By fire . Game Over')
#         elif step3=='yellow':
#             print('You Won')
#         elif step3=='blue':
#             print('You are eaten by the Beasts. Game over')
#         else:
#             print('Game over')       

#     else:
#         print('You are attacked by the Trout . Game Over')    
# else:
#     print('You fell into a hole . Game over')
    

# import random
# # here random is a module which the python team has created and module is a thing which is made for a certain task which means if we have a script which is meant for lot of tasks and it will be complex and to reduce the complexity we break the code into module that is distributing tasks among modules.
# random_integer=random.randint(1,10)

# # here this is used to generate a random number and it will include 1 and 10 that is range will be [1,10]
# print('Random number is : '+str(random_integer))

# sum=0
# for i in range(1,101):
#     sum+=i

# print(sum)
# import module_1
# # also we can make our own module.
# print(module_1.pi)
# print(module_1.h)
# # hence we got data from the other python script.
# # and thus in this way the tasks are divided into module
# # We can also generate a random float with this random module

# random_float=random.random()
# # this will generate a number between 0 and 1 but not exactly 1 and it is same like Math.random() in javascript
# print(format(random_float,'0.4f'))
# print(round(random_float)) #this will just round off the number to the nearest integer and this is not like greatest integer
# random_float2=float(format(random.random()*4,'0.4f'))+1
# print(random_float2)

# Decider=round(random.random())
# if Decider==1 :
#     print('You got a Head')
# else:
#     print('You go a Tail')    

# property=['offices','Server','House']
# # in javascript it is called as a array and it is a data structure that is used to store and similarly in python it is called as lists and it is also a data structure
# print(property)
# print(property[0])#this is totally similar to a array and the data stored in list is also called in this way if we know the index number of property and also it is a Zero base
# print(property[-1])#we can also use a negative index
# # we can also change the data stored in the list directly by using the index and this is similar to the javascript
# property[1]="Server Office"
# property.append('Manufacturing Plant')
# # this method is used to add the data to the end of the list and it is the push which is used in javascript
# # also we can add a list to a list 
# property.extend(['Shops','Complain Centre'])
# property.append(['Abroad Offices','Abroad Service Centres'])
# # there will be a difference in both the methods
# # that is in first method that is 'extend' is used to iterate the list into another list and which we do in javascript by using ...
# # but append simply adds the list to the other list as a independent list that it does not iterate 
# print(property)
# marks=[70,60,100,85,76]
# sum=0
# for i in range(0,len(marks)) :
#     sum+=marks[i]
# print(format(sum/3,'0.4f'))  

# for i in range(6):
#     sum=''
#     for j in range(i+1):
#         sum=(sum)+'#'
#     print(sum)

# Challenge to check the characteristic of a number

# from _typeshed import Self
# import math
# from os import name, pardir, umask
# import random
# import turtle
# from typing import Tuple, Type, final

# Number=int(input('Enter a number : '))
# factors=[]
# sum1=0
# for i in range(1,Number//2+1) :
#     if Number%i==0 :
#         factors.append(i)
# for i in range(len(factors)) :
#     sum1+=factors[i]
# print(sum1)
# print(factors)
# if sum1==Number :
#     print('The entered Number is a perfect Number')
# elif sum1<Number :
#     print('The Number is a decessive Number')
# else :
#     print('The number is a excessive number ')

# power=len(str(Number))
# sum2=0
# for i in range(power) :
#     num4=int(str(Number)[i])
#     sum2+=num4**(power)
# if sum2==Number :
#     print('The number is also a ArmStrong Number')

# Problem 1
# nums=[]
# for i in range(5) :
#     num4=int(input(f'Enter the Number{i+1} : '))
#     nums.append(num4)

# divisor=int(input('Enter the Divisor : '))

# for i in range(len(nums)) :
#     if nums[i]%divisor==0 :
#         print(f'{nums[i]} is divisible by {divisor}')

# Problem 2

# n=int(input('Enter the Number : '))

# factorial1=1

# for i in range(n,0,-1) :
#     factorial1=factorial1*i
# print(factorial1)

# Problem 3
# Number1=int(input('Enter the first Number : '))
# Number2=int(input('Enter the second Number : '))
# operation=input(' div /n multiply /n add /n sub /n ')
# if operation=='div' :
#     print(Number1/Number2)
# elif operation=='multiply' :
#     print(Number1*Number2)
# elif operation=='add' :
#     print(Number1+Number2)
# elif operation=='sub' :
#     print(Number1-Number2)
# else :
#     print('You have entered a wrong operation')  




# Problem 4
# Number=int(input('Enter a Number : '))
# factors=[]
# for i in range(2,Number//2+1) :
#     if Number%i==0 :
#         factors.append(i)

# for i in range(len(factors)):
#     if not factors[i]%2==0 :
#         print(factors[i],end=' , ')
#         # end='' is used so that the print command will not print the another arguement in separate line.

# if len(factors)==0 :
#     print('The number is a prime number and hence no factors other than 1 or itself')
 
# name='shakti'
# name_list=list(name)
# print()
# print(name_list)
# # list is a constructor like new in javascript
# # list() converts the string into a form of array or we can say list in python
# # list is a heterogenous data type like array in javascript because it can store data of any type

# for i in 'shakti' :
#     print(i)
# for i in 'shakti santosh nayak' :
#     print(i)

# #here this will print each character of the word 
# # it can also include a sentence

# list1=list()
# print(list1)
# # this creates a empty list as we already know this is a constructor
# # there are other data structures as well which are called as tuple,sets
# list1.extend(['Workdone','Manufaturing plants','Research Centres',''])
# list2=list1
# list2.remove('')
# print(id(list1))
# print(id(list2))
# print(list1)
# print(list2)
# # from here we come to know that list1 and list2 belong to exact same memory location and if we make changes in list2 the changes will also be reflected in list1 similar to the case in the objects in javascript

# # we can also do slicing over here
# list2.extend(['Best Workplace','Premium and Normal Stores'])
# list3=list2[0:2]
# # this will not take the element of index 2 and this will be always 1 less than the value mentioned in the range with what we are slicing
# print(list3)
# list3=list2[:3]
# # default starting of the range is set as 0
# print(list3)
# print(list3[-1])
# print(list3[1:])
# # here we did not mention the max value of the range so it will by default go from 3 to the last
# # print(list3[:])==print(list3)

# for i in list3 :
#     print(i)
# #this will print all the elements of list3 
# sum=0
# i=1
# while i<=10:
#     sum+=i
#     i+=1
# print(sum)    
# # this is called as while loop
# # if there is no premature break then the else block written will be executed. 

# list4=['Shakti','Santosh','Nayak',18,'CSE-AI','Founder',['Workdone','HealthCare','Manufacturing Sectors','Research Centers'],'']
# list4.remove('')
# # This above function removes the first occurence of the element whichever mentioned inside the list
# list4.insert(4,'B-tech') 
# # this above method is used to insert an element at the particular index we mention
# list4.append('')
# list4.pop(-1)
# print(list4)
# # whatever index we mention here will remove the element at that position or if we dont mention the index it will by default remove the last item which is same as javascript and also it returns the elemnt which it has removed

# list5=[1,6,8,3,0,10,7,19,15]
# list5.sort()
# # this sorts the element in the ascending order and this only mutates the list and does not return it

# list5.reverse()
# # this above function reverses all the elements in the list which means the last element will come at the first position and simulatneously all the elements will arrange themselves
# print(list5)
# list5.clear()
# # this above function removes all the elements in the list and keeps it as an empty list
# print(list5)
# n=int(input())
# sum=''
# m=str(n)
# if len(m)==2 :
#     print(0)
# else:    
#     for i in range(len(m)-2,len(m)):
#          sum=sum+m[i]
#     m=int(sum)
#     print(n%m)

# list6,list7=[1,2,3],['a','b','c']
# print(list6,' list6')
# print(list7,' list7')
# # We can also declare two consecutive lists at same time
# # They are not stored at the same memory location
# list6,list7=list7,list6
# print(list6,' list6')
# print(list7,' list7')
# list8=[1,2,4]
# print(list7<list8)
# # this inequality compares each element with the corresponding index in the another array
# # Also inequality works between the data of same type
# # You can compare list of different length because there is comparison between their elements only

# list9=[1,2,3,4,5,6]
# list10=[1,2,3,76,0,20,213,6,6,2,3]
# for i in list9 :
#     for j in list10:
#         if i==j :
#             print(i)
#             break

# # Here no common element will be repeatitively printed 
# # List follow the property of concatenation that is they can be simply interconnected
# list11=[1,2,3,4,5]
# list12=[6,7,8,9,10]
# print(list11+list12)

# list13=list11*2
# # this above thing will do repetition of the elements in the list twice and put them into a list
# print(list13)
# # We can also check whether the element is present or not
# print(1 in list11)
# # this is replaced by includes in javascript.
# print(list11[1::3])
# # this will give the 2nd and 4th value of the list1 and put into a array or list

# # Dictionary,Tuple are unmutable while list,set are mutable
# print(id(list11))
# list14=list11.copy()

# print(id(list14))
# list14=list11[:]
# print(id(list14))
# # None if them get stored in the same location so changes made in 1 is not reflected in another

# del list14[len(list11)-1]
# # this technique is also used to delete elements of the list
# print(list14)
# print(list11)

# a=5
# b=a
# print(id(a),id(b))
# # Here id comes out to be same 
# b+=5
# print(id(b))
# print(a)
# # But here changes will not be reflected on 'a' because it is just reflected in the lists.
# list15=[1,2,3,4,5]
# list16=[1,2,3,4,5,6]
# print(list15<list16)
# list15==list16 will not be equal which is quite obvious as they contain different elements though there is similarity in them
# the above boolean will be true because rest all the numbers are same and so it may comparing length in this case

# n1=int(input())
# n2=int(input())
# sum=[]
# for i in range(0,3):
#     digit=int(str(n1)[i])+int(str(n2)[i])
#     if len(str(digit))==2 :
#         sum.append(int(str(digit)[1]))
#     else :
#         sum.append(digit)
# sum.reverse()
                
# if sum[0]==0 :
#     sum[0]=9

# sum_new=''

# for i in sum :
#     sum_new+=str(i)
# print(sum_new)    

# Coding Challenge
# import random
# name=input('Enter the Names of the People with the comma between the names /nEx. Angela, Ben, Jenny, Michael, Chloe : /n')
# names=name.split(', ')

# # num4=random.randint(0,len(names)-1)
# # print(f'{names[num4]} is going to buy the meal today')

# # Shortcut
# print(random.choice(names)+' is going to buy the meal today')
# random.choice(table) is used to get a random element from list table
# row1=['⬜','⬜','⬜']
# row2=['⬜','⬜','⬜']
# row3=['⬜','⬜','⬜']
# map=[row1,row2,row3]
# print(f'{row1}/n{row2}/n{row3}')
# markup=(input('Where Do you want to put the Treasure  /nEx. (Column)(row) : '))
# column=int(markup[0])
# row=int(markup[1])
# map[row-1].pop(column-1)
# map[row-1].insert(column-1,' X')

# for i in map :
#     print(i)


# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
# import random
# player1=int(input('What do you choose ? 0 for rock, 1 for paper or 2 for scissors ? '))
# output=[rock, paper,scissors]
# player2=random.choice(output)
# print('/n You : /n /n')
# if player1==0 :
#     print(rock)
#     print('Computer : /n /n')
#     if player2==rock :
#         print(rock)
#         print('There is a Tie')
#     elif player2==paper:
#         print(paper)
#         print('You Lose')
#     else :
#         print(scissors)
#         print('You Win')
# elif player1==1 :
#     print(paper)
#     print('Computer : /n /n')
#     if player2==rock :
#         print(rock)
#         print('You win')
#     elif player2==paper:
#         print(paper)
#         print('There is a tie')
#     else :
#         print(scissors)
#         print('You lose')
# elif player1==2 :
#     print(scissors)
#     print('Computer : /n /n')
#     if player2==rock :
#         print(rock)
#         print('You Lose')
#     elif player2==paper:
#         print(paper)
#         print('You win')
#     else :
#         print(scissors)
#         print('There is a Tie')
# else :
#      print('You have given a invalid input ')       


# num4=str(bin(int(input())))
# m=int(input())-1
# print(num4)

# sum=''
# for i in range(2,len(num4)) :
#     sum+=(num4[i]+',')



# sum=sum.split(',')
# sum=sum[:-1]
# while not len(sum)==10 :
#     sum.insert(0,'0')

# print(sum)
# num4=sum.copy()

# for i in range(m,len(sum)) :
#     num4[i]=sum[i-m];

# for i in range(0,2) :
#     num4[i]='0'
# right_num=num4
# print(num4)
# right_number=0
# for i in range(0,len(num4)):
#     if not int(right_num[i])==0 :
#         right_number+=2**(len(num4)-1-i) 
    


# for i in range(m,len(sum)) :
#     num4[-i-1]=sum[len(num4)-1+m-i];

# for i in range(1,m+1) :
#     num4[-i]=sum[m-i]
# left_num=num4
# left_number=0
# for i in range(0,len(num4)):
#     if not int(left_num[i])==0 :
#         left_number+=2**(len(num4)-1-i) 

# print(num4)

# if int(sum[-(m+1)])==1 : 
#     print(right_number)
# else :
#    print(left_number)



# amount=int(input())
# if amount>=100 and amount<=10000:
#     if (amount%100)==0 :
#           n1=int(amount/2000)
        
        
          
        
#           n2=int((amount-2000*n1)/500)
          
#           n3=(amount-2000*n1-500*n2)//100
#           print((n1))
#           print((n2))
#           print((n3))
        
#     else :
#         print('invalid input')
# else:
#      print('invalid imput')

# Lower_boundary=int(input())
# Upper_boundary=int(input())
# excessive_number=[]
# if Upper_boundary>=12 and Lower_boundary>=12 and Lower_boundary != Upper_boundary :
#        for i in range(Lower_boundary,Upper_boundary+1) :
#            factors=[]
#            sum=0
#            for j in range(2,int(i/2)+1) :
#                if i%j==0 :
#                    factors.append(j)
#            for k in factors :
#                sum+=k
#            if sum > i :
#                excessive_number.append(i) 
#        for i in excessive_number   :
#             print(i)

# elif Lower_boundary==Upper_boundary :
#     print(Lower_boundary)

# else :
#     print('Invalid Input')    


# choice=int(input())


#List Compreshion 
# list17=[table**2 for table in range(0,26)]
# print(list17)

# Total_water=float(input())
# one_forth=Total_water/4
# s1=float(input())
# s2=float(input())
# s3=float(input())
# total_time=10*(s1+s2+2*s3)*one_forth
# print(total_time)
# Challenge
# sum=0
# heights=[180,124,165,173,189,169,146]
# for  i in heights :
#     sum+=i
# print(round(sum/len(heights)))
# Challenge
# scores=[78,65,89,86,55,91,64,89]
# print(max(scores))
# highest_score=0
# for i in scores :
#     if i>highest_score :
#         highest_score=i
# print(highest_score)
# sum=0
# for i in range(1,101):
#     sum+=i
# print(sum)

# sum=0
# for i in range(0,101,2):
#     sum+=i
# print(sum) 

# m=int(input())
# n=int(input())
# team_1=[1]
# team_2=[1]
# sum=1
# while sum<=(31-m) :
#     sum+=m
#     team_1.append(sum)
# sum=1
# while sum<=(31-n) :
#     sum+=n
#     team_2.append(sum)

# common_days=[]

# for i in team_1 :
#     for j in team_2 :
#         if i==j :
#             common_days.append(i)

# print(len(common_days))

# Initial=float(input())
# Rate=float(input())
# n=int(input())
# i=1
# while i <=n :
#     print(f'Bacteria Present at end of {i} hour is {format(Initial*Rate**(i),"0.0f")}')
#     i+=1 


# import math
# number=int(input())
# prime=[]
# for i in range(2,number) :
#     factors=[]
#     for j in range(2,i//2) :
#         if i%j==0 :
#             factors.append(j)
#     if len(factors)==0 :
#         prime.append(i)
# print(prime)
# print(len(prime))

# n1=int(input())
# n2=int(input())
# number1=[i for i in str(n1)]
# number2=[i for i in str(n2)]
# number1.reverse()
# number2.reverse()
# index=[]
# for i in number1 :
#     for j in number2:
#         if i==j and number2.index(j)==number1.index(i) and number2.index(j) not in index :
#             index.append(number1.index(i))
# index.sort()
# print(index)
# for i in index :
#     if 10**i==1 :
#         print(f"Same in {10**i}'s position ")
#     else :
#         print(f"Same in {10**i}th position ")

# n=int(input())
# a=int(input())
# b=int(input())
# numbers=[]
# if n>=a and a>=b :
#     if n==2*a+b:
#         numbers=[a,a,b]
#     elif n==a+2*b:
#         numbers=[a,b,b]
#     if len(numbers)>1:
#         for i in numbers[0:2] :
#                 print(i,end=' ')
#     print(numbers[2])
# else :
#     print('Cannot be written')
# prime=[i for i in range(4,100) if i%6==1 or i%6==5 ]
# prime_new=[2,3]
# prime_new.extend(prime)
# # As we know extend does not returns the modified list
# print(prime_new)


#There is another data structure called tuple 
# tests=((20,30),(35.5,40),(50,60),(100,120),(75.5,80))
# #Tuples is a data structure which cannot be modified or unmutable and tuples are concanatble
# Test_number=int(input())
# Range=int(input())
# if tests[Test_number-1][0]<Range and Range<tests[Test_number-1][1] :
#     print('Reports are normal')
# else : 
#     print('Reports are not normal')
# tests=tests+((70,90),(500,700),)
# print(tests)
# we can add elements into a existing tuple using this method
# a=list(input())
# a=[int(i) for i in a ]
# a=tuple(a)
# K1=4
# K2=10
# b=()
# for i in list(a) :
#     if K1<i<K2 :
#         b=b+(i,)
# for i in list(b)[0:-1] :
#     print(i,end=',')
# print(b[-1])


# chest_numbers=(100,101,102,103,104,105)
# user_chest=int(input())
# for i in chest_numbers :
#     if user_chest==i :
#         print(i)
#         break
# else:
#     print(0)

# array1=[1,3,5,7,7,9]
# k=int(input())
# solutions=[]
# for i in array1 :
#     num1=0
#     num2=0
#     for j in array1[array1.index(i)+1:] :
#         if (i+j)==k :
#             num1=i
#             num2=j
#             if (i,j) not in solutions :
#                 solutions.append((i,j))
#                 break

# for i in solutions :
#     print(i)

# set1={1,2,3,4,5}
# set1.add(6)
# # We can add only one element at a time inside a set and set is imutable that is the elements cannot be changed
# print(set1)
# # set1.add([2,3,45])
# # We cannot add a list and another set and therefore a nested set cannot be formed
# # But we can add a tuple
# set1.add((7,8,9,10))
# print(set1)
# print(len(set1))
# for i in set1 :
#     print(i)
# # Set is iterable
# set2=set([2,3,4,5,])
# print(set2)
# set3=set(('a','b','c','d'))
# print(set3)
# # Here order is not fixed and therefore the elements in the list may appear anyway
# # print(set3[1])
# # set is not subscripitable that its element cannot be called this way
# set4=set(('Shakti',))
# set4.add('Santosh Nayak')
# print(set4)
# tuple1=('hello',)
# print(tuple1)
# # here ',' will be present at the end because if we simply use bracket then it will be taken as simply a string and therefore in order to make a tuple with one element we should use this syntax and also when we print in at last there will be ',' and same reason is valid 
# tuple1=tuple1+('People',)
# # We can't mutate tuple but we can concatanate the tuple and here when we print the tuple the ',' won't appear because now two elements are present
# # tuple can be used to store sensitive data

# print(tuple1)

# for i in range(0,101):
#     if i%15==0 :
#         print('FizzBuzz')
#     elif i%5==0 :
#         print('Buzz')
#     elif i%3==0 :
#         print('Fizz')
#     else:
#         print(i)
# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'table', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?/n")) 
# nr_symbols = int(input(f"How many symbols would you like?/n"))
# nr_numbers = int(input(f"How many numbers would you like?/n"))

# letters=[random.choice(letters) for i in range(0,nr_letters)]
# symbol=[random.choice(symbols) for i in range(0,nr_symbols)]
# numbers=[random.choice(numbers) for i in range(0,nr_numbers)]

# Password=[]
# Password.extend(numbers)
# Password.extend(symbol)
# Password.extend(letters)
# length=len(Password)
# sum=''
# for i in range(0,length) :
#     a=random.choice(Password)
#     sum=sum+a
#     Password.remove(a)
# print(sum)

# # Instead of this we have another method which can be done y using the random.shuffle()
# name=[i for i in 'Shakti'.lower()]
# random.shuffle(name)
# print(name)
# print(abs(-25))
# # abs is used to provide the absolute value of the number

# def print_name(a):
#     print(a)
# # def is used to declare a function
# print_name('Shakti')

# Patient_Details=[]
# def details(name,age,symptoms,days_before):
#     Patient=[name,age,symptoms,days_before]
#     Patient_Details.append(Patient)
# details('XYZ',40,'Fever Cough','7 days')
# details('ABC',47,'Cold','4 days')
# print(Patient_Details)

# n=int(input())
# num2=n
# if 4<n<=1000000000 :
#     for i in range(0,10):
#         num1=i+1
#         num3=0
#         for j in str(num2):
#             num3+=(int(j))**2
#         if num3==4 :
#             print(num1)
#             break
#         num2=num3
#     else :
#         print('No')



# num4=int(input())
# if num4>8:
#     if num4%3==0:
#         print("Only three's")
#     elif num4%5==0:
#         print("Only Five's")
#     else :
#         i=0
#         while num4%3!=0:
#             num4-=5
#             i+=1
#         print(f"{num4//3} Three's and {i} Five's")
# else :
#     print('Invalid Input')

# n=int(input())
# if 0<n<1000000:
#     for i in range(2,n+1):
#         if n==((i*(i-1))//2):
#                 print(i)
#                 break
# name='Shakti Santosh Nayak'
# name[5]=''
# this will not work because assignement does not work similar in tuple and sets

# total=int(input())
# n1=int(input())
# combinations=[]

# for i in range(n1,total-n1,2):
#     for j in range(i+2,total-n1,2) :
#         for k in range(j+2,total-n1,2):
#             if j+k==total-i :
#                 combinations.append([i,j,k])
# if len(combinations)>0:
#     print(len(combinations))
#     for i in combinations:
#         for j in i[0:-1]:
#             print(j,end=' ')
#         print(i[-1])
# else :
#     print('No way')


# numbers1=[i for i in m]
# boo=[]
# if n==int(m):
#     boo.append(False)

# for i in numbers1:
#     for j in numbers1[numbers1.index(i)+1:]:
#         if i==int(j):
#             boo.append(False)
#     else:
#         boo.append(True)
# product=str(n*(int(m)))
# numbers2=[i for i in product]
# for i in numbers2:
#     for j in numbers2[numbers2.index(i)+1:]:
#         if i==int(j):
#             boo.append(False)
#     else:
#         boo.append(True)
# for i in numbers1:
#     for j in numbers2:
#         if i==int(j):
#             boo.append(False)
#     else:
#         boo.append(True)
# for i in numbers2:
#     if int(i)==n:
#         boo.append(False)
# else:
#     boo.append(True)

# for i in boo:
#     if i==False:
#         print('No')
#         break
# else:
#     print('Yes')
# print(boo)

# n=(input())
# m=(input())

# digits=['1','2','3','4','5','6','7','8','9']
# number1=[i for i in n]
# number2=[i for i in m]
# for i in number1:
#     digits.remove(i)
# for i in number2:
#     digits.remove(i)
# number3=[i for i in str(int(n)*int(m))]
# for i in number3:
#     if i in digits:
#         digits.remove(i)
# if len(digits)==0:
#     print('Yes')
# else:
#     print('No')
# print('shakti'*2)
# # shaktishakti
# n=int(input())
# m=int(input())



# sum_initial=10**(n-1)
# sum_final=10**n-1
# print(sum_initial,sum_final)
# numbers=[str(i)+str(i) for i in range(sum_initial,sum_final)]
# num4=[]
# for i in range(2,m+1):
#     for j in numbers:
#         if not int(j)%i==0:
#             break
#     else:
#         print(i)
#         num4.append(i)
# if len(num4)==0:
#     print('No Complete Factors')
# import random
# word_list1=['ardvark','baboon','camel']
# word=random.choice(word_list1)
# guess=input().lower()
# for i in word:
#     if i==guess:
#         print('Right')
#     else:
#         print('Wrong')

# word=input().lower()
# times=[]
# for i in word:
#     num4=0
#     for j in word:
#         if i==j:
#             num4+=1
#     times.append(num4)
# repeat=max(times)
# position=times.index(max(times))+1
# max_letter=word[position-1]
# times[position-1]=''
# nums=[]
# num4=0
# for i in times:
#     num4=num4+1
#     if i==repeat:
#         nums.append(num4-position-1)
        
#         position=num4
# print(max_letter)
# for i in nums:
#     if i==0:
#         print('No characters')
#     else:
#         print(i)


# list1=[8,4,1,6]
# num4=int(input())
# solutions=[]
# for i in list1:
#     for j in list1:
#         if i!=j and i+j==num4:
#             solutions.append([i,j])

# for i in solutions:
#     for j in solutions:
#         if j==i.reverse():
#             solutions.remove(j)
# print(solutions)
# solutions.reverse()
# print(solutions)

# import random
# list1=['tree','baboon','camel']
# word=random.choice(list1)
# print(word)
# blanks=['_']*(len(word))
# print(' '.join(blanks))
# lives=6

# while '_' in blanks:
#     letter=input().lower()
#     for i in range(len(word)):
#       if word[i]==letter:
#             blanks[i]=letter
#     else:
#         lives-=1
#     print(lives)
#     print(' '.join(blanks))
#     if not '_' in blanks:
#         print('You win')
#     if lives==0:
#         print('You Lose')
#         break


# Bill Challenge

# n=int(input())
# Products_info=[]
# Discounts=[]
# t_bill=0
# d_bill=0
# for i in range(n):
#     Item_code=input()
#     Quantity=float(input())
#     Item_price=float(input())
#     Products_info.append([Item_code,Quantity,Item_price])
# for i in range(n):
#     Item_code=input()
#     Discount=float(input())
#     Discounts.append([Item_code,Discount])

# for i in range(n):
#     for j in Discounts:
#         if Products_info[i][0]==j[0]:
#             Product_price=0
#             Product_price=Products_info[i][1]*Products_info[i][2]
#             Discount_price=Product_price*j[1]/100
#             Products_info[i].append(Product_price)
#             Products_info[i].append(Discount_price)
#             break
# for i in Products_info:
#     if len(i)==3:
#         Product_price=i[1]*i[2]
#         i.append(Product_price)
#         i.append(0)
# for i in Products_info:
#     t_bill+=i[-2]
# for i in Products_info:
#     d_bill+=i[-1]
# print(Products_info)
# print(Discounts)
# print(format(t_bill,'0.2f'))
# print(format(d_bill,'0.2f'))
# print(format(t_bill-d_bill,'0.2f'))


# Decoder and Encoder Challenge

# alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','table','y','z']
# def encoder(letter,shift):
#     position=alphabets.index(letter)
#     if shift +position+1>26:
#         new_position=shift+position-26
#         return alphabets[new_position]
#     else:
#         new_position=shift+position
#         return alphabets[new_position]
# def decoder(letter,shift):
#     position=alphabets.index(letter)
#     return alphabets[position-shift]
# Undergoing=True

# while Undergoing:
#     task=input("Type 'encode' to encrypt , type 'decode' to decrypt /n")
#     message=input('Type your message /n')
#     shift=int(input("Type the shift number /n"))
#     sum=''
#     if task=='encode':
#         for i in message:
#             sum+=encoder(i,shift)
#         print(f"Here's encoded result : {sum}")
#     elif task=='decode':
#         for i in message:
#             sum+=decoder(i,shift)
#         print(f"Here's decoded result : {sum}")
    
#     greeting=input("Type 'yes' if you want to go again or otherwise type 'no' /n")
#     if greeting=='no':
#         Undergoing=False


# Maximum Weaving Machine

# a=(input())
# b=(input())
# numbers=[]
# def part1(num1,num2):
#     number=''
#     for i in range(len(num1)):
#         number+=num1[i]
#         number+=num2[i]
#     for i in range(len(num1),len(num2)):
#         number+=num2[i]
#     print(number)
#     numbers.append(int(number))

# if len(b)>len(a):
#     part1(a,b)
#     number=''
#     for i in range(len(a)):
#         number+=b[i]
#         number+=a[i]
#     for i in range(len(a),len(b)):
#         number+=b[i]
#     print(number)
#     numbers.append(int(number))
#     number=''
#     for i in range(1,len(a)+1):
#         number+=a[-i]
#         number+=b[-i]
#     for i in range(len(a)+1,len(b)+1):
#         number+=b[-i]
#     print(number)
#     numbers.append(int(number))
#     number=''
#     for i in range(1,len(a)+1):
#         number+=b[-i]
#         number+=a[-i]
#     for i in range(len(a)+1,len(b)+1):
#         number+=b[-i]
#     print(number)
#     numbers.append(int(number))
# elif len(b)<len(a):
#     number=''
#     for i in range(len(b)):
#         number+=a[i]
#         number+=b[i]
#     for i in range(len(b),len(a)):
#         number+=a[i]
#     print(number)
#     numbers.append(int(number))
#     part1(b,a)
#     number=''
#     for i in range(1,len(b)+1):
#         number+=a[-i]
#         number+=b[-i]
#     for i in range(len(b)+1,len(a)+1):
#         number+=a[-i]
#     print(number)
#     numbers.append(int(number))
#     number=''
#     for i in range(1,len(b)+1):
#         number+=b[-i]
#         number+=a[-i]
#     for i in range(len(b)+1,len(a)+1):
#         number+=a[-i]
#     print(number)
#     numbers.append(int(number))
# else :
#     number=''
#     for i in range(len(a)):
#         number+=a[i]
#         number+=b[i]
#     print(number)
#     numbers.append(int(number))
#     number=''
#     for i in range(len(a)):
#         number+=b[i]
#         number+=a[i]
#     print(number)
#     numbers.append(int(number))
#     number=''
#     for i in range(1,len(a)+1):
#         number+=a[-i]
#         number+=b[-i]
#     print(number)
#     numbers.append(int(number))
#     number=''
#     for i in range(1,len(a)+1):
#         number+=b[-i]
#         number+=a[-i]
#     print(number)
#     numbers.append(int(number))


# print(max(numbers))


# def greet():
#     print('Hello')
#     print('Good Morning')
#     print('Good Afternoon')
#     print('Good Evening')
#     print('Good Night')


# greet()


# def greeting(name,location):
#     # Here name and location are called as parameters which we have already learnt
#     print(f'Hey ! {name}')
#     print(f'What kind of place is {location}')


# greeting('Shakti','Mumbai')
# # This are called as positional arguements
# # Here the order matters
# greeting(location='Mumbai',name='Snigdha')
# # This are called keyword arguements
# # but here the order does not mattters



# Paint Area Calculator
# import math
# height=int(input('Enter the height : /n'))
# width=int(input('Enter the width :  /n'))
# Area_coverage=5
# def number_cans(height,width,coverage):
#     cans=math.ceil((height*width)/coverage)
#     # this provides the next number of the decimal number
#     print(cans)
# number_cans(height=height,width=width,coverage=Area_coverage)



# Prime number Checker


# num4=int(input())
# def Prime_checker(number):
#     if number%6==5 or number%6==1 or number==2 or number==3:
#         print(f"It's a prime number")
#     else:
#         print(f"It's not a prime number")
# Prime_checker(num4)

# s1=input()
# s2=input()
# s1_word=[]
# s2_word=[]
# def word_converter(word,arr):
#     for i in word:
#         if i not in arr:
#             arr.append(i)
# word_converter(s1,s1_word)
# word_converter(s2,s2_word)
# common_letters=[i for i in s1_word if i in s2_word ]
# words=[]
# def crossover(letter):
#     position1=s1_word.index(letter)
#     position2=s2_word.index(letter)
#     prefix1=s1_word[0:position1]
#     suffix1=s2_word[position2+1:]
#     word1=('').join(prefix1+[letter]+suffix1)
#     prefix2=s2_word[0:position2]
#     suffix2=s1_word[position1+1:]
#     word2=('').join(prefix2+[letter]+suffix2)
#     if word1 not in words:
#         words.append(word1)
#     if word2 not in words:
#         words.append(word2)
        

# for i in common_letters:
#     crossover(i)
# words.sort()
# for i in words:
#     print(i,end=' ')


# Enter Medical : M, Marriage: F, Death : D, Sports : S,

# Placement: P,  Network Issue: N,  Travel: T')

#  Death of Family members, Representing sports event and placement interview
# n=int(input())
# Applications=[]
# for i in range(n):
#     id=input()
#     reason=input()
#     Applications.append([id,reason])
# length=len(Applications)
# for i in Applications:
#     if i[1]=='D' or i[1]=='S' or i[1]=='P':
#         print(i[0])
#         Applications.remove(i)
# if len(Applications)==length:
#     print('no eligible students')

# n=int(input())
# Products_info=[]
# Discounts=[]
# t_bill=0
# d_bill=0
# for i in range(n):
#     Item_code=input()
#     Quantity=float(input())
#     Item_price=float(input())
#     Products_info.append([Item_code,Quantity,Item_price])
# for i in range(n):
#     Item_code=input()
#     Discount=float(input())
#     Discounts.append([Item_code,Discount])
# n=int(input())
# Products_info=[]
# t_bill=0
# d_bill=0
# for i in range(n):
#     Item_code=input()
#     Quantity=float(input())
#     Item_price=float(input())
#     Products_info.append([Item_code,Quantity,Item_price])
# for i in range(n):
#     Item_code=input()
#     Discount=float(input())
#     for j in Products_info:
#         if Item_code in j:
#             Product_price=j[1]*j[2]
#             t_bill+=Product_price
#             d_bill+=Product_price*(Discount/100)
#             j.append(Product_price)
# for i in Products_info:
#     if len(i)==3:
#         Product_price=i[1]*i[2]
#         t_bill+=Product_price
#         i.append(Product_price)
# print(Products_info)
# print(format(t_bill,'0.2f'))
# print(format(d_bill,'0.2f'))
# print(format(t_bill-d_bill,'0.2f'))





# Dictionary

dictionary1={
    'shop':'WorkDone Healthy and Convenience Product Stores',
    'Revenue':200000000000000,
}
# the comma at last shows that we can add more elements to the dictionary.
print(dictionary1)
print(dictionary1['shop'])
# A dictionary can be similar to a object in a javascript


# if the key value will not be correct then it will show a error showing 'keyerror'

# We have to write key with its data type if it is a string then we have to write it in the quotation also we can declare key as number and in this case we simply write the number

dictionary1['Loaction']="Mumbai"


#This is the method to add new elements to the dictionary

print(dictionary1) 


# Dictionaries are mutable
print(dictionary1['Revenue'])
dictionary1['Revenue']=20000000000000000
print(dictionary1['Revenue'])

# thus it follow assignment property

for i in dictionary1:
    print(i)

# Here i will be key of each value not the value and so we have to separately get the value

    print(dictionary1[i])

# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }

# student_grades={}

# for i in student_scores:
#     if 91<=student_scores[i]<=100:
#         student_grades[i]='Outstanding'
#     elif 81<=student_scores[i]<=90:
#         student_grades[i]='Exceeds expectations'
#     elif 71<=student_scores[i]<=80:
#         student_grades[i]='Acceptable'
#     elif student_scores[i]<=70:
#         student_grades[i]='Fail'
# print(student_grades)


# We can form a nested list and a nested dictionary
dictionary2={
    'Team1':['Ramesh','Suresh','Rakesh'],
    'Team2':['Sam','Watson','George'],
}
print(dictionary2['Team1'])

Travel_log={
    "France":{
        'cities_visited':['Paris','Lille','Dijon']
    },
    "Germany":{
        'cities_visited':['Berlin','Hamburg','Stuttgart']
    }
}


# Challenge
# import math
# word=input()
# perfect_squares=[]
# for i in range(0,10**len(word)):
#     if math.sqrt(i)==round(math.sqrt(i),1):
#         perfect_squares.append(i)
# max_number=0
# for i in perfect_squares:
#     max_=max(perfect_squares)
#     max_word=f'{max_}'
#     unique=False
#     if len(list(set(list(max_word))))==len(max_word):
#         max_number=max_
#         break
#     else:
#         perfect_squares.remove(max)


# for i in range(len(word)):
#     print(word[i],end=' ')
#     print(f'{max_number}'[i])

# import math
# word=input()
# perfect_squares=[]
# for i in range(10**len(word)-300,10**len(word)):
#     if math.sqrt(i)==round(math.sqrt(i),1):
#         perfect_squares.append(i)
# max_number=0
# for i in perfect_squares:
#     max_=max(perfect_squares)
#     max_word=f'{max_}'
#     unique=False
#     if len(list(set(list(max_word))))==len(max_word):
#         max_number=max_
#         break
#     else:
#         perfect_squares.remove(max_)


# # print(f'{max_number}'[3])
# for i in range(len(word)):
#     print(word[i],end=' ')
#     print(f'{max_number}'[i])
    


# country_data={}
# number_entries=int(input('Enter number of entries : /n'))
# for i in range(number_entries):
#     a=input('Country Name : ')
#     b=input("Country 's Capital :  ")
#     country_data[a]=b

# country_needed=input('Enter the country to know its Capital : ')

# print(country_data[country_needed])



# Challenge -Dictionary


# Phone_directory={
#     'John Walker':[9201900021,1002002012],
#     'Michael John':[9019128021,10020122011],
#     'Michael Andrews':[61892929,10020122011],
#     'Gates Michael':[79100100,10020122011],
# }

# name=input('Enter the name : ')
# for i in Phone_directory:
#     if name in i :
#         print(Phone_directory[i])


# Challenge

# Player_details={
#     'Rohit Sharma':'mi',
#     'MS Dhoni':'csk',
#     'Kieron Pollard':'mi',
#     'Virat Kohli':'rcb',
#     'Yuvraj Singh':'kxip',
#     'Suresh Raina':'csk',
#     'Jasprit Bumrah':'mi',
# }

# Team_name=input()
# Players=[]
# for i in Player_details:
#     if Player_details[i]==Team_name:
#         Players.append(i)

# print(Players)


# Challenge
# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]

# def add_new_country(country,visits,city_visited):

#     dictionary3={}
#     dictionary3['country']=country
#     dictionary3['visits']=visits
#     dictionary3['cities']=city_visited
#     travel_log.append(dictionary3)



# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)




# Project

# level=int(input('Enter Your Diabetes Level : '))





# Diseases={
# 'Diabetes':{
#     'short-acting insulin':{'regular insulin':['Humulin','Novolin']},
#     'rapid-acting insulin':{
#         'insulin aspart':['Novolog','Flexpen','Fiasp'],
#         'insulin glulisine':['Apidra'],
#         'insulin lispro':['Humalog']

# },
# 'Intermediate-acting insulin':{
#     'insulin isophane':['Humulin N', 'Novolin N']
# },
# 'Long-acting insulin':{
# 'insulin degludec':['Tresiba'],
# "insulin detemir":['Levemir'],
# 'insulin glargine':['Lantus'],
# }
# },
# }

# if level<99:
#     print('You dont need medication')
# elif 125<level<130:
#     print(Diseases['Diabetes']['short-acting insulin'])
# else:
#     age=int(input('enter yor age : '))
#     if age<=40:
#         print(Diseases['Diabetes']['rapid-acting insulin'])
#     elif age>40 and age<60:
#         print(Diseases['Diabetes']['Intermediate-acting insulin'])
#     else:
#         print(Diseases['Diabetes']['Long-acting insulin'])
        


# Challenge

# n=int(input())
# numbers=[]
# for i in range(n):
#     num4=float(input())
#     numbers.append(num4)

# Averages=[]
# for i in range(1,n+1):
#     sum=0
#     for j in range(i):
#         sum+=numbers[j]
#     Averages.append(sum/i)

# sum=0
# for i in Averages:
#     sum+=Averages
# print(format(Averages/len(Averages),'0.2f'))


# BlackJack
# import random
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# def get_card():
#     """This function is used to get a random Card out of the deck"""
#     # Docstring👆👆
#     return random.choice(cards)
# def getArr_sum(arr):
#     sum=0
#     for i in arr:
#         sum+=i
#     return sum
# def score_board(player_1,player_2):
#      print(f'Your cards : {player_1} , current score : {getArr_sum(player_1)}')
#      print(f"Computer's First Card : {player_2[0]}")

# def game_starter():
#     player1_card=[]
#     player2_card=[]

#     game_play=input('Do you want to play a game of BlackJack ? Type "y" or "n" ? ')
#     player1_card.append(get_card())
#     player2_card.append(get_card())
#     player1_card.append(get_card())
#     score_board(player1_card,player2_card)
    
    
#     while game_play=='y':
    
#         game_play=input('Type "y" to get another card and "n" to pass ')
#         if game_play=='y':
#             player1_card.append(get_card())
#             score_board(player1_card,player2_card)
#         else:
#             while getArr_sum(player2_card) < 17:
#                 player2_card.append(get_card())
#             print(f'Your final hand : {player1_card}, final score : {getArr_sum(player1_card)}')
#             print(f"Computer's final hand : {player2_card}, final score : {getArr_sum(player2_card)}")
#             if getArr_sum(player2_card)<=21 and getArr_sum(player1_card)<=21:
#                 if 21-getArr_sum(player1_card)<21-getArr_sum(player2_card) and getArr_sum(player1_card)<21 :
#                     print('You won 😃')
#                     while game_play=='n':
#                         game_play=input('Do you want to play a game of BlackJack ? Type "y" or "n" ? ')
#                     player1_card=[]
#                     player2_card=[]
                    
#                     game_starter()
#                 else :
#                     print('You lose 😥')
#                 while game_play=='n':
#                     game_play=input('Do you want to play a game of BlackJack ? Type "y" or "n" ? ')
#                 player1_card=[]
#                 player2_card=[]
                
#                 game_starter()
#             elif getArr_sum(player2_card)>21 and getArr_sum(player1_card)>21:
#                 print('Draw')
#                 while game_play=='n':
#                     game_play=input('Do you want to play a game of BlackJack ? Type "y" or "n" ? ')
#                 player1_card=[]
#                 player2_card=[]
                
#                 game_starter()
#             else:
#                 if getArr_sum(player1_card)<21 and getArr_sum(player2_card)>21:
#                     print('You won 😃')
#                     while game_play=='n':
#                         game_play=input('Do you want to play a game of BlackJack ? Type "y" or "n" ? ')
#                     player1_card=[]
#                     player2_card=[]
                    
#                     game_starter()
#                 else :
#                     print('You lose 😥')
#                     while game_play=='n':
#                         game_play=input('Do you want to play a game of BlackJack ? Type "y" or "n" ? ')
#                     player1_card=[]
#                     player2_card=[]
                    
#                     game_starter()


# game_starter() 


# ECE circuit

# inputs=[[0,0],[0,1],[1,0],[1,1]]
# print('a/tb/tand/tor/tnand/tnor/txor/tnot xor')
# for i in inputs:
#     in_and=i[0] & i[1]
#     in_or=i[0] | i[1]
#     nand=not(in_and)
#     if nand:
#         nand=1
#     else:
#         nand=0
#     nor=not(in_or)
#     if nor:
#         nor=1
#     else:
#         nor=0
    
#     xor=i[0]^i[1]
#     not_xor=not(xor)
#     if not_xor:
#         not_xor=1
#     else:
#         not_xor=0
    
#     print(f'{i[0]}/t{i[1]}/t{in_and}/t{in_or}/t{nand}/t{nor}/t{xor}/t{not_xor}')

# BlackJack 2
# import random
# cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]*(8*52)
# def get_card():
#     """This function is used to get a random Card out of the deck"""
#     # Docstring👆👆
#     card=random.choice(cards)
#     cards.remove(card)
#     return card
# def getArr_sum(arr):
#     # sum=0
#     # for i in arr:
#     #     sum+=i
#     # return sum
#     # Instead we can do this 👇👇
#     return sum(arr)
# def score_board(player_1,player_2):
#      print(f'Your cards : {player_1} , current score : {getArr_sum(player_1)}')
#      print(f"Computer's First Card : {player_2[0]}")
# def check_A(player,card):
#     if card=='A':
#         if getArr_sum(player)+11<=21:
#                 return 11
#         else:
#                 return 1
#     else :
#         return card
# def game_starter():
#     player1_card=[]
#     player2_card=[]

#     game_play=input('Do you want to play a game of BlackJack ? Type "y" or "n" ? ')
#     for i in range(2):
#         player1_card.append(check_A(player1_card,get_card()))
#         player2_card.append(check_A(player2_card,get_card()))
        
#     score_board(player1_card,player2_card)
    
    
#     while game_play=='y':
    
#         game_play=input('Type "y" to get another card and "n" to pass ')
#         if game_play=='y':
    
#             player1_card.append(check_A(player1_card,get_card()))
#             score_board(player1_card,player2_card)
#         else:
#             while getArr_sum(player2_card) < 17:
#                   player2_card.append(check_A(player2_card,get_card()))
#             print(f'Your final hand : {player1_card}, final score : {getArr_sum(player1_card)}')
#             print(f"Computer's final hand : {player2_card}, final score : {getArr_sum(player2_card)}")
#             if getArr_sum(player2_card)<=21 and getArr_sum(player1_card)<=21:
#                 if getArr_sum(player1_card)==21 and getArr_sum(player2_card)!=21:
#                     print('You won')
#                 elif 21-getArr_sum(player1_card)<21-getArr_sum(player2_card) and getArr_sum(player1_card) !=21:
#                     print('You won 😃')
#                 elif getArr_sum(player1_card)==getArr_sum(player2_card):
#                     print('Draw 🎭')
#                 else :
#                     print('You lose 😥')


#                 if game_play=='n':
#                     while game_play=='n':
#                         game_play=input('Do you want to play a game of BlackJack ? Type "y" or "n" ? ')
#                     player1_card=[]
#                     player2_card=[]
#                     game_starter()
            
#             elif getArr_sum(player2_card)>21 or getArr_sum(player1_card)>21:
#                 if getArr_sum(player1_card)<21 and getArr_sum(player2_card)>21 :
#                     print('You won 😃')
#                 elif getArr_sum(player1_card)>21 and getArr_sum(player2_card)<21:
#                     print('You lose 😥')
#                 elif getArr_sum(player1_card)>21 and getArr_sum(player2_card)>21 :
#                     print('You lose')
#                 else :
#                     if getArr_sum(player1_card)==21:
#                         print('You won 😃')
#                     else:
#                         print('You lose 😥')
#                 if game_play=='n':
#                     while game_play=='n':
#                         game_play=input('Do you want to play a game of BlackJack ? Type "y" or "n" ? ')
#                     player1_card=[]
#                     player2_card=[]
#                     game_starter()
            

# game_starter() 



# here a is callled namespace and thus a memer of global scope
# def changer():
#     global a 
#     a+=1
#     print(a)
# We cannot modify the variable declared in global scope unless we declare with global and if global is not used then function will create it as a new variable and its new value will be stored into it and will be different fron the value of the global scope
# a=1
# changer()
# print(a) 

# Thus in this way we modified the variable in the global scope and we should have not able to do this without gloabl keyword.
# here there is no block scope and the variables declared in the block scope can be accessed outside the block scope and only below it which is quite logical.
# def changer2():
#     global b 
#     print(b)
# changer2()


# Rich-Poor



# import random
# cards=[]
# colours=['Red','Red','Black','Black']

# for i in colours:
#     cards=cards+[(j,i) for j in range(1,14)]
# # print(len(cards))
# print(cards)
# def card_distributor():
#     global cards
#     player=[]
#     for i in range(26):
#         card=random.choice(cards)
#         cards.remove(card)
#         player.append(card)
#     return player
    

# def game():
#     player1=card_distributor()
#     player2=card_distributor()
#     Winner=''
    
#     while not len(player1)==0 and not len(player2)==0: 
#         # print(player1)
#         # print(player2)
#         # print(cards)
            
#         Any_win=False
#         cards_played=[]
#         prev_card='  '
#         while not Any_win:
#             player1_approval=input('type "y" to throw the card : ')
#             if player1_approval=='y' :
#                 player1_res=random.choice(player1)
#                 # print(player1_res)
#                 player1.remove(player1_res)
#                 player1_code=player1_res[1]
#                 cards_played.append(player1_res)
#                 if not player1_code==prev_card[1]:
#                     player2_res=random.choice(player2)
#                     # print(player2_res)
#                     player2.remove(player2_res)
#                     player2_code=player2_res[1]
#                     prev_card=player2_res
#                     cards_played.append(player2_res)
#                     print(cards_played)
#                     if player1_code==player2_code:
#                         Any_win=True
#                         player2.extend(cards_played)
#                         cards_played=[]
#                         prev_card='  '
#                         Winner='Player2'
#                 else :
#                     Any_win=True
#                     player1.extend(cards_played)
#                     cards_played=[]
#                     Winner='Player1'
#             print(len(player1))
#             print(len(player2))
            
#         print(f'{Winner} won the set')
#     print(f'{Winner} won the game')
# player_approval=input('Do you want to play the game ? Type "y" to play or else "n" : ')
# if player_approval=='y':
#     game()                 
                

            

# challenge

# def marks_calc(i,j,k):
#     return i*10+j*30+k*50
# students={}
# mark_list=[]
# n=int(input())
# for i in range(n):
#     type_1=int(input())
#     type_2=int(input())
#     type_3=int(input())
#     students[f'student{i+1}']={
#         'total_marks':marks_calc(type_1,type_2,type_3),
#     }
#     mark_list.append(marks_calc(type_1,type_2,type_3))
#     rank=1
# while not len(mark_list)==0:
#     max_marks=max(mark_list)
#     for i in students:
#         if students[i]['total_marks']==max_marks:
#            students[i]['rank']=rank
#     for i in range(mark_list.count(max_marks)):
#         mark_list.remove(max_marks)
#     rank+=1

# for i in range(1,rank):
#     for j in students:
#         rank_=students[i]['rank']
#         if rank_==i:
#             print(f'{rank_}  {i}')


# Challenge



# import sys
# this sys consists of exit method which exits from the whole function
# import re
# check_state_codes=['AN','AP','AR','AS','BH','BR','CH','CG','DD','DL','GA','GJ','HR','HP','JK','JH','KA','KL','LA','LD','MP','MH','MN','ML','MZ','NL','OD','PY','PB','RJ','SK','TN','TS','TR','UP','UK','WB','OR','UA','DN']
# check_states=['Andaman and Nicobar islands','Andhra Pradesh','Arunachal Pradesh','Assam','Bharat(Nationwide)','Bihar','Chandigarh','Chattisgarh','Dadra and Nagar Haveli and Daman and Diu','Delhi','Goa','Gujarat','Haryana','Himachal Pradesh','Jammu and Kashmir','Jharkhand','Karnataka','Kerala','Ladakh','Lakshadweep','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Puducherry','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura','Uttar Pradesh','Uttarakhand','West Bengal','Orissa','Uttaranchal','Dadra and Nagar Haveli']
# check_state_dictionary={k:v for (k,v) in zip(check_state_codes,check_states)}
# number=input('Enter your Vehicle Number : /n').split(' ')
# number=list(map(lambda table: table.upper(),number))

# def number_checker(table):
#     if table[0] not in check_state_codes or table[1]=='00' and table[3]=='0000':
#         return False
#     if re.match('^[A-Z]{2}.[0-9]{1,2}.[A-Z]{1,2}.[0-9]{1,4}',' '.join(table)):
#         return True
#     else:
#         return False
# if number_checker(number):
#      check_state=check_state_dictionary[number[0]]
#      number=' '.join(number) 
#      print(f'The vehicle with number {number} belongs to {check_state}')
# else:
#     print(f'The number {number} is invalid') 


# Challenge
# n=input()
# n=list(map(lambda table : int(table),n.split('  ')))
# n1=list(map(lambda table : int(table),input().split('  ')))
# num4=0
# for i in range(n[1]):
#     if n[0]>n1[0]:
#         n[0]=n[0]+n1[1]
#         num4+=1
#     else:
#         print('No')
#         break
# if num4==n[1]:
#     print('Yes')

    
# countries=['India','USA','Brazil']
# capitals=['Delhi','Washington DC','Brazilia']
# country_capitals={k:v for (k,v) in zip(countries,capitals)}
# print(country_capitals)


# #mapping
# countries=list(map(lambda table: str(countries.index(table)+1)+'. '+table,countries))
# print(countries)


# nums=[1,2,3,4,5]


# #mapping can also be used for tuple


# def sqr(table):
#      return table**2
# nums_squares=tuple(map(sqr,nums))
# print(nums_squares)
# num_squares=set(map(sqr,nums))
# print(num_squares)


# BFT
# BME
# sense
# mechanical


# Regular Expressions

# from _typeshed import Self
from math import atan, atanh, inf, nan, sqrt
import math
from os import stat
import re
import string
import turtle

from numpy import number
from urllib3 import Retry
# from Score import Score1

from game_1 import Game

pattern1=re.compile('^[f]...$')
# This holds the regular expression pattern
word1=pattern1.finditer('fooo')
def printer(table):
    for i in table:
         print(i)
word2=re.compile('.').finditer('shakti')
print(r'/thello')
# r is used to ignore /t ,/n like expressions and this will print as it is without using tab
printer(word1)
printer(word2)

# now to ignore regualar expression's Metacharacter in the pattern we can do it by just using backslash /

word3=re.compile('./.com').finditer('''
Workdone.com
Amazon.com
''')
printer(word3)

word4=re.compile('.').finditer('shakti ')
printer(word4)
# .  means any character except new line
# /d means a digit
# /D means not a digit
# w=[A-Z a-z 0-9 _]
# /w means a character
# /W means not a character
# /s means whitespace(space,tab,new line)
# /S means no whitespace(space,tab,new line)
# /b means word boundary that before the charater provided there should be a space or not alphanumberic value 
# ^ means beginning of a string
# $ means the end of the string
# * means 1 or more occurences of 


word5=re.compile('/d').finditer('nshakti.10@gmail1.com')
printer(word5)
word6=re.compile('/D/d').finditer('nshakti.10@gmail1.com')
printer(word6)
word7=re.compile('/s').finditer('/t Shakti /n/t Santosh /n/t Nayak ')
# here this will consist of all the spaces new line that is /n and tab that is /t
printer(word7)
word8=re.compile('/BS').finditer('/t ShaktiSh /nSantosh /n/t Nayak ')
printer(word8)
word9=re.compile('^Shakti').finditer('Shakti Santosh Nayak')
printer(word9)
word10=re.compile('Naya/d*$').finditer('Shakti Santosh Nayak')
word11=re.compile('Naya/w*$').finditer('Shakti Santosh Nayaks')
word12=re.compile('^.*/w*$').finditer('Shakti Santosh Nayak')

printer(word10)
printer(word11)
printer(word12)


# it is obvious that the iterable word10 and word11 consists of one element only


#Challenge-Registration number checker 

# Programme_codes=['BRS','MIS','BCE','BAI','MAI','MCA','MCB','MCS','MIA','MPC']
# Programs=['B Tech CSE with Robotics','M Tech (Integrated )Software Engineering','B Tech Computer Science and Engineering','B Tech CSE with Artifical Intelligence and Machine Learning','M Tech CSE with Artificial Intelligence and Machine Learning','Master of Computer Application','M Tech CSE with Big Data Analytics','M Tech Computer Science and Engineering','M Tech (Integrated) CSE  with Business Analytics','M Tech CSE with Cyber Physical Systems']
# school=['SCOPE']*(len(Programs))
# information={k:[v,w] for (k,v,w) in zip(Programme_codes,Programs,school)}
# registration_num=input()
# def reg_checker(table):
#     if (table)[2:5] not in Programme_codes:
#         return False
#     if re.match('^[1-2][0-9][A-Z]{3}([1]/d{3}|[5]/d{3})$',table) and table[-4::1]!='1000':
#         return True
#     else:
#         return False

# if reg_checker(registration_num):
#     y=(registration_num)[2:5]
#     program=information[y][0]
#     if registration_num[5]=='1':
#         print('The registration number belongs to Chennai Campus')
#     else:
#         print('The registration number belongs to Vellore Campus')
#     if registration_num[2]=='B':
#         print(f"The student's program type is 'UG'")
#     else:
#         print(f"The student's program type is 'PG'")    
#     print(f'The registration number belongs to school of {information[y][1]}')
#     print(f'The year of joining is 20{registration_num[:2]}')
#     print(f'The registration number belongs to program : {program}')
# else:
#     print('The registration number is invalid')


# Challenge

# n=(input())
# list1=list(n)
# if 1<=int(n)<=10**18:
#     if not 9-int(list1[0])==0 and 9-int(list1[0])<int(list1[0]):
#         list1[0]=str(9-int(list1[0]))
#     for i in range(1,len(n)):
#         if 9-int(list1[i])<int(list1[i]):
#             list1[i]=str(9-int(list1[i]))

# print(('').join(list1))


# Scope

# Global constants

# We usually declare global constants with upper case characters like it is a convention so that we dont further dont declare a new variable in the function

# NAME='Shakti'
# def name():
#     return NAME
# print(name())



# Challenge


# import random
# print('''
#    _____                       _______ _             _____                      
#   / ____|                     |__   __| |           / ____|                     
#  | |  __ _   _  ___  ___ ___     | |  | |__   ___  | |  __  __ _ _ __ ___   ___ 
#  | | |_ | | | |/ _ // __/ __|    | |  | '_ / / _ / | | |_ |/ _` | '_ ` _ / / _ /
#  | |__| | |_| |  __//__ /__ /    | |  | | | |  __/ | |__| | (_| | | | | | |  __/
#   /_____|/__,_|/___||___/___/    |_|  |_| |_|/___|  /_____|/__,_|_| |_| |_|/___|
                                                                                
# ''')
# print('Welcome to Number guessing Game')
# print("I'm thinking of a number between 1 and 100")
# def game():
#     decider=input("Choose Difficulty . Type 'easy' or 'difficult' : ")
#     attempts=0
#     number=random.randint(1,100)
#     # this provides the random number between and including 1 and 100
#     if decider=='easy':
#         attempts=10
#     else:
#         attempts=5
#     print(f'You have {attempts} attempts to guess the number.')
#     while not attempts==0:
#         guess=int(input('Make a guess : '))
#         if guess==number:
#             print('You guessed the correct number')
#             break
#         elif guess>number:
#             attempts-=1
#             if attempts>0:
#                 print('Too high')
#                 print('Guess Again')
#                 print(f'You have {attempts} remaining with you . Try again')
#             else:
#                 print('Too High')
#                 print(f'{number} is the correct answer')
#                 print('You run out of guesses 😥')
#         else:
#             attempts-=1
#             if attempts>0:
#                 print('Too Low')
#                 print('Guess Again')
#                 print(f'You have {attempts} remaining with you . Try again')
#             else:
#                 print('Too Low')
#                 print(f'{number} is the correct answer')
#                 print('You run out of guesses 😥')
#     again='no'
#     while again=='no':
#         again=input("Do you want to play again ? type 'yes' or 'no' ")
#     if again=='yes' :
#         game()

# game()


# Regular Expressions
example1='''
Shakti Santosh Nayak
321-555-4321

123.555.1234

'''
word13=re.compile('/d{3}[-.]/d{3}[-.]/d{4}').finditer(example1)
printer(word13)

details="""


Santosh Nayak
932-151-3030
Mumbai-400053

Reenakhi Santosh Nayak
865-785-0331
Mumbai-400053

Shakti Santosh Nayak
887-975-5640
Mumbai-400053

Snigdha Santosh Nayak
983-357-0957
Mumbai-400053





"""                                                                                
phone_numbers=[]

word14=re.compile('/d{3}./d{3}./d{4}').finditer(details)
# printer(word14)
for i in word14:
    phone_numbers.append(i)
print(phone_numbers)
informations='''
Dave Martin
615-555-7164
173 Main St., Springfield RI 55924
davemartin@bogusemail.com

Charles Harris
800-555-5669
969 High St., Atlantis VA 34075
charlesharris@bogusemail.com

Eric Williams
560-555-5153
806 1st St., Faketown AK 86847
laurawilliams@bogusemail.com

Corey Jefferson
900-555-9340
826 Elm St., Epicburg NE 10671
coreyjefferson@bogusemail.com

Jennifer Martin-White
714-555-7405
212 Cedar St., Sunnydale CT 74983
jenniferwhite@bogusemail.com

Erick Davis
800-555-6771
519 Washington St., Olympus TN 32425
tomdavis@bogusemail.com

Neil Patterson
783-555-4799
625 Oak St., Dawnstar IL 61914
neilpatterson@bogusemail.com

Laura Jefferson
516-555-4615
890 Main St., Pythonville LA 29947
laurajefferson@bogusemail.com

Maria Johnson
127-555-1867
884 High St., Braavos‎ ME 43597
mariajohnson@bogusemail.com

Michael Arnold
608-555-4938
249 Elm St., Quahog OR 90938
michaelarnold@bogusemail.com

Michael Smith
568-555-6051
619 Park St., Winterfell VA 99000
michaelsmith@bogusemail.com

Erik Stuart
292-555-1875
220 Cedar St., Lakeview NY 87282
robertstuart@bogusemail.com

Laura Martin
900-555-3205
391 High St., Smalltown WY 28362
lauramartin@bogusemail.com

Barbara Martin
614-555-1166
121 Hill St., Braavos‎ UT 92474
barbaramartin@bogusemail.com

Linda Jackson
530-555-2676
433 Elm St., Westworld TX 61967
lindajackson@bogusemail.com

Eric Miller
470-555-2750
838 Main St., Balmora MT 56526
stevemiller@bogusemail.com

Dave Arnold
800-555-6089
732 High St., Valyria KY 97152
davearnold@bogusemail.com

Jennifer Jacobs
880-555-8319
217 High St., Old-town IA 82767
jenniferjacobs@bogusemail.com

Neil Wilson
777-555-8378
191 Main St., Mordor IL 72160
neilwilson@bogusemail.com

Kurt Jackson
998-555-7385
607 Washington St., Blackwater NH 97183
kurtjackson@bogusemail.com

Mary Jacobs
800-555-7100
478 Oak St., Bedrock IA 58176
maryjacobs@bogusemail.com

Michael White
903-555-8277
906 Elm St., Mordor TX 89212
michaelwhite@bogusemail.com

Jennifer Jenkins
196-555-5674
949 Main St., Smalltown SC 96962
jenniferjenkins@bogusemail.com

Sam Wright
900-555-5118
835 Pearl St., Smalltown ND 77737
samwright@bogusemail.com

John Davis
905-555-1630
451 Lake St., Bedrock GA 34615
johndavis@bogusemail.com

Eric Davis
203-555-3475
419 Lake St., Balmora OR 30826
neildavis@bogusemail.com

Laura Jackson
884-555-8444
443 Maple St., Quahog MS 29348
laurajackson@bogusemail.com

John Williams
904-555-8559
756 Hill St., Valyria KY 94854
johnwilliams@bogusemail.com

Michael Martin
889-555-7393
216 High St., Olympus NV 21888
michaelmartin@bogusemail.com

Maggie Brown
195-555-2405
806 Lake St., Lakeview MD 59348
maggiebrown@bogusemail.com

Erik Wilson
321-555-9053
354 Hill St., Mordor FL 74122
kurtwilson@bogusemail.com

Elizabeth Arnold
133-555-1711
805 Maple St., Winterfell NV 99431
elizabetharnold@bogusemail.com

Jane Martin
900-555-5428
418 Park St., Metropolis ID 16576
janemartin@bogusemail.com

Travis Johnson
760-555-7147
749 Washington St., Braavos‎ SD 25668
travisjohnson@bogusemail.com

Laura Jefferson
391-555-6621
122 High St., Metropolis ME 29540
laurajefferson@bogusemail.com

Tom Williams
932-555-7724
610 High St., Old-town FL 60758
tomwilliams@bogusemail.com

Jennifer Taylor
609-555-7908
332 Main St., Pythonville OH 78172
jennifertaylor@bogusemail.com

Erick Wright
800-555-8810
858 Hill St., Blackwater NC 79714
jenniferwright@bogusemail.com

Steve Doe
149-555-7657
441 Elm St., Atlantis MS 87195
stevedoe@bogusemail.com

Kurt Davis
130-555-9709
404 Oak St., Atlantis ND 85386
kurtdavis@bogusemail.com

Corey Harris
143-555-9295
286 Pearl St., Vice City TX 57112
coreyharris@bogusemail.com

Nicole Taylor
903-555-9878
465 Hill St., Old-town LA 64102
nicoletaylor@bogusemail.com

Elizabeth Davis
574-555-3194
151 Lake St., Eerie SD 17880
elizabethdavis@bogusemail.com

Maggie Jenkins
496-555-7533
504 Lake St., Gotham PA 46692
maggiejenkins@bogusemail.com

Linda Davis
210-555-3757
201 Pine St., Vice City AR 78455
lindadavis@bogusemail.com

Dave Moore
900-555-9598
251 Pine St., Old-town OK 29087
davemoore@bogusemail.com

Linda Jenkins
866-555-9844
117 High St., Bedrock NE 11899
lindajenkins@bogusemail.com

Eric White
669-555-7159
650 Oak St., Smalltown TN 43281
samwhite@bogusemail.com

Laura Robinson
152-555-7417
377 Pine St., Valyria NC 78036
laurarobinson@bogusemail.com

Charles Patterson
893-555-9832
416 Pearl St., Valyria AK 62260
charlespatterson@bogusemail.com

Joe Jackson
217-555-7123
683 Cedar St., South Park KS 66724
joejackson@bogusemail.com

Michael Johnson
786-555-6544
288 Hill St., Smalltown AZ 18586
michaeljohnson@bogusemail.com

Corey Miller
780-555-2574
286 High St., Springfield IA 16272
coreymiller@bogusemail.com

James Moore
926-555-8735
278 Main St., Gotham KY 89569
jamesmoore@bogusemail.com

Jennifer Stuart
895-555-3539
766 Hill St., King's Landing GA 54999
jenniferstuart@bogusemail.com

Charles Martin
874-555-3949
775 High St., Faketown PA 89260
charlesmartin@bogusemail.com

Eric Wilks
800-555-2420
885 Main St., Blackwater OH 61275
joewilks@bogusemail.com

Elizabeth Arnold
936-555-6340
528 Hill St., Atlantis NH 88289
elizabetharnold@bogusemail.com

John Miller
372-555-9809
117 Cedar St., Thundera NM 75205
johnmiller@bogusemail.com

Corey Jackson
890-555-5618
115 Oak St., Gotham UT 36433
coreyjackson@bogusemail.com

Sam Thomas
670-555-3005
743 Lake St., Springfield MS 25473
samthomas@bogusemail.com

Patricia Thomas
509-555-5997
381 Hill St., Blackwater CT 30958
patriciathomas@bogusemail.com

Jennifer Davis
721-555-5632
125 Main St., Smalltown MT 62155
jenniferdavis@bogusemail.com

Patricia Brown
900-555-3567
292 Hill St., Gotham WV 57680
patriciabrown@bogusemail.com

Barbara Williams
147-555-6830
514 Park St., Balmora NV 55462
barbarawilliams@bogusemail.com

James Taylor
582-555-3426
776 Hill St., Dawnstar MA 51312
jamestaylor@bogusemail.com

Eric Harris
400-555-1706
421 Elm St., Smalltown NV 72025
barbaraharris@bogusemail.com

Travis Anderson
525-555-1793
937 Cedar St., Thundera WA 78862
travisanderson@bogusemail.com

Sam Robinson
317-555-6700
417 Pine St., Lakeview MD 13147
samrobinson@bogusemail.com

Steve Robinson
974-555-8301
478 Park St., Springfield NM 92369
steverobinson@bogusemail.com

Mary Wilson
800-555-3216
708 Maple St., Braavos‎ UT 29551
marywilson@bogusemail.com

Sam Wilson
746-555-4094
557 Pearl St., Westworld KS 23225
samwilson@bogusemail.com

Charles Jones
922-555-1773
855 Hill St., Olympus HI 81427
charlesjones@bogusemail.com

Laura Brown
711-555-4427
980 Maple St., Smalltown MO 96421
laurabrown@bogusemail.com

Tom Harris
355-555-1872
676 Hill St., Blackwater AR 96698
tomharris@bogusemail.com

Patricia Taylor
852-555-6521
588 Pine St., Olympus FL 98412
patriciataylor@bogusemail.com

Barbara Williams
691-555-5773
351 Elm St., Sunnydale GA 26245
barbarawilliams@bogusemail.com

Maggie Johnson
332-555-5441
948 Cedar St., Quahog DE 56449
maggiejohnson@bogusemail.com

Kurt Miller
900-555-7755
381 Hill St., Quahog AL 97503
kurtmiller@bogusemail.com

Neil Stuart
379-555-3685
496 Cedar St., Sunnydale RI 49113
neilstuart@bogusemail.com

Linda Patterson
127-555-9682
736 Cedar St., Lakeview KY 47472
lindapatterson@bogusemail.com

Charles Davis
789-555-7032
678 Lake St., Mordor MN 11845
charlesdavis@bogusemail.com

Jennifer Jefferson
783-555-5135
289 Park St., Sunnydale WA 74526
jenniferjefferson@bogusemail.com

Erick Taylor
315-555-6507
245 Washington St., Bedrock IL 26941
coreytaylor@bogusemail.com

Robert Wilks
481-555-5835
573 Elm St., Sunnydale IL 47182
robertwilks@bogusemail.com

Travis Jackson
365-555-8287
851 Lake St., Metropolis PA 22772
travisjackson@bogusemail.com

Travis Jackson
911-555-7535
489 Oak St., Atlantis HI 73725
travisjackson@bogusemail.com

Laura Wilks
681-555-2460
371 Pearl St., Smalltown SC 47466
laurawilks@bogusemail.com

Neil Arnold
274-555-9800
504 Oak St., Faketown PA 73860
neilarnold@bogusemail.com

Linda Johnson
800-555-1372
667 High St., Balmora IN 82473
lindajohnson@bogusemail.com

Jennifer Wilson
300-555-7821
266 Pine St., Westworld DC 58720
jenniferwilson@bogusemail.com

Nicole White
133-555-3889
276 High St., Braavos‎ IL 57764
nicolewhite@bogusemail.com

Maria Arnold
705-555-6863
491 Elm St., Metropolis PA 31836
mariaarnold@bogusemail.com

Jennifer Davis
215-555-9449
859 Cedar St., Old-town MT 31169
jenniferdavis@bogusemail.com

Mary Patterson
988-555-6112
956 Park St., Valyria CT 81541
marypatterson@bogusemail.com

Jane Stuart
623-555-3006
983 Oak St., Old-town RI 15445
janestuart@bogusemail.com

Robert Davis
192-555-4977
789 Maple St., Mordor IN 22215
robertdavis@bogusemail.com

James Taylor
178-555-4899
439 Hill St., Olympus NV 39308
jamestaylor@bogusemail.com

Eric Stuart
952-555-3089
777 High St., King's Landing AZ 16547
johnstuart@bogusemail.com

Charles Miller
900-555-6426
207 Washington St., Blackwater MA 24886
charlesmiller@bogusemail.com
'''

details_1=list(re.compile('/d{3}[-.]/d{3}[-.]/d{4}').finditer(informations))
details_2=list(re.compile('[A-Za-z]*@bogusemail.com').finditer(informations))
details_3=list(re.compile('[89]00[-.]/d/d/d./d/d/d/d').finditer(informations))
# main_details=[(k,v) for (k,v) in zip(details_1,details_2)]
# print(main_details)
# printer(details_1)
# character set is represeneted by [] that is square brackets and whatever characters we mention in this set and out of this set any of the character is present in the string it will match it.

print('Numbers ....../n/n/n')

print(details_1)
print()
print('Emails....../n/n/n/n')
print(details_2)
print('/n/n/n/n')
print('800 and 900 numbers ....../n/n/n/n/n')
print(details_3)
print('/n/n/n/n/n')
example1='''
Shakti Santosh Nayak
321-555-4321

123.555.1234
800-555-1234
900-555-4321
915-555-1234

'''

word15=list(re.compile('[89]00[-.]/d/d/d./d/d/d/d').finditer(example1))
print(word15)


# [^table] this matches everything not in the character set table

example2='''
pat
mat
bat
aat
Mat
Pat
Rat


Mr. A
Mr. Santosh
Mrs. Reenakhi
Ms Shakti
Ms Snigdha
Mrs. E

'''

# word16=re.compile('[ac-zAC-Z]at').finditer(example2)
# or
word16=re.compile('[^b]at').finditer(example2)
print(list(word16))

# Quantifiers


'''


* - 0 or more occurence
+ - 1 or more occurence
? - 0 or 1
{5} - Exact number
{1,5} - Range of numbers (minimum,maximum)


'''

word17=re.compile('M[rs]{1,2}.*').finditer(example2)
# word18=re.compile('M[rs]{1,2}/.?').finditer(example2)
# or
word18=re.compile('M(r|rs|s)/.?/s[A-Z]/w*').finditer(example2)
# (table|y|z) we give number of patterns and out of them it will match any one pattern 
print(list(word17))
print(list(word18))
# We know we use a backslash to ignore the regular expression's metacharacter and ? denotes that the preceeding charcter can occur 1 time only or not


emails='''
nshakti.10@gmail.com
shaktisantosh.nayak2021@vitstudent.ac.in
santoshn3@rediffmail.com
nreena078@gmail.com
nayaksnigdha60@gmail.com
corey.schafer@university.edu
CoreyMSchafer@gmail.com
corey-321-schafer@my-work.net
'''


email_list=list(re.compile('[A-Za-z0-9.-]+@[A-Za-z-]+/.[A-Za-z]+').finditer(emails))
print(email_list)



# Challenge


# word=list(input())
# new_words=[]
# for i in range(len(word)):
#     y=word[-1:-(i+1):-1]
#     y.reverse()
#     table=y+word[0:(len(word)-i)]
#     new_words.append(('').join(table))
# new_words=list(set(new_words))
# print(len(new_words))


# Higher-Lower Game
# import random
# from game_data import data,logo,vs
# def info_printer(option1,option2):
#     name_A=option1['name']
#     name_B=option2['name']
#     Proff_A=option1['description']
#     Proff_B=option2['description']
#     country_A=option1['country']
#     country_B=option1['country']
#     print(f'Compare A : {name_A} , a {Proff_A} , from {country_A} /n')
#     print(vs)
#     print(f'Against B : {name_B} , a {Proff_B} , from {country_B} /n')

# def compare(option1,option2,num4):
#     score=num4
#     if option1['follower_count']>option2['follower_count']:
#         score+=1
#         print(f'You are right . Current score : {score}')
#         game_over=False
#     else:
#         print(f'Sorry you got a wrong one . Your score is {score} ')
#         game_over=True
#     return score,game_over

# def game():
#     pairs=[]
#     game_over=False
#     score=0
#     while not game_over:
#         if not score==0:
#             print(f'Your current score is {score}') 
#         print(logo)
#         option_A=random.choice(data)
#         option_B=random.choice(data)
#         table=[option_A,option_B]
#         y=table
#         table.reverse()
#         while y or table in pairs:
#             option_B=random.choice(data)
#             table=[option_A,option_B]
#             y=table
#             table.reverse()
#         pairs.append(y)
#         info_printer(option_A,option_B)
#         guess=input("Who has more followers . Type 'A' or 'B' : ")
#         if guess=='A':
#             tuple1=compare(option_A,option_B,score)
#             score=tuple1[0]
#             game_over=tuple1[1]
#         else:
#             tuple1=compare(option_B,option_A,score)
#             score=tuple1[0]
#             game_over=tuple1[1]
        
# game()



# Higher Lower Game

# import random
# from game_data import data,logo,vs

# def info_printer(option1,option2):
#     name_A=option1['name']
#     name_B=option2['name']
#     Proff_A=option1['description']
#     Proff_B=option2['description']
#     country_A=option1['country']
#     country_B=option2['country']
#     print(f'Compare A : {name_A} , a {Proff_A} , from {country_A} /n')
#     print(vs)
#     print(f'Against B : {name_B} , a {Proff_B} , from {country_B} /n')

# def compare(option1,option2,num4):
#     score=num4
#     if option1['follower_count']>option2['follower_count']:
#         score+=1
#         print(f'You are right . Current score : {score}')
#         game_over=False
#     else:
#         print(f'Sorry you got a wrong one . Your score is {score} ')
#         game_over=True
#     return score,game_over

# def game():
#     pairs=[]
#     game_over=False
#     score=0

#     option_A=random.choice(data)
#     previous=option_A
#     while not game_over:
#         if not score==0:
#             print(f'Your current score is {score}') 
#         print(logo)
#         option_A=previous
#         option_B=random.choice(data)
#         while option_A==option_B:
#            option_B=random.choice(data)
#         table=[option_A,option_B]
#         y=table
#         table.reverse()
#         check=True
#         while check:
            
#             if  y in pairs or table in pairs:
                
#                 option_B=random.choice(data)
#                 table=[option_A,option_B]
#                 y=table
#                 table.reverse()
#             else:
#                 check=False
#         pairs.append(y)
#         info_printer(option_A,option_B)
#         guess=input("Who has more followers . Type 'A' or 'B' : ")
#         if guess=='A':
#             tuple1=compare(option_A,option_B,score)
#             score=tuple1[0]
#             game_over=tuple1[1]
#             previous=option_A
            
#         else:
#             tuple1=compare(option_B,option_A,score)
#             score=tuple1[0]
#             game_over=tuple1[1]
#             previous=option_B
        
        
# game()


# Challenge= Coffee Machine Program

# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "coffee": 18,
#             "milk":0
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }

# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
# }

# Coffee_work=True
# def check_resources(table):
#     if table["water"]<=resources['water'] and table["milk"]<=resources['milk'] and table["coffee"]<=resources['coffee']:
        
#         return True
#     else:
#         return False 
# def resource_deductor(table):
#     resources['water']=resources['water']-table['water']
#     resources['milk']=resources['milk']-table['milk']
#     resources['coffee']=resources['coffee']-table['coffee']
   
# def coin_checker(q,d,n,p,cost):
#     total=q*0.25+d*0.1+n*0.05+p*0.01
#     if total>cost:
#         return True
#     else:
#         return False
# def change_calculator(q,d,n,p,cost):
#     total=q*0.25+d*0.1+n*0.05+p*0.01
#     return format(total-cost,'0.2f')


# def report_display():
#     for i in resources:
#         print(f'{i} : {resources[i]}')
# flavours=['espresso','latte','cappuccino']
# def coffeeMaker():
#     global Coffee_work
#     user_input=input('What would you like? (espresso/latte/cappuccino): ')
#     if user_input=='report':
#         report_display()
#     elif user_input=='off':
        
#         Coffee_work=False
#         print('The Machine has turned off for maintainence')
#         return
#     elif user_input in flavours:
#         if check_resources(MENU[user_input]['ingredients']):
#             quarters=int(input('How many quarters :'))
#             dimes=int(input('How many dimes :'))
#             nickels=int(input('How many nickels :'))
#             pennies=int(input('How many pennies :'))
#             cost=MENU[user_input]["cost"]
#             if coin_checker(quarters,dimes,nickels,pennies,cost):
#                 resource_deductor(MENU[user_input]['ingredients'])
#                 change=change_calculator(quarters,dimes,nickels,pennies,cost)
#                 print(f'here is your change ${change}')
#                 print(f'Enjoy your {user_input} ☕')
#             else:
#                 print(f'Insufficient Money')    


#         else:
#             print('Sufficient Resources not available')


# while Coffee_work:
#     coffeeMaker()



# Regular Expression

# urls = '''
# https://www.google.com
# http://coreyms.com
# https://youtube.com
# https://www.nasa.gov
# '''

# pattern2=re.compile('(https|http):[/]{2}(www.)?(/w+)(/./w+)')

# word19=pattern2.finditer(urls)

# #If we put parenthesis in the pattern then the particular string is divided into different groups. always the 0th group will be the entire url but after that other groups will hold position respectively
# #  (https|http):[/]{2}(www.)?(/w+)(/./w+) As here the 3rd part is (/w+) and therefore we used .group(3)


# for i in word19:
#     print(i.group(3))



# names='''
# Santosh Kumar Nayak
# Rennakhi Santosh Nayak
# Shakti Santosh Nayak
# Snigdha Santosh Nayak
# '''

# word20=re.compile('/w+/s/w*/s(/w+)').finditer(names)
# for i in word20:
#     print(i)


# for i in re.compile('(/w+)/.(com|gov)').finditer(urls):
#     print(i.group(1))

# # If we want to get a string directly just consisting of the thing what we wanted always using the python we can have it

# pattern3=re.compile('(/w+)/.(com|gov)')
# word21=pattern3.finditer(urls)
# for i in word21:
#     print(i)

# from turtle import Turtle,Screen

# object1=Turtle()
# object2=Turtle()
# object1.shape_right('turtle')
# print(turtle.position())
# object1.color('pink','green')
# object1.forward(100)
# position=list(map(lambda table:format(table,'0.0f'),list(object1.position())))
# print(position)
# object1.right(90)
# object1.backward(100)
# print(object1.position())
# object1.left(180)
# object2.shape_right('turtle')
# print(object1)
# monitor=Screen()
# print(monitor.canvheight)
# object1.forward(100)
# # Here monitor is the object and the canvheight is the attribute and also object1 is the object but the Turtle is a class which we have already learnt in javascript
# print(object1.position())
# monitor.exitonclick()
# # print()

# import prettytable
# table=prettytable.PrettyTable()
# table.add_column('SR.NO',['1','2','3','4','5'])
# table.add_column('Subject'.title(),['Python','Maths','ECE','Physics','STS'])
# print('Centered Text /n')
# print(table,'/n')


# # Modifying the attribute of the object which is quite logical

# table.align='l'
# table.junction_char='s'

# print('Text towards the Right /n ')
# print(table)

# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "coffee": 18,
#             "milk":0
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }


# OOP

# Class declaration

# class medicine:
#     pass
# We use pass when we dont want anything in that class and if we simply leave it empty without writing pass then it will show identation error and to skip that we use pass and also with we can also create a empty function

# def geneartor():
#     pass

# Disease1=medicine()
# Disease1.type='Diabetes'
# Disease1.tenure='LifeLong'
# print(Disease1.type)

class Medicine:
    # Whenever a new object is created out of this class then __init__ function is triggered that is executed and this function is used to intialize the class that is create the early attributes and it is same like the constructor we used in javascript
    
    def __init__(self,disease,type,ageGroup,price):
        print('A new Medicine is added')
        
        # here self reperesents the new object being created like 'this' keyword in case of javascript 
        
        
        self.disease=disease
        self.type=type
        self.age_section=ageGroup
        self.price=price
        self.orders=0

        # In this way we create attributes in a class while creation of the object itself but in another way we can also do by assigning each attribute manually for every object and obviously that is a very long process

        # Here whatever number of parameters asked have to be declared then only new object will be created which is quite logical because __init__ is a function which demands every parameter.

        # Declaring functions or methods

    def take_order(self,num4):
        self.orders+=num4    


Paracetaemol=Medicine('Fever','Generic','Above 14',30)
print(Paracetaemol.age_section)
print(Paracetaemol.orders)
Paracetaemol.take_order(20)
print(Paracetaemol.orders)

# class StoreDetails:
#     def __init__(self,store_name,store_owner,medicine_types,ratings,address):
#         self.StoreName=store_name
#         self.Owner=store_owner
#         self.MedicineTypes=medicine_types
#         self.Ratings=ratings
#         self.Address=address
#         self.orders=0

# Store1=StoreDetails('Workdone','WorkDone Limited','All',5,'Mumbai')
# print(Store1.Owner)
# print(Store1.Address)


class workdone_mini:
    def __init__(self,head,address,target,reach):
        self.director=head
        self.Address=address
        self.target=target
        self.reach=reach

Workdone_1=workdone_mini('abc','Mumbai',['tier-1','tier-2'],['Andheri','CSMT','Bandra','Goregaon'])
Workdone_2=workdone_mini('xyz','Navi Mumbai',['tier-1','tier-2'],['Vashi','Kharghar','Sanpada','Seawoods','Belapur','Kalamboli','Panvel'])
Workdone_3=workdone_mini('pqr','Navi Mumbai',['tier-3'],['Vashi','Kharghar','Sanpada','Seawoods','Belapur','Panvel','Kalamboli'])
branches=[Workdone_1,Workdone_2,Workdone_3]
Products=['Convinience','Medicine','Fitness Gym','Indian Food']
class Store:
    def __init__(self,name,city,owner,product,product_type,address,target):
        for i in branches:
            if city.title() in i.reach :
                
                break
        else:
            print('We do not serve at this location')
            self.status=False
            return
        if not product in Products:
            self.status='Invalid'
            return
        self.StoreName=name
        self.City=city.title()
        self.Owner=owner
        self.Product=product
        self.Product_type=product_type
        self.Address=address
        self.target='tier-2'
        self.Incharge=self.find_branch(city.title(),target)
        self.status=True
        
    def find_branch(self,city,target):
        city_deps=None
        for i in branches:
            if city in i.reach and target in i.target:
                city_deps=i
        return city_deps
        
     

Store1=Store('Satyakunj','kalamboli','Ramesh Desai','Medicine','Branded','Sector-11','tier-3')

     
if Store1.status :
    print(Store1.Incharge.director) 
else:
    print('Store not validating our conditions')      


# Challenge



# n=int(input())
# dimensions=[]
# for i in range(n):
#     element=[]
#     for i in range(n):
#         element.append(int(input()))
#     dimensions.append(element)
# # print(dimensions)
# swap_elements=[]
# for i in range(n):
#     if i==0 :
#         for j in dimensions[0]:
#             swap_elements.append(j)
#     elif i==n-1:
#         elements=[]
#         for j in dimensions[n-1]:
#             elements.append(j)
#         elements.reverse()
#         swap_elements.extend(elements)
#     else:
#         swap_elements.append(dimensions[i][-1])
# for i in range(n-2,0,-1):
#     swap_elements.append(dimensions[i][0])
# # print(swap_elements)
# for i in range(0,len(swap_elements),2):
#     x=swap_elements[i]
#     swap_elements[i]=swap_elements[i+2]
#     swap_elements[i+2]=x
# print(swap_elements)
# num4=0
# for i in range(n):
#     if i==0:
#         for j in range(n):
#             dimensions[0][j]=swap_elements[num4]
#             num4+=1
#     elif i==n-1:
#         elements=[]
#         for j in range(n):
#             elements.append(swap_elements[num4])
#             num4+=1
#         elements.reverse()
#         dimensions[i]=elements
#     else:
#         dimensions[i][-1]=swap_elements[num4]
#         num4+=1
# for i in range(n-2,0,-1):
#     dimensions[i][0]=swap_elements[num4]
#     num4+=1
# for i in dimensions:
#     for j in range(n-1):
#         print(i[j],end='/t')
#     print(i[-1])
        

#Challenge

import random

Lost=False
Score=0


question_data = [
{"text": "A slug's blood is green.", "answer": "True"},
{"text": "The loudest animal is the African Elephant.", "answer": "False"},
{"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
{"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
{"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
{"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a check_state funeral.", "answer": "False"},
{"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
{"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
{"text": "Google was originally called 'Backrub'.", "answer": "True"},
{"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
{"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
{"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]

class question:
    def __init__(self,questions_data) :
        self.Data=questions_data
    
    def question_checker(self,question,response):
        global Score,Lost
        main_question=question
        if main_question['answer']==response:
            Score+=1
            print(f'You are Correct. Your score is {Score}')
            return True
        else:
            print(f'You are wrong. Your score is {Score}')
            Lost=True
            return False

Questionaire=question(question_data)

def game():
    global Score,Lost
    picker=random.choice(Questionaire.Data)
    quiz_question=picker['text']
    response=input(f'{quiz_question} . True or False : ')
    Questionaire.question_checker(picker,response)
    
# while not Lost:
#     game()

class question1:
    def __init__(self,text,answer):
        self.question=text
        self.answer=answer
questions_set=[]
for i in question_data:
    x=question1(i['text'],i['answer'])
    questions_set.append(x)
        

# print(list(map(lambda x:(x.question,x.answer),questions_set)))


# list1=[]
# n=int(input())
# lab_reports=()
# for i in range(n):
#     list1.clear()
#     list1=[int(input()) for _ in range(3)]
#     if list1[0]<=list1[2] and list1[2]<=list1[1]:
#         list1.append('Normal')
#     else:
#         list1.append('Abnormal')
#     lab_reports+=(list1.copy(),)
    

# for i in lab_reports:
#     print(i[0])
#     print(i[1])
#     print(i[2])
#     print(i[3])


from game_1 import Game,KBC


Game1=Game(question_data)
x=0
# while not x==len(question_data):
#     Game1.ask()
#     x+=1
# print(f'Your final score is {Game1.score}/{len(question_data)}')
    

# book_list=(('Harry Potter',250,500),('Alexander',100,500))

# book_name=input()
# copy=int(input())
# for i in book_list:
#     if book_name in i:

#         if i[1]>=copy:
#             print(f'Bill is {copy*i[2]}')
#             break
#         else:
#             print('Insufficient Stock')
#             break
# else:
#     print('Stock is not available')

    
        
# KBC


from questions_set_trivia import questions

Game2=KBC(questions)

# Game2.start_game()


from turtle import Turtle,Screen, distance, forward, mode, position, turtles, update, width, window_height, ycor

# Atlanta=Turtle()
# # Atlanta.forward(102)
# # Atlanta.pen()
# Atlanta.fillcolor('black')
# Atlanta.shape('turtle')
# # Atlanta.shape_right('square')

# Atlanta.color('green','white')
# def circle_maker():
#     Atlanta.begin_fill()
#     Atlanta.circle(30)
#     Atlanta.end_fill()
#     Atlanta.dot(20,'Red')
#     Atlanta.forward(60)

# def circle(x):
#     for _ in range(x):
#         circle_maker()
#     Atlanta.backward(2*x*60)
#     for _ in range(x):
#         circle_maker()
        

# # circle(2)


# def square():
#     for _ in range(4):
#         Atlanta.forward(100)
#         Atlanta.left(90)
        
# # Atlanta.forward(220)
# # square()
# def human():
#     Atlanta.left(90)
#     Atlanta.right(45)
#     Atlanta.forward(100)
#     Atlanta.home()
#     Atlanta.left(90)
#     Atlanta.left(45)
#     Atlanta.forward(100)
#     Atlanta.home()
#     Atlanta.left(90)
#     Atlanta.forward(150)
#     Atlanta.right(90)
#     Atlanta.circle(25)
#     Atlanta.home()
#     Atlanta.right(90)
#     Atlanta.forward(150)
#     Atlanta.left(45)
#     Atlanta.forward(100)
#     Atlanta.backward(100)
#     Atlanta.right(90)
#     Atlanta.forward(100)
#     Atlanta.backward(100)
#     Atlanta.home()




# # from turtle import *

# # This line of code will import everything like the variables in it or more specifically attributes as importing the module will give a object which is quite logical and also the methods in it and now we can directly call the variables or methods which show like it is present in our global scope.


# # import turtle as t
# # Here just we are getting the module with our name whereas initially the object is used to be stored in the name which the module had but sometimes when the module has a long name we can use this functionality

# import heroes
# print(heroes.gen())   

# def dashed_line(x):
#     for _ in range(x//2):
#         Atlanta.pd()
#         Atlanta.forward(10)
#         Atlanta.pu()
#         Atlanta.forward(10)

# # dashed_line(50)
    
# colours=['blue','red','green','cyan','magenta','yellow','black','orange','violet','#76EE00','#FFD39B']

# def shape_right(sides,length):
#     Atlanta.color(random.choice(colours),'white')
#     angle=180*(sides-2)/sides
#     for i in range(sides):
#         Atlanta.forward(length)
#         Atlanta.right(180-angle)
# def shape_left(sides,length):
#     Atlanta.color(random.choice(colours),'white')
#     angle=180*(sides-2)/sides
#     for i in range(sides):
#         Atlanta.forward(length)
#         Atlanta.left(180-angle)

# def flower(length):
#     shape_right(3,length)
#     shape_right(4,length)
#     shape_right(5,length)
#     shape_right(6,length)
#     shape_right(7,length)
#     shape_right(8,length)
#     shape_right(9,length)


#     shape_left(3,length)
#     shape_left(4,length)
#     shape_left(5,length)
#     shape_left(6,length)
#     shape_left(7,length)
#     shape_left(8,length)
#     shape_left(9,length)

#     Atlanta.forward(length)
#     Atlanta.left(90)
#     Atlanta.backward(length//2)

#     shape_right(3,length)
#     shape_right(4,length)
#     shape_right(5,length)
#     shape_right(6,length)
#     shape_right(7,length)
#     shape_right(8,length)
#     shape_right(9,length)

#     Atlanta.forward(length//2)
#     Atlanta.left(90)
#     Atlanta.forward(length)
#     Atlanta.right(90)
#     Atlanta.backward(length//2)

#     shape_left(3,length)
#     shape_left(4,length)
#     shape_left(5,length)
#     shape_left(6,length)
#     shape_left(7,length)
#     shape_left(8,length)
#     shape_left(9,length)

#     Atlanta.forward(length//2)
#     Atlanta.right(90)

# # flower(100)
# # flower(130)
# Atlanta.speed(0)

# def colour_gen():
#     return (random.randint(0,255),random.randint(0,255),random.randint(0,255))


# def random_walk():
#     Atlanta.pensize(10)
#     angles=[0,90,180,270]
#     for _ in range(200):
#         # turtle.colormode(colour_gen())
#         Atlanta.color(random.choice(colours),'white')
#         Atlanta.setheading(random.choice(angles))
#         Atlanta.forward(30)

# # random_walk()

















# # Challenge

# # n=int(input())
# # points=[]
# # for i in range(n):
# #     points.append(input().split(' '))
# # checkpoint=input()
# # end_point=checkpoint
# # chain=[]
# # for _ in range(n):
# #     for i in points:
# #         if i[0]==end_point:
# #             chain.append(i)
# #             end_point=i[1]
# #             points.remove(i)
# #             break
# # if len(chain)>0 and chain[0][0]==chain[-1][1]:
# #     print(len(chain))
# # else:
# #     print(0)
    

# def graph_maker(num4):

#     Atlanta.penup()
#     Atlanta.backward(100)
#     Atlanta.pendown()
#     Atlanta.left(90)
#     Atlanta.backward(100)
#     Atlanta.forward(430)
#     Atlanta.backward(430)
#     Atlanta.right(90)
#     # print(Atlanta.pensize())

#     #Returns the pen_size 
    
#     def bar_maker(x,y):
#         Atlanta.forward(20)
#         Atlanta.left(90)
#         Atlanta.forward(10)
#         Atlanta.color(colours[y],'white')
#         Atlanta.pensize(20)
#         Atlanta.forward(x+10)
#         Atlanta.backward(x+10)
#         Atlanta.penup()
#         Atlanta.pensize(1)
#         Atlanta.color('green','white')
#         Atlanta.backward(10)
#         Atlanta.right(90)
#         Atlanta.pendown()
#     for i in range(num4):
#         bar_maker(random.randint(50,250),i)
#         Atlanta.forward(20)
        

# # graph_maker(11)







    







# # Challenge

# # number_rows=int(input())
# # number_chairs=int(input())
# # num1=input()
# # num2=input()
# # children=[]

# # for i in range(number_rows):
# #     children.append(input ().split (' '))
# # lucky_num=input()  
# # # print (children) 
# # children_old=[i.copy() for i in children]
# # numbers=[]
# # num3=0
# # for i in children_old:
# #     num4=0
# #     for j in i:
        
# #         columns=[]
# #         for k in children_old:
# #             columns.append(k[num4])
# #         if j==lucky_num:
# #             if lucky_num==num1 :
# #                 if i.count(num2)>=1 or columns.count(num2)>=1:
# #                     children[num3][num4]=num2
# #                 else:
# #                     numbers.append([num3+1,num4+1])

                

# #             elif lucky_num==num2:
# #                     if i.count(num1)>=1 or columns.count(num1)>=1:
# #                         children[num3][num4]=num1
# #                     else:
# #                         numbers.append([num3+1,num4+1])

# #         num4+=1
    
# #     num3+=1
# # print(children)


# def print_hello():
#     pass
#     Atlanta.home()
#     Atlanta.left(90)
#     Atlanta.forward(100)
#     Atlanta.backward(50)
#     Atlanta.right(90)
#     Atlanta.forward(40)
#     Atlanta.left(90)
#     Atlanta.forward(50)
#     Atlanta.backward(100)
#     Atlanta.penup()
#     Atlanta.right(90)
#     Atlanta.forward(20)
#     Atlanta.pendown()
#     Atlanta.left(90)
#     Atlanta.forward(100)
#     Atlanta.right(90)
#     Atlanta.forward(40)
#     Atlanta.backward(40)
#     Atlanta.right(90)
#     Atlanta.forward(50)
#     Atlanta.left(90)
#     Atlanta.forward(40)
#     Atlanta.backward(40)
#     Atlanta.right(90)
#     Atlanta.forward(50)
#     Atlanta.left(90)
#     Atlanta.forward(40)
#     Atlanta.penup()
#     Atlanta.forward(20)


# # import colorgram
# # colour1=list(map(lambda x:(x.rgb.r,x.rgb.g,x.rgb.b),colorgram.extract('dot_painting.jpg.jpg',10)))

# # print_hello()

# def spirograph():
#     angle=0
#     while not angle==360:
#         # coloures=random.choice(colour1)
#         Atlanta.color(random.choice(colours),'white')
#         Atlanta.setheading(angle)
#         Atlanta.circle(100)
#         angle+=10
# # spirograph()


# def dot_painting():
#     Atlanta.penup()
#     def dotter():
#         num_gym=0
#         while not num_gym==200:
            
#             Atlanta.dot(5,random.choice(colours))
#             Atlanta.forward(10)
#             num_gym+=5
#     dotter()
#     move=10
#     while not move==200:
#         Atlanta.home()
#         Atlanta.left(90)
#         Atlanta.forward(move)
#         Atlanta.right(90)
#         dotter()
#         move+=10

    

# dot_painting()


# print(colour1)
# print(type(colour1[0][0]))

# def move_upward():
#     # Atlanta.setheading(90)
#     Atlanta.forward(10)
# def move_forward():
#     Atlanta.setheading(0)
#     Atlanta.forward(10)
# def move_downward():
#     # Atlanta.setheading(270)
#     Atlanta.backward(10)
# def move_backward():
#     Atlanta.setheading(180)
#     Atlanta.backward(10)   

# Screen=Screen()
# Screen.listen()
# Screen.onkey(fun=move_upward,key='Up')
# Screen.onkey(fun=move_forward,key='Right')
# Screen.onkey(fun=move_downward,key='Down')
# Screen.onkey(fun=move_backward,key='Left')

# def eraser():
#     Atlanta.color('white','black')
#     Atlanta.backward(10)
#     Atlanta.color('green','white')
# def PenUp():
#     Atlanta.penup()
# def PenDown():
#     Atlanta.pendown()
# Screen.onkey(key='space',fun=eraser)
# Screen.onkey(key='u',fun=PenUp)
# Screen.onkey(key='d',fun=PenDown)

# def clockwise():
#     Atlanta.right(5)
# def Anticlockwise():
#     Atlanta.left(5)
# Screen.onkey(key='c',fun=clockwise)
# Screen.onkey(key='a',fun=Anticlockwise)
# def erase():
#     # turtle.resetscreen()
#     # Atlanta.color('green','white')
#     Atlanta.clear()
    
# Screen.onkey(key='e',fun= erase)





# Challenge

# people=int(input())
# connections=int(input())
# information={}
# for i in range(connections):
#     connect=input().split(' ')
    
#     if connect[0] in information:
#         information[connect[0]].append(connect[1])
#         if connect[1] in information:
#             information[connect[1]].append(connect[0])
#         else:
#             information[connect[1]]=[connect[0]]
        
        
#     else:
#         information[connect[0]]=[connect[1]]
#         if connect[1] in information:
#             information[connect[1]].append(connect[0])
#         else:
#             information[connect[1]]=[connect[0]]
        

# person=input()
# queries=int(input())
# # print(information)
# if person in information:
     
#     for _ in range(queries):
#         member=input()
#         check1=False
#         check2=False
#         if member in information[person]:
#             check1=True
#         else:
#             check1=False
#         if not check1:    
#             for i in information[person]:
                
#                 if i in information:
#                     if member in information[i]:
#                         check2=True
#                     for j in information[i]:
#                         if j in information:
#                             if member in information[j]:
#                                 check2=True
                            
#                     if check2:
#                         break
#         if check1 or check2:
#             print('yes')
#         else:
#             print('no')
# else :
#     for _ in range(queries):
#         print('no')

            
    

# def calculator(num1,num2):
#     def add(num1,num2):
#         return num1+num2
#     def divide(num1,num2):
#         return num1/num2
#     def sub(num1,num2):
#         return num1-num2
#     def multiply(num1,num2):
#         return num1*num2
#     ops=[add,sub,divide,multiply]

#     results=list(map(lambda x:x(num1,num2),ops))
#     print(results)
# calculator(int(input()),int(input()))



# Challenge

# letters=[['d','f'],['j','k']]
# words=[]
# for i in range(int(input())):
#     words.append(input())
# time=[]
# word_created=[]
# for i in words:
#     time1=0
#     if not i in word_created:
#         prev_index=2
#         for j in i:
#             for k in letters:
#                 if j in k:
#                     if prev_index==letters.index(k):
#                         time1+=4
                        
#                     else:
#                         prev_index=letters.index(k)
#                         time1+=2
                        
                        
#         time.append(time1)
#         word_created.append(i)
#     else :
        
#         time2=time[word_created.index(i)]//2
#         time1+=time2
#         time.append(time1)
        
        
# print(sum(time))


from game_1 import GymRegister

gym1=GymRegister('Body Power Gym','Plot No. 6, 1st Floor, Trimurti Enclave, opposite of Saksham Mall, Sector 9, Kamothe, Navi Mumbai, Maharashtra 410209','Kamothe',['Gymnasium','Aerobic'],'Mr.A','Franchise')
gym2=GymRegister('MY GYM','Ground floor, Ellora Heights, Plot No.36 Sector no.6/A, Kamothe New english School, Kamothe, Navi Mumbai, Maharashtra 410209','Kamothe',['Gymnasium','Aerobic'],'Mr.B','Franchise')
gym3=GymRegister('Physique Gym',' first floor,highlife residency,sector 22,plot no 24, Kamothe, Panvel, Navi Mumbai, Maharashtra 410209','Kamothe',['Gymnasium','Aerobic'],'Mr.C','Franchise')
gym4=GymRegister('Finding Fitness','Shop No. 1, 2, 3 & 4, Shree Gopal Krishna CHS  Sector 59E, Belpada, Kharghar, Navi Mumbai, Maharashtra 410210','Kharghar',['Gymnasium','Aerobic'],'Mr.D','Private')

gym_collection=[gym1,gym2,gym3,gym4]
num_gym,num1=(0,0)

def gymverifier(gym,address,product):
    global num_gym,num1
    match1=re.compile('([Ss]ector( no)?([.:-]|/s)(/d{1,3})[/]?[A-Za-z]?)')
    match2=re.compile('(/d{6})$')

    sector1=list(match1.finditer(gym.Address))[0].group(4)
    sector2=list(match1.finditer(address))[0].group(4)
    pincode1=list(match2.finditer(gym.Address))
    pincode2=list(match2.finditer(address))
    if len(pincode1)>0:
        pincode1=pincode1[0].group(1)
    else:
        return
    if len(pincode2)>0:
        pincode2=pincode2[0].group(1)
    else:
        return
    

    
    
    def type_checker(gym):
        
        if gym.Type=='Franchise':
            print('   This Gym is collaberated with WorkDone')
        else:
            print('   This is a Private Gym')
    
    
    if product in gym.Products:
        if pincode1==pincode2:
            num_gym+=1
            print(f'{num_gym}. {gym.GymName} is present at your town')
            if abs(int(sector1)-int(sector2))<=14:
                print('    {gym.GymName} is present quite near your sector ')

            type_checker(gym)
            return True
            
            
        elif abs(int(pincode1)-int(pincode2))<=2:
            num_gym+=1
            print(f'{num_gym}. {gym.GymName} is present at a different town but near to your town whose pincode is {pincode1} at sector {sector1} {gym.Place}')
            type_checker(gym)
            return True
        else:
            num1+=1
       
            


    
    

# print(gym1.Products)
# address=input('Enter your address :/n')
# product=input('Please Choose the product out of this list as per your choice : ')

# for i in gym_collection:
#      gymverifier(i,address,product)
# if not num1==0:
#     print('we dont provide this service')       
# elif num_gym==0:
#     print('We are not present at your location')



import turtle
# Screen=Screen()
# Screen.setup(width=600,height=600)


# Race game

# color_choosed=Screen.textinput('Bet the Race','Which turtle will you choose ? Enter the Color :').lower()
# position=int(Screen.textinput('Bet the Race','Select the position (less than equal to 7) :'))

# turtles=[Atlanta]
# for _ in range(6):
#     turtles.append(Turtle())

# colours1=['violet','indigo','blue','green','yellow','orange','red']


# turtles[position-1].color(color_choosed)
# colours1.remove(color_choosed)
# turtles[position-1].penup()
# turtles[position-1].shape('turtle')



# for i in (turtles[0:position-1]+turtles[position:]):
#     color_r=random.choice(colours1)
#     colours1.remove(color_r)
#     i.color(color_r)
#     i.penup()
#     i.shape('turtle')
# num=0
# for i in range(-90,120,30):
    
#     turtles[num].goto(-240,i)
    
#     num+=1

# def checker():
#     num=0
#     win=''
#     for i in turtles:
#         if i.xcor()>=241:
#             win=i
#             num+=1
#             break
#     if num==0:
        
#         return True
#     else:
#         if color_choosed==win.color()[0]:
#             print(f'{win.color()[0].title()} won the Race. You won the bet')
#         else:
#             print(f'{win.color()[0].title()} won the Race. You lost the bet')
#         return False
# while checker():
    
#     for i in turtles:
#         i.forward(random.randint(1,25))

import time




# def turn_left():
#     # for i in range(len(turtles)):
#     #     turtles[i].left(90)
        
#     #     for i in turtles:
#     #         i.forward(20)
#     turtles[0].left(90)
#     Screen.update()

# def turn_right():
    # for i in range(len(turtles)):
    #     turtles[i].right(90)
        
    #     for j in turtles:
    #         j.forward(20)
    # turtles[0].right(90)
    # Screen.update()
    

# Challenge
# n=int(input())
# inforamtion={}
# for _ in range(n):
#     number=input()
#     check_state_code=number[0:2]
#     year=int(number[4:8])
#     if 2021-year>15:
#         if check_state_code in inforamtion:
#             inforamtion[check_state_code]+=1
#         else:
#             inforamtion[check_state_code]=1
# if len(inforamtion)==0:
#     print('no expired licenses')
# else:
#     for i in inforamtion:
#         print(i,inforamtion[i])







Game_over=True
num=0

# DOt1=Turtle('circle')
# DOt1.color('red')
# # DOt1.shapesize(0.5,0.5,1)
# DOt1.penup()
# score=0

    
# Screen.bgcolor('black')
# Screen.title('Snake Game')
# Screen.tracer(0)
# Screen.listen()

        
# from Snake import Snake_game
# from food import Food
# from Score import Score

# Snake=Snake_game(Screen)
# Foodie=Food()
# # Snake.take_position()
# Score1=Score()
# # Score1.Score_Changer()


# Screen.onkey(key='Left',fun=Snake.snake_left)
# Screen.onkey(key='Right',fun=Snake.snake_right)
# Screen.onkey(key='Down',fun=Snake.snake_down)
# Screen.onkey(key='Up',fun=Snake.snake_up)



# while not Game_over:
#     Snake.move()
#     if abs(Snake.turtles[0].ycor())>=Screen.window_height()/2 or abs(Snake.turtles[0].xcor())>=Screen.window_width()/2:
            
#             Score2=Score()
#             Score2.Game_over()
#             Game_over=True

#     time.sleep(0.1)
#     Screen.update()
#     if Snake.turtles[0].distance(Foodie)<15:
#         Snake.new_turtle()
#         Foodie.Distribute_food()
#         Score1.score+=1
#         Score1.Score_Changer()
#     if Snake.self_collide():
#         Game_over=True

# Class Inheritance

# If we want to create a class which has properties and methods similar to a existing class then we can inherit those methods and properties with the help of Class Inheritance.

# class Shop:
#     def __init__(self,name,location,owner,dealer):
#         self.Name=name
#         self.Location=location
#         self.Owner=owner
#         self.Dealer=dealer

#     def greeting(self):
#         print(f'{self.Name} is located in {self.Location}')


# class Hardware_Shop(Shop):
#     def __init__(self, name, location, owner, dealer,products):
#         super().__init__(name, location, owner, dealer)
#         self.Products=products.split(' ')

#     def greeting(self):
#         print('This is a Hardware Shop')
#         super().greeting()


# This is called as inheriting the method
        
# This is Class Inheritances

# Shop1=Hardware_Shop('XYZ','Mumbai','ABC','KLM','Hardwares Paints')
# print(Shop1.Owner,Shop1.Products)
# Shop1.greeting()
# We can also modify the existing methods inherited from the super class




# Challenge


# def line_checker(p1,p2,p3):
    
    
#         if not ((p1[0]==p2[0]==0) or (p2[0]==p3[0]==0)): 
         
#             if not (p1[1]-p2[1])/(p1[0]-p2[0])==(p3[1]-p2[1])/(p3[0]-p2[0]):
#                 return True
#         else:
#             if p1[0]==p2[0]==p3[0]==0:
#                 return False
#             else:
#                 return True
    

# def distance_provider(*points):
#     points=list(points)
#     distances=[]
#     for i in range(len(points)):
#         if i+1==len(points):
#             distance=(points[i][0]-points[0][0])**2+(points[i][1]-points[0][1])**2
#             distance=sqrt(distance)

#             distances.append(int(distance))
#         else:
#             distance=(points[i+1][0]-points[i][0])**2+(points[i+1][1]-points[i][1])**2
#             distance=sqrt(distance)
#             distances.append(int(distance))
#     return distances







# def triangle_checker(p1,p2,p3):
    
#     if line_checker(p1,p2,p3):
#         distances=distance_provider(p1,p2,p3)
#         max_side=max(distances)
#         other_sides=[i for i in distances if not i==max_side]
#         if max_side<other_sides[0]+other_sides[1]:
#             print('It is a Triangle')
#         else:
#             print('Traingle cannot be as one side is greater than the sum of the other sides')
#     else:
#         print('Not a Triangle because all the points lie on a straight line')
        

# triangle_checker((1,0),(2,0),(3,0))
# triangle_checker((1,2),(2,4),(3,6))


# if re.match('^(WORK)/d{5}$','WORK12345'):
#     print('Valid Number')


# Function calling itself is called reccursive function
# Function calling another function is called nested function




# Screen.exitonclick()

# Challenge


# table=input().split(' ')
# rows=int(table[0])
# columns=int(table[1])
# info=[]
# for i in range(rows):
#     data_m=[i for i in input()]
#     info.append(data_m)
# queries_num=int(input())
# queries=[int(input()) for _ in range(queries_num)]
# distances=[]
# for i in range(len(info)):
#     for j in range(len(info[i])):
#         if info[i][j]=='1':
#             for k in range(len(info)):
                
#                     for l in range(len(info[k])):
#                         if not (l==j and i==k ):
#                             if info[k][l]=='1':
#                                 distances.append(abs(l-j)+abs(i-k))
                          
# for i in queries:
#     if i in distances:
        
#         print(distances.count(i)//2)
#     else:
#         print(0)

                            
# file=open('trial.txt')
# content=file.read()                          
# print(content)
# file.close()



# In This way we can open a text file and red the content in it and use it and then finally close it and thus we can understand if we forget to close the file then there will be lot of open files and we know that processing power decreases when lot of files are opened and there is thing that python closes on its own but when it will do it is not confirm so it is preffered to manually close the file

# There is a another method to do it

# with open('trial.txt') as file:
#     content=file.read()
#     print(content)



# Here this show a error that the file is closed
# Here we dont have to close the file manually it is automatically closed

# print(content)

# But  we can acess the content as this scope of this block would be global scope as for case in while and for


# and when we open the file it is by default in read only mode and therefore we cannot write into without defining some positional arguements while opening the file

# with open('trial.txt',mode='w') as file:
#     file.write('Hello this is Shakti Santosh Nayak')
# with open('trial.txt') as file1:
#     print(file1.read())


# if we mention a file name in the open function and if it is not there then it will automatically create a new file with that name and this only happens only in write mode

# with open('trial2.txt',mode='a') as file:
#     file.write('hello')
# with open('trial2.txt',mode='a') as file:
#     file.write('/nhey')

# a is used to append the text at the end of the existing file as in write it just replaces the whole code but here it does not replace the whole code instead it just adds the text whatever we enter to the end of the file

# with open('../trial3.txt',mode='w') as file:
#     file.write('This is outside this folder')

# '.' single dot represents the current folder
# '..' double dot represents the folder in which the current folder is


# with open('C:/Users/user/Desktop/javascript/trial4.txt',mode='w') as file:
#     file.write('This is outside this folder')

# This created the file in the javascript folder


# C:/Users/user/Desktop/javascript/trial4.txt This type of file path is called absolute file path

# ../trial3.txt this type of file is called relative file path


# with open('../../trial5.txt',mode='w') as file:
#     file.write('This is outside this folder')


# with open('../../trial6.txt',mode='w') as file:
#     file.write('This is outside this folder')


# with open('trial2.txt') as file:
#     content=file.read()
#     match=re.compile('{(.+)}')
#     matches=list(match.finditer(content))
    
    # for i in matches:
    #     print(i.group(1))
    
    # matches=list(map(lambda x:x.group(1).split(','),matches))
    # print(matches)



def invitation_printer():
    with open('./Input/Letters/starting_letter.txt') as file1:
        sample=file1.read()
        with open('./Input/Names/invited_names.txt') as file2:
            content=file2.read().split('\n')
            for i in content:
                with open(f'./Output/ReadyToSend/ready_to_send_{i}.txt',mode='w') as file3:
                    letter=sample.split('[name]')
                    modified=' '.join([letter[0],i,letter[1]])
                    file3.write(modified)

def people_add(name):
    with open('./Input/Names/invited_names.txt',mode='a') as file2:
            file2.write(f'\n{name}')
    invitation_printer()

# people_add('ABC')
# people_add('XYZ')
# people_add('KLM')
# people_add('OPQ')
# people_add('Vedant')



# Reading CSV Files

# CSV means comma separated vales and they are mostly used to repersent data in tabular format


# with open('weather_data.csv') as file:
    # content=file.read().split('\n')
    # updated=[]
    # for i in content:
    #     updated.extend(i.split(','))
    # print(content,updated)
    # content=file.readlines()
    # print(content)
    # .readlines reads each line of data and then puts into the list


import csv
import pandas

# there is also csv library in python to read the data


# with open('weather_data.csv') as file:
#     content=csv.reader(file)
#     # This is a iterable object that is which can be looped through
#     temperature=[]
#     num=0
#     for i in content:
#         if num==0:
#             continue
#         else:
#             temperature.append(i[1])
#         num+=1
#     for i in content:
#         print(i)
#     print(temperature)
        

# with open('weather_data.csv') as file:
#     data=file.readlines()
    
#     match=re.compile('(\d{2})')
#     temperature=[]
#     for i in data[1:]:
#         temp=list(match.finditer(i))[0].group(1)
#         temperature.append(int(temp))
#     print(temperature)


# data=pandas.read_csv('weather_data.csv')

# # By default panda takes the first line aa the heading for each column and due to these we can get individual column
# print(type(data))
# # From here we come to know that the 'data' is a class and this tabular format is a dataframe which means data represented in the spreadsheet or excel sheet is in the form of dataframe which is quite logical

# print(data)
# print(data['temp'])
# print(type(data['condition']))
# # The above thing is also a class but this is termed to be as series because this only represents a single column.


# data1=data.to_dict()
# data2=data['temp'].to_list()
# print(data1,'\n',data2)
# print(sum(data2)//len(data2))
# # This above thing denotes the average
# # But there is also another way to compute the mean or average 👇👇👇

# print(data['temp'].mean())
# print(data['temp'].max())
# print(data['temp'].min())
# print(data['temp'].median())
# print(list(data['temp']).count(14))

# data3=pandas.read_csv('Birth_year.csv')
# print(data3['BirthYear'])

# # We can do this way also
# print(data3.BirthYear)

# print(data3[data3.BirthYear==1967])
# # This will provide the row whose birthyear is equal to 1967

# print(data[data.temp==data['temp'].max()])
# print(data[data.day=='Sunday'])
# # This can also give multiple rows whose particular values assigned matches

# tuesday=data[data.day=='Tuesday']
# print(1.8*tuesday.temp+32)


# details={
#     'name':['Santosh','Reena','Shakti','Snigdha'],
#     'BirthMonth':['May','December','December','August']


# }


# # This method is used to create a Dataframe from the scratch

# data4=pandas.DataFrame(details)
# print(data4)

# # Now to convert the data into csv file

# data4.to_csv('Birth_month.csv')



# data=pandas.read_csv('250_sc.csv')
# data1=data[data.Industry=='IT']
# print(data1)


# data=pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
# data1=data['Primary Fur Color'].to_dict()
# colour_list=[]
# for i in data1:
#     if not data1[i] in colour_list:
#         colour_list.append(data1[i])
# number1={}
# for i in colour_list[1:]:
#     data_=data[data['Primary Fur Color']==i].to_dict()
#     sum1=0
#     for _ in data_['Primary Fur Color']:
#         sum1+=1
#     number1[i]=sum1
# print(number1)
# dict1={
#     'Fur colour':colour_list[1:],
#     'Count':[number1[i] for i in number1]

# }

# data3=pandas.DataFrame(dict1)
# print(data3)
# data3.to_csv('Fur_Colour.csv')

# Challenge


# from turtle import Turtle
# Screen.title('U.S. check_states Game')
# Screen.bgpic('./us-check_states-game-start/blank_check_states_img.gif')
# # turtle.shape('./us-check_states-game-start/blank_check_states_img.gif')

# data=pandas.read_csv('./us-check_states-game-start/50_check_states.csv')
# data1=data.to_dict()
# information={}
# num=0
# check_states=[]
# for i in data1['check_state']:
#     information[data1['check_state'][i]]={
#         'x':data1['x'][i],
#         'y':data1['y'][i]
#     }
#     check_states.append(data1['check_state'][i])
#     num+=1
# print(data1['check_state'])
# score=0
# while score<num:
#     answer=Screen.textinput('Quiz',f'{score}/50 check_states correct').title()
#     if answer in check_states:
#         res=Turtle()
#         res.hideturtle()
#         res.penup()
#         res.goto(information[answer]['x'],information[answer]['y'])
#         res.write(answer)
#         score+=1
#         check_states.remove(answer)
#     elif answer=='Exit':
#         score=50
#         dictionary2={'Missed check_states':check_states}
#         data2=pandas.DataFrame(dictionary2)
#         data2.to_csv('Missed_check_states.csv')
# def coords(x,y):
    # print(x,y)

# turtle.onscreenclick(coords)    
# This is a event listener which gets trigered on when we click the screen and here it is used to get the coords of the location wherever we click on the screen
# turtle.mainloop()
# Screen.exitonclick()






    
# Turtle only works with gif format not for jpeg or png


# data=pandas.read_csv('exp_csv.csv')
# data1=data.to_dict()
# for i in data1['Voltage (V)']:
#     data1['Power (W)'][i]=float(format(data1['Voltage (V)'][i]*data1['Current (mA)'][i],'0.2f'))
# print(data1)
# data2=pandas.DataFrame(data1)
# data2.to_csv('exp_modified.csv')



# range(),list,tuple,string are called sequences because they have a particular arrangement.

# birthmonth={
#     'Name':['Santosh','Reena','Shakti','Snigdha'],
#     'Birth Month':['May','December','December','August']
   
# }

# data=pandas.DataFrame(birthmonth)
# # for key,value in data.items():
# #     print(value)

# # Here each column is printed at once along with the index number


# # for (index,row) in data.iterrows():
# #     print(index)
# #     print(row)

# # Here individual row is printed 

# for (index,row) in data.iterrows():
#     print(index)
#     print(row.Name)
# # Here individual element of the row can be displayed just the name 
# for (index,row) in data.iterrows():
#     # print(index)
#     print(row['Birth Month'])


# Challenge

# with open('task_1.txt',mode='w') as file:
#     text='''1 2 3 4 5 6
# 100 102 1892 18920 182
# 1992 15 168 189 120
# 189 1782 1829 188 188829'''
#     file.write(text)
# info=[]
# with open('task_1.txt',mode='r') as file:
#     data=file.readlines()
#     for i in data:
#         word=i[:len(i)-1]
#         data_sub=list(map(lambda x:int(x),word.split(' ')))
#         info.append(word+f': {sum(data_sub)}\n')
# with open('task_1.txt',mode='w') as file:
#     file.writelines(info)

# Screen.exitonclick()

# data1=pandas.read_csv('./NATO-alphabet-start/nato_phonetic_alphabet.csv') 
# data2=data1.to_dict()
# info={data2['letter'][i]:data2['code'][i] for i in data2['letter']}


# word=input('Enter the word : \n')
# for i in word:
#     print(f'{i.upper()} : {info[i.upper()]}')



from tkinter import *
# This will import everything in it
# window=Tk()
# # This creates a window like the screen in the turtle

# window.title('First GUI')
# window.minsize(width=600,height=600)

# # Creating Label

# # label1=Label(text='WorkDone'.upper(),font=('Arial',26,'bold'))
# label1=Label(text='WorkDone'.upper(),font=('Arial',26,'italic'))
# # The last parameter in the tuple is used to bold the text ot set it as italic
# # label1.pack(side='left')
# label1.pack(side='top')
# # label1.pack(expand=True)
# # This above thing will set the label to be in the center of the window
# # By default side is set to top
# # This above syntax is used to add the label into window and by default it is aligned to center at the top

# label1['text']='WorkDone Corporation'
# # We can change the text of a label as if we are modifying a key in a dictionary
# label2=Label(text='',font=('Arial','15','bold'))
# label2.pack()
# label1.config(text='WorkDone Corporation ©',font=('Arial','27','bold'))
# # Through these method we can modify multiple variables

# # Create a input

# input1=Entry(width=25)
# input1.pack()
# input1.insert(END,string='Enter your Name')
# # This used to put the Placeholder value

# # Creating a button

# button1=Button(text='Submit')
# button1.pack()
# # We can add a click event function to a button


# def Clicked():
#     # print('Clicked')
#     label2.config(text=input1.get())
    
#     # input1.insert(END,string='Enter your Name')
#     # print(input1.get())
    
#     # input.get() will return the value in the input

# button1.config(command=Clicked)
# # This will create a button




# dir=['top','bottom','left','right']
# import random
# def printer(*a):
#     for i in a:
#         label1=Label(text=i,font=('New times Roman',15,'bold'))
#         label1.pack(expand=True)
#     print(sum(a))
# # printer(1,2,3,4,5,6,7,8)
# # This function can n number of positional arguements

# def taker(**a):
#     print(a)
#     for i in a:
#         print(a[i])


# taker(a=1,b=2,c=3,d=1,e=2,f=3,z=1,y=3)
# # This function will take n number of keyword arguements and this will be stored in the form of dictionary
# # This is the same thing used while making the class of because when we will see its description it shows **kw which means take n number of keyword arguements and thus this can be proved out to be important

# # a=2
# # a*=2
# # This can also be used to multiply on a existing variable and store it in the existing variable


# # Creating a Multiline Text
# text1=Text(height=10,width=20)
# text1.insert(END,'Multiline entry\nHello What\'s Up?\nHow are You?')
# text1.focus()
# text1.pack()
# print(text1.get('1.0','3.0'))
# # Here to get the text we need to give first the starting index and then the stop index and this does not includes the Stop Index

# # Creating a SpinBox

# def spin_clicked():
#     print(spinbox1.get())


# spinbox1=Spinbox(from_=0,to=10,width=5,command=spin_clicked)

# # The command given in the spinbox is called whenever the value in it is changed 
# # spinbox1.insert(END,'0')
# spinbox1.pack()

# def scale_used(value):
#     print(value)
#     if int(value)==50:
#         print('You got 50')


# scale1=Scale(from_=0,to=200,command=scale_used)

# # The command is executed when the scroll bar is scrolled
# scale1.pack()



# # Creating a CheckBox

# check_state=IntVar()
# def checker():
#     print(check_state.get())

# checkbutton1=Checkbutton(text='ON/OFF',variable=check_state,command=checker)
# print(check_state.get())
# checkbutton1.pack()

# # Creating a Radio button


# radio_state=IntVar()

# def radio_check():
#     print(radio_state.get())

# radio_1=Radiobutton(text='Premium',value=1,variable=radio_state,command=radio_check)
# radio_2=Radiobutton(text='Freemium',value=2,variable=radio_state,command=radio_check)
# radio_1.pack()
# radio_2.pack()


# # Creating a ListBox

# def listbox_state(event):
#     print(listbox1.get(listbox1.curselection()))
#     print(listbox1.curselection())
#     # listbox1.curselection() gives the index of the selected item

# listbox1=Listbox(height=5)
# work=['Paint','Decoration','Designing','Labour']
# for i in work:
#     listbox1.insert(work.index(i),i)

# listbox1.bind("<<ListboxSelect>>",listbox_state)
# listbox1.pack()

















# window.mainloop()
# # This will keep running the window until we close the window similar to Screen.exitonclick()
# window2=Tk()
# window2.title('Challenge')
# window2.minsize(width=300,height=300)
# label3=Label(text='KMS')

# label3.pack()
# input2=Entry()
# input2.insert(END,string='Enter the Distance')
# input2.pack()
# label4=Label(text='MILES')
# label4.pack()
# input3=Entry()
# input3.pack()

# def Calc():
#     input3.insert((0,),str(float(input2.get())/1.6))


# button2=Button(text='Get',command=Calc)



# button2.pack()
# window2.mainloop()
# # We can set the default values in a function in python like how we did in javascript

# def func(x=1,y=2,z=3):
#     print(x,y,z)

# func()
# Here without giving the value of arguements worked a default value of the parameters was set which is quite logical

# info=0
# file=open('task_1.txt',mode='r')
# data=file.readlines()
# for i in data:
#     word=i[:len(i)-1]

#     data_sub=list(word.split(' '))
#     # print(data_sub)
    
#     if data_sub[2]=='100':
#         info+=1

# print(info)


class Problem:
    def __init__(self,**kw):
        self.Name=kw.get('Name')
        self.Problem=kw.get('problem')
        self.Reffered=kw.get('Referred')
        # We used get method because if the particular key will not be present in kw then it will return None but while using [''] will lead to an error and prove to be blocking code.

Patient1=Problem(Name='ABC',problem='Fever')

print(Patient1.Name,Patient1.Problem,Patient1.Reffered)
# Though we did not declare Reffered it did not create error

# from stock_2 import anyalsis
# anyalsis('Bitcoin Historical Data - Investing.com India.csv')
# anyalsis('ETH_USD Binance Historical Data.csv')





# WorkDone Project


# window=Tk()


# window.title('WorkDone')
# window.minsize(width=1000,height=1000)



# label1=Label(text='WorkDone')
# # label1.pack()

# # Pack simply adds to the top left right bottom side but not on any othere position in the screen we will use place

# # label1.place(x=0,y=0)
# # This will place it at the left top most corner

# # label1.place(x=200,y=400)


# # Next is a grid system and this divides the screen into number of grids
# label1.grid(column=0,row=0)

# label2=Label(text='Name :')
# # label2.place(x=10,y=50)
# label2.grid(column=1,row=1)

# input1=Entry(width=20)
# input1.insert(END,'This is a input Box')
# # input1.pack()

# # input1.place(x=80,y=50)

# input1.grid(column=2,row=1)


# Button1=Button(text='Submit')
# # Button1.pack()

# # Button1.place(x=10,y=100)
# Button1.grid(row=2,column=1)


# # You cannot use grid and pack together in a window

# window.mainloop()



# Challenge


# window=Tk()
# window.title('Challenge')
# window.minsize(width=1000,height=1000)


# # We can also padding to the elements

# window.config(padx=20,pady=20)

# label1=Label(text='Label 1')
# label1.grid(row=0,column=0)
# label1.config(padx=10,pady=10)



# button1=Button(text='Button 1')
# button1.grid(row=1,column=1)

# button2=Button(text='Button 2')
# button2.grid(row=0,column=2)
# button2.config(padx=5,pady=5)

# # the content will be placed more away from the margin

# input1=Entry(width=20)
# input1.grid(row=2,column=3)
# input1.focus()

# window.mainloop()



# NUMPY

# import time
# import numpy as np

# list1=np.arange(100000)
# print(list1)
# print(list1.size*list1.itemsize)
# # This gives the byte used to store in memory

# list2=np.arange(100000,200000,1)
# # The value will start from 100000 and go till 200000 with step value equal to 1 and not include 200000
# print(list2)



# Challenge
# data=['ABC,1000\n','XYZ,100\n','KLM,600\n']
# with open('Challenge_1.txt',mode='w') as file:
#     file.writelines(data)

# information={
#     100:{
#         100:0
#     },
#     200:{
#         100:0,
#         '100':1.5
#     },
#     500:{
#         100:0,
#         '100':1.5,
#         300:3.5
#     },
#     999999:{
#         100:0,
#         '100':1.5,
#         300:3.5,
#         999999:6.6

#     }
# }

# with open('Challenge_1.txt') as file:
#     data=file.readlines()

# for i in data:
#     data1=i.split(',')
    
#     data1[1]=int(data1[1])
#     bill=data1[1]
    
#     # print(bill)
#     amount=0
#     for k in information:
#         if bill<=k:
#             data2=information[k]
#             # print(data2)
#             for j in data2:
#                 l=j
#                 j=int(j)

#                 if bill>0:
#                     if bill<=j:
#                         amount+=bill*data2[j]
#                         bill-=bill
#                         break
#                     else:
#                         amount+=j*data2[l]
#                         bill-=j
                        
#             break
#     print(data1[0],bill,amount)


# Sys module


# import sys
# sys.getsizeof(20)
# 28
# a=[]
# sys.getsizeof(a)
# 56


# In numpy we can give float number in arange function

# from math import *

# Challenge

# time_data=input().split(' ')
# suffix_8=['A.M','B.M','C.M','P.M']
# def time_checker(x):
#     if x[1] not in suffix_8:
#         return f'08:00:00 {x[1]}'
#     else:
#         time=x[0].split(':')
#         hour=int(time[0])
#         if x[1]=='A.M':
#             suffix=suffix_8[int(hour/8)]
#             hour=hour%8
        
#         else:
            
#             suffix=suffix_8[int((hour+12)/8)]
            
#             hour=(hour+12)%8
        
#         hour='0'+str(hour)
#         return f'{hour}:{time[1]}:{time[2]} {suffix}'
# print(time_checker(time_data))

# IndexError
# This error exists when we try to find a element in a list and index is out of range in it

# TypeError
# This error occurs when a string and number are added with each other

# KeyError
# This error occurs when a certain key in a dictionary is called and it does not exists in it.

# FileError
# This error occurs when we try to open and read a file which does not exist.


# Try except else finally in Python
# This is same like Try Catch and Finally method in javascript

# try:
#     file=open('*)_!_!.txt')
# except:
#     print('File not Found')



# Here we give a code in try block and if any error comes then it will execute the code in except block
# And in the above code we know that the error is going to occur and therefore the code in the except block got executed

# We can also define what type of error except block has to catch 

# try:
#     file=open('ready_to_send_Zuko.txt')
#     list1=['a','b','c']
#     print(list1[2])
#     # Here this error will occur because this was not a fileerror
# except FileNotFoundError:
#     print('File not found')
# except IndexError as message:
#     print(f'{message}')
#     # We can catch the error message as well
# else:
#     print(file.read())
#     print('The code successfully got executed')
#     #This will occur only when there is no error
# # We can give more than one except methods
# finally:
#     file.close()
#     print('Executed')
#     # This will occur at all the possibilties as like in the javascript

#     # We can raise our error as well

#     raise KeyError('I made an error to occur')
#     # KeyError(A) keyerror is the class and also in the javascript we used to use to new before Error to construct a new object and in oython  the A means error







# height=float(input('Enter your Height (meters): '))
# weight=float(input('Enter your Weight(kilogram) : '))
# try:
#     if height>3:
#         raise ValueError('Please enter your correct height.')
#     if weight>200:
#         raise ValueError('Please enter your correct weight.')
# except ValueError as error:
#     print(error)
# else:
#     bmi=weight/height**2
#     print(format(bmi,'0.1f'))


# JSON format

import json
# info_1={
#     'WorkDone':{
#         'Services':['BlockChain System','HealthCare','Construction','Wd World','NFT'],
#         'Owner':['Shakti Santosh Nayak','Other Investors']
#     }
# }
# with open('json_1.json',mode='w') as file:
#     json.dump(info_1,file,indent=5)

# In this wy we created a json file and wrote in it and this is similar to all other csv, text files
with open('json_1.json',mode='r') as file:
    data=json.load(file)
    # The type of data is a dictionary which is quite logical
    print(data)

#dict1={1:'1',2:'2'}
# dict2={3:'3'}
# dict1.update(dict2)
# dict1
# {1: '1', 2: '2', 3: '3'}

# if we want to update a dictionary with keys and values of other dictionary


# data=pandas.read_csv('./FlashCard/data/french_words.csv')
# data=data.to_dict(orient='records')
# print(data)
# This will contain a list of elements and element will be a dictionary which consist the row element as valuewith their specific heading as their key 


# class hello:
#     def __init__(self,x):
#         self.variable=x
#     def view(self):
#         print(self.variable)


# class hello2:
#     def __init__(self,y:hello):
#         y.view()

# b=hello('Shakti Santosh Nayak')
# c=hello2(b)



# If we declare like this it will say us that it expects y as type of hello class and also while doing operations in the class then it will automatically show the methods of hello over there because it knows the type of variable



number1:int
# First we declare data type of variable and then we can declare it any other time


number1=20

# We can dynamically change the data type of a variable and therefore python is known as dynamic typing language

number1:str

number1='hello'


def hello(x:int)->int:
    print(x)
    # text after arrow represent type of data which is returned

hello(20)

# This is known as type hints


# HTTP requests


# Till now we have done requests.get()

# requests.post() simply means that we are going to just send data to a api
# requests.put() simply means to update the existing data 
# requests.delete() simply means to delete the data

import random
def hash_gen():
    letter='a b c d e f g h i j k l m n o p q r s t u v x y z'.split(' ')
    symbols=[i for i in range(10)]+letter+[i.upper() for i in letter]+['#','$']
    address=[str(random.choice(symbols)) for _ in range(64)]
    return ''.join(address)

# HTML-HyperText Markup Language
# XML-Extended Markup Language
# GML-Generalised Markup Language

# The tag which dont have closing tags in html are called self closing tags