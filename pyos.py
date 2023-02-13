#Welcome to the passion porject of a script! Let's hope this works...
#Imports
from os import system
from os import chdir
from os import getcwd
from time import sleep
#Prerequisites
#Directory 'Integrity Check' of sorts, just verifies current working directory
cwd= getcwd()
if cwd.find('pyOS') >= 0:
    print('\n' * 35)
    print('Welcome to pyOS!')
    print('\n' * 12)
else:
    path= input('Enter the path to pyOS: ')
    chdir(path)
    print('\n' * 35)
    print('Welcome to pyOS!')
    print('\n' * 12)
chdir('UserDB')
usrdb= open('users.txt', 'r')
susrs= open('sudoers.txt', 'r')
adusr= open('adusr.txt', 'w')
#Function Definitons
#Basic login function, built from ground up
def login():
    usr= input('Enter your username: ')
    pwd= input('Enter your password: ')
    chk= usrdb.readline()
    if chk.find(usr) >= 0:
        if chk.find(pwd) >= 0:
            print('Welcome')
            aduser.write(usr)
            sleep(5)
            main()
        else:
            print('The username or password is incorrect')
            system('pause')
            login()
    else:
        print('The username or password is incorrect')
        system('pause')
        login()
#The main menu for the whole OS. Simple, yet effective
def main():
    print('\n' * 35)
    print('This is still in aplha! *WIP*')
    system('pause')
    print('\t' + 'Main Menu')
    print('1) File Browser')
    print('2) Apps')
    print('3) Settings')
    print('4) Shutdown...')
    sel= input('Make a selection: ')
    if sel == '1':
        print('*WIP*')
        system('explorer')
    elif sel == '2':
        print('*WIP*')
        system('pause')
        main()
    elif sel == '3':
        chdir('../')
        system('py oscfg.py')
    elif sel == '4':
        adusr.close()
        users.close()
        susrs.close()
        chdir('../')
        system('py poweropt.py')
    else:
        print('Invalid Input')
        sel= input('Make a selection: ')
#Main Execution        
login()
