S = "A an is just a kid with who grew up "

S_new = S[0:1] + " m" + S[2:]

print(S_new)

# Checking index for a particular element i.e. in a sentence

print(S_new.index("w"))

# Checking the starting index of a particular string in a sectence 

print(S_new.index("grew"))

# Checking existence of a particular word in a sentence

print("Child" in S_new)

print("kid" in S_new)