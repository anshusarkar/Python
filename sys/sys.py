#!/usr/bin/env python3
import sys
print(sys.argv)

# Now if the program is run by using command ./sys.py after chaging it's permission

# This will return a list consisting of [Comand-Line-Argumants] which means it will have ./sys,py init

# If the extra things words are passed with ./sys.py for example ./sys.py one two as command-line argument 

# Then the list that is to be returned would consist [./sys.py, one, two ] 

# In programing we return 0 to state that the program executed successfully

# even if we don't return 0 for a sucessful execution system records 0 

# to check this use command echo $? 

# and for a faulty execution the system keeps a rercord in the form of 1

# That is called exit ststus 

# Dont return 1 that dosen't states a sucessfull execution for the system

# Use 
a=10
b=12

if a<b:
    sys.exit(0) # To stste system a sucessfull execution 
sys.exit(1) # To state an execution with error, that propably applies to all the progrsming languages meaning returning 0 doesn't state a sucessfull execution as system won't be aware of it ....