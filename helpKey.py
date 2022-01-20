#!/bin/python3.10
#####################################################################
# Modulo desarrollado por Daniel García Baameiro para la asignatura #
# de Seguridad Ofensiva de la Escuela Internacional de Posgrados    #
#####################################################################

class KeysMap:
    ALTGR = '<65027>'
    DOS = "'2'"

atSign = {KeysMap.ALTGR, KeysMap.DOS}
currently_pressed = set()

def translateKey(key):
    global currently_pressed

    if str(key) in atSign:
        currently_pressed.add(str(key))

    if currently_pressed == atSign:
        goodKey = '@'
    elif str(key) == KeysMap.ALTGR:
        goodKey = ''
    else:
        try:
            goodKey = key.char
        except AttributeError:
            goodKey = key
        
    if str(key) == KeysMap.DOS:
        currently_pressed.clear()

    return goodKey
