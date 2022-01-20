#!/bin/python3.10

from keyUtils import initKeylogger


def startKeylogger():
    initKeylogger()


def menu():
    exitMenu = False
    print("""
    ================
    Actividad 1 - EIP Keylogger
    ================
    Menu
    1) Start Keylogger
    2) Read keylog.txt
    3) Exit
    """)

    while not(exitMenu):
        selectedMenu = int(input("Select:"))
        if (selectedMenu == 1):
            startKeylogger()
        elif(selectedMenu == 2):
            print("Keylog.txt file content")
        elif(selectedMenu == 3):
            exitMenu = True


if __name__ == '__main__':
    menu()
