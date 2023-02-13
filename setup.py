#Imports
from os import chdir
from os import getcwd
from os import system
from subprocess import check_output
import subprocess
#Function Definition
#File copy begin!
def copy(a):
    try:
        dst= a
        src= getcwd()
        check_output(f"Xcopy /E /I {src} {dst}", shell=True)
    except subprocess.CalledProcessError as e:
        output = e.output
    #Setup cleanup
    chdir(dst)
    system('del setup.py')
    system('del users.txt')
    system('del sudoers.txt')
#The actual setup, similar to XP-era and older Windows Setup programs, but no blue background
def Setup():
    header()
    print('Welcome to pyOS Setup!')
    print('Setup will guide the installation of pyOS onto your computer')
    system('pause')
    header()
    dpath= input('Enter the path where you would like the OS to be installed: ')
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
        chdir('UserDB')
        users= open('users.txt', 'w')
        users.write('admin' + '\t' + apwd)
        users.close()
        chdir('../')
    header()
    print('Setup is now ready to copy the OS files to your computer')
    print('Your computer will restart after the file copy process is complete')
    system('pause')
    print('Copying files...')
    #The setup copy begins...
    copy(dpath)
    #Upon completion, restart the computer
    system('pause')
    system('shutdown /r')
#The Setup Header
def header():
    system('cls')
    print('pyOS Setup')
    print('\n' * 25)
    return
#Main execution
Setup()