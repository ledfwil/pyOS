from os import chdir
from os import system
from base64 import b64encode
from base64 import b64decode
from os import getcwd
from time import sleep
import getpass
def db_create(usrdb):
    psk_db= dict()
    usr= usrdb.readline()
    psk= usrdb.readline()
    usr= usr.replace('\n', '')
    if usr != "admin":
        print("heyo! Seems the admin account is missing. You'll have to make it")
        print('Launching admin account recovery...')
        sleep(2)
        chdir('..\\')
        chdir('Systempy')
        system('py adminrecover.py')
        exit()
    elif usr == "" or psk == "":
        print("heyo! Seems we've got some missing info in the login files")
        print('Going to user management menu... (Choose option 1 when you get to the menu)')
        system('pause')
        chdir('..\\')
        chdir('Systempy')
        system('py pyosusrmgr.py')
        exit()
    while usr != '':
        psk_db.update({usr:psk})
        usr= usrdb.readline()
        usr= usr.replace('\n', '')       
        psk= usrdb.readline()
        if usr or psk == '':
            if len(psk_db) > 2:
                print("heyo! Seems we've got some missing info in the login files")
                print('Going to user management menu... (Choose option 1 when you get to the menu)')
                system('pause')
                chdir('..\\')
                chdir('Systempy')
                system('py pyosusrmgr.py')
                exit()
    return psk_db
def login():
    cwd= getcwd()
    print(cwd)
    while cwd.find('UserDB') < 0:
        try:
            if cwd.find('UserDB') < 0:
                chdir('UserDB')
                cwd=getcwd()
        except FileNotFoundError as e:
            print("heyo! Some shit's aint here or bugged.")
            print(f"{e} \n is what broke.")
            exit()
    try:
        usrdb= open('users.txt', 'r')
        susrs= open('sudoers.txt', 'r')
        adusr= open('adusr.txt', 'w')
    except FileNotFoundError:
        print("heyo! Seems we've got some missing files related to login info")
        print('Going to user management menu... (Choose option 1 when you get to the menu)')
        system('pause')
        chdir('..\\')
        chdir('Systempy')
        system('py pyosusrmgr.py')
        exit()
    psk_db = db_create(usrdb)
    usr= str(input('Enter your username: '))
    pwd= getpass.getpass('Enter your password: ')
    cpwd= b64encode(bytes(pwd, "utf-8"))
    if usr != 'admin':
        for i in psk_db.keys():
            if usr == i:
                while (psk_db.get(str(i))).find(str(cpwd)) != -1:
                    system('cls')
                    print("Welcome")
                    sleep(5)
                    chdir('..\\')
    else:
        print('admin account cannot be used in normal OS. Please choose another account')
        login()
    adusr.write(usr)
    usrdb.close()
    susrs.close()
    adusr.close() 
login()