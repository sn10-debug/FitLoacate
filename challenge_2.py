testcases=int(input())

# 2
# 5 3 2
# 1 2 3 4 5
# 5 2 4
# 1 2 3 4 5



def checker(num1,num2):
    global Dine,numbers;
    number=''
    
    for i in numbers:
        if i%(num1*num2)==0: 
            number=i
            break
    if number=='':
        for i in numbers:
            if i%num1==0:
                number=i
                numbers.remove(i)
                break
    # print(number,Dine)
    if number=='':
        numbers=[]
    Dine=not Dine

for i in range(testcases):
    N,a,b=(int(i) for i in input().split(' '))
    numbers=[int(i) for i in input().split(' ')]
    Dine=True
    while len(numbers)>0:
        if Dine:
            checker(a,b)
        else:
            checker(b,a)

    if Dine:
        print("BOB")
    else:
        print("ALICE")

