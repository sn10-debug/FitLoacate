# import numpy as np
# a=np.arange(1000)
# b=np.ones([5,5],dtype=int)
# c=np.array([[b for _ in range(5)],[b for _ in range(5)]])
# # print(c)
# print(c+50)
# print(b)
# d=np.arange(100).reshape(10,10)
# print(d[1,:])

# # If we make multiplication in matrixes of numpy they dont follow matrix multiplication rule instead they multiply corresponding elements
# # axis=0 is column and axis=1 is row
# e=np.arange(16).reshape(4,4)
# f=np.insert(e,1,[1,2,3,4],axis=0)
# print(np.sum(f,axis=1))
# mat1=np.matrix('4,5;6,7')
# print(mat1)
# print(type(mat1))
# # This is a real matrix
# mat2=np.matrix('12,13;14,15')
# print(mat1*mat2)
# # Here real matrix multiplication will take place
# print(mat1+mat2)

# 7777031159

import pandas
data=pandas.read_csv('./NATO-alphabet-start/nato_phonetic_alphabet.csv')
word=input().upper()
# for i in data.iterrows():
#     index,row=i
#     print(index)
#     print(row.letter)
#     print(row.code)
# data1=data[data.letter=='Z']
# print(data1)


info={row.letter:row.code for (_,row) in data.iterrows()}
print(info)
if word.isalnum() or word.isnumeric():
    print('Only letters are allowed')
    
else:
    list1=[info[i] for i in word]
    print(''.join(list1))

