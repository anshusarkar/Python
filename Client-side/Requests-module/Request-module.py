import requests as r

x = r.get('https://python.org')

# print(x.text)

# Using string sliceing we can print certain portion of the response.txt

print(x.text[:90])

# Using the pylance look for methods and by long pressing on them look into their 
# documentation
# read more in coursera course
