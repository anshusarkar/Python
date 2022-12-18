def average (*numbers): # '*' is character yhat gets used to pass arbitary argumunets in functions in python 
    sum = 0 
    for x in numbers :
        sum = sum + x
    print("The average is : " , sum/len(numbers))
    
average(1,2,3)