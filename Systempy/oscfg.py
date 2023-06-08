#Imports
from os import chdir
from os import getcwd
from os import system
from time import sleep
#Function Definition
def dirchk():
    cwd= getcwd()
    if cwd.find('pyOS') >=0:
        if cwd.find('UserDB') >= 0:
            continue
        chdir('UserDB')
        dirchk()
    path= input("Enter the path to pyOS on the system's primary hard disk: ")
    chdir(path)
    dirchk()
def login():
    pwd= input('Enter the password for account "admin": ')
    chk= usrdb.readline()
    if chk.find(pwd) >= 0:
        return
    else:
        print('The password is incorrect')
            system('pause')
            login()
def main():
    system('cls')
    print('\t' + 'Settings')
    print('1) User Management')
    print('2) System Management')
    print('3) Recovery')
    opt= input('Make a selection: ')
    if opt == '1':
        system('py pyosusrmgr.py')
    elif opt == '2':
        print('*WIP*')
        system('pause')
        system('cls')
        main()
    elif opt == '3':
        login()
        system('py recovery.py')
        
#Main Execution
usrdb= open('users.txt', 'r')
main()