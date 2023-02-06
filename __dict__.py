class Hello:
      """__dict__ get's used to pack up a constrouctor's conatins into a list """
      def __init__(self, name, age): 
            self.name = name
            self.age = age
            pass
      
h=Hello("Anshu",30)    
print( h.__doc__ )
print(h.__dict__)