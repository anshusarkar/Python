class Father :
    def __init__(self):
        pass
    
    def quality(self) :
        print("Is good at math \n")

class Child(Father):
    
    def __init__(self) :
        pass
    
    def quality(self) :
        print("Is good at programming \n")
        print(super().quality())

C = Child()
C.quality()