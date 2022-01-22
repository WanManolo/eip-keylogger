#!/bin/python3.10

from keyUtils import initKeylogger, readLogs


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
        selectedMenu = int(input("Select menu option:"))
        if (selectedMenu == 1):
            print("Keylogger started - Press ESC to stop")
            try:
                startKeylogger()
            except:
                print("Keylogger Stopped")
        elif(selectedMenu == 2):
            print("Keylog.txt file content:")
            readLogs()
        elif(selectedMenu == 3):
            print("Exit keylogger...")
            exitMenu = True


if __name__ == '__main__':
    menu()
