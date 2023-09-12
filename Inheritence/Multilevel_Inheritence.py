class Grand_father :
    def quality_of_grand_father(self): 
        print("\nGood at math \n")

#                   |
#                   |
#                   v

class Father(Grand_father):
    def quality_of_father(self):
        print(super().quality_of_grand_father())
        
#                   |
#                   |
#                   v
        
class Children(Father):
    def quality_of_children(self):
        print(super().quality_of_grand_father())
    pass

C = Children() # Here child class is inheriting method from a class 2-levels above hence it's multilevel inheritance

C.quality_of_children()
        
