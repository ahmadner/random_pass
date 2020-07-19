import random
import time
import string
from os import system
my_pass = []

_ = system('clear')

pass_long =int( input('Enter Long Pass You Want : '))

while pass_long < 8 :
    _=system('clear')
    print ('''
    
** pass is too shurt try again **
    
    ''')
    pass_long =int( input('Enter Long Pass You Want : '))

ch4 = string.ascii_lowercase
ch3 = string.ascii_uppercase
ch2 = string.digits
ch1 = ['!','@','#','$','%','$','^','&','*']

random_ = [ch1,ch2,ch3,ch4]

for i in range (int(pass_long)):

    rm = random.choice(random_)
    rm_ch = random.choice(rm)
    my_pass.append(rm_ch)


#print (my_pass)


def listToString(s):  
    
    str1 = ""     
    for ele in s:  
        str1 += ele

    return str1 

_ = system('clear')
print ('Creating.......')
time.sleep(2)

print (f'''

Random Password is: {listToString(my_pass)}

''')
 