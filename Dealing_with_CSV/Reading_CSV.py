import csv,os

print(os.getcwd()) # pls cd into Python/Dealing_with_CSV

file = open("csv_file.txt")

csv_f = csv.reader(file)

for row in csv_f:
        name , phone, role = row
        print("Name: {}, Phone: {}, Role: {}".format(name, phone, role))
        
        
file.close()