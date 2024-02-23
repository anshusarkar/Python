
# In python lists are mutable data types that can hold any data types in them in consigutive manner

# Often used when the number of insertion for a dataset is unkown

list=[] 
for  i in range(5):
    x=int(input("Enter a value : "))
    list.append(x) # append alaways inserts elements at the end position of the list
print(list)
   
# More List methods

fruits = ["Banana", "Pineapple","Apple","Melon"]

fruits.insert(0,"Kiwi") # Inserts values at specific idex

print(fruits)

fruits.insert(100,"Goava") # This will insert value at the max index + 1 position 

print(fruits)

fruits[2] = "Melon" # same as insert function() 

print(fruits)

fruits.remove("Kiwi") # Removes the mentioned value

print(fruits)

fruits.pop(0) # same as remove but pops a value at an index

print(fruits)

# Using ennumarate to iterate over a list 

Winners = ["Goku" , "Anshu" , "Zero"]

for position, name in enumerate(Winners):
    
    print("{} - {}".format(position, name))
    
    # The function would return two tuples


z = [x for x in range(0,11) if x % 3 == 0] # creating a list of multiplers of 3

print(z)
