# The assert keyword in Python is used for debugging purposes to test if a given condition evaluates to True. 
# If the condition is False, the program raises an AssertionError with an optional error message. 
# It's often used to catch bugs by ensuring that assumptions in the code are correct.

x = 10
assert x > 5, "assertion passed !"  # Passes since the condition is True
assert x < 5, "assertion failed !"  # Raises AssertionError because the condition is False


# Assertions can be disabled globally in Python by running the interpreter with the -O (optimize) flag:
# python -O script.py