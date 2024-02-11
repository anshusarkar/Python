class A :
    name = "Anshu" 
    def __len__(self):  # Dunder / magic methods with doube underscores at initialzion of the method
        i = 0             
        for _ in self.name :
            i = i +1 
            return i
print(len(A.name))

class B: 
    def __init__(self , n): # Constructure is also a dender method 
        self.names = n
    def __len__(self):
        i = 0
        for _ in self.names :
            i = i + 1
            return i

print(len("Anshu"))

# if__name=="__main__" dinder method 
# if _name_ == "__main__: 
# basically says "run this code if the file is being executed (and NOT imported)." 
# If you don't have it, importing your .py file will execute all of the code in the body of the 

