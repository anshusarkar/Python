import csv,os

print(os.getcwd())

os.chdir(os.path.join(os.getcwd(),"Dealing_with_CSV"))

print(os.getcwd())

users = [
    {"name" : "Human", "username" :"Hue", "Department": "IT analyst"},
    {"name" : "Another_Human", "username": "Another_Hue", "Department": "R&D"},
    {"name" : "Yet_another_human", "username": "Yet_an_hue", "Department": "Production"}
]

keys = ["name", "username", "Department"]

with open('Department.csv', 'w') as D_CSV :
    writer = csv.DictWriter(D_CSV, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)
    
if  os.path.exists(os.path.join(os.getcwd(), "Department.csv")) == True :
    print("The file has been generated !")  
else :
    print("There is an error in the code !")