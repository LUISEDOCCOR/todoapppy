import pyfiglet
from colorama import Fore, Back, Style
import os
import platform
import graphic as ui




def clearConsole():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
     

def todoapp():
    print(Fore.MAGENTA+ pyfiglet.figlet_format('Console Mode', font='digital'))
    print('\n')
    print(Fore.RED + 'Options:  \n')
    print("Option 1: Add")
    print("Option 2: Delete")
    print("Option 3: See")
    print(Style.RESET_ALL)


print(Fore.MAGENTA+ pyfiglet.figlet_format('To Do App'))
print('\n')
print(Fore.RED + 'Options:  \n')
print('Option 1: Graphic interface')
print('Option 2: Console mode')
print('Option 3: Info program \n')
print(Style.RESET_ALL)

option = None
while option != 1 and option != 2 and option != 3:
    option = int(input('What option do you want to do? '))
    if option == 1:
        clearConsole()
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

