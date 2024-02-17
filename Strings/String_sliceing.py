S = "This is a real big sentence belive me !"
   #----------------------------------------> +ve S[0:39]
   #<---------------------------------------- -ve S[-39:0] # That means starting from negative direction which is -39 to 0 that is the end point in 
                                                           # In negative direction and -39 is the begning point in negative direction
print(len(S))
print(S[0:20]) # Or print(S[:20]) same thing

print(S[-3:-1]) # Sliceing from -3 index to -1 index # Won't work if it is starting from -1 to -3 i.e. S[-1:-3]

print(S[0:len(S):2]) #S[start:end-point:skiping-steps]

# Sliceing using slice() 

S = "This is a real big sentence belive me !"

val = slice(0 , 2)

print(S[val])

val2 = slice(-3 , -1 )

print(S[val2])

val3 = slice(-39 , -28 , 2 ) # Starting from negative index -39 which is 0th index in +ve direction 
                             # to -28 which is 11 in +ve direction (39-28) skiping every 2nd element
print(S[val3])