import re
def rearrange_name():
    name = ""
    name=str(input("Enter a name staring following the below format \n lastname, firstname \n>> "))
    result = re.search(r"^(\w*), (\w*)$", name) # Checking if the inserted string matches our format or not
    if result == None :
        print("Entered name disn't match the specified format")
    else :
        print("The reversed version of the name srating with first name and endinth last name is : {} {} ".format(result[2], result[1]))
    
rearrange_name()