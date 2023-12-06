#Imports
from os import chdir
from os import getcwd
from os import system
from time import sleep
from base64 import b64encode
#Function Definition
def dirchk():
    cwd= getcwd()
    if cwd.find('pyOS') >=0:
        if cwd.find('UserDB') >= 0:
            return
        chdir('UserDB')
        dirchk()
    else:    
        path= input("Enter the path to pyOS on the system's primary hard disk: ")
        chdir(path)
        dirchk()
    return
def login(a):
    if a != 0:
        chdir('../')
        dirchk()
    usrdb= open('users.txt', 'r')
    pwd= input('Enter the password for account "admin": ')
    epwd= str(b64encode(bytes(pwd, 'utf-8')))
    chk= usrdb.readline()
    if chk.find(epwd) >= 0:
        return
    else:
        print('The password is incorrect')
        system('pause')
        login(0)
def menu():
    print(getcwd())
    chdir('../')
    chdir('Systempy')
    system('cls')
    print('\t' + 'Settings')
    print('1) User Management')
    print('2) System Management')
    print('3) Recovery')
    print('4) Exit')
    opt= input('Make a selection: ')
    if opt == '1':
        system('py pyosusrmgr.py')
        menu()
    elif opt == '2':
        system('py compmgmt.py')
        menu()
    elif opt == '3':
        login(1)
        chdir('../')
        chdir('Systempy')       
        system('py recovery.py')
        menu()
    elif opt == '4':
        exit()
    else:
        menu()
        
#Main Execution
def main():
    dirchk()
    login(0)
    menu()
main()