def factorial(n):
  if n < 2:
    return 1
  else:
    return n * factorial(n-1)

print(factorial(10))

# In python max number of recursion possible is 1000