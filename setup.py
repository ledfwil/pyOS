#Imports
from os import chdir
from os import getcwd
from os import system
from subprocess import check_output
import subprocess
from time import sleep
from re import sub
#Function Definition
#Directory Verification
def verify(dir):
    header()
    chdir(dir)
    system('dir')
    here= input('Is pyOS located here? [Y/N]: ')
    if here == 'Y':
        return dir
    if here == 'N':
        dir= input('Enter the path to pyOS on the computer: ')
        verify(dir)
    else:
        print('Invalid Input')
        system('pause')
        verify(dir)
#Updater
def instup(a):
    dst= verify(a)
    src= input('Enter the path to installation media: ')
    chdir(dst)
    dstc= dst + "/UserDB"
    dstu= dst + '/Users'
    stmp= src + '/tmp'
    stmpy= sub('pyOS', '', stmp)
    stmpu= stmpy + 'Users'
    stmpdb= stmpy + 'UserDB'
    opt= input('Would youu like to keep user data? [Y/N]: ')
    if opt == 'Y':
        #Temporary File Copy and Restore for User data
        check_output(f"Xcopy /s /e {dstc} {stmpy} ", shell=True)
        check_output(f"Xcopy /s /e {dstu} {stmpy}", shell=True)
        check_output(f"rmdir {dst} /s /q", shell=True)
        check_output(f"Xcopy /s /e {src} {dst}", shell=True)
        check_output(f"XCopy /s /e {stmpu} {dst}", shell=True)
        check_output(f"XCopy /s /e {stmpdb} {dst}", shell=True)
    if opt == 'N':
        #Otherwise, just clean it up...
        check_output(f"rmdir {dst} /s /q", shell=True)
        print('Go through the install steps to continue... ')
        system('pause')
        Setup()
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
    #Setup cleanup
    chdir(dst)
    header()
    #After Setup completes, restart the computer
    print('Setup wiil restart your computer in 10 seconds')
    sleep(5)
    system('shutdown /r')
#The actual setup, similar to XP-era and older Windows Setup programs, but no blue background
def Setup():
    header()
    print('Welcome to pyOS Setup!')
    print('Setup will guide you through the installation of pyOS onto your computer')
    system('pause')
    header()
    print('\n')
    path= input('Enter the path where you would like the OS to be installed(excluding pyOS): ')
    dpath= path + 'pyOS'
    header()
    print('Setup will create an account called admin that can be used to access the system in the event a system recovery is needed')
    apwd= input('Enter a secure password for the account: ')
    capwd= input('Comfirm it: ')
    #Password confirmnation for this admin account is key, so input validation is necessary.
    if apwd != capwd:
        print("Those passwords didn't match. Try again.")
        apwd= input('Enter a secure password for the account: ')
        capwd= input('Comfirm it: ')
        if apwd != capwd:
            print("Those passwords didn't match. Try again.")
            apwd= input('Enter a secure password for the account: ')
            capwd= input('Comfirm it: ')
            if apwd != capwd:
                print("Those passwords didn't match. Try again.")
                apwd= input('Enter a secure password for the account: ')
                capwd= input('Comfirm it: ')
                #After 3 attempts, Setup closes with the error: Too many failed attempts
                if apwd != capwd:
                    header()
                    print('Setup has been aborted due to too many incorrect password attempts for creating account: admin')
                    system('pause')
                    exit()
    #User database file writing
    else:
        header()
        print('Setup is going to create a user account for you to use')
        usrnm= input('Enter your username: ')
        pwd= input('Enter a secure password: ')
        cpwd= input('Confirm it: ')
        if pwd != cpwd:
            print("Those passwords didn't match. Try again.")
            pwd= input('Enter a secure password for the account: ')
            apwd= input('Comfirm it: ')
            if pwd != cpwd:
                print("Those passwords didn't match. Try again.")
                pwd= input('Enter a secure password for the account: ')
                apwd= input('Comfirm it: ')
                if pwd != cpwd:
                    print("Those passwords didn't match. Try again.")
                    pwd= input('Enter a secure password for the account: ')
                    cpwd= input('Comfirm it: ')
                    #After 3 attempts, Setup closes with the error: Too many failed attempts
                    if pwd != cpwd:
                        header()
                        print('Setup has been aborted due to too many incorrect password attempts for creating account: {usrnm} ')
                        system('pause')
                        exit()        
    header()
    print('Setup is now ready to copy the OS files to your computer')
    print('Your computer will restart after the file copy process is complete')
    system('pause')
    print('Copying files...')
    #The setup copy begins...
    copy(dpath)
    chdir('UserDB')
    users= open('users.txt', 'w')
    users.write('admin' + '\t' + apwd)
    users.write(usrnm + '\t' + pwd)
    users.close()
#The Setup Header
def header():
    system('cls')
    print('pyOS Setup')
    print('\n' * 19)
    return
def main():
    header()
    print('Welcome to pyOS!')
    print('1) Update an existing install of pyOS')
    print('2) Install pyOS')
    print('3) pyOS Recovery')
    print('4) Exit Setup')
    opt= input('Make a selection: ')
    if opt == '1':
        path= input('Enter the path to pyOS on this computer: ')
        instup(path)
    elif opt== '2':
        Setup()
    elif opt == '3':
        rosdir= input('Enter the directory pyOS is installed in (Path to the folder named pyOS, but excluding it): ')
        osdir= rosdir + 'pyOS'
        chdir(osdir)
        chdir('Systempy')
        system('py recovery.py')
    elif opt == '4':
        print('Remove the installation media, and press ENTER: ')
        input()
        system('shutdown /r /f /t 0')
    else:
        print('Invalid Input')
        sleep(1)
        main()
#Main execution
header()
print('Welcome to pyOS!')
sleep(2)
main()