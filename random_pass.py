from os import system
import platform
import random
import string
import time

def sysName():  # git system name ( Windows / Linux )
    sysName = platform.system()
    return sysName

def cleanScreen():

    if sysName() == 'Linux':
        cln = system('clear')
    else:
        cln = system('cls')

def randomPassword():   #creat random and strong password (lHn$dL7*r$0p$@Ip%ImD)
    password = ""
    ch1 = string.ascii_lowercase
    ch2 = string.ascii_uppercase
    ch3 = string.digits
    ch4 = ['!','@','#','$','%','$','&','*']

    random_ = [ch1,ch2,ch3,ch4]

    for i in range(20):
        rm_list = random.choice(random_)
        rmChar = random.choice(rm_list)
        password += rmChar
    return (password)

cleanScreen()

print('Creating .....\n\n\n')

time.sleep(3)

print (f'Your Random Password Is : {randomPassword()}\n\n\n')
