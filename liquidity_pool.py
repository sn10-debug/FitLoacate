import math


commodity1='abc'
commodity2='xyz'


quantity1=30000
quantity2=30000
total=quantity1*quantity2
price1=1
price2=1
class swap:
    def __init__(self):
        global quantity1,quantity2
        self.commodities=[commodity1,commodity2]
        self.quantities=[quantity1,quantity2]
        self.prices=[price1,price2]
        self.total=quantity1*quantity2
        

    def change(self,commodity1,quantity,commodity2):
        if commodity1 in self.commodities:
            index1=self.commodities.index(commodity1)
            index2=self.commodities.index(commodity2)
            self.quantities[index1]+=quantity
            quantity_return=self.quantities[index2]-(self.total/self.quantities[index1])
            self.quantities[index2]=(self.total/self.quantities[index1])
            self.prices[index1]=quantity1*price1/self.quantities[index1]
            self.prices[index2]=quantity2*price2/self.quantities[index2]
            return quantity_return
    
swap1=swap()

swap1.change('abc',20000,'xyz')
print(swap1.quantities)
print(swap1.prices)    


            




