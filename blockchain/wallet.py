import pandas
import random

class wallet:
    def __init__(self) -> None:
        self.public_key=self.key_generator()
        self.private_key=self.key_generator()
        self.coins={'sigma':0}
        self.NFT_address=[]
        self.transactions=[]

    def key_generator():
        characters='a b c d e f g h i j k l m n o p q r s t u v x y z'.split(' ')
        characters=characters+[i.upper() for i in characters]+[i for i in range(10)]+['#']
        return ''.join([random.choice(characters) for _ in range(64)])

    def send(self,coin,amount,receiver_pub_key):
        if not coin in self.coins:
            print(f"You don't own {coin}")
            return
        
        if amount<=self.coins[coin]:
            data_points={
                    "Sender":[self.public_key],
                    "Receiver":[receiver_pub_key],
                    "Amount":[amount],
                    "Status":['Pending']

                }
            try:
                data=pandas.read_csv('./blockchain/transacion_data.csv').to_dict()
                
                
            except FileNotFoundError:
                
                file=pandas.DataFrame(data_points)
                
            else:
                new_data={}
                new_data['Sender']=[data['Sender'][i] for i in data['Sender']]
                new_data['Receiver']=[data['Receiver'][i] for i in data['Receiver']]
                new_data['Amount']=[data['Amount'][i] for i in data['Amount']]
                new_data['Status']=[data['Status'][i] for i in data['Status']]
                
                for i in new_data:
                    new_data[i].extend(data_points[i])
                file=pandas.DataFrame(new_data)
                

            finally:
                file.to_csv('./blockchain/transacion_data.csv')


        else:
            print("You don't have enough amount of coins")
    
    def add_coin(self,coin):
       
        with open('./blockchain/coins_list.txt') as file:
            coins=file.readlines()
            if coin in coins:
                self.coins[coin]=0
            else:
                print('Coin not available.')

    

    




