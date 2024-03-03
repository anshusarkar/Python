import csv,os

print(os.getcwd())

os.chdir(os.path.join(os.getcwd(),"Dealing_with_CSV"))

print(os.getcwd())

hosts = [["Computer", "192.25.63.2"],["Computer2","192.56.32.58"]]

with open('Computer_names_&_IP_adds', 'w') as h_csv:
    writer = csv.writer(h_csv)
    writer.writerows(hosts)
    
# if using linux cd in the python/dealing_with_CSV direcotory and 
# in terminal use cat Computer_names_&_IP_adds to print the files in the terminal
# and to start writting into terminal a files conataing in linux
# use command cat > filename and start writting
# and to delete the file use command rm -rf filename
