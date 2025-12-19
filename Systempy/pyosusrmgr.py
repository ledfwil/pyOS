#Imports
from os import getcwd
from os import chdir
from os import rename
from os import remove
from os import system
from base64 import b64encode
from hashlib import sha256
import getpass
#Funciton Definition
def sudochk(usr, sudoers):
    susr= sudoers.readline()
    while susr != '':
        if susr != usr:
            susr= sudoers.readline()
        else:
            print('Your user account is not permitted to do this action')
            system('pause')    
def dirchk():
    cwd= getcwd()
    if cwd.find('Systempy') != -1:
        chdir('../')
        dirchk()
    elif cwd.find('pyOS') >= 0:
        chdir('UserDB')
    else:
        path= input('Enter the path to pyOS: ')
        chdir(path)
        system('cls')
        dirchk()
def usradd(sudoers, userdb):
    usr= input('Enter a username: ')
    pwd= getpass.getpass('Make a secure password: ')
    cpwd= getpass.getpass('Enter the password again to confirm it: ')
    pwdchk(pwd, cpwd, usr, userdb)
    is_su= input('Will this user be an administrator? [Y/N]: ')
    if is_su == 'Y' or is_su == 'y':
        sudoers.write(usr)
        print('Users added to sudoers file.')
    else:
        print('User has not been aded to sudoers file.')
    print('The user was added!')
def pwdchk(pwd, cpwd, usr, userdb):
    while True:
        if pwd == cpwd:
            bpwd = sha256(b64encode(pwd.encode()))
            usrdb.write('\n' + usr + '\n')
            usrdb.write(str(bpwd.hexdigest()))
            pass
            break
        else:
            pwd= getpass.getpass("The passswords didn't match. Try again. ")
            cpwd= getpass.getpass('Confirm it: ')
            pwdchk(pwd, cpwd)
def usrrm(adusr):
    system('cls')
    usrdb= open('users.txt' , 'r')
    print("Just a reminder: You can't remove your current user (should it be the only user account).") 
    print("To do that, create a new user with sufficient permissions, then use them to delete this account.")
    system('pause')
    ausr= adusr.readline()
    qusr= input('Enter a username: ')
    tmp= open('tmp.txt', 'w')
    line= usrdb.readline()
    if line != '':
        if line.find(qusr) >= 0:
            if qusr == ausr:
                adusr.close()
                usrrm()
            confirm= input('Are you sure you want to delete ' + qusr + ' ? [Y/N]')
            if confirm == 'Y' or confirm == 'y':
                print('User Removed')
                usrdb.readline()
            elif confrim == 'N' or confirm == 'n':
                print('User retained')
                tmp.write(line)
            else:
                print('Invalid Input')
                confirm= input('[Y/N]')
        else:
            tmp.write(line)
    else:
        tmp.close()
        usrdb.close()
        remove('users.txt')
        rename('tmp.txt', 'users.txt')
def chgpwd(ausr):
    adusr= ausr.readline()
    tmp= open('tmp.txt', 'w')
    users= open('users.txt', 'r')
    line= users.readline()
    if line.find(adusr) >= 0:
        pwd= getpass.getpass('Enter your new password: ')
        cpwd= getpass.getpass('Confirm it: ')
        pwdchk(pwd, cpwd, adusr)
        tmp.write(adusr + '\n' )
        bpwd= sha256(b64.encode(pwd))
        tmp.write(str(bpwd.hexdigest()))
        print('Password changed sucessfully!')
        tmp.close()
        users.close()
        rename('tmp.txt', 'users.txt')
    elif line != '':
        tmp.write(line)
        line= users.readline()
def main(sudoers, adusr, usrdb):
    while True:
        print('Please Select an Option')
        print('1) Add a User')
        print('2) Remove a User')
        print('3) Change Your Password')
        print('4) Exit')
        option= input('Selection: ')
        if option == '1':
            usradd(sudoers, usrdb)
        elif option == '2':
            sudochk(adusr, sudoers)
            usrrm(adusr)
        elif option == '3':
            chgpwd(adusr)
        elif option == '4':
            exit()
        else:
            print('Invalid Input')
            option= input('Make a selection')
#Main Execution
dirchk()
usrdb= open('users.txt', 'a')
sudoers= open('sudoers.txt', 'a')
adusr= open('adusr.txt', 'r')
main(sudoers, adusr, usrdb)