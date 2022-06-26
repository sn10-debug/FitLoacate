from hashlib import sha256


Blocks=[]




def disp_block_hash():
    global Blocks
    for i in Blocks:
        print(f'Block {i.block_number} hash : {i.hash_gen()}')



num_blocks=0
from datetime import datetime


class Block:
    def __init__(self,message):
        global num_blocks
        num_blocks+=1
        self.message=message
        self.children=[]
        self.time_creation=datetime.now()
        self.block_number=num_blocks
        Blocks.append(self)
        
        # self.hash=self.hash_gen()

    def hash_gen(self):
        self_message_hash=sha256(self.message.encode()).hexdigest()
        children_hash=''

        for i in self.children:
            children_hash+=i.hash_gen()
        
        children_message_hash=sha256(children_hash.encode()).hexdigest()

        return sha256((self_message_hash+children_message_hash).encode()).hexdigest()

    def add_child(self,block):
        self.children.append(block)
        self.hash=self.hash_gen()

    


Block1=Block('Hello message')

disp_block_hash()

Block2=Block('Good Morning People')

Block1.add_child(Block2)

disp_block_hash()

Block3=Block('Good Night')

Block1.add_child(Block3)

disp_block_hash()

Block4=Block('Hello this is Shakti ')

Block2.add_child(Block4)

disp_block_hash()


Block5=Block("Hello this is Shakti Santosh Nayak")
Block6=Block("This is Sigma Metaverse ")
Block7=Block("This is Sigma Wallet ")

Block1.add_child(Block7)

Block2.add_child(Block5)
Block2.add_child(Block6)

disp_block_hash()

print([((i.hash_gen()),i.block_number) for i in Block1.children])
print([(i.hash_gen(),i.block_number) for i in Block2.children])




info={
    '0':'0000',
    '1':'0001',
    '2':'0010',
    '3':'0011',
    '4':'0100',
    '5':'0101',
    '6':'0110',
    '7':'0111',
    '8':'1000',
    '9':'1001',
    'a':'1010',
    'b':'1011',
    'c':'1100',
    'd':'1101',
    'e':'1110',
    'f':'1111'

}


def convert_to_bits(x):
    y=''


    for i in x:
        y+=info[i]

    return y

message_hash_bits=convert_to_bits(sha256('Hello this is Code'.encode('utf-8')).hexdigest())

print(len(message_hash_bits))



private_key_0=[sha256(i.encode('utf-8')).hexdigest() for i in sha256('Hello this is Shakti  Santosh Nayak'.encode('utf-8')).hexdigest()*4]
private_key_1=[sha256(i.encode('utf-8')).hexdigest() for i in  sha256('Hello this is Shakti Santosh Nayak , Chairman and CEO , CTO of Sigma'.encode('utf-8')).hexdigest()*4]


public_key=[
    sha256(i.encode('utf-8')).hexdigest() for i in private_key_0+private_key_1]



signature=[]


for i in range(256):
    if message_hash_bits[i]=='1':
        signature.append(private_key_1[i])
    else :
        signature.append(private_key_0[i])



print(signature)








