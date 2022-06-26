
import pandas
def analysis_Stock_exchange(link):
    data=pandas.read_csv(link).to_dict()
    data1=data['ltp ']
    price_1=[]
    for i in data1:
        if ',' in str(data1[i]):
            data1[i]=float(''.join(data1[i].split(',')))
            
        price_1.append((data1[i]))
    price_1.reverse()
    # print(price_1)
    def rate_calc(x,diff,division):
        holdidays=int((13+105)/division)
        price_2=[]
        for i in range(0,len(x),diff-holdidays):
            price_2.append(x[i])
        
        rates=[]
        for i in range(0,len(price_2)-1):
            rate=((price_2[i+1]-price_2[i])/price_2[i])*100
            rates.append(rate)
        average=sum(rates)/len(rates)
        
        return average

    Monthly=rate_calc(price_1,30,12)
    Quaterly=rate_calc(price_1,90,4)
    Half_yearly=rate_calc(price_1,180,2)
    Yearly=rate_calc(price_1,365,1)
    return (Monthly,Quaterly,Half_yearly,Yearly)

    
    