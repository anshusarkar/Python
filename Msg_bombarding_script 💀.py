import pyautogui as auto
import time 

while True:
    auto.write("Hello, world!")
    auto.press('enter')
    time.sleep(1)
    
# The code will bombard any massage box and would make system press on enter button 
# continously (Syccesfull ran of fedora after maneging dependencies)

# requied dependencie to work 
# sudo dnf install python3-devel python3-pip python3-tkinter xorg-x11-server-Xvfb
# pip install pyautogui
# pip install Pillow pymsgbox PyScreeze mouseinfo
# change the package manager depending on the distro and for windows
# it should run ... 

# run it in python shell .. exicution through python3 command or in any code editor might not work ..
# meaning copy th code and run it in python shell by opening it using command "Python3"
# in any os then slowly move to the whatsapp web 
# opening the individual name and then presiing on the msg box 
# would iniciate the ms bombarding 
# Using time module you can auto mate the script to run on specific time 
# though don't chnage the time.sleep(1) as it sends the sg in the time duration of 1 sec .

