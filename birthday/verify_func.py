import re


def email_verify(x):
    Check=False
    if re.match('^[A-Za-z]{1}[A-Za-z._0-9]*@[A-za-z]*[.]{1}(com|io|edu)$',x):
        Check=True
    return Check
   


def number_verify(x):
    Check=False
    if re.match('[1-9]{1}[0-9]{9}',x):
        Check=True
    return Check

def name_verify(x):
    names=x.split(' ')
    check=True
    for i in names:
        if len(i)<2:
            check=False
    return check

def verify(name,number,email):
    if name_verify(name) and number_verify(number) and email_verify(email):
        return True
    else:
        return False


