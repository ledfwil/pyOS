#Welcome to the passion project of a crazy idea! Let's hope this works...
#Imports
from os import system
from os import chdir
from os import getcwd
<<<<<<< HEAD
from time import sleep 
import login
#Prerequisites
#Directory 'Integrity Check' of sorts, just verifies current working directory
def dirchk():
    cwd= getcwd()
    if cwd.find('UserDB') < 0 | cwd.find('Systempy') < 0:
        chdir('../')
        dirchk()
    elif cwd.find('pyOS') >= 0:
        system('cls')
        print('\n' * 3)
        print('Welcome to pyOS!')
        print('\n' * 12)
        sleep(2)
        login.login()
=======
from time import sleep
from base64 import b64encode
#Prerequisites
#Directory 'Integrity Check' of sorts, just verifies current working directory
cwd= getcwd()
if cwd.find('pyOS') >= 0:
    system('cls')
    print('\n' * 3)
    print('Welcome to pyOS!')
    print('\n' * 12)
else:
    path= input('Enter the path to pyOS: ')
    chdir(path)
    system('cls')
chdir('UserDB')
usrdb= open('users.txt', 'r')
susrs= open('sudoers.txt', 'r')
adusr= open('adusr.txt', 'w')
#Function Definitons
#Basic login function, built from ground up
def login():
    usr= input('Enter your username: ')
    pwd= input('Enter your password: ')
    bpwd = b64encode(pwd.encode())
    chk= usrdb.readline()
    if chk.find(usr) >= 0:
        resume
    else: 
        chk = usrdb.readline()
    qchk = chk.replace('\t', '')
    bchk = qchk.replace(usr, '')
    if usr != 'admin':
        if chk.find(usr) >= 0:
            if bpwd:
                print('Welcome')
                adusr.write(usr)
                sleep(5)
                print('This is still in aplha! *WIP*')
                system('pause')
                main()
            else:
                print('The username or password is incorrect')
                system('pause')
                login()
        else:
            print('The username or password is incorrect')
            system('pause')
            login()
>>>>>>> 7e22e964bfdd41c068cc9500d8c2d4dd4335cfec
    else:
        path= input('Enter the path to pyOS: ')
        chdir(path)
        system('cls')
        dirchk()
#Function Definitons
#The main menu for the whole OS. Simple, yet effective
def main():
    system('cls')
    print('\t' + 'Main Menu')
    print('1) File Browser')
    print('2) Apps')
    print('3) Settings')
    print('4) Shutdown...')
    sel= input('Make a selection: ')
    if sel == '1':
        #It is unknown if by some miracle I can think of a way to make this work, but most likely will be seperate script
        print('*WIP*')
        system('pause')
    elif sel == '2':
        print('*WIP*')
        system('pause')
        main()
    elif sel == '3':
        chdir('../')
        chdir('Systempy')
        system('py oscfg.py')
    elif sel == '4':
        adusr.close()
        usrdb.close()
        susrs.close()
        chdir('../')
        chdir('Systempy')
        system('py poweropt.py')
    else:
        print('Invalid Input')
        system('pause')
        main()
#Main Execution        
dirchk()
main()