import re

log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"

# log varriable contains a string That states an error in a log files line
# The PID can be extracted by string sliceing 
# How ever in this case the postion of the [] is need to be known for that and also the size of the string inside it

index = log.index("[")

print(log[index+1:index+6])

# As said before the that PID was extraced cause the length of the string 12345 was known to us
# To fix this re module or the regular expression module was used

regex = r"\[(\d+)\]"

result = re.search(regex, log)

print(result[1])

# Using regex The string 12345 was extrected from the string log 
# without knowing the index 

# Though if in linux the same operation can be done using grep command and meantioning the search directory conating the file to be searched with it 
# and if the expression is to be searched for a string regardless of it's case ie small or big the pass -i with it 

result = re.search(r"a" , log)

print(result)

# Searching in raw strings

result = re.search(r"n","anshu")

print(result)

# Wildcard chracters

print(re.search(r"^Z" , "Zero"))

print(re.search(r"[Pp]ython", "Python")) # That checks for the existance for both Python amd python in string "Python"

# Also if not sure the chracters can be searched starting from a-z 

print(re.search(r"[a-z]way", "The end of the highway"))

print(re.search("cloud[a-zA-Z0-9]", "cloudy"))

print(re.search("cloud[a-zA-Z0-9]", "cloud9"))

# Checking for 1st space in a code

print(re.search(r"[^a-zA-Z]", "This isasentencewithonespaceinit."))

#The ^ symbole checks for anything but the given list

# Checking for . in the senctence

print(re.search(r"[^a-zA-Z ]", "This is a sentence that contains a '.' athe the end .")) # This should return the locations of things accept a-zA-z and a " SPACE "

# Logical '|' i.e. or operator can be used to check for existance for anyof the words

print(re.search(r"cat|dog", "I like both cats and dogs")) # The ceaarch operation will stop when ither of the word get's found

# To find both the words in a string use re.findall

print(re.findall(r"dog|cat", "I like both dogs and cats")) # This return a list for both the words if the match is sucessfull

