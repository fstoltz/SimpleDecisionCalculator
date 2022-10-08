from Action import Action
import os
from time import sleep
import sys

ADD_CON = 2
ADD_PRO = 1
NEW_ACTION = 1
EXIT = 2
DISPLAY_SUMMARY = 3
GO_BACK = 5
SAVE_STATE_TO_FILE = 4

class Menu:
    def __init__(self):
        self.running = True
        self.actionMenu = False
        self.action = Action("")


    def printMenu(self):
        print("(1) New Action\n(2) Exit")
        
    def printActionMenu(self):
        #os.system('cls' if os.name == 'nt' else 'clear')
        print("(1) Add a pro\n(2) Add a con\n(3) Display Summary\n(4) Save State to File\n(5) Go Back to Main Menu")


    def startMenu(self):
        while(self.running):
            self.printMenu()
            userIn = int(input())


            if userIn == NEW_ACTION:
                self.actionMenu = True
                print("Please define the action...")
                self.action = Action(input())
                self.insideActionMenu()

            elif(userIn == EXIT):
                self.running = False
                break



    def insideActionMenu(self):
        while(self.actionMenu):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("|---"+self.action.actionName+"---|")
            self.printActionMenu()
            userIn = int(input())


            if(userIn == ADD_PRO):
                print("Please describe the pro in words...")
                proString = input()
                print("Please quantify the pro(+1...+10). For example +3.")
                value = int(input())
                self.action.addPro(proString, value)
                sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')

            elif(userIn == ADD_CON):
                print("Please describe the con in words...")
                conString = input()
                print("Please quantify the con(-1...-10). For example -4.")
                value = int(input())
                self.action.addCon(conString, value)
                sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')

            elif(userIn == DISPLAY_SUMMARY):
                print(self.action.getSummary())


            elif(userIn == SAVE_STATE_TO_FILE):
                print("Are you sure you want to save to a local file? (y/n)")
                answer = input()
                if answer == 'y':
                    print("Saving state to file: ActionName.act  ", end='')
                    for i in range(0, 10):
                        print('.', end='')
                        sys.stdout.flush()
                        sleep(0.2)
                    sleep(1)
                    os.system('cls' if os.name == 'nt' else 'clear')

            elif(userIn == GO_BACK):
                self.actionMenu = False


if __name__ == "__main__":
    menu = Menu()
    menu.startMenu()
