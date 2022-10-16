Set={}
def insert():
    x=int(input("Enter the number of of data to be inserted : "))
    for i in range (x) :
        print("Enter the value :")
        inp=int(input())
        Set[i]=inp
def display():
    print(Set)
def delete(): 
    i=int(input("Enter the initial index(Index starts from zero) : "))
    j=int(input("Enter the final index(Eter the initial index agagin to delete one at inital index) : "))
    if i==j :
        Set[i]=0
    else :
        for x in range(i,j):
            Set[x] = 0
choice = int     
while choice !=4:
    print("Enter 1 to insert the value,")
    print("Enter 2 to display the value,")
    print("Enter 3 to delete the value, ")
    print("Enter 4 to exit.")
    choice = int(input("\nEnter your choice : "))
    if choice == 1:
        insert()
    elif choice == 2:
        if Set=={}:
            print("\n\nNothing to display...\nEnter values by Entering choice as 1.\n\n")
        else:
            print("\n\n")
            display()
            print("\n\n")
    elif choice == 3:
        delete()
        print("\nDone...")
    if choice > 4:
        print("\nWrong choice!\n")
print("\n\nExiting......\n\n")