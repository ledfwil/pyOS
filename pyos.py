#Welcome to the passion project of a crazy idea! Let's hope this works...
#Imports
from os import system
from os import chdir
from os import getcwd
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
        print('Welcome to pyOS!')
        sleep(2)
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
        system('cls')
        print('*WIP*')
        system('pause')
        system('cls')
        print('Apps List')
        print("No apps installed, maybe we'll get some one day...")
        yeetus= input("Do you have any apps on hand? [y/n]: ")
        if yeetus == 'y':
            print("Alright! We'll have to modify the main script in a future commit for base apps.")
            print("External Installed Apps will be in a separate script that will have categories.")
            print('mayhaps.')
            print("However, that'll be a project for another day.")
            print("*WIP*")
            system('pause')
        if yeetus == 'n':
            print("Makes sense. I get it. Don't worry, some apps will come bundled eventually.")
            print("*WIP*")
            system('pause')
        main()
    elif sel == '3':
        chdir('../')
        chdir('Systempy')
        system('py oscfg.py')
    elif sel == '4':
        chdir('../')
        chdir('Systempy')
        system('py poweropt.py')
    else:
        print('Invalid Input')
        system('pause')
        main()
#Main Execution        
dirchk()
adusr= login.login()
main()