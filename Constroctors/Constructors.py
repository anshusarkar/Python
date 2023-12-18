class A_class : 
    
    # value1_to_be_passed_into_methods = 0   # This is not required in python unlike java classes
    # value2_to_be_passed_into_methods = 0
    
    
    def __init__(self,value,value2):
        
        self.value1_to_be_passed_into_methods = value 
        self.value2_to_be_passed_into_methods = value2
        
    def show_value(self):
        
        print("These values " ,self.value1_to_be_passed_into_methods , "," , self.value2_to_be_passed_into_methods , "are passed from a parameterized constrouctor \n ")



A = A_class(1,2) # This is a parameterized constructor
A.show_value()



class B_class :
    
    value =100 
    
    def __init__(self) -> None:
        print(self.value) # As it a constructor it will print the values on each function call 
    
    def Display_a_message(self):
        print("This method call is from a non parameterized constrouctor \n")
        
B = B_class()
B.Display_a_message()