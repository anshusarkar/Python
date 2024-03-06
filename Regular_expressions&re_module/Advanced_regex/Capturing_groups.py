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
