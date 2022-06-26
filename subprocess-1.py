# from subprocess import *

from re import sub
import subprocess
from tkinter.tix import Tree

# import selenium_1

# This will also auto run the program

# subprocess.run('dir',shell=True)

# subprocess.run('python selenium_1.py', shell=True)


# subprocess.run('cd ..',shell=True)




# As this dir is available in shell only therefore we have to set the shell atribute as true


# Thus we ran a external program


# Also if we dont use shell then we have to pass the command cd .. as ['cd','..'] which is in the form of list


output=subprocess.run('cd ..',shell=True,capture_output=True)

# Now command will be run but it will not be displayed in the console instead it is captured in this variable output

import pprint
pprint.pprint(output.stdout)

# if the command returns nothing then this will also be empty

print(output)

# This returns a Completed process object where we can see the arguements we passed and also see the returncode that whether there was a error or not
print(output.args)
print(output.returncode)

output2=subprocess.run('python subprocess-2.py',shell=True,capture_output=True,text=True)
# This command will no more print hello world because here the capture_output is set out to be true

pprint.pprint(output2.stdout)





# This will give hello world

# But here the output is somewhat different and so to print in the form of text we can decode method of stdout or we can pass keyword arguement in the run function as set to be True


# pprint.pprint(output2.stdout.decode())

# This will only run when the text arguement in the run method has not been set to True

# output3=subprocess.run('python',text=True,shell=True,stdout=subprocess.PIPE)

# Basically when we are setting capture_output as true then the stdout which is standard output is getting stored in subprocess pipe and instead of that basically we did it here

# so from here we can also directly capture it into a file

with open('sub-1.txt',mode='w') as file:
    subprocess.run('dir',shell=True,text=True,stdout=file)


# pprint.pprint(output3)



