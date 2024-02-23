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


# Conerting every 10th degit in range 10-100 from ferhenite to celsius

def fun(val)->int:
    return (val-32)*(5/9)

for i in range(10,110,10):
    cel = fun(i)
    print("{:>3}° F | {:>6.2f}° C".format(i,cel))
    
# The :>3 specifies to print values of varriables to be allinged at right by three number of spaces
# and for :>6 specifies to print values following 6 spaces by right 

# {:d}   integer value "{0:.0f}".format(10.5) → '10'
# {:.2f} floating point with that many decimals'{:.2f}'.format(0.5) → '0.50'
# {:.2s} string with that many characters'{:.2s}'.format('Python') → 'Py'
# {:<6s} string aligned to the left that many spaces'{:<6s}'.format('Py') → 'Py    '
# {:>6s} string aligned to the right that many spaces'{:>6s}'.format('Py') → '    Py'
# {:^6s} string centered in that many spaces '{:^6s}'.format('Py') → '  Py  '


