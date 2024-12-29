

from dataclasses import dataclass



 @dataclass

 class Person:

    name: str
    age: int


 person = Person("Alice", 30)
 print(person)
 person.age = 31
 print(person)