import subprocess as s
import os
import re
import time as t

# A function that checks for teh presences 'ALL' key woard in the update.log file 
def check_for_all_keyword(log_file_path):
    """
    This function checks for the presence of the word "All" in the update.log file.

    Args:
        log_file_path (str): The path of the update.log file.

    Returns:
        int: 0 if the word "All" is found, 1 otherwise.

    Raises:
        FileNotFoundError: If the log file is not found.
        Exception: If an error occurs.
    """
    
    # To check the function driscription call that function using __doc__ in a print function - print(check_for_all_keyword(log_file_path.__doc__))
    # Pattern to match "All"
    pattern = r'\bAll\b'
    
    try:
        # Open the log file
        with open(log_file_path, 'r') as file:
            # Read the content of the log file
            log_file_content = file.read()
            
            # Search for the pattern in the log file content
            matches = re.findall(pattern, log_file_content)
            
            # Print all matches found
            if matches:
                return 0
            return 1
    except FileNotFoundError:
        print("Log file not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


# The commands for apt based distros to check for update
command = "sudo apt update"
command2 = "sudo apt upgrade"
# Run the command, capturing the output and errors
process = s.Popen(command, shell=True, stdin=s.PIPE, stdout=s.PIPE, stderr=s.PIPE)

# Provide the password to put oupts and errors in a varriable 
password = "19471947"
output, error = process.communicate(input=password.encode())

# Print the output and errors
print("\nThe fletched repos are : \n\n",output.decode())
print("\nThe errors encounterd are : \n",error.decode())

output = output.decode()
error = error.decode()

with open("update.log", 'w') as o :
    o.write("The repos fetched are : \n\n"+output+"\n\n The erros found are :\n\n"+error)
    

if os.path.exists("update.log"):
    print("\nThe update log hasbeen generated \n\n")



if  check_for_all_keyword("update.log") == 0 :
    print("Nothing to update, Check latter\n")
else:
    a = 0
    while a < 1: 
        t.sleep(5)
        a += 1
        Aborad = str(input("The update's are synced the updageade will begin in 5 secs...\nEnter 'S' to abroad\n"))
        
    i = 0    
    while i < 1:
        if Aborad == 'S':
            print("\nUpgrade stoped !\n")
            i += 1
            break
        else :
            print("The upgrade is intiated")
            s.Popen(command2, shell=True, stdin = s.PIPE, stdout=s.PIPE, stderr=s.PIPE)
            i += 1

print("Bye !")
