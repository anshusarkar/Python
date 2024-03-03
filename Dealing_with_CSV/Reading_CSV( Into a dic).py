import csv,os

print(os.getcwd())

os.chdir(os.path.join(os.getcwd(),"Dealing_with_CSV"))

print(os.getcwd())

with open('software.csv') as software:
    reader = csv.DictReader(software)
    for row in reader :
        print(("{} has {} users in {} in {} phase").format(row["name"], row["users"], row["status"], row["version"]))