import pandas
data=pandas.read_csv('./blockchain/transaction_data.csv')
data=data.to_dict()
print(data)