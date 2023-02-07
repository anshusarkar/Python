class parent :
    def parent(self):
        print("Hello I am a parent !")
class child(parent):
    def child(self):
        super().parent()
        print("Hello !, and I am his child ")
        
c=child()
c.child()