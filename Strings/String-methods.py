# To strip spaces out of strings use .strip()
print("Hello ".strip())

print(" hello".lstrip())

print("hello ".rstrip())

print("The number of times e ocurs in this string ".count("e"))

print("Forest".endswith("rest"))

print("123456789".isnumeric())

print("abcdefg".isalpha())

print(int("12345") + int("54321"))

print("Mountains".upper())

print("Montains".lower())

# join function to concatinate all list elements

# joing list elements with "space" in between

l = ["This" , "is" , "a" ,"sentence"]

print(" ".join(l))

# joining with "..." in between

print("...".join(l))

# split function splits a sentence into a list

S = "Hello, world !"

print(S.split())

print(S.replace("world", "sekai"))