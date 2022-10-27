list=[]
def insert ():
    inp=int(input("Enter the size : "))
    for i in range (inp):
        x=input("Enter the value : ")
        list.append(x)
def display ():
    print("\n",list[::-1],"\n")  #reversing list using slice operator  
def deletion ():
    print("This is stack, maintains LIFO \n")
    i = int(input("Enter the target index to delete (index starts from zero) :"))
    j= int (input("Enter the final index (Enter the same index again to delete only one index): "))
    if i == j:
        list[i]=0
    else:
        for x in range(i,j):
            list[x]=0

choice = int
print("\nHello their !")
while choice != 4:
    print("\nEnter 1 for insertion\nEnter 2 for deletion\nEnter 3 to display\nEnter 4 to exit\n")
    choice = int( input("Enter a choice :\n>> ") )
    if choice == 1:
        insert()
    elif choice == 2:
        deletion()
    elif choice == 3:
        display()
    elif choice > 4 :
        print("Worong choice...\n")
print("\nExiting...\n")