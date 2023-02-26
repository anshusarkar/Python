x=0
try :
    x=int(input("Enter a number : ")) 
except ValueError : # A specific error get's checked here in the expect block
    print("Please enter a number that is int ") 
finally :
    print("Enterred number is : ",x) # Finally block alaways get's executed even for a error
 
 
if x == 0 :    
    raise Exception ("Invalid input")
