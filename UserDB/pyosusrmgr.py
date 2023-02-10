#Imports
from os import getcwd
from os import chdir
from os import rename
from os import remove
#Funciton Definition
def chkdir():
    cwd= getcwd()
    if cwd.find('pyos') >= 0:
        if cwd.find('UserDB') >= 0:
            print('Accessing User Database...')
        else:
            chdir('UserDB')
    else:
        path= input('Enter the path to pyOS: ')
        chdir(path)
def usradd():
    usr= input('Enter a username: ')
    pwd= input('Make a secure password: ')
    cpwd= input('Enter the password again to confirm it: ')
    if pwd == cpwd:
        usrprofile.write(usr + '\t' + pwd)
        is_su= input('Will this user be an administrator? [Y/N]: ')
        if is_su == 'Y':
            sudoers.write(usr)
            print('Users added to sudoers file.')
        else:
            print('User has not been aded to sudoers file.')
    else:
        pwd= input("The passswords didn't match. Try again. ")
        cpwd= input('Confirm it: ')
    print('The user was added!')
    main()
    tmp.close()
    usrprofile.close()
    remove('users.txt')
    rename('tmp.txt', 'users.txt')
def usrrm():
    print('\n' * 35)
    usrprofile= open('users.txt' , 'r')
    print("Just a reminder: You can't remove your current user. To do that, use the recovery menu.")
    adusr= open('adusr.txt', 'r')
    ausr= adusr.readline()
    qusr= input('Enter a username: ')
    tmp= open('tmp.txt', 'w')
    line= usrprofile.readline()
    if line != '':
        if line.find(qusr) >= 0:
            if qusr == ausr:
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
        usrprofile.close()
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
        else:
            pwd= input("The passswords didn't match. Try again. ")
            cpwd= input('Confirm it: ')
            if pwd == cpwd:
                tmp.write(adusr + '\t' + pwd)
                print('Password changed sucessfully!')
                tmp.close()
                users.close()
                rename('tmp.txt', 'users.txt')
                main()
            else:
                pwd= input("The passswords didn't match. Try again. ")
                cpwd= input('Confirm it: ')
                tmp.write(adusr + '\t' + pwd)                    
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
usrprofile= open('users.txt', 'a')
sudoers= open('sudoers.txt', 'a')
main()