import shutil

disk_usages = shutil.disk_usage("/")

print(disk_usages)

# This will print total number of bits, used_bits, free_bits of total avalable space in system

print("The total number of disk space used is : {:.2f} %" .format (disk_usages.free/disk_usages.total*100))

