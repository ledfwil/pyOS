from os import chdir
from os import system
from base64 import b64encode
from base64 import b64decode
from os import getcwd
from time import sleep
def login():
    if getcwd().find('UserDB') < 0:
        chdir('UserDB')
    usrdb= open('users.txt', 'r')
    susrs= open('sudoers.txt', 'r')
    adusr= open('adusr.txt', 'w')
    usr= str(input('Enter your username: '))
    pwd= input('Enter your password: ')
    cpwd= b64encode(bytes(pwd, "utf-8"))
    chk= usrdb.readline()
    if chk.find(usr) < 0:
        chk=usrdb.readline()
    else:
        pass    
    if usr != 'admin':
        if chk.find(usr) >= 0:
            if chk.find(str(cpwd)) >= 0:
                print('Welcome')
                adusr.write(usr)
                sleep(5)
                print('This is still in aplha! *WIP*')
                sleep(3)
            else:
                print('The username or password is incorrect')
                system('pause')
                login()
        else:
            print('The username or password is incorrect')
            system('pause')
            login()
    else:
        print('The admin account cannot be used in the normal OS. Try another account')
        system('pause')
        login()