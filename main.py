import pyfiglet
from colorama import Fore, Back, Style
import os
import sys
import platform
import graphic as ui
option = None

def clearConsole():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
     
def add(newAct):
    with open('data\\data.txt','a+',encoding='UTF 8') as data:
                data.seek(0, 2)
                data.writelines(newAct + '\n')
                clearConsole()
                print(Fore.GREEN + 'Current list \n')
                data.seek(0)
                print(Fore.MAGENTA +data.read())
                print(Style.RESET_ALL)
                data.close()
        
def delete(deleteAct):
    with open('data\\data.txt','r',encoding='UTF 8') as data:
        clearConsole()
        lineas = data.readlines()
    if deleteAct > len(lineas) or deleteAct <= 0:
        print(Fore.RED + 'This data does not exist')
        print(Style.RESET_ALL)
    else:
        lineas[deleteAct -1] = '' + '\n'
        with open('data\\data.txt','w',encoding='UTF 8') as data:
            data.writelines(lineas)
            clearConsole()
            print('Actual activities\n')
        with open('data\\data.txt', 'r+', encoding='UTF-8') as data:
           print(Fore.MAGENTA + data.read())
            
    
def todoapp():
    option = None
    print(Fore.MAGENTA+ pyfiglet.figlet_format('Console Mode', font='digital'))
    print('\n')
    print(Fore.RED + 'Options:  \n')
    print("Option 1: See")
    print("Option 2: Add")
    print("Option 3: Delete")
    print(Style.RESET_ALL)
    while option != 1 and option != 2 and option != 3:
        option = int(input('What option do you want to do? '))
        if option == 1:
            clearConsole()
            print(Fore.GREEN + 'His pending activities are:\n')
            with open('data\\data.txt','r',encoding='UTF 8') as data:
                act = data.read()
                if act == '':
                    print(Fore.RED + 'No activities')
                else:
                    print(Fore.MAGENTA + act) 
                    print(Style.RESET_ALL)
                    data.close()
            
        elif option == 2:
            # del option
            # option = True
            while option:
                clearConsole()
                new = input( Fore.GREEN +'Activity to add: ' + Style.RESET_ALL)
                add(new)
                x = input(Fore.RED + 'Add another activity: (s/n) ')
                x.lower()
                if x == 's':
                    option  = True
                else: 
                    option = False
                    print(Style.RESET_ALL) 
                    clearConsole()
                    sys.exit()  
        elif option == 3:
            while option:
                clearConsole()
                with open('data\\data.txt','r',encoding='UTF 8') as data:
                    print(Fore.RED + 'Activities to delete:\n')
                    for index,line in enumerate(data.readlines()):
                        print(Fore.MAGENTA + f'Activity number {index+1}: {line} ')   
                    else:
                        print(Style.RESET_ALL)
                print('\n')        
                new = int(input( Fore.GREEN +'Number of activity to delete: ' + Style.RESET_ALL))
                delete(new)
                x = input(Fore.RED + 'Delete another activity: (s/n) ')
                x.lower()
                if x == 's':
                    option  = True
                else: 
                    option = False
                    print(Style.RESET_ALL) 
                    clearConsole()
                    sys.exit()                  
            


print(Fore.MAGENTA+ pyfiglet.figlet_format('To Do App'))
print('\n')
print(Fore.RED + 'Options:  \n')
print('Option 1: Graphic interface')
print('Option 2: Console mode')
print('Option 3: Info program \n')
print(Style.RESET_ALL)

while option != 1 and option != 2 and option != 3:
    option = int(input('What option do you want to do? '))
    if option == 1:
        clearConsole()
        print(Fore.MAGENTA+ pyfiglet.figlet_format('Graphic interface', font='digital'))
        print(Style.RESET_ALL)    
        ui.ui()
    elif option == 2:
        clearConsole()
        todoapp()
    else:
        clearConsole()
        with open('info\\data.txt', encoding='UTF 8') as data:
            print(Fore.MAGENTA+ pyfiglet.figlet_format('Info Program', font='digital'))
            print('\n')
            print(Fore.BLUE + data.read())
            print(Style.RESET_ALL)

