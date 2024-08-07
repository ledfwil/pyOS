#Imports
from os import getcwd
from os import chdir
from os import rename
from os import remove
from base64 import b64encode
#Funciton Definition
def chkdir():
    cwd= getcwd()
    if cwd.find('pyos') >= 0:
        if cwd.find('UserDB') >= 0:
            print('Accessing User Database...')
        else:
            chdir('UserDB')
            chkdir()
    else:
        path= input('Enter the path to pyOS: ')
        chdir(path)
        chkdir()
def usradd():
    usr= input('Enter a username: ')
    pwd= input('Make a secure password: ')
    cpwd= input('Enter the password again to confirm it: ')
    pwdchk(pwd, cpwd)
    is_su= input('Will this user be an administrator? [Y/N]: ')
    if is_su == 'Y':
        sudoers.write(usr)
        print('Users added to sudoers file.')
    else:
        print('User has not been aded to sudoers file.')
    main()
    print('The user was added!')
def pwdchk(pwd, cpwd):
    if pwd == cpwd:
        bpwd = b64encode(pwd.encode())
        usrdb.write(usr + '\t' + bpwd)
    else:
        pwd= input("The passswords didn't match. Try again. ")
        cpwd= input('Confirm it: ')
        pwdchk(pwd, cpwd)
def usrrm():
    system('cls')
    usrdb= open('users.txt' , 'r')
    print("Just a reminder: You can't remove your current user. To do that, use the recovery menu.")
    adusr= open('adusr.txt', 'r')
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
            if confirm == 'Y':
                print('User Removed')
            elif confrim == 'N':
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
def chgpwd():
    ausr= open('adusr.txt', 'r')
    adusr= ausr.readline()
    tmp= open('tmp.txt', 'w')
    users= open('users.txt', 'r')
    line= users.readline()
    if line.find(adusr) >= 0:
        pwd= input('Enter your new password: ')
        cpwd= input('Confirm it: ')
        if pwd == cpwd:
            tmp.write(adusr + '\t' + pwd)
            print('Password changed sucessfully!')
        else:
            pwd= input("The passswords didn't match. Try again. ")
            cpwd= input('Confirm it: ')
            pwdchk(pwd, cpwd)
            tmp.write(adusr + '\t' + pwd)
            print('Password changed sucessfully!')
            tmp.close()
            users.close()
            rename('tmp.txt', 'users.txt')
            main()
    elif line != '':
        tmp.write(line)
        line= users.readline()
def main():
    print('Please Select an Option')
    print('1) Add a User')
    print('2) Remove a User')
    print('3) Change Your Password')
    print('4) Exit')
    option= input('Selection: ')
    if option == '1':
        usradd()
    elif option == '2':
        usrrm()
    elif option == '3':
        chgpwd()
    elif option == '4':
        exit()
    else:
        print('Invalid Input')
        option= input('Make a selection')

#Main Execution
chkdir()
usrdb= open('users.txt', 'a')
sudoers= open('sudoers.txt', 'a')
main()