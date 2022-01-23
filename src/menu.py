#!/bin/python3.10

from credentials import detectEIPassword, readCredentials
from keylogger import KeyLogger
from keyUtils import readLogs


class Menu:
    def startMenu():
        exitMenu = False

        while not(exitMenu):
            try:
                print("""
        ================
        Actividad 1 - EIP Keylogger
        ================
        Menu
        1) Start Keylogger
        2) Read keylog.txt
        3) Find EIP Password
        4) Read credentials.txt
        5) Exit
        """)
                selectedMenu = int(input("Select menu option > "))
            except:
                print("Invalid input, please use a number.")
            finally:
                if (selectedMenu == 1):
                    keylogger = KeyLogger()
                    print("Keylogger started - Press ESC to stop")
                    try:
                        keylogger.startKeylogger()
                    except:
                        print("Keylogger Stopped")
                elif(selectedMenu == 2):
                    print("Keylog.txt file content:")
                    readLogs()
                elif(selectedMenu == 3):
                    print("Looking for EIP credentials in keylog file...")
                    detectEIPassword()
                elif(selectedMenu == 4):
                    print("credentials.txt file content:")
                    readCredentials()
                elif(selectedMenu == 5):
                    print("Exiting keylogger...")
                    exitMenu = True
                else:
                    print("Unknown option, please try again.")
