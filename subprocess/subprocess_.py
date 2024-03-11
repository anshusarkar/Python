import subprocess as s

s.run(["date"]) # This execte a linux command that is passed in the string 

# Don't name the script with the name of the module to be imported cause that will create a conflict called circular import 

result = s.run(["host", "8.8.8.8"], capture_output = True) # capture_output = True sotres the output in stdout attribute

print(result.returncode)

print(result) # This stores the result in the stdout attribute
print(result.stdout) # This will have a b at the begning stating that the resutrned value is actualy an array of bytes that python can't read

# The error of a program get's stored in stderr attribute

result = s.run(["rm", "does_not_exists"], capture_output=True) # capture_output = True stores the output in the stderr attribute

print(result.stderr)

