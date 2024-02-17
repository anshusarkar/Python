class B_class :
    
    value =100 
    
    def __init__(self) -> None:
        print(self.value) # As it a constructor it will print the values on each function call 
    
    def Display_a_message(self):
        print("This method call is from a non parameterized constrouctor \n")
        
B = B_class()
B.value = 200
B.Display_a_message()