name=input("Enter your name : ")
if(name == "Anshu Sarkar"):
    print("Hello , Anshu !")
    age=int(input("Enter your age : "))
    if age in range (15,17):
        print("\nWelcome ! ")
        print("\nSo you are now " , age , "!\n")
    elif age == 18 :
        print("\nYou just turnd ",age," !\nSo cool !\n")
    else:
        print("\n  SUS !! ")
        age1=age
        if age1 in range (19,100) :
            print("\nSo you are now :  " , age , "\n" )
        elif age1 == 100 :
            print("\nHuh ! Himalayan monk sopted ! 😃 \n")
        elif age1 >100:
            print("\nTell me is imortality a curse ?\n")
else :
    print("Not Welocme ! Bye ")     