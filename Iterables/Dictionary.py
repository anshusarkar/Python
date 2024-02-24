Identity = {
    "name" : "Anshu Sarkar" ,
    "adress" : "Berhampure" ,
    "email" : "anshu@anshu.com"
}

print(Identity["adress"])

Student = {
   "Anshu":  1 ,
   "Ram" :2  ,
   "Lelouch": 3  
}

# Iterating over Dictionaries 

for i in Student:
    print(Student[i])
    
# uSING two varriables to print both key and value pairs

for i , j in Student.items():
    print("{}'s rollno. is : {}".format(i,j))
    
# Dictionaries are more like enum in c and java
# Where values are stored in key value pair and also they are mutable 

Student["Zero"] = 4

print(Student)

# To print the valeus of a dictionary 

print(Student.values())

# To print the keys of a dictionary 

print(Student.keys())

# Or the values and keys can be iterated using for loops

for _ in Student.values():
    print(_)
    
for _ in Student.keys():
    print(_)