#Imports
from os import system
from os import chdir
#Main Execution
system('cls')
print('\t' + 'Power Options')
print('1) Logoff')
print('2) Shutdown')
print('3) Restart')
prnit('4) Exit to shell')
sel= input('Make a selection: ')
if sel == '1':
    chdir('../')
    system('py pyos.py')
elif sel == '2':
    system('shutdown /s')
elif sel == '3':
    system('shutdown /r')
elif sel == '4':
    exit()
else:
    print('Invalid input')
    sel= input('Make a selection: ')