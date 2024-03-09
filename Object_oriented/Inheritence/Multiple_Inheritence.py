class Father():
    def quality1(self):
        print("Is good at math \n")
        
#                        +

class Mother():
    def quality2(self):
        print("Is good at management \n")
 
#                        |
#                        |
#                        |
#                        v
 
        
class Child(Father , Mother): # Here child class is inheriting qualities from multiple source hence it's multiple inheritence
    
    def quality(self):
        print("Is good at programming \n")
        print(super().quality1() , super().quality2())
        
C=Child()        
C.quality()