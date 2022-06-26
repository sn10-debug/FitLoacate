import pandas
import re
data1=pandas.read_csv('nulltri16-12-2020-15-12-2021.csv')
match1=re.compile('(\d{2})$')
match2=re.compile('^(\d{2})')
data2=data1[data1.Month=='Dec']
data3=data2.to_dict()
data4={'Dates':[],'Prices':[]}
for i in data3['Date']:
    if list(match1.finditer(data3['Date'][i]))[0].group(1)=='20':
    
        data4['Dates'].append(data3['Date'][i])
        data4['Prices'].append(data3['Total Returns Index'][i])

data5=data1.to_dict()

data6={'Dates':[],'Prices':[]}
for i in data5['Date']:
    if list(match2.finditer(data5['Date'][i]))[0].group(1)=='31':
        data6['Dates'].append(data5['Date'][i])
        data6['Prices'].append(data5['Total Returns Index'][i])

print(data6)
data7={'Dates':[],'Prices':[]}
for i in data3['Date']:
    if list(match1.finditer(data3['Date'][i]))[0].group(1)=='21':
    
        data7['Dates'].append(data3['Date'][i])
        data7['Prices'].append(data3['Total Returns Index'][i])


Months=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov']
Monthly={'Dec-20':data4}
for i in Months:
    data_=data1[data1.Month==i].to_dict()
    Dates=[]
    Prices=[]
    for j in data_['Date']:
        Dates.append(data_['Date'][j])
    for j in data_['Total Returns Index']:
        Prices.append(data_['Total Returns Index'][j])
    Monthly[i]={'Dates':Dates,'Prices':Prices}
Month_ending=[]
Monthly['Dec-21']=data7
for i in Monthly:
    amount=Monthly[i]['Prices'][-1]
    Month_ending.append(amount)
def average(el,diff):
    sum1=[]
    elements=[]
    for i in range(0,len(el),diff):
        elements.append(el[i])
    for j in range(len(elements)-1):
        num=(elements[j+1]-elements[j])*100/elements[j]
        sum1.append(num)
    average=sum(sum1)/len(sum1)
    return average
print(format(average(Month_ending,1),'0.2f')+' %')
print(format(average(Month_ending,3),'0.2f')+' %')
print(format(average(Month_ending,12),'0.2f')+' %')

