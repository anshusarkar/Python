from pynput.keyboard import Key, Controller
import time

# Dosen't work in wsl 

# Initialize the keyboard controller
keyboard = Controller()

def timer(seconds : int, minutes : int)-> None :

    print(f"Timer started for {minutes} minutes \ntime remaing is : ")
    while seconds != 0 :
        time.sleep(1)
        seconds -= 1
        print(f"{seconds} seconds")

def bombard():

    while True:
        # Type "Hello, world!"
        keyboard.type("Hello, world!") # Change the msg according to your preferance !
        
        # Press 'Enter' key
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        
        # Sleep for 1 second
        time.sleep(1)


min = float(input("Enter the time in minutes before the bombardmant : "))
sec : int = min * 60


if 1 != 2 :
    keyboard.press(Key.enter) 
    keyboard.release(Key.enter)
    timer(seconds = sec, minutes = min)
    bombard()   

# Before execution put the cursour in a message box in any chatting application and wait 
# for the amount of time that was given as input to the program
# the individual would be bombarded with messages :) 
# I would propose somebody with this script someday !  