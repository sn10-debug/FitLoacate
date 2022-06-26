from operator import sub
import subprocess
import os


# subprocess.run('gcc file1.cpp',shell=True,check=True)
# subprocess.run('./a.exe',shell=True,check=True)
# os.chdir('../final')
# subprocess.run('dir',shell=True,check=True)
# os.chdir('../starter')
# paths=os.path.split('Hello/hkkdk')
# print(paths)

files=["file1.cpp","challenge.c"]

num=int(input(f'1 - {files[0]}\n2 - {files[1]}\n'))
if num==1:
    subprocess.run(f'g++ {files[0]}',shell=True)
elif num==2:
    subprocess.run(f'gcc {files[1]}',shell=True)
subprocess.run('a.exe',text=True)

# response=subprocess.run('python selenium_1.py',shell=True)
# print(response.returncode)


# print()
