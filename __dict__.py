class Hello:
     def __init__(self, name, age):
      self.name = name
      self.age = age
      pass

h=Hello("Anshu",30)    
print(h.__dict__)