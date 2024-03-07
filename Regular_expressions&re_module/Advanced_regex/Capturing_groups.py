# In python regular expressions Capturing groups are portions of the pattern that are enclosed in parentheses
# If we have a list of people with last name and first name but if we want to make it firstname and lastname then it would become handy

import re

result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada") # Note the capturing group must follow the format of the givven string or in the other words the string should match the space in between 

print(result)

# The group method return a tuple contaning the the parts of the givven sting seperated by ,

print(result.group())  

# These strings can be accesed using indexing

print(result[0]) # This will return the entire string

print(result[1]) # This will return the first part of the string)

print(result[2]) # This will return the second part of the string

# Now using indexing the strings can be reversed 

print("{} {}".format(result[2], result[1]))

# checking if a string conatains exactaly five letter word in the sentence 

print(re.search(r"[a-zA-Z]{5}", "a ghost is scary")) # In this case this case ghost is the five letter word

# In the above even though the string conatained two words made of five latters it only returned the first match which is ghost
# to fix that a method of the re class called .findall can the used

print(re.findall(r"[a-zA-Z]{5}","a ghost is scary AF"))

# But findall method might just return a string that has more than five letters 

# To fix that \b can be used to in the raw string

print(re.findall(r"\b[a-zA-Z]{5}\b", "a ghost is scary AF though you shouldn't get scared if you encounter one")) # this won't return thoug, should, scare, encou

# the part under {} in the raw string part can be altered with ranges like if I want to gather strings with 5 charcters and 6 chracters in them then both the values can be passed to check the strings

print(re.findall(r"\w{5,6}", "a GHOST IS SCARY AF so though you shouldn't get scared if you encounter one"))

# searching for an word that starts with s\ but ends with upto 20 alpha numeric characters

print(re.search(r"s\w{,20}", "I really like strawberries"))

