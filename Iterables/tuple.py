# in python tuples are a sequence of data types of any type that are immutable
# positions in the tuples holds meanings

x=("Anshu" , "Sarkar") # here tuple is holding the first name at the 1st index and last name at the last index and tha's the meaning of it 

print(x) # Printing the tuple

# Printing the cntains of the tuples

for _ in range(len(x)):
    print(x[_])
    
# If a function is returuing multiple values then it would return it in a tuple

def convert_secs(seconds:int):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours , minutes , remaining_seconds

result = convert_secs(6000)

print(type(result))

print(result)

# also the output being a tuple it can be inserted into multiple varriables

hours , minutes , seconds = result

print(hours , minutes , seconds)
    