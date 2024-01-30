#Imports
from os import chdir
from os import getcwd
from os import system
from subprocess import check_output
import subprocess
from time import sleep
from re import sub
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
#Login
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
#File copy begin!
def copy(a):
    dst= a
    src= getcwd()
    try:
        check_output(f'mkdir {a}', shell=True)
    except subprocess.CalledProcessError as e:
        output = e.output
    try:    
        check_output(f"Xcopy /s /e {src} {dst}", shell=True)
    except subprocess.CalledProcessError as e:
        output = e.output    
#Header
def header():
    system('cls')
    print('pyOS Recovery')
    print('\n' * 19)
    return  
#Menu
def menu():
    header()
    print('1) Exit and continue to pyOS')
    print('2) Use a Device (CD/DVD, USB, etc.)')
    print('3) Troubleshoot (Reset, Advanced...)')
    print('4) Turn off PC')
    opt= input('Make a selection: ')
    if opt == '1':
        system('shutdown /r /f /t 0')
    elif opt== '2':
        print('*WIP*')
        system('pause')
    elif opt == '3':
        system('cls')
        print('Troubleshoot')
        print('\n' * 10)
        print('1) Reset this PC')
        print('2) Advanced...')
        opt= input("Make a selection: ")
        if opt == '1':
            login(1)
            system('py resetOS.py')
        elif opt == '2':
            system('cls')
            print('Advanced')
            print('\n'* 13)
            print('1) System Startup Repair')
            print('\t' + 'Runs utilities at startup to check for errors and correct them')
            print('2) Repair via DOS')
            print('\t' + 'Use DOS for advanced troubleshooting')
            opt= input("Make a selection: ")
            if opt == '1':
                system
    elif opt == '4':
        print('Remove the installation media, and press ENTER: ')
        input()
        system('shutdown /r /f /t 0')
    else:
        print('Invalid Input')
        sleep(1)
        main()   