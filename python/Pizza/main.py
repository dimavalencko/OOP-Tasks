from terminal import *

if __name__ == "__main__":

    terminal_1 = Terminal()
    print(terminal_1)
    while True:
        terminal_1.displayMenu()
        menuItem = input()
        terminal_1.processComand(menuItem)
