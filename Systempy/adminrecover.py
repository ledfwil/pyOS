from os import getcwd
from os import chdir
from os import rename
from os import remove
from os import system
from base64 import b64encode
import getpass
def dirchk():
    cwd= getcwd()
    if cwd.find('Systempy') != -1:
        chdir('../')
        dirchk()
    elif cwd.find('pyOS') >= 0:
        chdir('UserDB')
        pass
    else:
        path= input('Enter the path to pyOS: ')
        chdir(path)
        system('cls')
        dirchk()
def pwdchk(pwd, cpwd, usr, usrdb):
    while True:
        if pwd == cpwd:
            bpwd = b64encode(bytes(pwd, "utf-8"))
            usrdb.write(usr + '\n')
            usrdb.write(bpwd)
            pass
        else:
            pwd= getpass.getpass("The passswords didn't match. Try again. ")
            cpwd= getpass.getpass('Confirm it: ')
            pwdchk(pwd, cpwd)
def main():
    dirchk()
    usr= "admin"
    usrdb= open('users.txt', 'w')
    sudoers= open('sudoers.txt', 'w')
    pwd= getpass.getpass('Make a secure password: ')
    cpwd= getpass.getpass('Enter the password again to confirm it: ')
    pwdchk(pwd, cpwd, usr, usrdb)
    is_su= 'Y'
    if is_su == 'Y':
        sudoers.write(usr)
    else:
        print('User has not been aded to sudoers file.')
    print('admin account recovered')
main()    