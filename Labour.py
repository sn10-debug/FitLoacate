
Shops_list=[]
Labours=[]



def sector(sec):
    sector=''
    for i in sec:
          if i.isnumeric():
              sector+=i
    return sector


class ShopInfo:
    def __init__(self,Name,address,Products,Owner_name,Dealers='Workdone'):
        self.Shop_Name=Name
        self.Address=address
        self.Products=Products
        self.Owner_Name=Owner_name
        self.Dealers=Dealers
        Shops_list.append(self)

class LabourInfo:
    def __init__(self,Name,res_Address,Skills):
        self.Name=Name
        self.Residential=res_Address
        self.Skills=Skills
        Labours.append(self)

    def Shop_checker(self,list_shops,working_address):
        import re
        match1=re.compile('[sS]ector([:-]|\s)(no.|No.)?\s?(\d{1,3}[/]?[\w]?)')
        sector_work=sector(list(match1.finditer(working_address))[0].group(3))
        match2=re.compile('\d{6}$')
        pincode_work=list(match2.finditer(working_address))[0].group(0)
        num=1
        priority_1=[]
        priority_2=[]
        for i in list_shops:
            
            shop_sector=list(match1.finditer(i.Address))
            shop_sector=sector(shop_sector[0].group(3))
            
            shop_pincode=list(match2.finditer(i.Address))[0].group(0)
    
            if shop_pincode==pincode_work:
                priority_2.append(i)
                if  int(shop_sector)-int(sector_work)<10 :
                        print(num,end='.\n')
                        print(i.Shop_Name)
                        print(i.Address)
                        priority_1.append(i)
                        num+=1
        for i in priority_2:
            if i not in priority_1:
                print(num,end='.\n')
                print(i.Shop_Name)
                print(i.Address)
                num+=1
        
        if len(priority_2)==0:
            print('We are currently not available at your area')        







Shop1=ShopInfo('Purnima electric & hardware','Shop no. Kalindi society Sector No. 48,, Roadpali, Kalamboli, Navi Mumbai, Maharashtra 410218',['Hardware Materials','Pipes','Paints'],'Mr.Dowal')

Shop2=ShopInfo('Royalé Touché',' Shivalay, Unit No. 1-2-3 Plot No. 55, Sector No. 19/C Warehousing Complex, APMC Rd, Vashi, Navi Mumbai, Maharashtra 400703',['Hardware Materials','Pipes','Paints','Luxury Amenities'],'Mr.Mehta')

Shop3=ShopInfo('js hardware','Shop no 4, Sector 3, Kalamboli, Panvel, Navi Mumbai, Maharashtra 410218',['Hardware Materials','Pipes','Paints'],'Mr.kailash')

Shop4=ShopInfo('Welcome Hardware & Electrical Stores','Shop No.12, Plot No.5,Shree Apartment, Sector 1, Kalamboli, Navi Mumbai, Maharashtra 410218',['Hardware Materials','Pipes','Paints','Electrical Equipments'],'Mr.Shailesh')

Shop5=ShopInfo('Mahavir Electric And Hardware Store','Satyam Apartments, Shop Number 16 Plot Number 11, Sector 2E, Kalamboli, Panvel, Navi Mumbai, Maharashtra 410218',['Hardware Materials','Pipes','Paints','Electrical Equipments'],'Mr.Mahavir')

Shop6=ShopInfo('Manoj Electrical & Hardware','Shop No. 1 Neel Udyan, Sector 3E, Kalamboli, Panvel, Navi Mumbai, Maharashtra 410218',['Hardware Materials','Pipes','Paints','Electrical Equipments'],'Mr.Manoj')

Shop7=ShopInfo('Kailash Electric & Hardware','Shop No.6, 31, Sector-3E/B, Sector 3E, Kalamboli, Panvel, Navi Mumbai, Maharashtra 410218',['Hardware Materials','Pipes','Paints'],'Mr.Kailash')

Shop8=ShopInfo('Saikrupa Traders','F, Shop, No.4, A, Sector 4E, Kalamboli, Panvel, Navi Mumbai, Maharashtra 410218',['Hardware Materials','Pipes','Paints'],'Mr.Sainath')

Shop9=ShopInfo('Vishal Electric and Hardware Stores',' Shop No.11, Sector-3EA, Kalamboli, Panvel, Navi Mumbai, Maharashtra 410218',['Hardware Materials','Pipes','Paints'],'Mr.Vishal')

Shop10=ShopInfo('Jalaram Electric and Hardware Stores','Sector 3E, Kalamboli, Panvel, Navi Mumbai, Maharashtra 410218',['Hardware Materials','Pipes','Paints','Electrical Equipments'],'Mr.Jalaram')

Shop11=ShopInfo('Malaram Electric and Hardware Stores','Sector 30E, Kalamboli, Panvel, Navi Mumbai, Maharashtra 410218',['Hardware Materials','Pipes','Paints','Electrical Equipments'],'Mr.Malaram')


Labour1=LabourInfo('Ramesh','Sector-1 Kalamboli 410218',['Painter','Furniture Maker'])

Labour1.Shop_checker(Shops_list,'Sector no. 50 400703')


