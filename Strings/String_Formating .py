x ="My home is in {} , I live in the sate {}" #Adding number in the bracess i.e 'My home is in {0} , I live in this sate {1}'  
home = "Murshidabad"                           #would make the sring follow a numric format given in the format function
state ="WestBengal"
print(x.format(home,state)) # formated string
print(x)

# formating float values to print upto certain decimal place of it

price = 1254.9862

tax = 0.18

print("The prince of the product is : {}".format(price))

print("The absolute cost of the product with tax is : {:.2f}".format(price+price*tax))