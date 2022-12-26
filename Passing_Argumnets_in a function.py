def average (*numbers): # '*' is character that get's used to pass a tuple as an argument or a parameter, that is called 'args'
    print(type(numbers))
    sum = 0
    for x in numbers :
        sum = sum + x
    print("The average is : " , sum/len(numbers))
    
average(1,2,3)

def name (**names): #'**' is character that get's used to pass a dictionary as an argumnet, that is called kargs
    print(type(names))
    print("Hello !",names["Firstpreson"],names["Secondperson"],names["Thirdperson"])
name(Firstpreson = "Anshu" , Secondperson="X", Thirdperson="Y" )