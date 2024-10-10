from os import chdir
from os import system
from base64 import b64encode
from base64 import b64decode
from os import getcwd
from time import sleep
import getpass
def db_create(usrdb):
    db= usrdb
    psk_db= dict()
    usr= db.readline()
    psk= db.readline()
    while usr != '':
        psk_db.update({usr:psk})
        usr= db.readline()
        psk= db.readline()
    return psk_db
def login():
    if getcwd().find('UserDB') < 0:
        chdir('UserDB')
    usrdb= open('users.txt', 'r')
    susrs= open('sudoers.txt', 'r')
    adusr= open('adusr.txt', 'w')
    psk_db = db_create(usrdb)
    usr= str(input('Enter your username: '))
    pwd= getpass.getpass('Enter your password: ')
    cpwd= b64encode(bytes(pwd, "utf-8"))
    chk= verify(usrdb, usr, False, "null")
    if usr != 'admin':
        for i in psk_db.keys():
            if usr == i:
                while (psk_db.get(i)).find(cpwd) != -1:
                    system('cls')
                    print(Welcome)
                    sleep(5)
                    chdir('..\\')
login()