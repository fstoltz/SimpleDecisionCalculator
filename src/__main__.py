from src.Action import Action


ADD_CON = 2
ADD_PRO = 1
NEW_ACTION = 1
EXIT = 2
DISPLAY_SUMMARY = 3
GO_BACK = 4


class Menu:
    def __init__(self):
        self.running = True
        self.actionMenu = False
        self.action = Action("")


    def printMenu(self):
        print("(1) New Action\n(2) Exit")

    def printActionMenu(self):
        print("(1) Add a pro\n(2) Add a con\n(3) Display Summary\n(4) Go Back to Main Menu")


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
            print("|---"+self.action.actionName+"---|")
            self.printActionMenu()
            userIn = int(input())


            if(userIn == ADD_PRO):
                print("Please describe the pro...")
                proString = input()
                print("Please quantify the pro(+1...+10)")
                value = int(input())
                self.action.addPro(proString, value)

            elif(userIn == ADD_CON):
                print("Please describe the con...")
                conString = input()
                print("Please quantify the con(-1...-10)")
                value = int(input())
                self.action.addCon(conString, value)

            elif(userIn == DISPLAY_SUMMARY):
                print(self.action.getSummary())

            elif(userIn == GO_BACK):
                self.actionMenu = False


if __name__ == "__main__":
    menu = Menu()
    menu.startMenu()