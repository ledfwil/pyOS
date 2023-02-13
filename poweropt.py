#Imports
from os import system
from os import chdir
#Main Execution
print('\t' + 'Power Options')
print('1) Logoff')
print('2) Shutdown')
print('3) Restart')
sel= input('Make a selection: ')
if sel == '1':
    system('py pyos.py')
elif sel == '2':
    system('shutdown /s')
elif sel == '3':
    system('shutdown /r')
else:
    print('Invalid input')
    sel= input('Make a selection: ')