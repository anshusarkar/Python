def fib_sequence() -> None :
    print("Enter the limit (Don't worry about the limit it won't be Problem like CPP where the best it could is 48th sequence for python max limit is 4300 ): ", end="")
    inp = int(input())
    prevar = 0
    nextvar = 1
    print(prevar, end=",")
    
    for i in range(3, inp):
        fibnum = prevar + nextvar
        if fibnum > 0:
            print(fibnum, end=",")
        else:
            print("\nThis is the limit! After this, the program starts printing negative numbers! lol that ain't CPP or C") # That part won't even execute cause it's python known for robustness ! won't sotp untill it get's the job done !
            var = i
            print(f"\nThe program stopped at {var}")
            break
        
        prevar = nextvar
        nextvar = fibnum
    
    print("\nYeah! Now that's a golden ratio!")
    print("Cause any number of the sequence if divided by the previous number is 1.67 except for the first three numbers of the sequence!")
    print("FYI: Golden ratio is the Fibonacci sequence!")


fib_sequence()
