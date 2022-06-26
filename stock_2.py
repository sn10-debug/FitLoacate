import pandas
# with open('Bitcoin Historical Data - Investing.com India.csv') as file:
#     data=file.read()
def analysis(link,x):
    '''Returns average_Price,Monthly_Return,Quanterly_return,Half_return,Yearly_Return'''
    data=pandas.read_csv(link)
    # data1=data.to_dict()
    data2=data[x].to_dict()
    for i in data2:
        new=data2[i].split(',')
        sum_=''
        for j in new:
            sum_+=j
        data2[i]=sum_

    data2=[float(data2[i]) for i in data2]
    data2.reverse()
    average=sum(data2)/len(data2)
    average=format(average,'0.2f')
    
    def rate_calc(el):
        list1=[]
        for k in range(1,len(el)):
            per=((el[k]-el[k-1])/el[k-1])*100
            list1.append(per)
        return (sum(list1)/len(list1))

    def interval(el,diff):
        list2=[]
        for i in range(0,len(el),diff):
            list2.append(el[i])
        return list2


    Monthly_Prices=interval(data2,30)
    Monthly_Return=rate_calc(Monthly_Prices)
    Yearly_Return=((data2[-1]-data2[0])/data2[0])*100
    Quaterly_Prices=interval(data2,90)
    Quanterly_return=rate_calc(Quaterly_Prices)
    Half_prices=interval(data2,180)
    Half_return=rate_calc(Half_prices)
    return average,Monthly_Return,Quanterly_return,Half_return,Yearly_Return
    

# anyalsis('Bitcoin Historical Data - Investing.com India.csv')

