from pynput.keyboard import Key, Controller
import time

# Put the code in execution then choose what you want to do 
# then after entering the message and time duration hover over to any messaging services chat box and put the cursour in the chat box !

# Initialize the keyboard controller
keyboard = Controller()

def timer(seconds = int, minutes = float)-> None :
    if 1 != 2 : # JUst to take Remote access permission 
        keyboard.press(Key.enter) 
        keyboard.release(Key.enter)

    print(f"Timer started for {minutes} minutes \ntime remaing is : ")
    while seconds != 0 :
        time.sleep(1)
        #print(type(seconds)) I had to check the type of the as for some reasone using type hinting at the timer functions parametrs was making it str type _/-('_')-\_
        seconds -= 1
        print(f"{seconds} seconds")

def print_msg(repetation, msg : str):


    if repetation == 'U': # That would mean Unlimited repetations or in the other words "Bombardment of msgs !"

        while True: # Open loop to send the msg repedetly !
            
            keyboard.type(f"{msg}") # Change the msg according to based on what you want to be deliveredd repetadely 
            # Press 'Enter' key
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            
            # Sleep for 1 second
            time.sleep(1)

    elif repetation == 1 : # One time delivery of msg 
            
            keyboard.type(f"{msg}") # Change the msg according to your preferance !
            # Press 'Enter' key
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)





def bombard():
    
        msg = str(input("Enter a message that is to be bomberded : "))
        min = float(input("Enter the time in minutes before the bombardmant : "))
        sec : int = min * 60
        timer(seconds = sec, minutes = min)
        print_msg(repetation = 'U', msg = msg)   


def proposal_req(): # I want to propose somebody with it so I named it proposal ... th function mainly sends a msg once ..

        msg = str(input('Enter a message that is to be send once ! : '))
        min = float(input("Enter the time in minutes before exact time when message is to be delivered : "))
        sec : int = min * 60
        timer(seconds = sec, minutes = min )
        print_msg(repetation = 1, msg = msg)
        print("\nMessage has been delivered ! Boss !\n\n")


if __name__ == '__main__': # The script is kinda dangerous so better to use it 
   

   choice = str

   while choice != 'exit':
       
        choice = input("\n\nEnter 1 to send a msg\n\nEnter 2 to bombard with msg\n\nType exit to exit\n\n")

        if choice == 'exit':
           print("Bye !")
           break
        elif choice == '1':
           proposal_req()
           break
        elif choice == '2':
           bombard() # To stop the bombardment press ctrl + z or ctrl + d or ctrl + c in linux 
           break
        else :
           print("Wrong choice !")



# Before execution put the cursour in a message box in any chatting application and wait 
# for the amount of time that was given as input to the program
# the individual would be bombarded with messages :) 
# I would propose somebody with this script someday ! 












































































#                                                                                                                                                                       All right I made that happen ! though I got the Idea from instragrm feed the library that was used in it was 'Pyautogui' it wasn't even getting imported (26/05/2024) Al suggested me alternative library called 'Pynput' ... And I made it happen ! 
#                                                                                                                                                                                                                                                                                                                                          even though it isn't something that big it's an achivement to me !(Anshu Sarkar!) 