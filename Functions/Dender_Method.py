class A :
    name = "Anshu" 
    def __len__(self):  # Dender / magic methods with doube underscores at initialzion of the method
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
